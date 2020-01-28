(* Arbre binaire de recherche*)

type ('a, 'b) abr = Leaf | Node of ('a, 'b) node
and ('a, 'b) node = {ls : ('a, 'b) abr;
                     key : 'a;
                     value : 'b;
                     rs : ('a, 'b) abr}

let tree_1 = Node { ls = Node {
                             ls = Node {
                                      ls = Leaf;
                                      key = 1;
                                      value = 2;
                                      rs = Leaf};
                             key = 3;
                             value = 1;
                             rs = Node {
                                      ls = Leaf;
                                      key = 4;
                                      value = 5;
                                      rs = Leaf}};
                    key = 6;
                    value = 2;;
                    rs = Node {
                             ls = Leaf;
                             key = 7;
                             value = 3;
                             rs = Leaf}};;
                              
                      
let rec treat treat_leaf treat_node a tree =
  match tree with
    Leaf -> treat_leaf () 
  | Node n -> if a = n.key then treat_node n
              else if a < n.key then treat treat_leaf treat_node a n.ls
              else treat treat_leaf treat_node a n.rs;;
(* Complexité : hauteur de l'arbre 
 Meilleur des cas O(1), pire cas O(n) on peut rien dire de plus si pas équilibré. 
 Meme coplexite pour les autres fonctions*)
                         
let trouve = treat (fun () -> failwith "arbre vide") (fun n -> n.value);;
                
let insert a b tree = treat
                        (fun () -> Node {ls = Leaf; key = a; value = b; rs = Leaf})
                        (fun n -> Node {ls = n.ls; key = a; value = b; rs = n.rs})
                        a tree;;

let rec split_min tree =
  match tree with
    Leaf -> failwith "arbre vide"
  | Node n -> match n.ls with
                Leaf -> (n.rs, n.key, n.value)
              | Node m -> let (l, k, v) = split_min n.ls in
                          (Node {ls = l; key = n.key; value = n.value; rs = n.rs}, k, v);;

let del = treat
            (fun () -> Leaf)
            (fun n -> match n.rs with
                        Leaf -> n.ls
                      | Node m -> let (l,k,v) = split_min n.rs in
                                  (Node {ls = n.ls; key = k; value = v; rs =  l}));;

            
(* let fusion tree_1 tree_2 ...  a faire *)
            
(* Avantage : Recherche en O(ln(n)) si équilibré*)
(* Inconvénients : pas nécessairement équilibré: si on insere les valeurs par clés croissantes par exemple *)
(* Autre structure de données: les AVL qui sont des arbres binaires de recherche équilibrés*)
