
Random.self_init ();;
let print = Format.printf;;

print "Chaine de caractere\n";;

print "Chaine avec variables : il faut retenir %%i, %%f, %%s et %%c...\n" ;;
print "\n - %%i pour un entier : %i, " 1 ;;
print "\n - %%f pour un flottant : %f, " 3.1415 ;;
print "\n - %%s pour une string : %s, " "OK?" ;;
print "\n - %%c pour un caractère : %c\n" 'c' ;;

type nim = int array;;

let print_nim =
  Array.iteri (fun case total -> begin
    print "\n%i: " case;
    for j = 1 to total do
      print "! ";
    done;
  end);;

let a = [| 1; 3; 5 |] ;;
print "\n Configuration (a) de la Figure 1 :";
print_nim a;;

let b = [| 1; 3; 2 |] ;;
print "\n Configuration (b) de la Figure 1 :";
print_nim b;;

let somme_nim = ( lxor ) ;;

let somme_nim x y = x lxor y ;;

somme_nim 0 0;; (** = 0 *)
somme_nim 0 1;; (** = 1 *)
somme_nim 1 0;; (** = 1 *)
somme_nim 1 1;; (** = 0 *)

somme_nim 3 5;;  (** 3 xor 5  =  011_2 xor 101_2  = 111_2  = 6  *)
somme_nim 5 9;;  (** 5 xor 9  = 0101_2 xor 1001_2 = 1100_2 = 12 *)
somme_nim 12 1;; (** 12 xor 1 = 1100_2 xor 0001_2 = 1101_2 = 13 *)
somme_nim 12 2;; (** 12 xor 2 = 1100_2 xor 0010_2 = 1110_2 = 14 *)

Array.fold_left ;;

let gamma = Array.fold_left somme_nim 0;;

print "\nGamma(a) = %i" (gamma(a));;
print "\nGamma(b) = %i" (gamma(b));;

exception Pas_de_Strat_Gagnante;;

let next ?(id=0) config =
  let g = gamma config in
  (** La prop. 5 donne directement : si g(s_0) = 0 alors échec. *)
  if g = 0 then raise Pas_de_Strat_Gagnante;
  (** Sinon, on calcul les gamma des fils, et on pointe vers le fils avec un gamma nul. *)
  print "\n\nIl y a une stratégie gagnante :\n";
  (** En pratique, on aurait pas besoin de calculer chaque fils,
      comme on sait que g != 0, et on doit obtenir g' = 0,
      on peut s'arreter au premier coup qui donne g' = 0.
  *)
  let config' = Array.copy config in
  let colonne = ref 0 and
      nb      = ref 1 in
  (** Il suffit d'explorer toutes les configurations accessibles depuis l'état actuel : *)
  for   j = 0 to (Array.length config') - 1 do
    for i = 1 to config'.(j) do
      config'.(j) <- config'.(j) - i;  (** On essaie d'appliquer ce coup. *)
      if (gamma config') = 0 then begin
          (** On a trouvé un coup gagnant, on le stocke. *)
          colonne := j;
          nb := i;
      end;
      config'.(j) <- config'.(j) + i;  (** On annule ce coup. *)
    done;
  done;
  (**  On applique le coup retenu, dernier coup à donner gamma(c') = 0. *)
  print "\nLe joueur courant (numéro %i) doit enlever %i allumette à la %i-ième rangée." id !nb !colonne;
  config'.(!colonne) <- config.(!colonne) - !nb; (** On retire nb allumette sur cette colonne. *)
  (* assert ((gamma config') = 0); (** Si on veut vérifier *)  *)
  config'
;;

try
  print_nim (next ~id:0 a);
with _ -> print "\n\nBlocage durant la simulation 1 (sur a).";;

try
  print_nim (next ~id:1 b);
with _ -> print "\n\nBlocage durant la simulation 2 (sur b).";;

let array_filter pred a =
  Array.of_list (List.filter pred (Array.to_list a));;

let choose a
  = a.(Random.int (Array.length a));;

(** Un adversaire stupide qui joue aléatoirement. *)
let random ?(id=1) config =
  print "\nLe joueur courant (numéro %i) joue aléatoirement.\n" id;
  let indices = array_filter ( fun i -> (config.(i) > 0) ) (Array.init (Array.length config) (fun i -> i)) in
  let i = choose indices in
  print "Le joueur (%i) choisi de regarder la %i-ième rangée.\n" id i;
  let nbAEnlever = 1 + Random.int config.(i) in
  print "Le joueur (%i) choisi d'enlever %i allumettes parmi les %i disponibles.\n" id nbAEnlever config.(i);
  let config' = Array.copy config in
  config'.(i) <- config.(i) - nbAEnlever;
  config';
;;

let a0 = a ;; (* Debut du jeu *)
print_nim a0 ;;
let a1 = random ~id:0 a0 ;;
print_nim a1 ;;
let a2 = random ~id:1 a1 ;;
print_nim a2 ;;
let a3 = random ~id:0 a2 ;;
print_nim a3 ;;
(* ... etc *)

let c = [| 2; 3; 2 |] ;;
let a0 = c ;; (* Debut du jeu *)
print_nim a0 ;;
let a1 = next ~id:0 a0 ;;
print_nim a1 ;;
let a2 = random ~id:1 a1 ;;
print_nim a2 ;;
let a3 = next ~id:0 a2 ;;
print_nim a3 ;;
(* ... etc *)

exception Perdu of int;;

let kpas config id nbPas =
  let id = ref id in
  let config' = ref (Array.copy config) in
  for i = 1 to nbPas do
    print "\nTour numéro %i." i;
    print_nim !config';
    print "\n";
    if (Array.fold_left ( + ) 0 !config') = 0 then raise (Perdu !id);
    begin
      if !id = 0 then (** Le joueur 0 joue bien. *)
        config' := next   ~id:(!id) !config'
      else (** Mais le joueur 1 joue aléatoirement. *)
        config' := random ~id:(!id) !config'
    end;
    id := 1 - !id; (** Juste pour alterner entre 0 et 1 : 0 -> 1, 1 -> 0 *)
  done;
  !config';
;;

let simulation config =
  (** On compte le nombre total d'allumettes. *)
  let n = Array.fold_left (fun i j -> i + j + 1) 0 config in
  (** Puis on lance le joueur 0 avec au plus [n] pas. *)
  kpas config 0 n;
;;

(** Dernière fonction, [nim], qui lance [simulation] et rattrape les exceptions. *)
let nim a =
  let resultat =
    (* try ignore (simulation a) with *)
    try ignore(simulation a); None with
      | Perdu i -> (Some i)
      | Pas_de_Strat_Gagnante -> None
  in
  begin
    match resultat with
    | None -> print "Blocage à cause de la stratégie optimisée.\n\n"
    | Some i -> print "\n ==> Le joueur %i a perdu !\n\n" i
  end;
  resultat
;;

nim a;;

nim b;;

nim c;;

let randomstart k p () = Array.init (1 + Random.int k) (fun i -> 1 + Random.int p);;

let c = randomstart 5 8 ();;
print_nim c;; 

let c = randomstart 5 8 () ;;
print "Configuration random c :" ;;
print_nim c;;
nim c;;

c = randomstart 5 8 () ;;
print "Configuration random c :" ;;
print_nim c ;;
nim c ;;
