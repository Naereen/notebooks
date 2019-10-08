(*
This OCaml script was exported from a Jupyter notebook
using an open-source software (under the MIT License) written by @Naereen
from https://github.com/Naereen/Jupyter-Notebook-OCaml
This software is still in development, please notify me of a bug at
https://github.com/Naereen/Jupyter-Notebook-OCaml/issues/new if you find one
*)

(* # Table of Contents
 <p><div class="lev1 toc-item"><a href="#TP-2---Programmation-pour-la-préparation-à-l'agrégation-maths-option-info" data-toc-modified-id="TP-2---Programmation-pour-la-préparation-à-l'agrégation-maths-option-info-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>TP 2 - Programmation pour la préparation à l'agrégation maths option info</a></div><div class="lev1 toc-item"><a href="#Listes" data-toc-modified-id="Listes-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Listes</a></div><div class="lev2 toc-item"><a href="#Exercice-1-:-taille" data-toc-modified-id="Exercice-1-:-taille-21"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Exercice 1 : <code>taille</code></a></div><div class="lev2 toc-item"><a href="#Exercice-2-:-concat" data-toc-modified-id="Exercice-2-:-concat-22"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Exercice 2 : <code>concat</code></a></div><div class="lev2 toc-item"><a href="#Exercice-3-:-appartient" data-toc-modified-id="Exercice-3-:-appartient-23"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Exercice 3 : <code>appartient</code></a></div><div class="lev2 toc-item"><a href="#Exercice-4-:-miroir" data-toc-modified-id="Exercice-4-:-miroir-24"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>Exercice 4 : <code>miroir</code></a></div><div class="lev2 toc-item"><a href="#Exercice-5-:-alterne" data-toc-modified-id="Exercice-5-:-alterne-25"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>Exercice 5 : <code>alterne</code></a></div><div class="lev2 toc-item"><a href="#Exercice-6-:-nb_occurrences" data-toc-modified-id="Exercice-6-:-nb_occurrences-26"><span class="toc-item-num">2.6&nbsp;&nbsp;</span>Exercice 6 : <code>nb_occurrences</code></a></div><div class="lev2 toc-item"><a href="#Exercice-7-:-pairs" data-toc-modified-id="Exercice-7-:-pairs-27"><span class="toc-item-num">2.7&nbsp;&nbsp;</span>Exercice 7 : <code>pairs</code></a></div><div class="lev2 toc-item"><a href="#Exercice-8-:-range" data-toc-modified-id="Exercice-8-:-range-28"><span class="toc-item-num">2.8&nbsp;&nbsp;</span>Exercice 8 : <code>range</code></a></div><div class="lev2 toc-item"><a href="#Exercice-9-:-premiers" data-toc-modified-id="Exercice-9-:-premiers-29"><span class="toc-item-num">2.9&nbsp;&nbsp;</span>Exercice 9 : <code>premiers</code></a></div><div class="lev1 toc-item"><a href="#Quelques-tris-par-comparaison" data-toc-modified-id="Quelques-tris-par-comparaison-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Quelques tris par comparaison</a></div><div class="lev2 toc-item"><a href="#Exercice-10-:-Tri-insertion" data-toc-modified-id="Exercice-10-:-Tri-insertion-31"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Exercice 10 : Tri insertion</a></div><div class="lev2 toc-item"><a href="#Exercice-11-:-Tri-insertion-générique" data-toc-modified-id="Exercice-11-:-Tri-insertion-générique-32"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Exercice 11 : Tri insertion générique</a></div><div class="lev2 toc-item"><a href="#Exercice-12-:-Tri-selection" data-toc-modified-id="Exercice-12-:-Tri-selection-33"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>Exercice 12 : Tri selection</a></div><div class="lev2 toc-item"><a href="#Exercices-13,-14,-15-:-Tri-fusion" data-toc-modified-id="Exercices-13,-14,-15-:-Tri-fusion-34"><span class="toc-item-num">3.4&nbsp;&nbsp;</span>Exercices 13, 14, 15 : Tri fusion</a></div><div class="lev2 toc-item"><a href="#Comparaisons-des-tris" data-toc-modified-id="Comparaisons-des-tris-35"><span class="toc-item-num">3.5&nbsp;&nbsp;</span>Comparaisons des tris</a></div><div class="lev1 toc-item"><a href="#Listes-:-l'ordre-supérieur" data-toc-modified-id="Listes-:-l'ordre-supérieur-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Listes : l'ordre supérieur</a></div><div class="lev2 toc-item"><a href="#Exercice-16-:-applique" data-toc-modified-id="Exercice-16-:-applique-41"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Exercice 16 : <code>applique</code></a></div><div class="lev2 toc-item"><a href="#Exercice-17" data-toc-modified-id="Exercice-17-42"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>Exercice 17</a></div><div class="lev2 toc-item"><a href="#Exercice-18-:-itere" data-toc-modified-id="Exercice-18-:-itere-43"><span class="toc-item-num">4.3&nbsp;&nbsp;</span>Exercice 18 : <code>itere</code></a></div><div class="lev2 toc-item"><a href="#Exercice-19" data-toc-modified-id="Exercice-19-44"><span class="toc-item-num">4.4&nbsp;&nbsp;</span>Exercice 19</a></div><div class="lev2 toc-item"><a href="#Exercice-20-:-qqsoit-et-ilexiste" data-toc-modified-id="Exercice-20-:-qqsoit-et-ilexiste-45"><span class="toc-item-num">4.5&nbsp;&nbsp;</span>Exercice 20 : <code>qqsoit</code> et <code>ilexiste</code></a></div><div class="lev2 toc-item"><a href="#Exercice-21-:-appartient-version-2" data-toc-modified-id="Exercice-21-:-appartient-version-2-46"><span class="toc-item-num">4.6&nbsp;&nbsp;</span>Exercice 21 : <code>appartient</code> version 2</a></div><div class="lev2 toc-item"><a href="#Exercice-22-:-filtre" data-toc-modified-id="Exercice-22-:-filtre-47"><span class="toc-item-num">4.7&nbsp;&nbsp;</span>Exercice 22 : <code>filtre</code></a></div><div class="lev2 toc-item"><a href="#Exercice-23" data-toc-modified-id="Exercice-23-48"><span class="toc-item-num">4.8&nbsp;&nbsp;</span>Exercice 23</a></div><div class="lev2 toc-item"><a href="#Exercice-24-:-reduit" data-toc-modified-id="Exercice-24-:-reduit-49"><span class="toc-item-num">4.9&nbsp;&nbsp;</span>Exercice 24 : <code>reduit</code></a></div><div class="lev2 toc-item"><a href="#Exercice-25-:-somme,-produit" data-toc-modified-id="Exercice-25-:-somme,-produit-410"><span class="toc-item-num">4.10&nbsp;&nbsp;</span>Exercice 25 : <code>somme</code>, <code>produit</code></a></div><div class="lev2 toc-item"><a href="#Exercice-26-:-miroir-version-2" data-toc-modified-id="Exercice-26-:-miroir-version-2-411"><span class="toc-item-num">4.11&nbsp;&nbsp;</span>Exercice 26 : <code>miroir</code> version 2</a></div><div class="lev1 toc-item"><a href="#Arbres" data-toc-modified-id="Arbres-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Arbres</a></div><div class="lev2 toc-item"><a href="#Exercice-27" data-toc-modified-id="Exercice-27-51"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>Exercice 27</a></div><div class="lev2 toc-item"><a href="#Exercice-28" data-toc-modified-id="Exercice-28-52"><span class="toc-item-num">5.2&nbsp;&nbsp;</span>Exercice 28</a></div><div class="lev2 toc-item"><a href="#Exercice-29" data-toc-modified-id="Exercice-29-53"><span class="toc-item-num">5.3&nbsp;&nbsp;</span>Exercice 29</a></div><div class="lev2 toc-item"><a href="#Exercice-30" data-toc-modified-id="Exercice-30-54"><span class="toc-item-num">5.4&nbsp;&nbsp;</span>Exercice 30</a></div><div class="lev1 toc-item"><a href="#Parcours-d'arbres-binaires" data-toc-modified-id="Parcours-d'arbres-binaires-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Parcours d'arbres binaires</a></div><div class="lev2 toc-item"><a href="#Exercice-31" data-toc-modified-id="Exercice-31-61"><span class="toc-item-num">6.1&nbsp;&nbsp;</span>Exercice 31</a></div><div class="lev2 toc-item"><a href="#Exercice-32-:-Parcours-naifs-(complexité-quadratique)" data-toc-modified-id="Exercice-32-:-Parcours-naifs-(complexité-quadratique)-62"><span class="toc-item-num">6.2&nbsp;&nbsp;</span>Exercice 32 : Parcours naifs (complexité quadratique)</a></div><div class="lev2 toc-item"><a href="#Exercice-33-:-Parcours-linéaires" data-toc-modified-id="Exercice-33-:-Parcours-linéaires-63"><span class="toc-item-num">6.3&nbsp;&nbsp;</span>Exercice 33 : Parcours linéaires</a></div><div class="lev2 toc-item"><a href="#Exercice-34-:-parcours-en-largeur-et-en-profondeur" data-toc-modified-id="Exercice-34-:-parcours-en-largeur-et-en-profondeur-64"><span class="toc-item-num">6.4&nbsp;&nbsp;</span>Exercice 34 : parcours en largeur et en profondeur</a></div><div class="lev2 toc-item"><a href="#Exercice-35-et-fin" data-toc-modified-id="Exercice-35-et-fin-65"><span class="toc-item-num">6.5&nbsp;&nbsp;</span>Exercice 35 et fin</a></div><div class="lev1 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Conclusion</a></div> *)

(* # TP 2 - Programmation pour la préparation à l'agrégation maths option info
- En OCaml. *)

(* In[1]: *)


let print = Printf.printf;;
Sys.command "ocaml -version";;

(* ----
# Listes *)

(* ## Exercice 1 : `taille` *)

(* In[2]: *)


let rec taille (liste : 'a list) : int =
    match liste with
    | [] -> 0
    | _ :: q -> (taille q) + 1
;;

taille [];;
taille [1; 2; 3];;

(* Pas sûr qu'elle soit récursive terminale, alors que celle là oui : *)

(* In[3]: *)


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

(* In[6]: *)


let taille = List.fold_left (fun acc _ -> acc + 1) 0;;

taille [];;
taille [1; 2; 3];;

(* In[7]: *)


List.length [];;
List.length [1; 2; 3];;

(* ## Exercice 2 : `concat` *)

(* In[8]: *)


let rec concatene (liste1 : 'a list) (liste2 : 'a list) : 'a list =
    match liste1 with
    | [] -> liste2
    | h :: q -> h :: (concatene q liste2)
;;

concatene [1; 2] [3; 4];;

(* Autre approche, moins simple mais de même complexité en $\mathcal{O}(n)$. *)

(* In[9]: *)


let miroir (liste : 'a list) : 'a list =
    let rec aux acc = function
    | [] -> acc
    | h :: q -> aux (h :: acc) q
    in aux [] liste
;;

(* In[10]: *)


let concatene (liste1 : 'a list) (liste2 : 'a list) : 'a list =
    let rec aux acc l1 l2 =
        match l1 with
        | [] when l2 = [] -> acc
        | [] -> aux acc l2 []
        | h :: q -> aux (h :: acc) q l2
    in
    miroir (aux [] liste1 liste2)
;;

(* In[11]: *)


concatene [1; 2] [3; 4];;

(* In[12]: *)


List.append [1; 2] [3; 4];;

(* ## Exercice 3 : `appartient` *)

(* In[1]: *)


let rec appartient x = function
    | [] -> false
    | h :: _ when h = x -> true
    | _ :: q -> appartient x q
;;


let rec appartient2 x = function
    | [] -> false
    | h :: q -> (h = x) || (appartient2 x q)
;;

appartient 1 [];;
appartient 1 [1];;
appartient 1 [1; 2; 3];;
appartient 4 [1; 2; 3];;

appartient2 1 [];;
appartient2 1 [1];;
appartient2 1 [1; 2; 3];;
appartient2 4 [1; 2; 3];;

(* In[14]: *)


List.mem 1 [];;
List.mem 1 [1];;
List.mem 1 [1; 2; 3];;
List.mem 4 [1; 2; 3];;

(* ## Exercice 4 : `miroir` *)

(* In[15]: *)


let miroir (liste : 'a list) : 'a list =
    let rec aux acc = function
    | [] -> acc
    | h :: q -> aux (h :: acc) q
    in aux [] liste
;;

(* In[16]: *)


miroir [2; 3; 5; 7; 11];;

List.rev [2; 3; 5; 7; 11];;

(* ## Exercice 5 : `alterne` *)

(* La sémantique n'était pas très claire, mais on peut imaginer quelque chose comme ça : *)

(* In[17]: *)


let alterne (liste1 : 'a list) (liste2 : 'a list) : 'a list =
    let rec aux acc l1 l2 =
        match (l1, l2) with
        | [], [] -> acc
        | [], ll2 -> acc @ ll2
        | ll1, [] -> acc @ ll1
        | h1 :: q1, h2 :: q2 -> aux (h1 :: h2 :: acc) q1 q2
    in List.rev (aux [] liste1 liste2)
;;

(* In[18]: *)


alterne [1; 3; 5] [2; 4; 6];;

(* La complexité est linéaire en $\mathcal{O}(\max(|\text{liste 1}|, |\text{liste 2}|)$. *)

(* Mais on manque souvent la version la plus simple : *)

(* In[19]: *)


let rec alterne (l1 : 'a list) (l2 : 'a list) : 'a list =
    match l1 with
    | [] -> l2
    | t::q -> t::(alterne l2 q)
;;

(* ## Exercice 6 : `nb_occurrences` *)

(* In[5]: *)


(* O(n) en temps, et en espace d'appel : pas récursif terminal ! *)
let rec nb_occurrences (x : 'a) (liste : 'a list) : int =
    match liste with
    | [] -> 0
    | h :: q when h = x -> (nb_occurrences x q) + 1
    | _ :: q -> nb_occurrences x q
;;

(* O(n) en temps, et O(1) en espace d'appel : récursif terminal ! *)
let nb_occurrences (x : 'a) (liste : 'a list) : int =
    let rec aux acc x l =
    match l with
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

(* In[21]: *)


let nb_occurrences (x : 'a) : 'a list -> int =
    List.fold_left (fun acc y -> if x = y then (acc + 1) else acc) 0
;;

nb_occurrences 0 [1; 2; 3; 4];;
nb_occurrences 2 [1; 2; 3; 4];;
nb_occurrences 2 [1; 2; 2; 3; 3; 4];;
nb_occurrences 5 [1; 2; 3; 4];;

(* ## Exercice 7 : `pairs`

C'est un filtrage : *)

(* In[22]: *)


let pairs = List.filter (fun x -> x mod 2 = 0);;

(* In[23]: *)


pairs [1; 2; 3; 4; 5; 6];;
pairs [1; 2; 3; 4; 5; 6; 7; 100000];;
pairs [1; 2; 3; 4; 5; 6; 7; 100000000000];;
pairs [1; 2; 3; 4; 5; 6; 7; 1000000000000000000];;

(* ## Exercice 8 : `range` *)

(* In[24]: *)


let range (n : int) : int list =
    let rec aux acc = function
    | 0 -> acc
    | n -> aux (n :: acc) (n - 1)
    in aux [] n
;;

(* In[25]: *)


range 30;;

(* In[26]: *)


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

(* In[27]: *)


let premiers_entiers = entiers 0;; (* Bel exemple de currification *)

entiers 4 10;;
premiers_entiers 7;;

(* ## Exercice 9 : `premiers`
Plusieurs possibilités. Un filtre d'Erathosthène marche bien, ou une filtration.
Je ne vais pas utiliser de tableaux donc on est un peu réduit d'utiliser une filtration (filtrage ? *pattern matching*) *)

(* In[28]: *)


let racine (n : int) : int =
    int_of_float (floor (sqrt (float_of_int n)))
;;

racine 17;;

(* In[29]: *)


let estDivisible (a : int) (b : int) : bool =
    (a mod b) = 0
;;

estDivisible 10 2;;
estDivisible 10 6;;
estDivisible 10 5;;

(* In[30]: *)


let range2 (debut : int) (fin : int) (taille : int) : int list =
    let rec aux acc = function
    | n when n > fin -> acc
    | n -> aux (n :: acc) (n + taille)
    in
    List.rev (aux [] debut)
;;

(* In[31]: *)


range2 2 12 3;;

(* Une version purement fonctionnelle est moins facile qu'une version impérative avec une référence booléenne (rappel : pas de `break` dans les boucles `for` en OCaml...). *)

(* In[32]: *)


let estPremier (n : int) : bool =
    List.fold_left (fun b k -> b && (not (estDivisible n k))) true (range2 2 (racine n) 1)
;;

(* In[33]: *)


let premiers (n : int) : int list =
    List.filter estPremier (range2 2 n 1)
;;

(* In[34]: *)


premiers 10;;

(* In[35]: *)


premiers 100;;

(* ----
# Quelques tris par comparaison *)

(* On fera les tris en ordre croissant. *)

(* In[33]: *)


let test = [3; 1; 8; 4; 5; 6; 1; 2];;

(* ## Exercice 10 : Tri insertion *)

(* In[34]: *)


let rec insere (x : 'a) : 'a list -> 'a list = function
    | [] -> [x]
    | t :: q ->
        if x <= t then
            x :: t :: q
        else
            t :: (insere x q)
;;

(* In[35]: *)


let rec tri_insertion : 'a list -> 'a list = function
    | [] -> []
    | t :: q -> insere t (tri_insertion q)
;;

(* In[36]: *)


tri_insertion test;;

(* Complexité en temps $\mathcal{O}(n^2)$. *)

(* ## Exercice 11 : Tri insertion générique *)

(* In[37]: *)


let rec insere2 (ordre : 'a -> 'a -> bool) (x : 'a) : 'a list -> 'a list = function
    | [] -> [x]
    | t :: q ->
        if ordre x t then
            x :: t :: q
        else
            t :: (insere2 ordre x q)
;;

(* In[38]: *)


let rec tri_insertion2 (ordre : 'a -> 'a -> bool) : 'a list -> 'a list = function
    | [] -> []
    | t :: q -> insere2 ordre t (tri_insertion2 ordre q)
;;

(* In[39]: *)


let ordre_croissant a b = a <= b;;

(* In[40]: *)


tri_insertion2 ordre_croissant test;;

(* In[41]: *)


let ordre_decroissant = (>=);;

(* In[42]: *)


tri_insertion2 ordre_decroissant test;;

(* ## Exercice 12 : Tri selection *)

(* In[43]: *)


let selectionne_min (l : 'a list) : ('a * 'a list) =
    let rec cherche_min min autres = function
        | [] -> (min, autres)
        | t :: q ->
            if t < min then
                cherche_min t (min :: autres) q
            else
                cherche_min min (t :: autres) q
    in
    match l with
    | [] -> failwith "Selectionne_min sur liste vide"
    | t :: q -> cherche_min t [] q
;;

(* In[44]: *)


selectionne_min test;;

(* In[45]: *)


let rec tri_selection : 'a list -> 'a list = function
    | [] -> []
    | l ->
        let (min, autres) = selectionne_min l in
        min :: (tri_selection autres)
;;

(* In[46]: *)


tri_selection test;;

(* Complexité en temps : $\mathcal{O}(n^2)$. *)

(* ## Exercices 13, 14, 15 : Tri fusion *)

(* In[47]: *)


let print_list (liste : int list) : unit =
    print_string "[";
    List.iter (fun i -> print_int i; print_string "; " ) liste;
    print_endline "]";
;;

(* In[48]: *)


test;;
print_list test;;

(* In[49]: *)


let rec separe : 'a list -> ('a list * 'a list) = function
    | [] -> ([], [])
    | [x] -> ([x], [])
    | x :: y :: q ->
    (* n'est pas stable : on perturbe l'ordre des éléments en entrée *)
        let (a, b) = separe q
        in (x::a, y::b)
;;

separe test;;

(* In[50]: *)


let rec fusion (l1 : 'a list) (l2 : 'a list) : 'a list =
    match (l1, l2) with
    | (l, []) | ([], l) -> l  (* syntaxe concise pour deux cas identiques *)
    | (h1::q1, h2::q2) ->
        if h1 <= h2 then
            h1 :: (fusion q1 l2)
        else
            h2 :: (fusion l1 q2)
;;

fusion [1; 3; 7] [2; 3; 8];;

(* In[51]: *)


(* O(n log(n)) en temps et O(n) en mémoire *)
let rec tri_fusion : 'a list -> 'a list = function
    | [] -> []
    | [x] -> [x] (* ATTENTION A NE PAS OUBLIER CE CAS *)
    | l ->
        let a, b = separe l in
        fusion (tri_fusion a) (tri_fusion b)
;;

(* In[52]: *)


tri_fusion test;;

(* Complexité en temps $\mathcal{O}(n \log n)$. *)

(* ## Comparaisons des tris *)

(* In[53]: *)


Random.self_init();;

(* In[75]: *)


Random.int 100;;

(* In[65]: *)


let random_tableau (n : int) : int array =
    Array.init n (fun _ -> -1000 + (Random.int 2000))
;;

let random_list (n : int) : int list =
    Array.to_list (random_tableau n)
;;

(* In[84]: *)


random_tableau 10;;

(* In[62]: *)


let timeit (nbrepetitions : int) (f : 'a -> 'b) (lazy_x : unit -> 'a) : float =
    let debut = Sys.time () in
    for _ = 1 to nbrepetitions do
        ignore (f (lazy_x ()));
    done;
    let fin = Sys.time () in
    (fin -. debut) /. (float_of_int nbrepetitions)
;;

(* In[67]: *)


let nbrepetitions = 100 in
let n = 10 in
let temps_insertion = timeit nbrepetitions tri_insertion (fun () -> random_list n) in
let temps_selection = timeit nbrepetitions tri_selection (fun () -> random_list n) in
let temps_fusion = timeit nbrepetitions tri_fusion (fun () -> random_list n) in
(temps_insertion, temps_selection, temps_fusion);;

(* In[68]: *)


let nbrepetitions = 100 in
let n = 100 in
let temps_insertion = timeit nbrepetitions tri_insertion (fun () -> random_list n) in
let temps_selection = timeit nbrepetitions tri_selection (fun () -> random_list n) in
let temps_fusion = timeit nbrepetitions tri_fusion (fun () -> random_list n) in
(temps_insertion, temps_selection, temps_fusion);;

(* In[69]: *)


let nbrepetitions = 100 in
let n = 1000 in
let temps_insertion = timeit nbrepetitions tri_insertion (fun () -> random_list n) in
let temps_selection = timeit nbrepetitions tri_selection (fun () -> random_list n) in
let temps_fusion = timeit nbrepetitions tri_fusion (fun () -> random_list n) in
(temps_insertion, temps_selection, temps_fusion);;

(* In[86]: *)


let nbrepetitions = 1 in
let n = 10000 in
let temps_insertion = timeit nbrepetitions tri_insertion (fun () -> random_list n) in
let temps_selection = timeit nbrepetitions tri_selection (fun () -> random_list n) in
let temps_fusion = timeit nbrepetitions tri_fusion (fun () -> random_list n) in
(temps_insertion, temps_selection, temps_fusion);;

(* On a pu vérifier **empiriquement** que les complexités des tris par insertion et sélection sont quadratiques (multiplier $n$ par $10$ multiplie le temps par en gros $10^2$), et que le tri fusion est quasiment linéaire (multiplier $n$ par $10$ multiplie le temps par en gros $10$). *)

(* Une petite question de culture camelistique : *)

(* In[92]: *)


function x -> function y -> x;;

(* In[93]: *)


fun x y -> x;;

(* ----
# Listes : l'ordre supérieur

Je ne corrige pas les questions qui étaient traitées dans le TP1. *)

(* ## Exercice 16 : `applique` *)

(* In[19]: *)


(* Temps O(n) pire des cas, et O(n) mémoire *)
let rec applique f = function
    | [] -> []
    | h :: q -> (f h) :: (applique f q)
;;

(* ## Exercice 17 *)

(* In[55]: *)


let premiers_carres_parfaits (n : int) : int list =
    applique (fun x -> x * x) (entiers 1 n)
;;

(* In[56]: *)


premiers_carres_parfaits 12;;

(* ## Exercice 18 : `itere` *)

(* In[57]: *)


let rec itere (f : 'a -> unit) = function
    | [] -> ()
    | h :: q -> begin
        f h;
        itere f q
    end
;;

(* ## Exercice 19 *)

(* In[58]: *)


let print = Printf.printf

let f x = print "%i\n" x;;

(* In[62]: *)


let affiche_liste_entiers (liste : int list) =
    print "Debut\n";
    itere (print "%i\n") liste;
    print "Fin\n";
    flush_all ();
;;

affiche_liste_entiers [1; 2; 4; 5];;

(* ## Exercice 20 : `qqsoit` et `ilexiste` *)

(* In[20]: *)


(* Temps O(n) pire cas, et O(1) mémoire car récursif terminal *)
let rec qqsoit (pred : 'a -> bool) = function
    | [] -> true (* piege ! *)
    | h :: q -> (pred h) && (qqsoit pred q)
    (* le && n'évalue pas le deuxième si le premier argument est false
       donc ceci est efficace et récursif terminal.
    *)
;;

(* In[64]: *)


let rec ilexiste (pred : 'a -> bool) = function
    | [] -> false
    | h :: q -> (pred h) || (ilexiste pred q)
    (* le || n'évalue pas le deuxième si le premier argument est true
       donc ceci est efficace et récursif terminal.
    *)
;;

(* In[65]: *)


qqsoit (fun x -> (x mod 2) = 0) [1; 2; 3; 4; 5];;

ilexiste (fun x -> (x mod 2) = 0) [1; 2; 3; 4; 5];;

(* ## Exercice 21 : `appartient` version 2 *)

(* In[66]: *)


let appartient x = ilexiste (fun y -> x = y);;

let appartient x = ilexiste ((=) x);; (* syntaxe simplifiée par curification *);;

(* In[67]: *)


let toutes_egales x = qqsoit ((=) x);;

(* In[68]: *)


appartient 1 [1; 2; 3];;
appartient 5 [1; 2; 3];;

toutes_egales 1 [1; 2; 3];;
toutes_egales 2 [2; 2; 2];;

(* ## Exercice 22 : `filtre` *)

(* In[69]: *)


let rec filtre (pred : 'a -> bool) : 'a list -> 'a list = function
    | [] -> []
    | h :: q when pred h -> h :: (filtre pred q)
    | _ :: q -> filtre pred q
;;

(* In[70]: *)


filtre (fun x -> (x mod 2) = 0) [1; 2; 3; 4; 5];;

filtre (fun x -> (x mod 2) != 0) [1; 2; 3; 4; 5];;
filtre (fun x -> (x mod 2) <> 0) [1; 2; 3; 4; 5];; (* syntaxe non conseillée *);;

(* ## Exercice 23
Je vous laisse trouver pour `premiers`. *)

(* In[71]: *)


let pairs = filtre (fun x -> (x mod 2) = 0);;
let impairs = filtre (fun x -> (x mod 2) != 0);;

(* ## Exercice 24 : `reduit` *)

(* In[72]: *)


let rec reduit (tr : 'a -> 'b -> 'a) (acc : 'a) (liste : 'b list) : 'a =
    match liste with
    | [] -> acc
    | h :: q -> reduit tr (tr acc h) q
;;

(* Très pratique pour calculer des sommes, notamment. *)

(* ## Exercice 25 : `somme`, `produit` *)

(* In[73]: *)


let somme = reduit (+) 0;;

somme [1; 2; 3; 4; 5];;
List.fold_left (+) 0 [1; 2; 3; 4; 5];;

(* In[74]: *)


let produit = reduit ( * ) 1;;

produit [1; 2; 3; 4; 5];;
List.fold_left ( * ) 1 [1; 2; 3; 4; 5];;

(* ## Exercice 26 : `miroir` version 2 *)

(* In[75]: *)


let miroir = reduit (fun a b -> b :: a) [];;

(* In[76]: *)


miroir [2; 3; 5; 7; 11];;

List.rev [2; 3; 5; 7; 11];;

(* In[77]: *)


miroir [2.; 3.; 5.; 7.; 11.];;

(* ----
# Arbres *)

(* ## Exercice 27 *)

(* In[5]: *)


type 'a arbre_bin0 = Feuille0 of 'a | Noeud0 of ('a arbre_bin0) * 'a * ('a arbre_bin0);;

(* In[6]: *)


let rec arbre_complet_entier (n : int) : int arbre_bin0 =
    match n with
    | n when n < 2 -> Feuille0 0
    | n -> Noeud0((arbre_complet_entier (n / 2)), n, (arbre_complet_entier (n / 2)))
;;

arbre_complet_entier 4;;

(* Autre variante, plus simple : *)

(* In[7]: *)


type arbre_bin = Feuille | Noeud of arbre_bin * arbre_bin;;

(* In[8]: *)


let arbre_test = Noeud (Noeud (Noeud (Feuille, Feuille), Feuille), Feuille);;

(* ## Exercice 28 *)

(* Compte le nombre de feuilles et de sommets. *)

(* In[10]: *)


let rec taille : arbre_bin -> int = function
    | Feuille -> 1
    | Noeud(x, y) -> 1 + (taille x) + (taille y)
;;

(* In[11]: *)


taille arbre_test;;

(* ## Exercice 29 *)

(* In[12]: *)


let rec hauteur : arbre_bin -> int = function
    | Feuille -> 0
    | Noeud(x, y) -> 1 + (max (hauteur x) (hauteur y)) (* peut etre plus simple *)
;;

(* In[13]: *)


hauteur arbre_test;;

(* ## Exercice 30 *)

(* Bonus. *)

(* ----
# Parcours d'arbres binaires *)

(* ## Exercice 31 *)

(* In[14]: *)


type element_parcours = F | N;;

type parcours = element_parcours list;;

(* ## Exercice 32 : Parcours naifs (complexité quadratique) *)

(* In[15]: *)


let rec parcours_prefixe : arbre_bin -> element_parcours list = function
    | Feuille -> [F]
    | Noeud (g, d) -> [N] @ (parcours_prefixe g) @ (parcours_prefixe d)
;;

parcours_prefixe arbre_test;;

(* In[16]: *)


let rec parcours_postfixe : arbre_bin -> element_parcours list = function
    | Feuille -> [F]
    | Noeud(g, d) -> (parcours_postfixe g) @ (parcours_postfixe d) @ [N]
;;

parcours_postfixe arbre_test;;

(* In[17]: *)


let rec parcours_infixe : arbre_bin -> element_parcours list = function
    | Feuille -> [F]
    | Noeud(g, d) -> (parcours_infixe g) @ [N] @ (parcours_infixe d)
;;

parcours_infixe arbre_test;;

(* Pourquoi ont-ils une complexité quadratique ? La concaténation (`@`) ne se fait pas en temps constant mais linéaire dans la taille de la première liste. *)

(* ## Exercice 33 : Parcours linéaires

On ajoute une fonction auxiliaire et un argument `vus` qui est une liste qui stocke les élements observés dans l'ordre du parcours *)

(* In[18]: *)


let parcours_prefixe2 a =
    let rec parcours vus = function
        | Feuille -> F :: vus
        | Noeud(g, d) -> parcours (parcours (N :: vus) g) d
    in List.rev (parcours [] a)
;;

parcours_prefixe2 arbre_test;;

(* In[21]: *)


let parcours_postfixe2 a =
    let rec parcours vus = function
        | Feuille -> F :: vus
        | Noeud(g, d) -> N :: (parcours (parcours vus g) d)
    in List.rev (parcours [] a)
;;

parcours_postfixe2 arbre_test;;

(* In[22]: *)


let parcours_infixe2 a =
    let rec parcours vus = function
        | Feuille -> F :: vus
        | Noeud(g, d) -> parcours (N :: (parcours vus g)) d
    in List.rev (parcours [] a)
;;

parcours_infixe2 arbre_test;;

(* ## Exercice 34 : parcours en largeur et en profondeur *)

(* In[23]: *)


let parcours_largeur a =
    let file = Queue.create () in
    (* fonction avec effet de bord sur la file *)
    let rec parcours () =
        if Queue.is_empty file
        then []
        else match Queue.pop file with
            | Feuille -> F :: (parcours ())
            | Noeud(g, d) -> begin
                Queue.push g file;
                Queue.push d file;
                N :: (parcours ())
            end
    in
    Queue.push a file;
    parcours ()
;;

parcours_largeur arbre_test;;

(* En remplaçant la file par une pile (`Stack`), on obtient le parcours en profondeur, avec la même complexité. *)

(* In[24]: *)


let parcours_profondeur a =
    let file = Stack.create () in
    (* fonction avec effet de bord sur la file *)
    let rec parcours () =
        if Stack.is_empty file
        then []
        else match Stack.pop file with
            | Feuille -> F :: (parcours ())
            | Noeud(g, d) -> begin
                Stack.push g file;
                Stack.push d file;
                N :: (parcours ())
            end
    in
    Stack.push a file;
    parcours ()
;;

parcours_profondeur arbre_test;;

(* ## Exercice 35 et fin *)

(* In[25]: *)


(* Reconstruction depuis le parcours prefixe *)

let test_prefixe = parcours_prefixe2 arbre_test;;

(* In[26]: *)


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
    | F :: p -> (Feuille, p)
    | N :: p ->
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
reconstruit_prefixe (N :: F :: F :: test_prefixe);; (* échoue *);;

(* In[27]: *)


(* Reconstruction depuis le parcours en largeur *)

(* Ce n'est pas évident quand on ne connait pas. L'idée est de se servir d'une file
   pour stocker les arbres qu'on reconstruit peu à peu depuis les feuilles. La file
   permet de récupérer les bons sous-arbres quand on rencontre un noeud *)

let largeur_test = parcours_largeur arbre_test;;

(* In[28]: *)


let reconstruit_largeur parcours =
    let file = Queue.create () in
    (* Fonction avec effets de bord *)
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

(* In[29]: *)


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

(* ----
# Conclusion

Fin. À la séance prochaine. *)
