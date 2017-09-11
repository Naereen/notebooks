(* # TP 2 - Programmation pour la préparation à l'agrégation maths option info *)
(* - En OCaml. *)

let print = Printf.printf;;
print "\n\tOcaml version %s\n" Sys.ocaml_version;;

(* # Listes *)
(* ## Exercice 1 : `taille` *)

let rec taille (liste : 'a list) : int =
   match liste with
   | [] -> 0
   | _ :: q -> (taille q) + 1
;;

taille [];;
taille [1; 2; 3];;

(* Pas sûr qu'elle soit récursive terminale, alors que celle là oui : *)

let taille (liste : 'a list) : int =
   let rec aux acc = function
       | [] -> acc
       | _ :: q -> aux (acc + 1) q
   in
   aux 0 liste
;;

taille [];;
taille [1; 2; 3];;

(* Solution plus ésotérique : *)

let taille = List.fold_left (fun acc x -> acc + 1) 0;;

taille [];;
taille [1; 2; 3];;

List.length [];;
List.length [1; 2; 3];;

(* ## Exercice 2 : `concat` *)

let rec concatene (liste1 : 'a list) (liste2 : 'a list) : 'a list =
   match liste1 with
   | [] -> liste2
   | h :: q -> h :: (concatene q liste2)
;;

concatene [1; 2] [3; 4];;

(* Autre approche, moins simple mais de même complexité en $\mathcal{O}(n)$. *)

let miroir (liste : 'a list) : 'a list =
   let rec aux acc = function
   | [] -> acc
   | h :: q -> aux (h :: acc) q
   in aux [] liste
;;

let concatene (liste1 : 'a list) (liste2 : 'a list) : 'a list =
   let rec aux acc l1 l2 =
       match l1 with
       | [] when l2 = [] -> acc
       | [] -> aux acc l2 []
       | h :: q -> aux (h :: acc) q l2
   in
   miroir (aux [] liste1 liste2)
;;

concatene [1; 2] [3; 4];;

List.append [1; 2] [3; 4];;


(* ## Exercice 3 : `appartient` *)

let rec appartient x = function
   | [] -> false
   | h :: _ when h = x -> true
   | _ :: q -> appartient x q
;;

appartient 1 [];;
appartient 1 [1];;
appartient 1 [1; 2; 3];;
appartient 4 [1; 2; 3];;

List.mem 1 [];;
List.mem 1 [1];;
List.mem 1 [1; 2; 3];;
List.mem 4 [1; 2; 3];;


(* ## Exercice 4 : `miroir` *)

let miroir (liste : 'a list) : 'a list =
   let rec aux acc = function
   | [] -> acc
   | h :: q -> aux (h :: acc) q
   in aux [] liste
;;

miroir [2; 3; 5; 7; 11];;

List.rev [2; 3; 5; 7; 11];;


(* ## Exercice 5 : `alterne` *)

(* La sémantique n'est pas forcément claire, mais on peut imaginer quelque chose comme ça : *)

let alterne (liste1 : 'a list) (liste2 : 'a list) : 'a list =
   let rec aux acc l1 l2 =
       match (l1, l2) with
       | [], [] -> acc
       | [], ll2 -> acc @ ll2
       | ll1, [] -> acc @ ll1
       | h1 :: q1, h2 :: q2 -> aux (h1 :: h2 :: acc) q1 q2
   in List.rev (aux [] liste1 liste2)
;;

alterne [1; 3; 5] [2; 4; 6];;

(* La complexité est linéaire en $\mathcal{O}(\max(|\text{liste 1}|, |\text{liste 2}|)$. *)

(* Mais on manque souvent la version la plus simple : *)

let rec alterne (l1 : 'a list) (l2 : 'a list) : 'a list =
   match l1 with
   | [] -> l2
   | t::q -> t::(alterne l2 q)
;;


(* ## Exercice 6 : `nb_occurrences` *)

let nb_occurrences (x : 'a) (liste : 'a list) : int =
   let rec aux acc x = function
   | [] -> acc
   | h :: q when h = x -> aux (acc + 1) x q
   | _ :: q -> aux acc x q
   in aux 0 x liste
;;

nb_occurrences 0 [1; 2; 3; 4];;
nb_occurrences 2 [1; 2; 3; 4];;
nb_occurrences 2 [1; 2; 2; 3; 3; 4];;
nb_occurrences 5 [1; 2; 3; 4];;

(* Autre approche, avec un `List.fold_left` bien placé : *)

let nb_occurrences (x : 'a) : 'a list -> int =
   List.fold_left (fun acc y -> if x = y then (acc + 1) else acc) 0
;;

nb_occurrences 0 [1; 2; 3; 4];;
nb_occurrences 2 [1; 2; 3; 4];;
nb_occurrences 2 [1; 2; 2; 3; 3; 4];;
nb_occurrences 5 [1; 2; 3; 4];;


(* ## Exercice 7 : `pairs` *)

(* C'est un filtrage : *)

let pairs = List.filter (fun x -> x mod 2 = 0);;

pairs [1; 2; 3; 4; 5; 6];;
pairs [1; 2; 3; 4; 5; 6; 7; 100000];;
pairs [1; 2; 3; 4; 5; 6; 7; 100000000000];;
pairs [1; 2; 3; 4; 5; 6; 7; 1000000000000000000];;


(* ## Exercice 8 : `range` *)

let range (n : int) : int list =
   let rec aux acc = function
   | 0 -> acc
   | n -> aux (n :: acc) (n - 1)
   in aux [] n
;;

range 30;;

(* Vous avez parfois eu du mal à construire la liste des entiers de a à b
  ca serait bon de savoir le faire car ca peut vous donner des exemples
  d'entree pour vos algos *)

let entiers a b =
 let rec construit x =
   if x > b
   then []
   else x::(construit (x + 1))
 in construit a
;;

let premiers_entiers = entiers 0;; (* Bel exemple de currification *)

entiers 4 10;;
premiers_entiers 7;;

(* ## Exercice 9 : `premiers` *)
(* Plusieurs possibilités. Un filtre d'Erathosthène marche bien, ou une filtration.
   Je ne vais pas utiliser de tableaux donc on est un peu réduit d'utiliser une filtration (filtrage ? pattern matching)
   *)

let racine (n : int) : int =
   int_of_float (floor (sqrt (float_of_int n)))
;;

racine 17;;

let estDivisible (a : int) (b : int) : bool =
   (a mod b) = 0
;;

estDivisible 10 2;;
estDivisible 10 6;;
estDivisible 10 5;;

let range2 (debut : int) (fin : int) (taille : int) : int list =
   let rec aux acc = function
   | n when n > fin -> acc
   | n -> aux (n :: acc) (n + taille)
   in
   List.rev (aux [] debut)
;;

range2 2 12 3;;

(* Une version purement fonctionnelle est moins facile qu'une version impérative avec une référence booléenne (rappel : pas de `break` dans les boucles `for` en OCaml...). *)

let estPremier (n : int) : bool =
   List.fold_left (fun b k -> b && (not (estDivisible n k))) true (range2 2 (racine n) 1)
;;

let premiers (n : int) : int list =
   List.filter estPremier (range2 2 n 1)
;;

premiers 10;;

premiers 100;;


(* Tris *)
(* ---- *)

(* On fera les tris en ordre croissant *)

let test = [3; 1; 8; 4; 5; 6; 1; 2];;

(* Tri insertion *)

let rec insere x = function
  | [] -> [x]
  | t::q ->
    if x <= t then
      x::t::q
    else
      t::(insere x q)
;;

let rec tri_insertion = function
  | [] -> []
  | t::q -> insere t (tri_insertion q)
;;

tri_insertion test;;

(* Complexité en temps O(n2) *)

(* Tri selection *)

let selectionne_min l =
  let rec cherche_min min autres = function
    | [] -> (min, autres)
    | t::q ->
      if t < min then
	cherche_min t (min::autres) q
      else
	cherche_min min (t::autres) q
  in
  match l with
    | [] -> failwith "Selectionne_mion sur liste vide"
    | t::q -> cherche_min t [] q
;;

selectionne_min test;;

let rec tri_selection = function
  | [] -> []
  | l ->
    let (min, autres) = selectionne_min l in
    min::(tri_selection autres)
;;

tri_selection test;;
(* Complexité en temps : O(n2) *)

(* Tri fusion *)

let rec separe = function
  | [] -> ([], [])
  | [x] -> ([x], [])
  | x::y::q -> let (a, b) = separe q in (x::a, y::b)
;;

separe test;;

let rec fusion l1 l2 = match (l1, l2) with
  | (l, []) | ([], l) -> l
  | (x::a, y::b) ->
    if x <= y then
      x::(fusion a (y::b))
    else
      y::(fusion (x::a) b)
;;

fusion [1; 3; 7] [2; 3; 8];;

let rec tri_fusion = function
  | [] -> []
  | [x] -> [x] (* ATTENTION A NE PAS OUBLIER CE CAS *)
  | l -> let (a, b) = separe l in
	 fusion (tri_fusion a) (tri_fusion b)
;;

tri_fusion test;;
(* Complexité en temps O(nlogn) *)


(* # Listes : l'ordre supérieur *)

(* Je ne corrige pas les questions qui étaient traitées dans le TP1. *)

(* ## Exercice 16 : `applique` *)

let rec applique f = function
    | [] -> []
    | h :: q -> (f h) :: (applique f q)
;;


(* ## Exercice 17 *)

let premiers_carres_parfaits (n : int) : int list =
    applique (fun x -> x * x) (entiers 1 n)
;;

premiers_carres_parfaits 12;;


(* ## Exercice 18 : `itere` *)

let rec itere (f : 'a -> unit) = function
    | [] -> ()
    | h :: q -> begin
        f h;
        itere f q
    end
;;


(* ## Exercice 19 *)

let print = Printf.printf

let f x = print "%i\n" x;;

let affiche_liste_entiers (liste : int list) =
    print "Debut\n";
    itere (print "%i\n") liste;
    print "Fin\n"
;;

affiche_liste_entiers [1; 2; 4; 5];;


(* ## Exercice 20 : `qqsoit` et `ilexiste` *)

let rec qqsoit (pred : 'a -> bool) = function
    | [] -> true (* piege ! *)
    | h :: q -> (pred h) && (qqsoit pred q)
    (* le && n'évalue pas le deuxième si le premier argument est false
       donc ceci est efficace et récursif terminal.
    *)
;;

let rec ilexiste (pred : 'a -> bool) = function
    | [] -> false
    | h :: q -> (pred h) || (ilexiste pred q)
    (* le || n'évalue pas le deuxième si le premier argument est true
       donc ceci est efficace et récursif terminal.
    *)
;;

qqsoit (fun x -> (x mod 2) = 0) [1; 2; 3; 4; 5];;

ilexiste (fun x -> (x mod 2) = 0) [1; 2; 3; 4; 5];;


(* ## Exercice 21 : `appartient` version 2 *)

let appartient x = ilexiste (fun y -> x = y);;

let appartient x = ilexiste ((=) x);; (* syntaxe simplifiée par curification *)

let toutes_egales x = qqsoit ((=) x);;

appartient 1 [1; 2; 3];;
appartient 5 [1; 2; 3];;

toutes_egales 1 [1; 2; 3];;
toutes_egales 2 [2; 2; 2];;


(* ## Exercice 22 : `filtre` *)

let rec filtre (pred : 'a -> bool) : 'a list -> 'a list = function
    | [] -> []
    | h :: q when pred h -> h :: (filtre pred q)
    | _ :: q -> filtre pred q
;;

filtre (fun x -> (x mod 2) = 0) [1; 2; 3; 4; 5];;

filtre (fun x -> (x mod 2) != 0) [1; 2; 3; 4; 5];;
filtre (fun x -> (x mod 2) <> 0) [1; 2; 3; 4; 5];; (* syntaxe non conseillée *)


(* ## Exercice 23 *)
(* Je vous laisse trouver pour `premiers`. *)

let pairs = filtre (fun x -> (x mod 2) = 0);;
let impairs = filtre (fun x -> (x mod 2) != 0);;


(* ## Exercice 24 : `reduit` *)

let rec reduit (tr : 'a -> 'b -> 'a) (acc : 'a) (liste : 'b list) : 'a =
    match liste with
    | [] -> acc
    | h :: q -> reduit tr (tr acc h) q
;;

(* Très pratique pour calculer des sommes, notamment. *)


(* ## Exercice 25 : `somme`, `produit` *)

let somme = reduit (+) 0;;

somme [1; 2; 3; 4; 5];;
List.fold_left (+) 0 [1; 2; 3; 4; 5];;

let produit = reduit ( * ) 1;;

produit [1; 2; 3; 4; 5];;
List.fold_left ( * ) 1 [1; 2; 3; 4; 5];;


(* ## Exercice 26 : `miroir` version 2 *)

let miroir = reduit (fun a b -> b :: a) [];;

miroir [2; 3; 5; 7; 11];;

List.rev [2; 3; 5; 7; 11];;

miroir [2.; 3.; 5.; 7.; 11.];;

(* Parcours d'arbres *)
(* ----------------- *)

type arbre_bin = Feuille | Noeud of arbre_bin * arbre_bin;;

type element_parcours = F | N;;

type parcours = element_parcours list;;

let arbre_test = Noeud (Noeud (Noeud (Feuille, Feuille), Feuille), Feuille);;

(* Parcours naifs (complexité quadratique) *)

let rec parcours_prefixe = function
  | Feuille -> [F]
  | Noeud (g, d) -> [N] @ (parcours_prefixe g) @ (parcours_prefixe d)
;;

parcours_prefixe arbre_test;;

let rec parcours_postfixe = function
  | Feuille -> [F]
  | Noeud(g, d) -> (parcours_postfixe g) @ (parcours_postfixe d) @ [N]
;;

parcours_postfixe arbre_test;;

let rec parcours_infixe = function
  | Feuille -> [F]
  | Noeud(g, d) -> (parcours_infixe g) @ [N] @ (parcours_infixe d)
;;

parcours_infixe arbre_test;;

(* Parcours linéaire en la taille de l'arbre *)

(* On ajoute une fonction auxiliaire et un argument vus
   qui est une liste qui stocke les élements observés
   dans l'ordre du parcours *)

let parcours_prefixe2 a =
  let rec parcours vus = function
    | Feuille -> F::vus
    | Noeud(g, d) -> parcours (parcours (N::vus) g) d
  in List.rev (parcours [] a)
;;

parcours_prefixe2 arbre_test;;

let rec parcours_postfixe2 a =
  let rec parcours vus = function
    | Feuille -> F::vus
    | Noeud(g, d) -> N::(parcours (parcours vus g) d)
  in List.rev (parcours [] a)
;;

parcours_postfixe2 arbre_test;;

let rec parcours_infixe2 a =
  let rec parcours vus = function
    | Feuille -> F::vus
    | Noeud(g, d) -> parcours (N::(parcours vus g)) d
  in List.rev (parcours [] a)
;;

parcours_infixe2 arbre_test;;

(* Parcours en largeur *)

let parcours_largeur a =
  let file = Queue.create () in
  let rec parcours () =
    if Queue.is_empty file then
      []
    else
      match Queue.pop file with
	| Feuille -> F::(parcours ())
	| Noeud(g, d) ->
	  (Queue.push g file;
	   Queue.push d file;
	   N::(parcours ()))
  in
  Queue.push a file;
  parcours ()
;;

parcours_largeur arbre_test;;

(* EN REMPLACANT LA FILE PAR UNE PILE AVEC LE MEME ALGO ON
   OBTIENT LE PARCOURS EN PROFONDEUR *)

(* Reconstruction depuis le parcours prefixe *)

let test_prefixe = parcours_prefixe2 arbre_test;;

(* L'idée de cette solution est la suivante :
   j'aimerais une fonction récursive qui fasse le travail;
   le problème c'est que si on prend un parcours prefixe, soit il commence
   par F et l'arbre doit être une feuille; soit il est de la forme N::q
   où q n'est plus un parcours prefixe mais la concaténation de DEUX parcours
   prefixe, on ne peut donc plus appeler la fonction sur q.
   On va donc écrire une fonction qui prend une liste qui contient plusieurs
   parcours concaténé et qui renvoie l'arbre correspondant au premier parcours
   et ce qui n'a pas été utilisé : *)

let reconstruit_prefixe parcours =
  let rec reconstruit = function
    | F::p -> (Feuille, p)
    | N::p ->
      let (g, q) = reconstruit p in
      let (d, r) = reconstruit q in
      (Noeud(g, d), r)
    | [] -> failwith "pacours invalide"
  in
  match reconstruit parcours with
    | (a, []) -> a
    | _ -> failwith "parcours invalide"
;;

reconstruit_prefixe test_prefixe;;
reconstruit_prefixe (N::F::F::test_prefixe);;

(* Reconstruction depuis le parcours en largeur *)

(* Ce n'est pas évident quand on ne connait pas. L'idée est de se servir d'une file
   pour stocker les arbres qu'on reconstruit peu à peu depuis les feuilles. La file
   permet de récupérer les bons sous-arbres quand on rencontre un noeud *)

let largeur_test = parcours_largeur arbre_test;;

let reconstruit_largeur parcours =
  let file = Queue.create () in
  let lire_element = function
    | F -> Queue.push Feuille file
    | N ->
      let d = Queue.pop file in
      let g = Queue.pop file in
      Queue.push (Noeud(g, d)) file
  in
  List.iter lire_element (List.rev parcours);
  if Queue.length file = 1 then
    Queue.pop file
  else
    failwith "parcours invalide"
;;

reconstruit_largeur largeur_test;;

(* Le même algorithme (enfin presque, modulo interversion de g et d)
   avec une pile donne une autre version de la reconstruction du parcours prefixe *)

let reconstruit_prefixe2 parcours =
  let pile = Stack.create () in
  let lire_element = function
    | F -> Stack.push Feuille pile
    | N ->
      let g = Stack.pop pile in
      let d = Stack.pop pile in
      Stack.push (Noeud(g, d)) pile
  in
  List.iter lire_element (List.rev parcours);
  if Stack.length pile = 1 then
    Stack.pop pile
  else
    failwith "parcours invalide"
;;

reconstruit_prefixe2 test_prefixe;;