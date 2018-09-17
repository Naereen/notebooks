(*
This OCaml script was exported from a Jupyter notebook
using an open-source software (under the MIT License) written by @Naereen
from https://github.com/Naereen/Jupyter-Notebook-OCaml
This software is still in development, please notify me of a bug at
https://github.com/Naereen/Jupyter-Notebook-OCaml/issues/new if you find one
*)

(* # Table of Contents
 <p><div class="lev1 toc-item"><a href="#TP-1---Programmation-pour-la-préparation-à-l'agrégation-maths-option-info" data-toc-modified-id="TP-1---Programmation-pour-la-préparation-à-l'agrégation-maths-option-info-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>TP 1 - Programmation pour la préparation à l'agrégation maths option info</a></div><div class="lev1 toc-item"><a href="#Fonctions" data-toc-modified-id="Fonctions-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Fonctions</a></div><div class="lev2 toc-item"><a href="#Exercice-4" data-toc-modified-id="Exercice-4-21"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Exercice 4</a></div><div class="lev2 toc-item"><a href="#Exercice-5" data-toc-modified-id="Exercice-5-22"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Exercice 5</a></div><div class="lev2 toc-item"><a href="#Exercice-6" data-toc-modified-id="Exercice-6-23"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Exercice 6</a></div><div class="lev1 toc-item"><a href="#Récursivité" data-toc-modified-id="Récursivité-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Récursivité</a></div><div class="lev2 toc-item"><a href="#Exercice-7" data-toc-modified-id="Exercice-7-31"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Exercice 7</a></div><div class="lev2 toc-item"><a href="#Exercice-8" data-toc-modified-id="Exercice-8-32"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Exercice 8</a></div><div class="lev2 toc-item"><a href="#Exercice-9" data-toc-modified-id="Exercice-9-33"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>Exercice 9</a></div><div class="lev2 toc-item"><a href="#Exercice-10" data-toc-modified-id="Exercice-10-34"><span class="toc-item-num">3.4&nbsp;&nbsp;</span>Exercice 10</a></div><div class="lev2 toc-item"><a href="#Exercice-11" data-toc-modified-id="Exercice-11-35"><span class="toc-item-num">3.5&nbsp;&nbsp;</span>Exercice 11</a></div><div class="lev1 toc-item"><a href="#Listes" data-toc-modified-id="Listes-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Listes</a></div><div class="lev2 toc-item"><a href="#Exercice-12" data-toc-modified-id="Exercice-12-41"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Exercice 12</a></div><div class="lev2 toc-item"><a href="#Exercice-13" data-toc-modified-id="Exercice-13-42"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>Exercice 13</a></div><div class="lev2 toc-item"><a href="#Exercice-14" data-toc-modified-id="Exercice-14-43"><span class="toc-item-num">4.3&nbsp;&nbsp;</span>Exercice 14</a></div><div class="lev2 toc-item"><a href="#Exercice-15" data-toc-modified-id="Exercice-15-44"><span class="toc-item-num">4.4&nbsp;&nbsp;</span>Exercice 15</a></div><div class="lev2 toc-item"><a href="#Exercice-16" data-toc-modified-id="Exercice-16-45"><span class="toc-item-num">4.5&nbsp;&nbsp;</span>Exercice 16</a></div><div class="lev2 toc-item"><a href="#Exercice-17" data-toc-modified-id="Exercice-17-46"><span class="toc-item-num">4.6&nbsp;&nbsp;</span>Exercice 17</a></div><div class="lev1 toc-item"><a href="#Exponentiation-rapide" data-toc-modified-id="Exponentiation-rapide-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Exponentiation rapide</a></div><div class="lev2 toc-item"><a href="#Exercice-18" data-toc-modified-id="Exercice-18-51"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>Exercice 18</a></div><div class="lev2 toc-item"><a href="#Exercice-19" data-toc-modified-id="Exercice-19-52"><span class="toc-item-num">5.2&nbsp;&nbsp;</span>Exercice 19</a></div><div class="lev2 toc-item"><a href="#Exercice-20" data-toc-modified-id="Exercice-20-53"><span class="toc-item-num">5.3&nbsp;&nbsp;</span>Exercice 20</a></div><div class="lev2 toc-item"><a href="#Exercice-21" data-toc-modified-id="Exercice-21-54"><span class="toc-item-num">5.4&nbsp;&nbsp;</span>Exercice 21</a></div><div class="lev2 toc-item"><a href="#Exercice-22" data-toc-modified-id="Exercice-22-55"><span class="toc-item-num">5.5&nbsp;&nbsp;</span>Exercice 22</a></div><div class="lev2 toc-item"><a href="#Exercice-23" data-toc-modified-id="Exercice-23-56"><span class="toc-item-num">5.6&nbsp;&nbsp;</span>Exercice 23</a></div><div class="lev1 toc-item"><a href="#Formule-du-calcul-propositionnel" data-toc-modified-id="Formule-du-calcul-propositionnel-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Formule du calcul propositionnel</a></div><div class="lev2 toc-item"><a href="#Exercice-24" data-toc-modified-id="Exercice-24-61"><span class="toc-item-num">6.1&nbsp;&nbsp;</span>Exercice 24</a></div><div class="lev2 toc-item"><a href="#Exercice-25" data-toc-modified-id="Exercice-25-62"><span class="toc-item-num">6.2&nbsp;&nbsp;</span>Exercice 25</a></div><div class="lev2 toc-item"><a href="#Exercice-26" data-toc-modified-id="Exercice-26-63"><span class="toc-item-num">6.3&nbsp;&nbsp;</span>Exercice 26</a></div><div class="lev2 toc-item"><a href="#Exercice-27" data-toc-modified-id="Exercice-27-64"><span class="toc-item-num">6.4&nbsp;&nbsp;</span>Exercice 27</a></div><div class="lev2 toc-item"><a href="#Exercice-28" data-toc-modified-id="Exercice-28-65"><span class="toc-item-num">6.5&nbsp;&nbsp;</span>Exercice 28</a></div><div class="lev1 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Conclusion</a></div> *)

(* # TP 1 - Programmation pour la préparation à l'agrégation maths option info
- En OCaml. *)

(* In[12]: *)


let print = Printf.printf;;

Sys.command "ocaml -version";;

(* # Fonctions *)

(* ## Exercice 4 *)

(* In[2]: *)


let successeur (n : int) : int =
    n + 1
;;

(* In[3]: *)


successeur(3);;
successeur(2 * 2);;
successeur(2.5);;

(* ## Exercice 5 *)

(* In[4]: *)


let produit3 (x : int) (y : int) (z : int) : int =
    x * y * z
;;

let produit3_2 =
    fun (x : int) (y : int) (z : int) : int ->
        x * y * z
;;

let produit3_3 =
    fun (x : int) ->
        fun (y : int) ->
            fun (z : int) : int ->
                x * y * z
;;

let produit3_4 (tuple : (int * int * int)) : int =
    let x, y, z = tuple in
    x * y * z
;;

(* In[5]: *)


produit3 1 2 3;;
produit3_2 1 2 3;;
(produit3_3 1)(2);;  (* fun (z : int) -> int : 1 * 2 * z *)
((produit3_3 1)(2))(3);;
produit3_4 (1, 2, 3);;

(* ## Exercice 6 *)

(* In[8]: *)


let print = Printf.printf;;

let exercice6 (n : int) : unit =
    for i = 1 to n do
        print "%i\n" i;
    done;
    for i = n downto 1 do
        print "%i\n" i;
    done;
    flush_all ();
;;

(* In[10]: *)


exercice6(4);;

(* # Récursivité *)

(* ## Exercice 7 *)

(* In[13]: *)


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

(* In[16]: *)


factoriel 4;;
factoriel 0;;

for i = 1 to 8 do
    print "%i! = %i\n" i (factoriel i)
done;;
flush_all ();;

(* ## Exercice 8 *)

(* In[17]: *)


(* Remarque: si a>b alors pgcd a b = pgcd (a-b) b *)
let rec pgcd (a : int) (b : int) : int =
    if a = b
    then a
    else
        if (a > b)
        then pgcd (a-b) b
        else pgcd a (b-a)
;;

(* In[18]: *)


pgcd 16 1024;;
pgcd 25 130;;

(* Utilisons le générateur de nombres aléatoires pour faire quelques tests : *)

(* In[19]: *)


Random.self_init();;

(* In[20]: *)


for _ = 1 to 10 do
    let x = 1 + Random.int 100
    and y = 1 + Random.int 100 in
    let d = pgcd x y in
    print " %i ^ %i = %i\n" x y d;
done;;
flush_all ();;

(* ## Exercice 9 *)

(* In[21]: *)


(* fonction naive *)
let rec fibonacci (n : int) : int =
    match n with
    | 0 -> 1
    | 1 -> 1
    | n -> fibonacci (n-1) + fibonacci (n-2)
;;

(* Avec ce morceau de code on peut facilement mesurer le temps d'exécution : *)

(* In[22]: *)


let time (f : unit -> 'a) : 'a =
    let t = Sys.time() in
    let res = f () in
    Printf.printf "    Temps en secondes: %fs\n" (Sys.time() -. t);
    flush_all ();
    res
;;

(* In[23]: *)


fibonacci 5;;
fibonacci 17;;

(* In[24]: *)


time (fun () -> fibonacci 40);;

(* In[26]: *)


let fibonacci_lin (n : int) : int =
   (*  invariant:
       m >= 1
       u = fibo(n-m+1)
       v = fibo(n-m)
       aux m u v = fibo(n) *)
    let rec aux (m : int) (u : int) (v : int) : int =
        assert (m>0);
        if m = 1 then u
        else aux (m-1) (u+v) u
    in aux n 1 1
;;

(* In[27]: *)


for i = 1 to 10 do
    assert ((fibonacci i) = (fibonacci_lin i))
done;;

(* In[28]: *)


time (fun () -> fibonacci_lin 35);;

(* In[29]: *)


time (fun () -> fibonacci_lin 40);;

(* Voilà la différence. *)

(* ## Exercice 10

Aucune hypothèse n'est faite sur les arguments de la fonction, on supposera seulement qu'elle est itérable sur sa sortie. *)

(* In[30]: *)


let rec itere (f : 'a -> 'a) (n : int) : 'a -> 'a =
    match n with
    | 0 -> (fun x -> x);
    | n -> (fun x -> f (itere (f) (n - 1) x))
;;

(* In[31]: *)


(itere (fun x -> x + 1) 10)(1);;

(* ## Exercice 11 *)

(* In[33]: *)


let print = Printf.printf;;

let rec hanoi (n : int) (a : string) (b : string) (c : string) : unit =
    if n > 1 then
        hanoi (n-1) a c b;
    print "%s -> %s\n" a c;
    if n > 1 then
        hanoi (n-1) b a c;
    flush_all ();
;;

(* In[34]: *)


hanoi 1 "T1" "T2" "T3";;

(* In[35]: *)


hanoi 2 "T1" "T2" "T3";;

(* In[36]: *)


hanoi 5 "T1" "T2" "T3";; (* 2^5 - 1 = 31 coups *);;

(* Avec un compteur de coups joués (ce sera toujours $2^n - 1$) : *)

(* In[38]: *)


let rec hanoi2 (n : int) (a : string) (b : string) (c : string) : int =
    if n > 1 then begin
        let coup = ref 0 in
        coup := !coup + (hanoi2 (n-1) a c b);
        print "%s -> %s\n" a c;
        coup := !coup + (hanoi2 (n-1) b a c);
        flush_all ();
        !coup + 1
    end else begin
        print "%s -> %s\n" a c;
        flush_all ();
        1;
    end;
;;

(* In[39]: *)


hanoi2 2 "T1" "T2" "T3";;

(* ----
# Listes
## Exercice 12
Les listes en Python sont des `list`.
Elles ne fonctionnent **pas** comme des listes simplement chaînées comme en Caml. *)

(* In[40]: *)


let rec concatenation (l1 : 'a list) (l2 : 'a list) : 'a list =
    match l1 with
    | [] -> l2
    | t :: q -> t :: (concatenation q l2)
;;

(* In[41]: *)


concatenation [1; 2; 3] [4; 5];;

(* In[42]: *)


List.append [1; 2; 3] [4; 5];;

(* ## Exercice 13 *)

(* In[43]: *)


let rec applique (f : 'a -> 'b) (liste : 'a list) : 'b list =
    match liste with
    | [] -> []
    | t :: q -> (f t) :: (applique f q)
;;

(* In[44]: *)


applique (fun x -> x + 1) [1; 2; 3];;

(* In[45]: *)


let plus_un_liste = applique ((+) 1);;
plus_un_liste [1; 2; 3];; (* syntaxe sympa *);;

(* ## Exercice 14 *)

(* Avantage à la notation concise `applique f l` autorise à avoir `(applique f)(l)` au lieu de faire `fun l -> applique l f` si les deux arguments étaient dans l'autre sens. *)

(* In[46]: *)


let liste_carree = applique (fun x -> x*x);;

(* In[47]: *)


liste_carree [1; 2; 3];;

(* ## Exercice 15 *)

(* In[1]: *)


let rec miroir_quad : 'a list -> 'a list = function
    | [] -> []
    | a :: q -> (miroir_quad q) @ [a]
;;

let miroir_lin (liste : 'a list) : 'a list =
  (* sous fonction utilisant un deuxieme argument d'accumulation du resultat *)
  let rec miroir (l : 'a list) (accu : 'a list) : 'a list =
    match l with
      | [] -> accu
      | a :: q -> miroir q (a::accu)
  in
  miroir liste []
;;

(* In[49]: *)


miroir_quad [1; 2; 3];;
miroir_lin [1; 2; 3];;

(* In[50]: *)


time (fun () -> miroir_quad [1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20]);;
time (fun () -> miroir_lin [1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20]);;
(* Pas de différence observable ici *);;

(* In[51]: *)


let longue_liste (n : int) : int list =
    Array.to_list (Array.init n (fun i -> i))
;;

(* Avec de grandes listes, on voit la différence. *)

(* In[52]: *)


let _ = time (fun () -> miroir_quad (longue_liste 10000));;
let _ = time (fun () -> miroir_lin (longue_liste 10000));;

(* ## Exercice 16 *)

(* In[53]: *)


let rec insertionDansListeTriee (liste : 'a list) (x : 'a) : 'a list =
    match liste with
    | [] -> [x]
    | t :: q when t < x -> t :: (insertionDansListeTriee q x)
    | _ -> x :: liste  (* x est plus petit que le plus petit de la liste *)
;;

(* In[54]: *)


insertionDansListeTriee [1; 2; 5; 6] 4;;

(* In[55]: *)


let triInsertion (liste : 'a list) : 'a list  =
    let rec tri (l : 'a list) (accu : 'a list) : 'a list =
        match l with
        | [] -> accu
        | t :: q -> tri q (insertionDansListeTriee accu t)
    in
    tri liste []
;;

(* In[56]: *)


triInsertion [5; 2; 6; 1; 4];;

(* ## Exercice 17

Pour un ordre, de type `ordre : 'a -> 'a -> 'a` :
- `x < y` $\implies$ `ordre x y = -1`,
- `x = y` $\implies$ `ordre x y = 0`,
- `x > y` $\implies$ `ordre x y =1`. *)

(* In[57]: *)


type 'a ordre = 'a -> 'a -> 'a;;

(* In[58]: *)


let ordre_croissant : int ordre =
    fun (x : int) (y : int) ->
    match y with
    | yv when yv = x -> 0
    | yv when yv < x -> +1
    | yv when yv > x -> -1
    | _ -> failwith "Erreur comparaison impossible (ordre_decroissant)"
;;

let ordre_decroissant : int ordre =
    fun (x : int) (y : int) ->
    match y with
    | yv when yv = x -> 0
    | yv when yv < x -> -1
    | yv when yv > x -> +1
    | _ -> failwith "Erreur comparaison impossible (ordre_decroissant)"
;;

(* In[59]: *)


let rec insertionDansListeTrieeOrdre (ordre : 'a ordre) (liste : 'a list) (x : 'a) : 'a list =
    match liste with
    | [] -> [x]
    | t :: q when (ordre t x < 0) -> t :: (insertionDansListeTrieeOrdre ordre q x)
    | _ -> x :: liste  (* x est plus petit que le plus petit de la liste *)
;;

(* In[60]: *)


insertionDansListeTrieeOrdre ordre_decroissant [6; 5; 2; 1; 2] 4;;

(* In[61]: *)


let triInsertionOrdre (ordre : 'a ordre) (liste : 'a list) : 'a list  =
    let rec tri (l : 'a list) (accu : 'a list) : 'a list =
        match l with
        | [] -> accu
        | t :: q -> tri q (insertionDansListeTrieeOrdre ordre accu t)
    in
    tri liste []
;;

(* In[62]: *)


triInsertionOrdre ordre_decroissant [5; 2; 6; 1; 4];;

(* In[63]: *)


triInsertionOrdre ordre_croissant [5; 2; 6; 1; 4];;

(* ----
# Exponentiation rapide
## Exercice 18 *)

(* In[64]: *)


let rec puiss (x : int) : int -> int = function
    | 0 -> 1
    | n -> x * (puiss x (n-1))
;;

(* **Complexité** : linéaire ($\mathcal{O}(x)$)... *)

(* In[67]: *)


let x = 3 in
for n = 0 to 10 do
    print "  %i ** %i = %i\n" x n (puiss x n);
done;;
flush_all ();;

(* ## Exercice 19 *)

(* In[68]: *)


let rec puissRapide (x : int) : int -> int = function
    | 0 -> 1
    | n when (n mod 2) = 0 -> puissRapide (x * x) (n / 2)
    | n -> (puissRapide (x * x) ((n-1)/2)) * x
    (* Important de mettre * x à droite pour être récursive terminale. *)
;;

(* **Complexité** : logarithmique ($\mathcal{O}(\log_2 x)$). *)

(* In[69]: *)


let x = 3 in
for n = 0 to 10 do
    print "  %i ** %i = %i\n" x n (puissRapide x n);
done;;
flush_all ();;

(* ## Exercice 20 *)

(* In[70]: *)


(* le type monoide *)
type 'a monoide = { mult : 'a -> 'a -> 'a; neutre : 'a };;

(* Avec des champs d'enregistrement, c'est concis : *)

(* In[71]: *)


let floatMonoide : 'float monoide = {
    mult = ( *. ); (* fun x y -> x *. y *)
    neutre = 1.
};;

(* Par contre, impossible d'avoir un neutre de taille quelconque donc on doit écrire un monoied pour les matrices qui soit dépendent d'une taille $n$. *)

(* In[72]: *)


let mult_matrice (x : int array array) (y : int array array) : int array array =
    let n = Array.length x in
    let z = Array.make_matrix n n 0 in
    for i = 0 to n-1 do
        for j = 0 to n-1 do
            for k = 0 to n-1 do
                z.(i).(j) <- z.(i).(j) + x.(i).(k) * y.(k).(j)
            done
        done
    done;
    z
;;

(* In[73]: *)


mult_matrice [|[|1; 1|]; [|1; 1|]|] [|[|1; 2|]; [|3; 4|]|];;

(* Manuellement ce n'est pas trop dur : *)

(* In[74]: *)


let matrixMonoide n = {
    mult = mult_matrice;
    neutre = Array.init n (fun i -> Array.init n (fun j -> if i = j then 1 else 0));
};;

(* ## Exercice 21 *)

(* In[75]: *)


let rec exp_rapide (m : 'a monoide) (x : 'a) (n : int) : 'a =
    match n with
    | 0 -> m.neutre
    | n -> m.mult (exp_rapide m x (n-1)) x
;;

(* ## Exercice 22 *)

(* In[76]: *)


let exp_rapide_float = exp_rapide floatMonoide;;

(* In[77]: *)


exp_rapide_float 2.0 8;;

(* In[78]: *)


exp_rapide_float 0.2 8;;

(* Et pour les matrices, un petit piège à cause des tailles : *)

(* In[79]: *)


let exp_rapide_mat x n = exp_rapide (matrixMonoide (Array.length x)) x n;;

(* In[80]: *)


exp_rapide_mat [|[|1; 1|]; [|1; 1|]|] 0;;
exp_rapide_mat [|[|1; 1|]; [|1; 1|]|] 1;;
exp_rapide_mat [|[|1; 1|]; [|1; 1|]|] 2;;
exp_rapide_mat [|[|1; 1|]; [|1; 1|]|] 3;;
exp_rapide_mat [|[|1; 1|]; [|1; 1|]|] 4;;

(* In[81]: *)


(* nilpotente ! *)
exp_rapide_mat [|[|0; 1; 2|]; [|0; 0; 1|]; [|0; 0; 0|]|] 0;;
exp_rapide_mat [|[|0; 1; 2|]; [|0; 0; 1|]; [|0; 0; 0|]|] 1;;
exp_rapide_mat [|[|0; 1; 2|]; [|0; 0; 1|]; [|0; 0; 0|]|] 2;;
exp_rapide_mat [|[|0; 1; 2|]; [|0; 0; 1|]; [|0; 0; 0|]|] 3;;
exp_rapide_mat [|[|0; 1; 2|]; [|0; 0; 1|]; [|0; 0; 0|]|] 4;;

(* ## Exercice 23 *)

(* In[82]: *)


let monoideFonction = {
    mult = (fun f g x -> f (g x) );
    neutre = (fun x -> x)
};;

let itereMonoide f n = exp_rapide monoideFonction f n;;

(* In[83]: *)


itereMonoide (fun x -> x + 1) 10 0;;
itereMonoide ((+) 1) 10 0;;

(* ----
# Formule du calcul propositionnel

## Exercice 24 *)

(* In[2]: *)


type variable = string;;

type formule =
    | V of variable
    | Non of formule
    | Conj of formule * formule
    | Disj of formule * formule
;;

(* In[3]: *)


let f = (
    Conj(
        Non(V("p")),
        Disj(
            Conj(V("q"), Non(V("p"))),
            Disj(V("r"), V("q"))
        )
    )
) ;;

(* ## Exercice 25 *)

(* In[4]: *)


let rec taille : formule -> int = function
    | V(_) -> 1
    | Non(f) -> 1 + (taille f)
    | Conj(f,g) -> 1 + (taille f) + (taille g)
    | Disj(f,g) -> 1 + (taille f) + (taille g)
;;

(* In[87]: *)


taille f;;

(* ## Exercice 26 *)

(* In[5]: *)


let rec formule_to_string : formule -> string = function
    | V(p) -> p
    | Non(f) -> "non "^(formule_to_string f)
    | Conj(f,g) -> "("^(formule_to_string f)^" ^ "^(formule_to_string g)^")"
    | Disj(f,g) -> "("^(formule_to_string f)^" v "^(formule_to_string g)^")"
;;

(* In[6]: *)


let print = Printf.printf;;

let affiche (f : formule) : unit =
    print "%s\n" (formule_to_string f);
    flush_all ();
;;

(* In[7]: *)


affiche f;;

(* Et voilà. Pas si difficile non ? *)

(* ## Exercice 27
Les valeurs des variables seront données comme une fonction associant nom de variable à valeurs booléennes.
On a l'avantage de pouvoir mettre les valeurs par défaut à `true` ou `false` via la filtration. *)

(* In[8]: *)


type valuation = variable -> bool;;

let rec eval (v : valuation) : formule -> bool = function
    | V(x) -> v(x)
    | Non(f) -> not (eval v f)
    | Conj(f,g) -> (eval v f) && (eval v g)
    | Disj(f,g) -> (eval v f) || (eval v g)
;;

let valuFalse : valuation = function
    | "p" -> true
    | "q" -> false
    | "r" -> false
    | _ -> false
;;

let valuTrue : valuation = function
    | "p" -> false
    | "q" -> false
    | "r" -> true
    | _ -> false
;;

(* In[93]: *)


eval valuTrue f;;

(* In[94]: *)


eval valuFalse f;;

(* ## Exercice 28 *)

(* In[9]: *)


let rec inserUneFois (x : 'a) : ('a list -> 'a list) = function
    | [] -> [x]
    | t :: q when (x = t) -> t :: q
    | t :: q -> t :: (inserUneFois x q)
;;

(* In[10]: *)


let recupererVariable (f : formule) : variable list =
    let rec recup (l : variable list) : formule -> variable list = function
        | V(x) -> inserUneFois x l
        | Non(f) -> recup l f
        | Conj(f,g) -> recup (recup l f) g
        | Disj(f,g) -> recup (recup l f) g
    in
    recup [] f
;;

(* In[11]: *)


recupererVariable f;;

(* In[12]: *)


let rec nouvelleValu (v : valuation) : 'a list -> valuation = function
    | [] -> v
    | t :: q ->
    if (v t) then
        let nv x = if (x = t) then false else v x in
        nouvelleValu nv q
    else function x ->
        if (x = t) then true else v x
;;

(* In[13]: *)


let rec isTrue (v : valuation) : variable list -> bool = function
    | [] -> true
    | t :: q -> if v t then isTrue v q else false
;;

(* In[14]: *)


let rec valuToString (v : valuation) : variable list -> string = function
    | [] -> ""
    | t :: q -> (if v t then "1" else "0") ^ " " ^ (valuToString v q)
;;

(* In[17]: *)


let print = Printf.printf;;

let rec printVariableList : variable list -> unit = function
    | [ ] -> print "| "
    | t :: q ->
        print "%s " t;
        flush_all ();
        printVariableList q
;;

(* In[18]: *)


let tableVerite (f : formule) : unit =
    let variables = recupererVariable f in
    let valu = ref (function _ -> false) in
    (* on construit dynamiquement la nouvelle valuation... moche mais ça marche *)
    printVariableList variables;
    affiche f;
    while not (isTrue (!valu) variables) do
        print_string ( (valuToString (!valu) variables)^"| "^(if eval (!valu) f then "1" else "0")^"\n");
        valu := nouvelleValu (!valu) variables
    done
;;

(* In[19]: *)


tableVerite f;;

(* > On peut vérifier, par exemple sur [Wolfram|Alpha](https%3A%2F%2Fwww.wolframalpha.com%2Finput%2F%3Fi%3D%28%7Ep%2B%2526%2B%28%28q%2B%2526%2B%7Ep%29%2B%257C%2B%28r%2B%257C%2Bq%29%29%29) que l'on obtient bien le bon résultat... *)

(* ----

# Conclusion

Voilà pour aujourd'hui !

Cette solution est aussi disponible en Python : [TP1__Python.ipynb](https://nbviewer.jupyter.org/github/Naereen/notebooks/tree/master/agreg/TP_Programmation_2017-18/TP1__Python.ipynb/).

Là où Caml excelle pour les types définis, le filtrage et la récursion, Python gagne en simplicité sur l'affichage, sa librairie standard et les dictionnaires et ensembles... *)
