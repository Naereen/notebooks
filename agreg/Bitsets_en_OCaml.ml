(*
This OCaml script was exported from a Jupyter notebook
using an open-source software (under the MIT License) written by @Naereen
from https://github.com/Naereen/Jupyter-Notebook-OCaml
This software is still in development, please notify me of a bug at
https://github.com/Naereen/Jupyter-Notebook-OCaml/issues/new if you find one
*)

(* # Table of Contents
 <p><div class="lev1 toc-item"><a href="#BitSets-en-OCaml" data-toc-modified-id="BitSets-en-OCaml-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>BitSets en OCaml</a></div><div class="lev2 toc-item"><a href="#Type-abstrait" data-toc-modified-id="Type-abstrait-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Type abstrait</a></div><div class="lev2 toc-item"><a href="#Implémentation" data-toc-modified-id="Implémentation-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Implémentation</a></div><div class="lev2 toc-item"><a href="#Exemples" data-toc-modified-id="Exemples-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Exemples</a></div><div class="lev3 toc-item"><a href="#Tests-des-opérations-unaires" data-toc-modified-id="Tests-des-opérations-unaires-131"><span class="toc-item-num">1.3.1&nbsp;&nbsp;</span>Tests des opérations unaires</a></div><div class="lev3 toc-item"><a href="#Tests-des-opérations-binaires" data-toc-modified-id="Tests-des-opérations-binaires-132"><span class="toc-item-num">1.3.2&nbsp;&nbsp;</span>Tests des opérations binaires</a></div><div class="lev2 toc-item"><a href="#Comparaison" data-toc-modified-id="Comparaison-14"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Comparaison</a></div><div class="lev3 toc-item"><a href="#Mesure-un-temps-d'éxecution" data-toc-modified-id="Mesure-un-temps-d'éxecution-141"><span class="toc-item-num">1.4.1&nbsp;&nbsp;</span>Mesure un temps d'éxecution</a></div><div class="lev3 toc-item"><a href="#Suite-de-test-pour-bit_set_32" data-toc-modified-id="Suite-de-test-pour-bit_set_32-142"><span class="toc-item-num">1.4.2&nbsp;&nbsp;</span>Suite de test pour <code>bit_set_32</code></a></div><div class="lev3 toc-item"><a href="#Suite-de-test-pour-bool-array" data-toc-modified-id="Suite-de-test-pour-bool-array-143"><span class="toc-item-num">1.4.3&nbsp;&nbsp;</span>Suite de test pour <code>bool array</code></a></div><div class="lev3 toc-item"><a href="#Suite-de-test-pour-Set.Make(Int)" data-toc-modified-id="Suite-de-test-pour-Set.Make(Int)-144"><span class="toc-item-num">1.4.4&nbsp;&nbsp;</span>Suite de test pour <code>Set.Make(Int)</code></a></div><div class="lev3 toc-item"><a href="#Mesurer-les-temps-d'exécution" data-toc-modified-id="Mesurer-les-temps-d'exécution-145"><span class="toc-item-num">1.4.5&nbsp;&nbsp;</span>Mesurer les temps d'exécution</a></div><div class="lev2 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-15"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Conclusion</a></div> *)

(* # BitSets en OCaml

Let *BitSets* sont une implémentation efficace pour représenter, stocker et manipuler des ensembles de *petits* entiers.

Avec un seul entier 32 bits, on peut représenter *tous* les ensembles d'entiers de $\{0,\dots,31\}$.

On utilise les [opérations bit à bit ("bitwise")](caml.inria.fr/pub/docs/manual-ocaml/libref/Pervasives.html#VALmin_int) de OCaml pour effectuer les opérations de base sur les ensembles.

Cette implémentation est inspiré de [celle ci](http://ocaml-lib.sourceforge.net/doc/BitSet.html). *)

(* ## Type abstrait
Je vais faire ça à l'arrache, mais on pourrait faire soit un module qui contient un type interne (caché), soit avec un champ d'enregistrement `{ n : int }`.

Cette approche est la plus simple, mais montre un peu le fonctionnement interne (on pourrait vouloir l'éviter). *)

(* In[1]: *)


type bit_set_32 = int;;

(* In[2]: *)


let max_size_bit_set_32 = 32;;

(* Avec [Int64](http://caml.inria.fr/pub/docs/manual-ocaml/libref/Int64.html) on pourrait faire la même chose avec des entiers sur 64 bits. La flemme. *)

(* ---
## Implémentation
Les ensembles ne seront pas mutables dynamiquement : comme une liste, toute fonction qui modifie un `bit_set_32` renvoit un nouveau `bit_set_32`. *)

(* In[3]: *)


let empty () : bit_set_32 = 0
;;

(* Le singleton $\{i\}$ est codé comme $2^i$ donc $1$ au bit en $i$ème position.
En Python, c'est `1 << i` (ou `2**i`), et en OCaml c'est `1 lsl i`. *)

(* In[4]: *)


let create (i : int) : bit_set_32 =
    assert ((0 <= i) && (i < max_size_bit_set_32));
    1 lsl i
;;

(* Si on voulait utiliser la syntaxe Python, on pourrait faire ça : *)

(* In[5]: *)


let ( << ) = ( lsl );;
let ( >> ) = ( lsr );;

(* La copie ne fait pas beaucoup de sens comme la stucture n'est pas mutable... Mais soit. *)

(* In[6]: *)


let copy (b : bit_set_32) : bit_set_32 =
    b + 0 (* enough ? *)
;;
let clone = copy;;

(* `set b n` permet d'ajouter `n` dans l'ensemble `b`, et `unset b n` permet de l'enlever (peu importe s'il était présent ou non). *)

(* In[7]: *)


let set (b : bit_set_32) (n : int) : bit_set_32 =
    b lor (1 lsl n)
;;

let add = set;;

(* In[8]: *)


let unset (b : bit_set_32) (n : int) : bit_set_32 =
    b land (lnot (1 lsl n))
;;

let remove = unset;;

(* On peut combiner `set` et `unset` pour faire : *)

(* In[9]: *)


let put (b : bit_set_32) (p : bool) (n : int) : bit_set_32 =
    if p then set b n else unset b n
;;

(* Ces deux autres opérations sont rapides : *)

(* In[10]: *)


let is_set (b : bit_set_32) (n : int) : bool =
    let i = (b land (1 lsl n)) lsr n in
    i = 1
;;

let contains_int = is_set;;
let is_in = is_set;;

(* In[11]: *)


let toggle (b : bit_set_32) (n : int) : bit_set_32 =
    put b (not (is_set b n)) n
;;

(* La comparaison et le test d'égalité sont évidents. *)

(* In[12]: *)


let compare (b1 : bit_set_32) (b2 : bit_set_32) : int =
    Pervasives.compare b1 b2
;;

(* In[13]: *)


let equals (b1 : bit_set_32) (b2 : bit_set_32) : bool =
    b1 = b2
;;

(* On peut chercher à être plus efficace que cette implémentation impérative et naïve. Essayez ! *)

(* In[14]: *)


let count (b : bit_set_32) : int =
    let s = ref 0 in
    for n = 0 to max_size_bit_set_32 - 1 do
        if is_set b n then incr s
    done;
    !s
;;

let length = count;;

(* Pour la création des exemples, on va aussi se permettre de convertir un `bit_set_32` en une `int list`, et inversement de créer un `bit_set_32` depuis une `int list`. *)

(* In[15]: *)


let bit_set_32_to_list (b : bit_set_32) : (int list) =
    let list_of_b = ref [] in
    for n = 0 to max_size_bit_set_32 - 1 do
        if is_set b n then
        list_of_b := n :: !list_of_b
    done;
    List.rev (!list_of_b)
;;

(* In[16]: *)


let bit_set_32_from_list (list_of_b : int list) : bit_set_32 =
    let b = ref (empty()) in
    List.iter (fun i -> b := add !b i) list_of_b;
    !b
;;

(* In[17]: *)


let bit_set_32_iter (f : int -> unit) (b : bit_set_32) : unit =
    List.iter f (bit_set_32_iter_to_list b)
;;

(* Pour l'affichage des exemples, on va aussi se permettre de convertir un `bit_set_32` en une `string`. *)

(* In[18]: *)


let bit_set_32_to_string (b : bit_set_32) : string =
    let list_of_b = bit_set_32_to_list b in
    match List.length list_of_b with
    | 0 -> "{}"
    | 1 -> "{" ^ (string_of_int (List.hd list_of_b)) ^ "}"
    | _ -> begin
        let s = ref ("{" ^ (string_of_int (List.hd list_of_b))) in
        List.iter (fun i -> s := !s ^ ", " ^ (string_of_int i)) (List.tl list_of_b);
        !s ^ "}"
    end
;;

(* In[19]: *)


let print_bit_set_32 (b : bit_set_32) : unit =
    print_endline (bit_set_32_to_string b)
;;

(* Comme le domaine est fixé (à $\{0,\dots,31\}$), on peut prendre le complémentaire. *)

(* In[20]: *)


let complementaire (b : bit_set_32) : bit_set_32 =
    lnot b
;;

(* Les opérations intersection, union, différence et différence symétrique sont très faciles. *)

(* In[21]: *)


let intersection (b1 : bit_set_32) (b2 : bit_set_32) : bit_set_32 =
    b1 land b2
;;

(* In[22]: *)


let union (b1 : bit_set_32) (b2 : bit_set_32) : bit_set_32 =
    b1 lor b2
;;

(* Avec l'union on peut facilement tester si `b1` est contenu dans `b2` ($b_1 \subset b_2 \equiv (b_1 \cup b_2) = b_2$) *)

(* In[23]: *)


let contains (b1 : bit_set_32) (b2 : bit_set_32) : bool =
    (union b1 b2) = b2
;;

(* In[24]: *)


let difference (b1 : bit_set_32) (b2 : bit_set_32) : bit_set_32 =
    intersection b1 (complementaire b2)
;;

(* In[25]: *)


let difference_sym (b1 : bit_set_32) (b2 : bit_set_32) : bit_set_32 =
    b1 lxor b2
;;

(* ---
## Exemples *)

(* In[26]: *)


print_bit_set_32 (empty());;

(* In[27]: *)


let b1 = bit_set_32_from_list [0; 12]
and b2 = bit_set_32_from_list [1; 3; 6]
and b3 = bit_set_32_from_list [0; 3; 6; 17]
;;

print_bit_set_32 b1;;
print_bit_set_32 b2;;
print_bit_set_32 b3;;

(* ### Tests des opérations unaires *)

(* Tester l'appartenance : *)

(* In[28]: *)


(is_in b1 3);;
(is_in b2 3);;
(is_in b3 3);;

(* In[29]: *)


(is_in b1 0);;
(is_in b2 0);;
(is_in b3 0);;

(* On peut ajouter une valeur : *)

(* In[30]: *)


print_bit_set_32 (add b1 20);;
print_bit_set_32 (add b2 20);;
print_bit_set_32 (add b3 20);;

(* Ou l'enlever : *)

(* In[31]: *)


print_bit_set_32 (remove b1 3);;
print_bit_set_32 (remove b2 3);;
print_bit_set_32 (remove b3 3);;

(* In[32]: *)


length b1;;
length b2;;
length b3;;

(* In[33]: *)


print_bit_set_32 (complementaire b1);;
print_bit_set_32 (complementaire b2);;
print_bit_set_32 (complementaire b3);;

print_bit_set_32 (complementaire (union (union b1 b2) b3));;

(* ### Tests des opérations binaires *)

(* In[34]: *)


print_bit_set_32 (union b1 b2);;
print_bit_set_32 (union b1 b3);;
print_bit_set_32 (union b2 b3);;

(* In[35]: *)


contains b1 b2;;
contains b1 b3;;
contains b1 (intersection b1 b3);;
contains (intersection b1 b3) b1;;
contains b1 (union b1 b3);;
contains b2 b3;;

(* In[36]: *)


print_bit_set_32 (intersection b1 b2);;
print_bit_set_32 (intersection b1 b3);;
print_bit_set_32 (intersection b2 b3);;

(* In[37]: *)


print_bit_set_32 (difference b1 b2);;
print_bit_set_32 (difference b1 b3);;
print_bit_set_32 (difference b2 b3);;

(* In[38]: *)


print_bit_set_32 (difference_sym b1 b2);;
print_bit_set_32 (difference_sym b1 b3);;
print_bit_set_32 (difference_sym b2 b3);;

(* ---
## Comparaison
On va essayer de comparer notre implémentation avec une implémentation naïve utilisant des `bool array` et une utilisant le [module `Set`](http://caml.inria.fr/pub/docs/manual-ocaml/libref/Set.S.html) de la bibliothèque standard. *)

(* ### Mesure un temps d'éxecution *)

(* In[132]: *)


let time (n : int) (f : unit -> 'a) : float =
    let t = Sys.time() in
    for _ = 0 to n-1 do
        ignore (f ());
    done;
    let delta_t = Sys.time() -. t in
    let t_moyen = delta_t /. (float_of_int n) in
    Printf.printf "    Temps en secondes: %fs\n" t_moyen;
    flush_all ();
    t_moyen
;;

(* In[43]: *)


Random.self_init();;

let random_int_0_31 () =
    Random.int 32
;;

(* ### Suite de test pour `bit_set_32` *)

(* Notre test va consister à créer un ensemble vide, et ajouter 100 fois de suite des valeurs aléatoires, en enlever d'autres etc. *)

(* In[50]: *)


let test_bit_set_32 n n1 n2 () =
    let b = ref (empty ()) in
    for _ = 0 to n do
        let nb_ajout = Random.int n1 in
        let nb_retrait = Random.int n2 in
        for i = 0 to nb_ajout + nb_retrait do
            let n = random_int_0_31 () in
            if i mod 2 = 0 then
                b := add !b n
            else
                b := remove !b n;
        done
    done;
    length !b
;;

(* In[91]: *)


test_bit_set_32 100 20 10 ();;

(* ### Suite de test pour `bool array` *)

(* Avec des `bool array`, on a l'avantage d'avoir une structure dynamique. *)

(* In[99]: *)


let test_boolarray n n1 n2 () =
    let b = Array.make max_size_bit_set_32 false in
    for _ = 0 to n do
        let nb_ajout = Random.int n1 in
        let nb_retrait = Random.int n2 in
        for i = 0 to nb_ajout + nb_retrait do
            let n = random_int_0_31 () in
            if i mod 2 = 0 then
                b.(n) <- true
            else
                b.(n) <- false
        done;
    done;
    Array.fold_left (+) 0 (Array.map (fun x -> if x then 1 else 0) b)
;;

(* In[127]: *)


test_boolarray 100 20 10 ();;

(* ### Suite de test pour `Set.Make(Int)` *)

(* In[116]: *)


module Int = struct
   type t = int
   let compare = compare
 end;;

module Int32Set = Set.Make(Int);;

(* Avec des `Set`, on a l'avantage d'avoir une structure dynamique, mais moins facile à manipuler. *)

(* In[125]: *)


let test_Int32Set n n1 n2 () =
    let b = ref (Int32Set.empty) in
    for _ = 0 to n do
        let nb_ajout = Random.int n1 in
        let nb_retrait = Random.int n2 in
        for i = 0 to nb_ajout + nb_retrait do
            let n = random_int_0_31 () in
            if i mod 2 = 0 then
                b := Int32Set.add n !b
            else
                b := Int32Set.remove n !b
        done;
    done;
    Int32Set.cardinal !b
;;

(* In[126]: *)


test_Int32Set 100 20 10 ();;

(* ### Mesurer les temps d'exécution *)

(* On va faire 500 répétitions de ces tests aléatoires, chacun avec 1000 fois des ajouts de 30 valeurs et des retraits de 20 valeurs. *)

(* In[134]: *)


time 500 (test_bit_set_32 1000 30 20);;

(* In[135]: *)


time 500 (test_boolarray 1000 30 20);;

(* In[136]: *)


time 500 (test_Int32Set 1000 30 20);;

(* Pour un second et dernier test, on va faire 500 répétitions de ces tests aléatoires, chacun avec 500 fois des ajouts de 100 valeurs et des retraits de 110 valeurs. *)

(* In[140]: *)


time 500 (test_bit_set_32 500 100 110);;

(* In[141]: *)


time 500 (test_boolarray 500 100 110);;

(* In[142]: *)


time 500 (test_Int32Set 500 100 110);;

(* ---
## Conclusion

Tout ça n'a pas servi à grand chose, on a réussi à montrer que pour des petits entiers, utiliser un `bool array` de taille 32 (fixe) est plus efficace qu'utiliser ces `bit sets`.

Ça suffit pour aujourd'hui !

> Allez voir [d'autres notebooks](https://github.com/Naereen/notebooks/) que j'ai écrit. *)
