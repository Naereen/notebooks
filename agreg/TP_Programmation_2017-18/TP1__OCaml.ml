(************ 3 Recursivite *************)

(** Exo 8 **)

let rec factoriel = function
  | 0 -> 1
  | n -> n * factoriel ( n - 1 );;

let rec factoriel = fun n ->
  match n with
  | 0 -> 1
  | n -> n * factoriel ( n - 1 );;

let rec factoriel (n:int) : int =
  match n with
  | 0 -> 1
  | n -> n * factoriel ( n - 1 );;

let rec factoriel (n:int) : int =
  if n = 0
  then 1
  else n * factoriel ( n - 1 );;

(* tests *)
let _ = factoriel 4;;
let _ = factoriel 0;;


(** Exo 9 **)

(* Remarque: si a>b alors pgcd a b = pgcd (a-b) b *)
let rec pgcd (a:int) (b:int) : int =
  if a = b
  then a
  else
    if (a > b)
    then pgcd (a-b) b
    else pgcd a (b-a);;

  (* tests *)
let _ = pgcd 16 1024;;
let _ = pgcd 25 130;;


(** Exo 10 *)

(* fonction naive *)
let rec fibonacci (n:int) : int =
  match n with
  | 0 -> 1
  | 1 -> 1
  | n -> fibonacci (n-1) + fibonacci (n-2);;

(* tests *)
let _ = fibonacci 5;;
let _ = fibonacci 17;;


let fibo_lin (n:int) : int =
  (* invariant:
       m >= 1
       u = fibo(n-m+1)
       v = fibo(n-m)
       aux m u v = fibo(n) *)
  let rec aux (m:int) (u:int) (v:int) : int =
    assert (m>0);
    if m = 1 then u
    else aux (m-1) (u+v) u
  in aux n 1 1;;

(* tests *)
let _ = fibo_lin 5;;
let _ = fibo_lin 17;;


(* Comparaison des rapidite d'execution *)

let _ =
  let c = Sys.time() in
  let _ = fibonacci 40 in
  print_float ( Sys.time() -. c);;

let _ =
  let c = Sys.time() in
  let _ = fibo_lin 40 in
  print_float ( Sys.time() -. c);;


(** Exo 11 **)
(* *)
let rec itere (f:'a -> 'a) (n:int) : 'a -> 'a =
  match n with
  | 0 -> (fun x -> x);
  | n -> (fun x -> f (itere (f) (n-1) x));;

(* tests *)
let _ = itere (function x->x+1) 10 0;;
let _ = itere (function x->x/2) 4 1024;;



(** Exo 12 **)

let rec hanoi (n:int) (a:string)(b:string)(c:string) : unit =
  if n>1 then
    hanoi (n-1) a c b
  else ();
  print_string a;
  print_string " -> ";
  print_endline c;
  if n>1 then
    hanoi (n-1) b a c
  else ();
  ;;

let _ = hanoi 3 "a" "b" "c"

(* exception levee quand le nombre de disques ets a 0 *)
exception PasDeDisque;;

(*affiche a l'ecran les deplacement pour deplacer n disques de T1 vers T3 en s'aidant de T2 *)
let rec hanoi t1 t2 t3 = function
  | 0 -> raise PasDeDisque
  | 1 -> print_string (t1^" -> "^t3^"\n")
  | n ->
    hanoi t1 t3 t2 (n-1);(* on en deplace n-1 disques de T1 vers T2 en s'aidant de T3*)
    print_string (t1^" -> "^t3^"\n");(* puis on en deplace n-1 disquesLe plus grand disque de T1 vers T3*)
    hanoi t2 t1 t3 (n-1);(* efin on en deplace les n-1 disques de T2 vers T3 en s'aidant de T1*)
;;

(*
  # hanoi "T1" "T2" "T3" 3;;
  T1 -> T3
  T1 -> T2
  T3 -> T2
  T1 -> T3
  T2 -> T1
  T2 -> T3
  T1 -> T3
  - : unit = ()
*)


(**************** 4 Listes ***************)

(** Exo 13 **)

let rec concatenation l1 l2 =
  match l1 with
    | [] -> l2
    | t :: q -> t :: (concatenation q l2);;
(*
  # concatenation [1;2;3;4] [5;6;7;8];;
  - : int list = [1; 2; 3; 4; 5; 6; 7; 8]
*)

(** Exo 14 **)

let rec applique l f =
  match l with
    | [] -> []
    | t :: q -> (f t)::(applique q f);;
(*
  # applique [0;1;2;3;4;5] (function x -> x+1);;
  - : int list = [1; 2; 3; 4; 5; 6]
*)

(** Exo 15 **)

let liste_carre = (function l -> applique l (function x -> x*x));;

(*
  # liste_carre [1;2;3;4;5];;
  - : int list = [1; 4; 9; 16; 25]
*)

(** Exo 16 **)
let rec miroir_quad = function
  | [] -> []
  | a :: q -> (miroir_quad q)@[a];;

let miroir_lineaire l =
  (* sous fonctions utilisant un deuxieme argument d'accumulation du resultat *)
  let rec miroir l accu =
    match l with
      | [] -> accu
      | a :: q -> miroir q (a::accu)
  in
  miroir l [];;

(*
  # let c = Sys.time() in let l = miroir_quad [1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20] in print_float (Sys.time() -.c);l;;
  4.70000000021e-05- : int list =
  [20; 19; 18; 17; 16; 15; 14; 13; 12; 11; 10; 9; 8; 7; 6; 5; 4; 3; 2; 1]
  #  let c = Sys.time() in let l = miroir_lineaire [1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20] in print_float (Sys.time() -.c);l;;
  6.99999999654e-06- : int list =
  [20; 19; 18; 17; 16; 15; 14; 13; 12; 11; 10; 9; 8; 7; 6; 5; 4; 3; 2; 1]
*)


(** Exo 17 **)

let rec insertionDansListeTriee l x =
  match l with
      [] -> [x]
    | t :: q when t < x -> t :: ( insertionDansListeTriee q x)
    | _ -> x::l;;

let triInsertion l =
  let rec tri l accu =
    match l with
	[] -> accu
      | t :: q -> tri q (insertionDansListeTriee accu t)
  in
  tri l [];;

(*
  # triInsertion [1;9;6;7;3;4;5;8;2;0];;
  - : int list = [0; 1; 2; 3; 4; 5; 6; 7; 8; 9]
*)

(** Exo 18 **)

(*
  Pour un ordre :
  * x < y => ordre x y = -1
  * x = y => ordre x y = 0
  * x > y => ordre x y =1
*)
let rec insertionDansListeTrieeOrdre l x ordre =
  match l with
      [] -> [x]
    | t :: q when ((ordre t x) < 0) -> t :: ( insertionDansListeTrieeOrdre q x ordre)
    | _ -> x::l;;

let triInsertionOrdre l ordre =
  let rec tri l accu =
    match l with
	[] -> accu
      | t :: q -> tri q (insertionDansListeTrieeOrdre accu t ordre)
  in
  tri l [];;

let ordreDecroissant x y =
  if x > y
  then -1
  else
    if x=y
    then 0
    else 1;;

(*
  #  triInsertionOrdre [1;9;6;7;3;4;5;8;2;0] ordreDecroissant;;
  - : int list = [9; 8; 7; 6; 5; 4; 3; 2; 1; 0]
*)


(******************* 5 Exponentiation rapide *****************)

(** Exo 19 **)

let rec puiss x = function
  | 0 -> 1
  | n -> x * (puiss x (n-1));;

(*
  # puiss 3 3;;
  - : int = 27

  complexite: O(n)
*)


(** Exo 20 *)
let rec puissRapide x = function
  | 0 -> 1
  | n when (n mod 2) = 0 -> puissRapide (x*x) (n/2)
  | n -> (puissRapide (x*x) (n/2)) * x
;;
(*
# puissRapide 3 3;;
- : int = 27
# puissRapide 3 6;;
- : int = 729
*)

let rec puissDivRegner x = function
  | 0 -> 1
  | n when (n mod 2) = 0 -> (puissDivRegner x (n/2))*(puissDivRegner x (n/2))
  | n -> (puissDivRegner x (n/2))*(puissDivRegner x (n/2)) * x;;

(*
  # puissDivRegner 3 6;;
  - : int = 729

  * Ca n'est pas equivalent en complexite:
  * expo rapide O(log n)
  * div pr regner O(n)

  * C'est equivalent si plutot que de faire:
  * (puissDivRegner x (n/2))*(puissDivRegner x (n/2))
  * on fait:
  * let y=(puissDivRegner x (n/2)) in y*y;
*)


(** Exo 21 **)

(* le type monoide *)
type 'a monoide = { mult : 'a-> 'a -> 'a; neutre : 'a };;

let floatMonoide = {
  mult = (function x ->(function y -> x*.y));
  neutre = 1.
};;


let matrixMonoide n =
  {
    mult =
      (function x ->
	function y ->
	  let z = Array.make_matrix n n 0 in
	  for i = 0 to n-1 do
	    for j = 0 to n-1 do
	      for k = 0 to n-1 do
		z.(i).(j) <- z.(i).(j) + x.(i).(k) * y.(k).(j)
	      done
	    done
	  done;
	  z
      );
    neutre =
      let z = Array.make_matrix n n 0 in
      for i = 0 to n-1 do
	  z.(i).(i) <- 1
      done;
      z
  };;


(** Exo 22 **)

let rec exp_rapide m x = function
  | 0 -> m.neutre
  | n -> m.mult (exp_rapide m x (n-1)) x;;

(** Exo 23 **)

let exp_float x n = exp_rapide floatMonoide x n;;
let exp_mat x n = exp_rapide (matrixMonoide (Array.length x)) x n;;

(** Exo 24 *)

let monoideFonction = {
  mult = (function f -> function g -> function x -> f (g x) );
  neutre = function x -> x
}

let itereMonoide f n = exp_rapide monoideFonction f n;;

(*
  # itereMonoide (function x->x+1) 10 0;;
  - : int = 10
*)


(***************** 6 Formules du calcul propositionnel **********)

(** Exo 25 **)
type variable = string;;
type formule =
    V of variable
  | Not of formule
  | Conj of formule * formule
  | Disj of formule * formule;;

(** Exo 26 **)

let rec taille = function
  | V(_) -> 1
  | Not(f) -> 1 + (taille f)
  | Conj(f,g) -> 1 + (taille f) + (taille g)
  | Disj(f,g) -> 1 + (taille f) + (taille g);;

(** Exo 27 **)

let rec formule_to_string = function
  | V(p) -> p
  | Not(f) -> "not "^(formule_to_string f)
  | Conj(f,g) -> "("^(formule_to_string f)^" ^ "^(formule_to_string g)^")"
  | Disj(f,g) -> "("^(formule_to_string f)^" v "^(formule_to_string g)^")"
 ;;

let affiche f = print_string ((formule_to_string f)^"\n");;

let f = (Conj(Not(V("p")),Disj(Conj(V("q"),Not(V("p"))),Disj(V("r"),V("q")))));;
(*
  # affiche f;;
  (not p ^ ((q ^ not p) v (r v q)))
  - : unit = ()
*)

(** Exo 28 **)

let rec eval v = function
  | V(x) -> v(x)
  | Not(f) -> not (eval v f)
  | Conj(f,g) -> (eval v f) && (eval v g)
  | Disj(f,g) -> (eval v f) || (eval v g);;

let valuFalse = function
  | "p" -> true
  | "q" -> false
  | "r" -> false
  | _ -> false;;

let valuTrue =  function
  | "p" -> false
  | "q" -> false
  | "r" -> true
  | _ -> false;;



(*
  # eval valuFalse f;;
  - : bool = false
  # eval valuTrue f;;
  - : bool = true
*)


(** Exo 24 **)

let rec inserUneFois x = function
  | [] -> [x]
  | t :: q when (x=t) -> t::q
  | t :: q -> t::(inserUneFois x q);;


let recuperVariable f =
  let rec recup l = function
    | V(x) -> inserUneFois x l
    | Not(f) -> recup l f
    | Conj(f,g) -> recup (recup l f) g
    | Disj(f,g) -> recup (recup l f) g
  in
  recup [] f;;

let rec nouvelleValu v = function
  | [] -> v
  | t :: q ->
    if (v t)
    then let nv x =
	   if (x=t)
	   then false
	   else v x in
	 nouvelleValu nv q
    else function x -> if (x=t) then true else v x;;

let rec isTrue v = function
  | [] -> true
  | t :: q -> if v t then isTrue v q else false;;


let rec valuToString v = function
  | [] -> ""
  | t :: q -> (if v t then "1" else "0")^" "^(valuToString v q);;

let rec printVariableList = function
  | [] -> print_string "| "
  | t :: q -> print_string (t^" "); printVariableList q;;

let tableVerite f =
  let variables = recuperVariable f in
  let valu = ref (function _ -> false) in
  printVariableList variables;
  affiche f;
  while not (isTrue (!valu) variables)
  do
    print_string ( (valuToString (!valu) variables)^"| "^(if eval (!valu) f then "1" else "0")^"\n");
    valu := nouvelleValu (!valu) variables
  done
;;

(*
  # tableVerite f;;
  p q r | (not p ^ ((q ^ not p) v (r v q)))
  0 0 0 | 0
  1 0 0 | 0
  0 1 0 | 1
  1 1 0 | 0
  0 0 1 | 1
  1 0 1 | 0
  0 1 1 | 1
  - : unit = ()
*)


(******************* 7 Modules et foncteurs ******************)

(** Exo 30 **)
module type MONOIDE = sig
  type element
  val neutre: element
  val mult: element -> element -> element
end;;


module Exp = functor (M:MONOIDE) -> struct
  let rec expo_rapide x = function
    | 0 -> M.neutre
    | 1 -> x
    | n when (n mod 2 = 0) ->
     let a = expo_rapide x (n / 2) in
     M.mult a a
    | n ->
     let a = expo_rapide x (n / 2) in
     M.mult x (M.mult a a)
end;;
module N = struct
  type element = int
  let neutre = 1
  let mult = ( * )
end;;
module R = struct
  type element = float
  let neutre = 1.
  let mult = ( *. )
end;;
module Exp_entiers = Exp(N);;
let exp_entiers = Exp_entiers.expo_rapide;;
module Exp_flottants = Exp(R);;
let exp_float = Exp_flottants.expo_rapide;;
exp_entiers 3 3;;
exp_float 3. 3;;
