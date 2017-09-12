(** Arbres binaires de recherche **)

(* exercice 1 *)
type 'a abr =
  | Leaf
  | Node of 'a anode
and 'b anode =
  { key: int;
    value: 'b;
    left: 'b abr; (* pour toute clé [k] dans [left], [k] < [key] *)
    right: 'b abr (* pour toute clé [k] dans [right], [key] < [k] *)
  }

(* variante non polymorphe et sans utilisation d'enregistrement pour
   nommer les champs
type abr =
  | Leaf
  | Node of (int * string * abr * abr)
 *)

let rec nb_keys (a: 'a abr) : int =
  match a with
  | Leaf -> 0
  | Node n -> 1 + nb_keys n.left + nb_keys n.right

(*
let rec nb_keys a =
  match a with
  | Leaf -> 0
  | Node (key, value, left, right) -> 1 + nb_keys left + nb_keys right
 *)

let a1 =
  Node { key=1; value="un"; left=Leaf; right=Leaf }

(*
let a1 = Node (1,"un",Leaf,Leaf)
 *)

let a2 =
  Node { key=2; value="deux"; left=a1; right=Leaf }
(*
  let a2 = Node (2,"deux",a1,Leaf)
 *)

(* exercice 2 *)

let rec trouve (a: 'a abr) (k:int) : 'a option =
  match a with
  | Leaf -> None
  | Node n when k=n.key -> Some n.value
  | Node n when k < n.key -> trouve n.left k
  | Node n -> trouve n.right k

let _ = trouve a2 1
let _ = trouve a2 3

let rec trouve2 (a: 'a abr) (k:int) : 'a =
  match a with
  | Leaf -> failwith "key not found"
  | Node n when k=n.key -> n.value
  | Node n when k < n.key -> trouve2 n.left k
  | Node n -> trouve2 n.right k

let _ = trouve2 a2 1
let _ = trouve2 a2 3

(* exercice 3 *)

let rec insere (a: 'a abr) (k:int) (v:'a) : 'a abr =
  match a with
  | Leaf -> Node { key=k; value=v; left=Leaf; right=Leaf }
  | Node n when k=n.key ->
     Node { n with value = v; key = k}
  | Node n when k < n.key ->
(*
     Node { key = n.key;
            value = n.value;
            left = insere n.left k v
            right = n.right }
 *)
     Node {n with left = insere n.left k v}
  | Node n ->
     Node {n with right = insere n.right k v}

let _ = trouve (insere (insere Leaf 2 "deux") 1 "un") 1
let _ = trouve (insere (insere Leaf 2 "deux") 1 "un") 2
let _ = trouve (insere (insere Leaf 2 "deux") 1 "un") 3

(* exercice 4 *)

(* [min a] renvoie le couple [(key,value)] de l'arbre [a]
   avec [key] minimal dans [a].
   Lance une exception si [a] est vide *)
let rec min (a: 'a abr) : int * 'a =
  match a with
  | Leaf -> failwith "empty tree"
  | Node n ->
     if n.left = Leaf then (n.key, n.value)
     else min n.left

let _ = min (insere (insere Leaf 2 "deux") 1 "un")

let rec delete (a: 'a abr) (k:int) : 'a abr =
  match a with
  | Leaf -> Leaf
  | Node n when k=n.key ->
     if n.right = Leaf
     then n.left
     else
       let (k_min,v) = min n.right in
       Node { key = k_min;
	      value = v;
	      left = n.left;
	      right = delete n.right k_min }
  | Node n when k < n.key ->
     Node {n with left = delete n.left k}
  | Node n ->
     Node {n with right = delete n.right k}

let _ = trouve
	  (delete
	     (insere (insere Leaf 2 "deux") 1 "un") 1)
	  1
let _ = trouve
	  (delete
	     (insere (insere Leaf 2 "deux") 1 "un") 1)
	  2

(* exercice 5 *)

(* [split a k] sépare l'arbre [a] en deux arbres [(a1,a2)]
   tels que l'union des clés-valeurs de a1 et a2 est égale à
   l'ensemble des clés-valeurs de a (privé de l'association
   liée à [k] si elle était présente dans [a]).
   Les clés de [a1] sont < à [k].
   Les clés de [a2] sont > à [k].  *)

let rec split (a: 'a abr) (k:int) : ('a abr) * ('a abr) =
  match a with
  | Leaf -> (Leaf, Leaf)
  | Node n when k = n.key -> (n.left, n.right)
  | Node n when k < n.key ->
     let (left1,left2) = split n.left k in
     (left1, Node {n with left = left2})
  | Node n ->
     let (right1,right2) = split n.right k in
     (Node {n with right = right1}, right2)

(* si une clé est présente dans les deux arbres, nous gardons
   celle de [a1] *)
let rec fusion (a1: 'a abr) (a2: 'a abr) : 'a abr =
  match a1 with
  | Leaf -> a2
  | Node n ->
     let (left2,right2) = split a2 n.key in
     Node {n with left=fusion n.left left2;
		  right=fusion n.right right2}

let a1 = insere (insere Leaf 2 "deux") 1 "un"

let a2 = insere (insere Leaf 2 "two") 3 "trois"

let _ = trouve (fusion a1 a2) 1
let _ = trouve (fusion a1 a2) 2
let _ = trouve (fusion a1 a2) 3
let _ = trouve (fusion a1 a2) 4

let _ =
  ()
















































(* Union find *)
(* Les connaisseurs pourront implémenter cette partie dans un module dédié *)

(* Version simple *)

type representant = Aucun | Element of int;;

type unionfind = representant array;;

let create_uf n = Array.make n Aucun;;

let makeset uf i =
  if uf.(i) = Aucun then
    uf.(i) <- Element i
  else
      failwith "Element deja present"
;;

let union uf i j =
  let n = Array.length uf in
  if (uf.(i) = Aucun || uf.(j) = Aucun) then
    failwith "Element absent";
  for k = 0 to (n - 1) do
    if uf.(k) = Element j then
      uf.(j) <- Element i
  done
;;

let find uf i = match uf.(i) with
  | Aucun -> failwith "Element absent"
  | Element i -> i;;
;;

(* Version avancée *)

type position = Aucun | Racine | Fils of int;;

type unionfind = position array;;

let create_uf n = Array.make n Aucun;;

let makeset uf i =
  if uf.(i) = Aucun then
    uf.(i) <- Racine
  else
    failwith "Element deja present"
;;

let rec find uf i = match uf.(i) with
  | Aucun -> failwith "Element absent"
  | Fils j ->
    let racine = find uf j in
    uf.(i) <- Fils racine;
    racine
  | Racine -> i
;;

let union uf i j =
  if (uf.(i) = Aucun || uf.(j) = Aucun) then
    failwith "Element absent"
  else
    let racinei = find uf i in
    uf.(racinei) <- Fils j
;;

(* Tests de Union find *)

let uf_test = create_uf 6;;
for i = 0 to 5 do
  makeset uf_test i
done;;
uf_test;;
find uf_test 5;;
union uf_test 1 2;;
uf_test;;
union uf_test 2 5;;
uf_test;;
find uf_test 0;;
uf_test;;
find uf_test 1;;
uf_test;;
find uf_test 1 = find uf_test 5;;
find uf_test 1 = find uf_test 4;;

(* Representations de graphe pondérés *)

type poids = int;;

type arete = Absent | Present of poids;;
type graphe_matrix = arete array array;;

type graphe_list = ((int * poids) list) array;;

let taille_graphe = Array.length;; (*nb sommets*)

let liste_aretes gl =
  let resultat = ref [] in
  let n = taille_graphe gl in
  let rec traitement_liste i = function (* c'est un List.iter... *)
    | [] -> ()
    | (j, p)::q -> (resultat := (i, j, p)::!resultat;
		    traitement_liste i q)
  in
  for i = 0 to (n - 1) do (* c'est un Array.iter *)
    traitement_liste i gl.(i)
  done;
  !resultat
;;

let graphe_test =
  [| [(1, 11); (2, 2); (3, 1)];
     [(2, 7)];
     [];
     [(4, 5)];
     [(1, 1)]
  |]
;;

liste_aretes graphe_test;;

(* Algorithme de Kruskal *)

let kruskal gl =
  let aretes = liste_aretes gl in
  let aretes = List.sort (function (_, _, x) -> function (_, _, y) -> x - y) aretes in
  let n = taille_graphe gl in
  let uf = create_uf n in
  let result = ref [] in
  let traitement_arete (i, j, p) =
    if not (find uf i = find uf j) then
      begin
	result := (i, j, p)::!result;
	union uf i j
      end
  in
  for i = 0 to (n - 1) do
    makeset uf i
  done;
  List.iter traitement_arete aretes;
  !result
;;

kruskal graphe_test;;
