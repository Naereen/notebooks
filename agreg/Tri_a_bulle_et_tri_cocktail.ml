(*
This OCaml script was exported from a Jupyter notebook
using an open-source software (under the MIT License) written by @Naereen
from https://github.com/Naereen/Jupyter-Notebook-OCaml
This software is still in development, please notify me of a bug at
https://github.com/Naereen/Jupyter-Notebook-OCaml/issues/new if you find one
*)

(* # Table of Contents
 <p><div class="lev1 toc-item"><a href="#Exercice-d'algorithmique---Agrégation-Option-Informatique" data-toc-modified-id="Exercice-d'algorithmique---Agrégation-Option-Informatique-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Exercice d'algorithmique - Agrégation Option Informatique</a></div><div class="lev2 toc-item"><a href="#Préparation-à-l'agrégation---ENS-de-Rennes,-2016-17" data-toc-modified-id="Préparation-à-l'agrégation---ENS-de-Rennes,-2016-17-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Préparation à l'agrégation - ENS de Rennes, 2016-17</a></div><div class="lev2 toc-item"><a href="#À-propos-de-ce-document" data-toc-modified-id="À-propos-de-ce-document-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>À propos de ce document</a></div><div class="lev2 toc-item"><a href="#Le-problème-:-tri-à-bulles-et-tri-cocktail" data-toc-modified-id="Le-problème-:-tri-à-bulles-et-tri-cocktail-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Le problème : tri à bulles et tri cocktail</a></div><div class="lev2 toc-item"><a href="#Tri-à-bulles" data-toc-modified-id="Tri-à-bulles-14"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Tri à bulles</a></div><div class="lev2 toc-item"><a href="#Tests" data-toc-modified-id="Tests-15"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Tests</a></div><div class="lev3 toc-item"><a href="#Utilitaire-pour-des-tests" data-toc-modified-id="Utilitaire-pour-des-tests-151"><span class="toc-item-num">1.5.1&nbsp;&nbsp;</span>Utilitaire pour des tests</a></div><div class="lev3 toc-item"><a href="#Tests-du-tri-à-bulle" data-toc-modified-id="Tests-du-tri-à-bulle-152"><span class="toc-item-num">1.5.2&nbsp;&nbsp;</span>Tests du tri à bulle</a></div><div class="lev2 toc-item"><a href="#Tri-cocktail" data-toc-modified-id="Tri-cocktail-16"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Tri cocktail</a></div><div class="lev2 toc-item"><a href="#Tests" data-toc-modified-id="Tests-17"><span class="toc-item-num">1.7&nbsp;&nbsp;</span>Tests</a></div><div class="lev2 toc-item"><a href="#Comparaison" data-toc-modified-id="Comparaison-18"><span class="toc-item-num">1.8&nbsp;&nbsp;</span>Comparaison</a></div><div class="lev3 toc-item"><a href="#Première-comparaison-:-$n-=-100$" data-toc-modified-id="Première-comparaison-:-$n-=-100$-181"><span class="toc-item-num">1.8.1&nbsp;&nbsp;</span>Première comparaison : <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax MathJax_Processing" id="MathJax-Element-3-Frame" tabindex="0"></span><script type="math/tex" id="MathJax-Element-3">n = 100</script></a></div><div class="lev3 toc-item"><a href="#Autre-comparaison-:-$n-=-1000$" data-toc-modified-id="Autre-comparaison-:-$n-=-1000$-182"><span class="toc-item-num">1.8.2&nbsp;&nbsp;</span>Autre comparaison : <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax MathJax_Processing" id="MathJax-Element-4-Frame" tabindex="0"></span><script type="math/tex" id="MathJax-Element-4">n = 1000</script></a></div><div class="lev2 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-19"><span class="toc-item-num">1.9&nbsp;&nbsp;</span>Conclusion</a></div><div class="lev3 toc-item"><a href="#Question-/-exercice" data-toc-modified-id="Question-/-exercice-191"><span class="toc-item-num">1.9.1&nbsp;&nbsp;</span>Question / exercice</a></div><div class="lev3 toc-item"><a href="#Liens" data-toc-modified-id="Liens-192"><span class="toc-item-num">1.9.2&nbsp;&nbsp;</span>Liens</a></div> *)

(* # Exercice d'algorithmique - Agrégation Option Informatique
## Préparation à l'agrégation - ENS de Rennes, 2016-17
- *Date* : 29 août 2017
- *Auteur* : [Lilian Besson](https://GitHub.com/Naereen/notebooks/) *)

(* ## À propos de ce document
- Ceci est une *proposition* de correction, pour un exercice (simple) d'algorithmique, pour la préparation à l'[agrégation de mathématiques, option informatique](http://Agreg.org/Textes/).
- Ce document est un [notebook Jupyter](https://www.Jupyter.org/), et [est open-source sous Licence MIT sur GitHub](https://github.com/Naereen/notebooks/tree/master/agreg/), comme les autres solutions de textes de modélisation que [j](https://GitHub.com/Naereen)'ai écrite cette année.
- L'implémentation sera faite en OCaml, version 4+ : *)

(* In[1]: *)


Sys.command "ocaml -version";;

(* ----

## Le problème : tri à bulles et tri cocktail

On s'intéresse à deux algorithmes de tris.
Pour plus de détails, voir les pages Wikipédia (ou le [Cormen] par exemple) :

- [Tri à bulle](https://fr.wikipedia.org/wiki/Tri_%C3%A0_bulles),
- [Tri cocktail](https://fr.wikipedia.org/wiki/Tri_cocktail).

On veut implémenter les deux et les comparer, sur plein d'entrées. *)

(* ----

## Tri à bulles

Commençons par le plus classique. *)

(* In[2]: *)


(** Un échange T[i] <-> T[j]. Utilise une valeur temporaire *)
let swap tab i j =
    let tmp = tab.(i) in
    tab.(i) <- tab.(j);
    tab.(j) <- tmp
;;

(* Le tri à bulle a une complexité en $\mathcal{O}(n^2)$ dans le pire des cas et en moyenne.
Il a l'avantage d'être en place. *)

(* In[3]: *)


let tri_bulle cmp tab =
    let n = Array.length tab in
    for i = n - 1 downto 1 do
        for j = 0 to i - 1 do
            if cmp tab.(j + 1) tab.(j) < 0 then
                swap tab (j + 1) j;
        done
    done
;;

(* On utilise une fonction de comparaison générique. La fonction ``compare`` ([``Pervasives.compare``](http://caml.inria.fr/pub/docs/manual-ocaml/libref/Pervasives.html#VALcompare)) fonctionne pour tous les types par défaut. *)

(* Une version plus efficace existe aussi ([voir ces explications](https://fr.wikipedia.org/wiki/Tri_%C3%A0_bulles#Principe_et_pseudo-code)). *)

(* In[4]: *)


let tri_bulle_opt cmp tab =
    let n = Array.length tab in
    let i = ref 0 in
    let last_swap = ref (-1) in
    while !i < n - 1 do
        (* séquence d'échanges sur T[i..n]: *)
        last_swap := n - 1;
        for j = n-1 downto !i + 1 do
            if cmp tab.(j) tab.(j-1) < 0 then begin
                swap tab j (j-1);
                last_swap := j - 1
            end;
            (* i avance "plus vite" :*)
            i := !last_swap + 1;
        done
    done
;;

(* ----

## Tests

On fait quelques tests. *)

(* ### Utilitaire pour des tests *)

(* In[5]: *)


(** Taille max des éléments dans les tableaux aléatoires *)
let maxint = int_of_float(1e3);;

(* In[9]: *)


(** Créer un tableau aléatoire. En O(n). *)
let rand_array length =
    Array.init length (fun _ -> Random.int maxint)
;; 

(* In[10]: *)


(** Vérifie que chaque élément du tableau n'y est qu'une seule fois (test l'égalité <> et pas !==).
    Mal codé, en O(n^2). *)
let isInjArray tab =
    try begin
        Array.iteri (fun i x -> 
            (Array.iteri (fun j y -> 
                assert( (x<>y) || (i=j) ) 
            ) tab) 
        ) tab;
        true
        end
    with _ -> false
;;

(* In[11]: *)


(** En moyenne, est en O(n^2) si [maxint] est bien plus grand que [n]. *)
let rand_array_inj = function
    | 0 -> [||]
    | length ->
        let tab = ref (rand_array length) in
        while not(isInjArray (!tab)) do
            tab := rand_array length;
        done;
        !tab
;;

(* Cette fonction prend un seul argument, la taille du tableau : *)

(* In[12]: *)


rand_array_inj 12;;

(* In[13]: *)


rand_array_inj 12;;

(* In[14]: *)


rand_array_inj 12;;

(* Fonction de test : *)

(* In[22]: *)


let print = Printf.printf;; 

let testtri mysort cmp length nbrun () =
    print "Test d'un tri, %i simulations avec des tableaux de longueur %i.\n " nbrun length;
    for i = 0 to nbrun - 1 do
        let t1 = rand_array length in
        let t2 = Array.copy t1 in
        mysort cmp t1;
        Array.fast_sort cmp t2;
        try assert( t1 = t2 ) with _ -> begin
            print "Avec des tableaux de taille %i, le test numéro %i a échoué." length i;
            Format.printf "@[t1=[|"; Array.iter (fun i -> Format.printf " %i;" i) t1; Format.printf "|]@]@ ";
            Format.printf "@[t2=[|"; Array.iter (fun i -> Format.printf " %i;" i) t2; Format.printf "|]@]@ ";
        end;
    done;
    flush_all ();
;;

(* ### Tests du tri à bulle *)

(* La fonction de tri par défaut marche bien, évidemment. *)

(* In[23]: *)


testtri Array.sort compare 10 10 ();;

(* In[24]: *)


testtri tri_bulle compare 10 10 ();;

(* In[25]: *)


testtri tri_bulle_opt compare 10 10 ();;

(* Ça marche ! *)

(* In[26]: *)


testtri tri_bulle compare 100 1000 ();;

(* ----

## Tri cocktail *)

(* Il est très semblable au tri à bulle, sauf que le tableau sera parcouru alternativement dans les deux sens.

Le tri cocktail a une complexité en $\mathcal{O}(n^2)$ dans le pire des cas et en moyenne.
Il a l'avantage d'être en place. *)

(* In[27]: *)


let tri_cocktail cmp tab =
    let n = Array.length tab in
    let echange = ref true in
    while !echange do
        echange := false;
        (* Parcours croissant *)
        for j = 0 to n - 2 do
            if cmp tab.(j + 1) tab.(j) < 0 then begin
                swap tab (j + 1) j;
                echange := true
            end;
        done;
        (* Parcours decroissant *)
        for j = n - 2 downto 0 do
            if cmp tab.(j + 1) tab.(j) < 0 then begin
                swap tab (j + 1) j;
                echange := true
            end;
        done;
    done;
;;

(* Il existe aussi une version plus efficace, qui diminue la taille des parcours au fur et à mesure. *)

(* In[28]: *)


let tri_cocktail_opt cmp tab =
    let n = Array.length tab in
    let echange = ref true in
    let debut = ref 0 and fin = ref (n - 2) in
    while !echange do
        echange := false;
        (* Parcours croissant *)
        for j = !debut to !fin do
            if cmp tab.(j + 1) tab.(j) < 0 then begin
                swap tab (j + 1) j;
                echange := true
            end;
        done;
        fin := !fin - 1;
        (* Parcours decroissant *)
        for j = !fin downto !debut do
            if cmp tab.(j + 1) tab.(j) < 0 then begin
                swap tab (j + 1) j;
                echange := true
            end;
        done;
        debut := !debut + 1;
    done;
;;

(* ----

## Tests
Et d'autres tests. *)

(* In[52]: *)


testtri tri_cocktail compare 10 10 ();;

(* In[53]: *)


testtri tri_cocktail_opt compare 10 10 ();;

(* Ça marche ! *)

(* In[54]: *)


testtri tri_cocktail compare 100 1000 ();;

(* ----

## Comparaison *)

(* Avec [ce morceau de code](https://stackoverflow.com/a/9061574/) on peut facilement mesurer le temps d'exécution : *)

(* In[33]: *)


let time f =
    let t = Sys.time() in
    let res = f () in
    Printf.printf "    Temps en secondes: %fs\n" (Sys.time() -. t);
    flush_all ();
    res
;;

(* ### Première comparaison : $n = 100$ *)

(* In[75]: *)


time (testtri Array.sort compare 100 10000);;

(* In[76]: *)


time (testtri tri_bulle compare 100 10000);;

(* In[79]: *)


time (testtri tri_bulle_opt compare 100 10000);;

(* In[80]: *)


time (testtri tri_cocktail compare 100 10000);;

(* In[41]: *)


time (testtri tri_cocktail_opt compare 100 10000);;

(* Sur de petits tableaux, les versions "optimisées" ne sont pas plus forcément plus rapides (comme toujours).

On vérifie quand même que sur des tableaux aléatoires, le tri cocktail optimisé semble le plus rapide des quatre implémentations. *)

(* ### Autre comparaison : $n = 1000$

Ca suffit à voir que les quatre algorithmes implémentés ici ne sont pas en temps sous quadratique. *)

(* In[81]: *)


time (testtri Array.sort compare 1000 1000);;

(* In[82]: *)


time (testtri tri_bulle compare 1000 1000);;

(* In[83]: *)


time (testtri tri_bulle_opt compare 1000 1000);;

(* In[84]: *)


time (testtri tri_cocktail compare 1000 1000);;

(* In[85]: *)


time (testtri tri_cocktail_opt compare 1000 1000);;

(* ----

## Conclusion

Les deux algorithmes ne sont pas trop difficiles à implémenter, et fonctionnent de façon très similaire.

### Question / exercice
- Prouver la correction de chaque algorithme, à l'aide d'invariants bien choisis.
- Prouver la complexité en temps.
- Pourquoi ces noms, à bulle et cocktail ?

### Liens
Allez voir [d'autres notebooks](https://nbviewer.jupyter.org/github/Naereen/notebooks/tree/master/agreg/) ! *)
