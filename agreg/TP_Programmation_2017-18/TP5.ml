type graphe_mat = bool array array
type sommet = int

let nb_sommets (g:graphe_mat) : int = Array.length g

let ajoute_arc (g:graphe_mat) (i:sommet) (j:sommet) : unit =
  assert (0<= i && i<nb_sommets g);
  assert (0<= j && j<nb_sommets g);
  g.(i).(j) <- true;
  g.(j).(i) <- true

(* Faux à cause du partage de [ligne] en mémoire
let vide (taille:int) : graphe_mat =
  let ligne = Array.make taille false in
  Array.make taille ligne *)

(* Crée un triangle
let vide (taille:int) : graphe_mat =
  Array.init taille (fun i -> Array.make i false)
 *)

let vide (taille:int) : graphe_mat =
  Array.init taille (fun i -> Array.make taille false)

(* une autre version plus simple *)
let vide (taille:int) : graphe_mat =
  Array.create_matrix taille taille false

(* test si la matrice est bien symmétrique *)
let valide (g:graphe_mat) : bool =
  let n = nb_sommets g in
  let b = ref true in
  for i=0 to n-1 do
    for j=0 to i do
      b := !b && (g.(i).(j)=g.(j).(i))
    done
  done;
  !b

(* version sans référence *)
let array_forall (f:int -> 'a -> bool) (t:'a array) : bool =
  let rec aux i = if i>=0 then f i t.(i) && aux (i-1) else true in
  aux (Array.length t -1)

let valid (g:graph_mat) : bool =
  array_forall
    (fun (i:int) (ligne:bool array) ->
     array_forall
       (fun (j:int) (b:bool) -> b = g.(j).(i))
       ligne)
    g


let count_edge (g:graph_mat) : int =
  let n = count_vertex g in
  let nb = ref 0 in
  for i=0 to n-1 do
    for j=0 to i do
      if g.(i).(j) then incr nb (* nb := !nb + 1 *)
    done
  done;
  !nb

let degre_noeud (g:graphe_mat) (n:sommet) : int  =
  let nb = ref 0 in
  let ligne = g.(n) in
  for i=0 to (nb_sommets g) -1 do
    if ligne.(i) then incr nb
  done;
  !nb

let degre (g:graphe_mat) : int array =
  Array.init (nb_sommets g) (degre_noeud g)

let ex1 =
  let g1 = vide 9 in
  ajoute_arc g1 1 2;
  ajoute_arc g1 1 4;
  ajoute_arc g1 1 5;
  ajoute_arc g1 2 3;
  ajoute_arc g1 2 5;
  ajoute_arc g1 3 6;
  ajoute_arc g1 5 6;
  ajoute_arc g1 7 8;
  ajoute_arc g1 8 0;
  g1

let _ = valide ex1

let _ = nb_arcs ex1

let _ = degre ex1

type graphe_adj = int list array
type sommet = int

let nb_sommets (g:graphe_adj) : int = Array.length g

let ajoute_arc (g:graphe_adj) (i:sommet) (j:sommet) : unit =
  assert (0<= i && i<nb_sommets g);
  assert (0<= j && j<nb_sommets g);
  g.(i) <- j :: g.(i);
  g.(j) <- i :: g.(j)


let vide (taille:int) : graphe_adj =
  Array.init taille (fun i -> [])

(* test si la matrice est bien symmétrique *)
let array_forall (f:int -> 'a -> bool) (t:'a array) : bool =
  let rec aux i = if i>=0 then f i t.(i) && aux (i-1) else true in
  aux (Array.length t -1)

let valide (g:graphe_adj) : bool =
  array_forall
    (fun (i:int) (ligne:int list) ->
     List.for_all
       (fun (j:int) -> List.mem i g.(j))
       ligne)
    g


let nb_arcs (g:graphe_adj) : int =
  let n = nb_sommets g in
  let nb = ref 0 in
  for i=0 to n-1 do
    nb := !nb + List.length g.(i)
  done;
  !nb/2 (* ne marche pas si on accepte les graphes
          avec des sommets reliés à eux-même *)

let degre_noeud (g:graphe_adj) (n:sommet) : int  =
  List.length g.(n)

let degre (g:graphe_adj) : int array =
  Array.init (nb_sommets g) (degre_noeud g)

let ex1 =
  let g1 = vide 9 in
  ajoute_arc g1 1 2;
  ajoute_arc g1 1 4;
  ajoute_arc g1 1 5;
  ajoute_arc g1 2 3;
  ajoute_arc g1 2 5;
  ajoute_arc g1 3 6;
  ajoute_arc g1 5 6;
  ajoute_arc g1 7 8;
  ajoute_arc g1 8 0;
  g1

let _ = valide ex1

let _ = nb_arcs ex1

let _ = degre ex1


(* parcours en profondeur - version recursive *)
let dfs_rec (g:graphe_adj) (debut:sommet) : unit =
  let vu = Array.make (nb_sommets g) false in
  let rec visite (i:sommet) =
    Printf.printf "visite(%d)\n" i;
    vu.(i) <- true;
    List.iter (fun j -> if not vu.(j) then visite j) g.(i)
  in
  visite debut

let _ = dfs_rec ex1 1

let dfs_rec (g:graphe_adj) (sommet_debut:sommet) : unit =
  let vu = Array.make (nb_sommets g) false in
  let debut = Array.make (nb_sommets g) 0 in
  let fin = Array.make (nb_sommets g) 0 in
  (* pere dans l'arbre couvrant *)
  let pere = Array.make (nb_sommets g) (-1) in
  let date = ref 0 in
  let rec visite (i:sommet) =
    Printf.printf "visite(%d)\n" i;
    vu.(i) <- true;
    incr date;
    debut.(i) <- !date;
    List.iter (fun j -> if not vu.(j) then
			  begin
			    pere.(j) <- i;
			    visite j
			  end
			else if pere.(i)<>j then
			  Printf.printf "cycle détecté en %d\n" i
	      ) g.(i);
    incr date;
    fin.(i) <- !date
  in
  visite sommet_debut;
  for i=0 to nb_sommets g -1 do
    Printf.printf "interval(%d)=[%d,%d]\n" i debut.(i) fin.(i);
    Printf.printf "pere(%d)=%d\n" i pere.(i)
  done

let _ = dfs_rec ex1 1

let composantes_connexes g =
  let vu = Array.make (nb_sommets g) false in
  let cc_courante = ref [] in
  let rec visite (i:sommet) =
    Printf.printf "visite(%d)\n" i;
    vu.(i) <- true;
    cc_courante := i :: !cc_courante;
    List.iter (fun j -> if not vu.(j) then visite j) g.(i)
  in
  let cc = ref [] in
  for i=0 to nb_sommets g -1 do
    if not vu.(i) then
      begin
	visite i;
	cc := !cc_courante :: !cc;
	cc_courante := []
      end
  done;
  !cc

let _ = composantes_connexes ex1

(* parcours en profondeur - version iterative *)
let dfs_iter (g:graphe_adj) (debut:sommet) : unit =
  let vu = Array.make (nb_sommets g) false in
  let pile = Stack.create () in
  Stack.push debut pile;
  vu.(debut) <- true;
  while not (Stack.is_empty pile) do
    let i = Stack.pop pile in
    Printf.printf "visite(%d)\n" i;
    List.iter (fun j -> if not vu.(j) then
			  begin
			    Stack.push j pile;
			    vu.(j) <- true
			  end) g.(i)
  done

let _ = dfs_iter ex1 1
