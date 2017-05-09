
(* On définit les symboles du calcul propositionnel et les formules du calcul propositionnel = liste de symboles. *)

type symbole_calcul_prop = F | V | Ou | Et | Non | ITE ;;

type formule_calcul_prop = symbole_calcul_prop list ;;


(* Cette fonction calcule l'arité du symbole du calcul propositionnel pris en argument.

    Notez qu'on peut supposer que l'appel à cette fonction d'arité se fait en $\mathcal{O}(1)$ dans les calculs de complexité, puisqu'après compilation, cette fonction sera une simple lecture d'un tableau.
*)
let arite_calcul_prop (s : symbole_calcul_prop) : int =
    match s with
    | F -> 0
    | V -> 0
    | Non -> 1
    | Ou -> 2
    | Et -> 2
    | ITE -> 3
;;


(* Quelques exemples de formules du calcul propositionnel. *)
let ex_correct = [Ou; Non; Ou; F; V; Ou; Non; V; F];;
let ex_incorrect = [Ou; Non; F; Non];;
let ex_ite = [ITE; V; F; V];;
let ex_vide = [];;


(* Cette fonction prend en argument une liste de symboles [l] et une fonction d'arité sur ces symboles et renvoie "vrai" (`true`) si [l] est l'écriture préfixe d'un terme et "faux" sinon (`false`).

    Notez que le "et" en Caml est paresseux, i.e., `x && y` n'évalue pas `y` si `x` est `false`.
    Donc cette fonction peut s'arrêter avant d'avoir parcouru tous les symboles, dès qu'elle trouve un symbole qui contredit le critère sur les hauteurs $h_p$.

    Et cela permet aussi d'obtenir une indication sur le premier symbole à contredire le critère, comme implémenté ensuite.
*)
let ecriture_prefixe_valide (l : 'a list) (arite : 'a -> int) : bool =
    let rec aux (l : 'a list) (h : int) : bool =
    match l with
    | [] -> false
    | [t] -> ((h + 1 - (arite t)) = 1)
    | t :: q  ->
        let h_suivant = (h + 1 - (arite t)) in
        (h_suivant <= 0) && (aux q h_suivant)
    in aux l 0
;;


(* Avec la remarque précédente, on peut écrire une fonction très similaire, mais qui donnera une indication sur la position (i.e., l'indice) du premier symbole qui fait que le mot n'est pas bien équilibré, si le mot n'est pas bien formé. Si le mot est bien formé, `None` est renvoyé. *)
let ecriture_prefixe_valide_info (l : 'a list) (arite : 'a -> int) : int option =
    let rec aux (l : 'a list) (compteur : int) (h : int) : int option =
    match l with
    | [] -> Some compteur
    | [t] ->
        if (h + 1 - (arite t)) = 1 (* h = arite(t) *)
        then None
        else Some compteur
    | t :: q  ->
        (* h est l'accumulateur qui contient la somme des 1 - arite(t) *)
        let h_suivant = (h + 1 - (arite t)) in
        if h_suivant <= 0 then
            Some compteur
        else
            aux q (compteur + 1) h_suivant
    in
    aux l 0 0
;;



(* Quelques tests *)
let _ = ecriture_prefixe_valide ex_correct   arite_calcul_prop;; (* true *)
let _ = ecriture_prefixe_valide ex_incorrect arite_calcul_prop;; (* false *)
let _ = ecriture_prefixe_valide ex_ite       arite_calcul_prop;; (* true *)
let _ = ecriture_prefixe_valide ex_vide      arite_calcul_prop;; (* false *)


let _ = ecriture_prefixe_valide_info ex_correct   arite_calcul_prop;; (* None *)
let _ = ecriture_prefixe_valide_info ex_incorrect arite_calcul_prop;; (* Some XXX *)
let _ = ecriture_prefixe_valide_info ex_ite       arite_calcul_prop;; (* None *)
let _ = ecriture_prefixe_valide_info ex_vide      arite_calcul_prop;; (* Some XXX *)










(* Du rab ! *)
(* L'objectif est de construire la fonction d'évaluation d'un terme en écriture postfixe présentée dans le texte *)
(* La pile utilisée dans l'algo est implémentée par une liste *)
(* Ce que le texte appelle "valeur" et "omegabarre" sont regroupés dans une liste de couples tels que le premier élément du couple est un symbole s et le deuxième la fonction f_s permettant d'interpréter ce symbole ; on considère que les constante sont des fonctions d'arite0. Cette fonction f_s prend en arguments une liste d'éléments du domaine et renvoie un élément du domaine. *)


(* Cette fonction renvoie un couple de listes : (la liste des [k] éléments en sommet de la pile [p] de sorte que le sommet de la pile [p] se trouve en dernière position dans cette liste, la pile [p] une fois qu'on a dépilé ses k éléments du sommet). *)
let depile (k : int) (p : 'a list) : ('a list * 'a list) =
    let rec aux (k : int) (p : 'a list)  (sommet_pile : 'a list) : ('a list * 'a list) =
    match k with
    | 0 -> (sommet_pile, p)
    | i when p = [] ->
        failwith "Liste vide"
    | i ->
        let sommet_modif = (List.hd p) :: sommet_pile in
        let p_modif = List.tl p in
        aux (i - 1) p_modif sommet_modif
    in
    aux k p []
;;

(* Implémentation alternative avec des appels à `Array.sub`. *)
let depile_2 (k : int) (p : 'a list) : ('a list * 'a list) =
    let pa = Array.of_list p in
    let debut = Array.sub pa 0 k in
    let fin   = Array.sub pa k ((Array.length pa) - k) in
    (List.rev (Array.to_list debut)), (Array.to_list fin)
;;


(* Cette fonction prend en entrée une liste [interpretation] de couples (symbole, fonction interprétant ce symbole), un symbole [t] et une liste d'arguments [arg] et renvoie f_t(arg) où f_t est la fonction associée au sympole [t] via [interpretation] *)
let interprete (interpretation : ('a * ('d list -> 'd)) list) (t : 'a) (arg : 'd list) : 'd =
    (List.assoc t interpretation) arg;;


(* Cette fonction prend une liste [l] de symboles que l'on suppose correspondre a l'ecriture postfixe correcte d'un terme, une fonction [arite] : symbole -> entier et une liste [interpretation] d'interpretation des symboles. Elle renvoie le resultat de l'evaluation du terme [l] pour l'interpretation [interpretation] *)
let evalue (l : 'a list) (arite : 'a -> int) (interpretation : ('a * ('d list -> 'd)) list) : 'd =
    let rec aux (l : 'a list) (p : 'd list) : 'd  =
        match l with
        | [] -> List.hd p
        | t :: q  ->
            let k = arite t in
            let (arguments, p_temp) = depile k p in
            let valeur = interprete interpretation t arguments in
            let p_fin = valeur :: p_temp
        in (aux q p_fin)
    in
    aux l [];;


(* Un premier exemple : l'interpretation choisie consiste a evaluer la valeur de verite d'une formule du calcul propositionnel *)

let interp_V _    = true;;
let interp_F _    = false;;
let interp_Non l  = not (List.hd l);;
let interp_Ou l   = (List.hd l) || (List.hd (List.tl l));;
let interp_Et l   = (List.hd l) && (List.hd (List.tl l));;
let interp_ITE l  = if (List.hd l) then (List.hd (List.tl l)) else (List.hd (List.tl (List.tl l)));;

let interp_calcul_prop = [
    (V, interp_V); (F, interp_F);      (* Arité 0 *)
    (Non, interp_Non);                 (* Arité 1 *)
    (Ou, interp_Ou); (Et, interp_Et);  (* Arité 2 *)
    (ITE, interp_ITE)                  (* Arité 3 *)
];;


let ex2 = [F; V; Ou; Non; V; Non; F; Ou; Ou];;
let _ = evalue ex2 arite_calcul_prop interp_calcul_prop;;


(* Un second exemple : l'interpretaion choisie consiste à construire l'arbre syntaxique d'une formule du calcul propositionnel *)

type arbre =
    | FeuilleV | FeuilleF                          (* Arité 0 *)
    | NNon of arbre                                (* Arité 1 *)
    | NEt of arbre * arbre | NOu of arbre * arbre  (* Arité 2 *)
    | NITE of arbre * arbre * arbre                (* Arité 3 *)
;;

let interp_V_a _    = FeuilleV;;
let interp_F_a _    = FeuilleF;;
let interp_Non_a l  = NNon (List.hd l);;
let interp_Ou_a l   = NOu ( (List.hd l), (List.hd (List.tl l) ) );;
let interp_Et_a l   = NEt ( (List.hd l), (List.hd (List.tl l) ) );;
let interp_ITE_a l  = NITE ( (List.hd l), (List.hd (List.tl l) ), (List.hd (List.tl (List.tl l) ) ) );;

let interp_calcul_prop_a = [
    (V, interp_V_a); (F, interp_F_a);      (* Arité 0 *)
    (Non, interp_Non_a);                   (* Arité 1 *)
    (Ou, interp_Ou_a); (Et, interp_Et_a);  (* Arité 2 *)
    (ITE, interp_ITE_a);                   (* Arité 3 *)
];;

let _ = evalue ex2 arite_calcul_prop interp_calcul_prop_a;;
