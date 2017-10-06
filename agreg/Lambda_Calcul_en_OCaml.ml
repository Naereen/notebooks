
let identite = fun x -> x ;;

let vide = fun x -> x ;;

let si = fun cond valeur_vraie valeur_fausse -> cond valeur_vraie valeur_fausse ;;

let vrai = fun valeur_vraie valeur_fausse -> valeur_vraie ;;
let faux = fun valeur_vraie valeur_fausse -> valeur_fausse ;;

let non = fun v x y -> v y x;;

let vrai_paresseux = fun valeur_vraie valeur_fausse -> valeur_vraie () ;;
let faux_paresseux = fun valeur_vraie valeur_fausse -> valeur_fausse () ;;

let paresseux = fun f -> fun () -> f ;;

type 'a nombres = ('a -> 'a) -> 'a -> 'a;;  (* inutilisé *)
type entiers_church = (int -> int) -> int -> int;;

let zero = fun (f : ('a -> 'a)) (z : 'a) -> z ;;

let un = fun (f : ('a -> 'a)) -> f ;;

let compose = fun f g x -> f (g x);;

let deux = fun f -> compose f f;;  (* == compose f (un f) *)
let trois = fun f -> compose f (deux f) ;;
let quatre = fun f -> compose f (trois f) ;;
(* etc *)

let rec entierChurch (n : int) =
    fun f z -> if n = 0 then z else f ((entierChurch (n-1)) f z)
;;

(entierChurch 0) (fun x -> x + 1) 0;; (* 0 *)
(entierChurch 7) (fun x -> x + 1) 0;; (* 7 *)
(entierChurch 3) (fun x -> 2*x) 1;; (* 8 *)

let entierNatif c : int =
    c (fun x -> x + 1) 0
;;

entierNatif (si vrai zero un);; (* 0 *)
entierNatif (si faux zero un);; (* 1 *)

entierNatif (entierChurch 100);; (* 100 *)

(* prend un lambda f lambda z. ... est donne vrai ssi n = 0 ou faux sinon *)
let estnul = fun n -> n (fun z -> faux) (vrai);;

(* prend un lambda f lambda z. ... est donne vrai ssi n > 0 ou faux sinon *)
let estnonnul = fun n -> n (fun z -> vrai) (faux);;

entierNatif (si (estnul zero) zero un);; (* 0 *)
entierNatif (si (estnul un)   zero un);; (* 1 *)
entierNatif (si (estnul deux) zero un);; (* 1 *)

entierNatif (si (estnonnul zero) zero un);; (* 0 *)
entierNatif (si (estnonnul un)   zero un);; (* 1 *)
entierNatif (si (estnonnul deux) zero un);; (* 1 *)

entierNatif (si (non (estnul zero)) zero un);; (* 0 *)
entierNatif (si (non (estnul un))   zero un);; (* 1 *)
entierNatif (si (non (estnul deux)) zero un);; (* 1 *)

let succ = fun n f z -> f ((n f) z) ;;

entierNatif (succ un);; (* 2 *)

let pred = fun n ->
    if (entierNatif n) > 0 then entierChurch ((entierNatif n) - 1)
    else zero
;;

entierNatif (pred deux);; (* 1 *)

entierNatif (pred trois);; (* 2 *)

let somme = fun n m f z -> n(f)( m(f)(z));;

let cinq = somme deux trois ;;

entierNatif cinq;;

let sept = somme cinq deux ;;

entierNatif sept;;

let produit = fun n m f z -> m(n(f))(z);;

let produit = fun n m -> compose m n;;

let six = produit deux trois ;;

entierNatif six;;

let huit = produit deux quatre ;;

entierNatif huit;;

let paire = fun a b -> fun f -> f(a)(b);;

let gauche = fun p -> p(fun a b -> a);;
let droite = fun p -> p(fun a b -> b);;

entierNatif (gauche (paire zero un));;
entierNatif (droite (paire zero un));;

let pred n suivant premier =
    let pred_suivant = paire vrai premier in
    let pred_premier = fun p ->
        si (gauche p)
        (paire faux premier)
        (paire faux (suivant (droite p)))
    in
    let paire_finale = n pred_suivant pred_premier in
    droite paire_finale
;;

entierNatif (pred deux);; (* 1 *)

let listevide = fun survide surpasvide -> survide();;

let cons = fun hd tl -> fun survide surpasvide -> surpasvide hd tl;;

let estvide = fun liste -> liste (fun () -> vrai) (fun tt qu -> faux);;

entierNatif (si (estvide (listevide)) un zero);; (* estvide listevide == vrai *)
entierNatif (si (estvide (cons un listevide)) un zero);; (* estvide (cons un listevide) == faux *)

let tete = fun liste -> liste (vide) (fun tt qu -> tt);;
let queue = fun liste -> liste (vide) (fun tt qu -> qu);;

entierNatif (tete (cons un listevide));;
entierNatif (tete (queue (cons un (cons un listevide))));;

let u = fun f -> f (f);;

let rec y = fun f -> f (y(f));;

let fact = y(fun f n -> si (estnul n) (un) (produit n (f (pred n))));;

let rec y = fun f -> f (fun x -> y(f)(x));;

let fact = y(fun f n -> si (estnul n) (un) (produit n (f (pred n))));;
