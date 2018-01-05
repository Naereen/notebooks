(*
This OCaml script was exported from a Jupyter notebook
using an open-source software (under the MIT License) written by @Naereen
from https://github.com/Naereen/Jupyter-Notebook-OCaml
This software is still in development, please notify me of a bug at
https://github.com/Naereen/Jupyter-Notebook-OCaml/issues/new if you find one
*)

(* # Table of Contents
 <p><div class="lev1 toc-item"><a href="#Texte-d'oral-de-modélisation---Agrégation-Option-Informatique" data-toc-modified-id="Texte-d'oral-de-modélisation---Agrégation-Option-Informatique-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Texte d'oral de modélisation - Agrégation Option Informatique</a></div><div class="lev2 toc-item"><a href="#Préparation-à-l'agrégation---ENS-de-Rennes,-2017-18" data-toc-modified-id="Préparation-à-l'agrégation---ENS-de-Rennes,-2017-18-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Préparation à l'agrégation - ENS de Rennes, 2017-18</a></div><div class="lev2 toc-item"><a href="#À-propos-de-ce-document" data-toc-modified-id="À-propos-de-ce-document-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>À propos de ce document</a></div><div class="lev2 toc-item"><a href="#Question-de-programmation" data-toc-modified-id="Question-de-programmation-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Question de programmation</a></div><div class="lev3 toc-item"><a href="#Modélisation" data-toc-modified-id="Modélisation-131"><span class="toc-item-num">1.3.1&nbsp;&nbsp;</span>Modélisation</a></div><div class="lev2 toc-item"><a href="#Solution" data-toc-modified-id="Solution-14"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Solution</a></div><div class="lev3 toc-item"><a href="#Types-et-représentations" data-toc-modified-id="Types-et-représentations-141"><span class="toc-item-num">1.4.1&nbsp;&nbsp;</span>Types et représentations</a></div><div class="lev3 toc-item"><a href="#Algorithmes" data-toc-modified-id="Algorithmes-142"><span class="toc-item-num">1.4.2&nbsp;&nbsp;</span>Algorithmes</a></div><div class="lev2 toc-item"><a href="#Complexités" data-toc-modified-id="Complexités-15"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Complexités</a></div><div class="lev3 toc-item"><a href="#En-espace" data-toc-modified-id="En-espace-151"><span class="toc-item-num">1.5.1&nbsp;&nbsp;</span>En espace</a></div><div class="lev3 toc-item"><a href="#En-temps" data-toc-modified-id="En-temps-152"><span class="toc-item-num">1.5.2&nbsp;&nbsp;</span>En temps</a></div><div class="lev2 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-16"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Conclusion</a></div><div class="lev3 toc-item"><a href="#Qualités" data-toc-modified-id="Qualités-161"><span class="toc-item-num">1.6.1&nbsp;&nbsp;</span>Qualités</a></div><div class="lev3 toc-item"><a href="#Défauts" data-toc-modified-id="Défauts-162"><span class="toc-item-num">1.6.2&nbsp;&nbsp;</span>Défauts</a></div> *)

(* # Texte d'oral de modélisation - Agrégation Option Informatique
## Préparation à l'agrégation - ENS de Rennes, 2017-18
- *Date* : 6 décembre 2017
- *Auteur* : [Lilian Besson](https://GitHub.com/Naereen/notebooks/)
- *Texte*: Annale 2018, ["Polynômes avec des nombres flottants" (public2018-D2)](http://agreg.org/Textes/public2018-D2.pdf) *)

(* ## À propos de ce document
- Ceci est une *proposition* de correction, partielle et probablement non-optimale, pour la partie implémentation d'un [texte d'annale de l'agrégation de mathématiques, option informatique](http://Agreg.org/Textes/).
- Ce document est un [notebook Jupyter](https://www.Jupyter.org/), et [est open-source sous Licence MIT sur GitHub](https://github.com/Naereen/notebooks/tree/master/agreg/), comme les autres solutions de textes de modélisation que [j](https://GitHub.com/Naereen)'ai écrite cette année.
- L'implémentation sera faite en OCaml, version 4+ : *)

(* In[1]: *)


Sys.command "ocaml -version";;
print_endline Sys.ocaml_version;;

(* In[7]: *)


let print f =
    let r = Printf.printf f in
    flush_all();
    r
;;

(* ----
## Question de programmation
La question de programmation pour ce texte était donnée en page 6 :

Cet exercice consiste à observer le comportement des nombres en virgule flottante de la
machine.
Toutes les variables utilisées seront de type `double` ou `float` selon le langage choisi.
On écrit un programme qui évalue $$S = \sum_{i=0}^{\infty} \left(1 - \frac{1}{\rho}\right)^i$$
où $\rho$ est une puissance de $2$ suffisamment grande, par exemple $\rho = 2^{20}$.

Si on calcule naïvement $S_n = \sum_{i=0}^{n} (1 - \frac{1}{\rho})^i$, en ajoutant les termes un par un dans l'ordre des puissances croissantes, on remarque quand $n$ est suffisamment grand, $S_{n+1} = S_n \oplus (1 - \frac{1}{\rho})^{n+1}$
lorsqu’on calcule en `double` (ou `float`).

En évaluant $S$ sous la forme $$S = \sum_{j=0}^{\infty} \sum_{k=0}^{K-1} \left(1 - \frac{1}{\rho}\right)^{jK + k}$$
ce phénomène se produit pour des rangs plus grands que précedemment, l'approximation de $S$ calculée est donc meilleure. On pourra essayer plusieurs valeurs de $K$ ($1,10,100,1000,10000$) et comparer. $K = 1$ correspond au calcul naïf de $S$ ci-dessus.
Optionnellement, le programme pourra également calculer une borne sur l’erreur com-
mise sur $S$.

### Modélisation
On est libre de choisir l'approche, mais ici il n'y a pas tellement de choix, on va utiliser des `float` de OCaml. *)

(* ----
## Solution

On va essayer d'être rapide et de faire simple. *)

(* ### Types et représentations

Rien à faire ici, on va travailler avec des `float` de OCaml classiques. *)

(* ### Algorithmes *)

(* Première méthode de calcul. On remarque qu'on est déjà malin, on n'utilise aucune exponentiation mais simplement un accumulateur `terme` qui vaut $(1-1/\rho)^j$ pour les valeurs successives de $j$, et qu'on met à jour par une simple multiplication. *)

(* In[39]: *)


let premiercalcul (rho : float) (n : int) =
    let somme = ref 0. in
    let unmoinsunsurrho = 1. -. (1. /. rho) in
    let terme = ref 1. in
    for _ = 0 to n do  (* terme = (1-1/rho)^j pour j = _ *)
        somme := !somme +. !terme; (* somme = sum_k=0^j terme_k *)
        terme := !terme *. unmoinsunsurrho; (* conserve l'invariant de boucle *)
    done;
    !somme
;;

(* Voyons un exemple : *)

(* In[10]: *)


let rho = 2. ** 20.;;

(* In[14]: *)


1. -. 1. /. rho;;

(* Cette valeur est proche de $1$, mais strictement plus petite que $1$, et donc $(1-1/\rho)^i \to 0$ géométriquement vite, ainsi $S_n$ converge bien vers $S$ pour $n \to \infty$. *)

(* In[40]: *)


for n = 0 to 10 do
    print "\nS_%i \t= %g" n (premiercalcul rho n);
done;;;

(* In[42]: *)


for n = 1000 to 1010 do
    print "\nS_%i \t= %g" n (premiercalcul rho n);
done;;;

(* Deuxième méthode de calcul : *)

(* In[21]: *)


let deuxiemecalcul (rho : float) (k : int) (n : int) =
    let somme = ref 0. in
    let unmoinsunsurrho = 1. -. (1. /. rho) in
    let terme = ref 1. in
    for _ = 0 to n do
        for _ = 0 to k-1 do
            somme := !somme +. !terme;
            terme := !terme *. unmoinsunsurrho;
        done;
        terme := !terme *. unmoinsunsurrho;
    done;
    !somme
;;

(* Voyons le même exemple : *)

(* In[27]: *)


let valeurs_k = [|1; 10; 100; 1000; 10000|] in

for i = 0 to (Array.length valeurs_k) - 1 do
    let k = valeurs_k.(i) in
    print "\n\nFor K = %i ..." k;
    for n = 0 to 10 do
        print "\nS_%i \t= %g" n (deuxiemecalcul rho k n);
    done;
done;;;

(* Avec de grandes valeurs de $n$, on semble converger vers la limite $S$, d'autant plus vite que $K$ est grand. *)

(* In[38]: *)


let valeurs_n = [|100; 1000; 10000; 100000|] in
let valeurs_k = [|1; 10; 100; 1000; 10000|] in

for i = 0 to (Array.length valeurs_k) - 1 do
    let k = valeurs_k.(i) in
    print "\n\nFor K = %i ..." k;
    for j = 0 to (Array.length valeurs_n) - 1 do
        let n = valeurs_n.(j) in
        print "\nS_%i \t= %g" n (deuxiemecalcul rho k n);
    done;
done;;;

(* ## Complexités *)

(* ### En espace
Ces calculs coûtent un espace constant en mémoire.

(ou $\log n$ si on considère que stocker des entiers bornés par $n$ coûtent un espace $\log n$) *)

(* ### En temps
Ces calculs coûtent un temps linéaire en $n$. *)

(* ----
## Conclusion

Voilà pour la question obligatoire de programmation.

### Qualités
- On a fait des exemples et *on les garde* dans ce qu'on présente au jury,
- On a testé la fonction exigée sur de petits exemples et sur un exemple de taille réelle (venant du texte).

### Défauts
- Par contre, on est un peu pauvre en visualisation et explication,
- Et on a implémenté aucun autre développement. A suivre, j'en ajouterai quand je peux.


> Bien-sûr, ce petit notebook ne se prétend pas être une solution optimale, ni exhaustive.

> Vous auriez pu choisir de modéliser le problème avec une autre approche, mais je ne vois pas ce qu'on aurait pu faire différement. *)

(* > C'est tout pour aujourd'hui les amis, allez voir [ici pour d'autres corrections](https://github.com/Naereen/notebooks/tree/master/agreg), et que la force soit avec vous ! *)
