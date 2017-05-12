(* robots.pdf : texte modélisation 2012

 @date: 12-05-17
 @author: Romain Dubourg
 *)

type etat = int array;;
type liste_rdv = (int array) array;;

(*On crée une fonction "trouve" qui rend la première position de x dans un tableau et -1 sinon.*)

let rec trouve (x:int) (a:int array) (i:int) : (int) =
  match (Array.to_list a) with
    |[] -> -1
    |t::_ when (t=x) -> i
    |_::q -> trouve x (Array.of_list q) (i+1);;

(*On crée une fonction "rdv" qui pour un état du système nous rend la liste des paires de robots pouvant réaliser un rendez-vous.*)

let rdv (u:etat) : ((int*int) list) = 
  let ls = ref [] in
  let n = Array.length u in
  for k=0 to n-1 do
    let i = (trouve u.(k) (Array.sub u (k+1) (n-(k+1))) 0) in
      if (i>=0) then
	ls := (k,i+k+1)::!ls;
  done;
   !ls;;

(*On crée une fonction "realise_rdv" qui étant donné un état et une paire de robots pouvant réaliser un rendez-vous, le réalise.*)

let realise_rdv ((i1,i2):int*int) (u:etat) (l:liste_rdv) : (etat) =
  u.(i1) <- (((u.(i1)+1) mod (Array.length l.(i1))));
  u.(i2) <- (((u.(i2)+1) mod (Array.length l.(i2))));
  u;;

(*On crée la fonction principale "transition" qui à partir d'un état calcule l'étal suivant.*)

let transition (u1:etat) (l:liste_rdv) : (etat) =
  let ls = rdv u1 in
  let rec aux (u2:etat) (l1:(int*int) list) (l2:liste_rdv) : (etat) =
    match l1 with
      |[] -> u2
      |t::q -> aux (realise_rdv t u2 l2) q l2 in
    aux u1 ls l;;

(*On crée la fonction "n_transitions" qui effectue n transitions successives.*)

let rec n_transitions (u:etat) (l:liste_rdv) (n:int) : (etat) =
  if (n=0) then u
  else n_transitions u l (n-1);;




(*TESTS*)

let ex1 = [| [|0;1;2|]; [|0|]; [|1;3|]; [|2;3|] |];;
let ex1_1 = [| 0;0;1;2 |];;
let ex1_2 = [| 0;0;3;2 |];;

let _ = transition ex1_1 ex1
let _ = n_transitions ex1_1 ex1 4
