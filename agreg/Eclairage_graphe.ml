(*
This OCaml script was exported from a Jupyter notebook
using an open-source software (under the MIT License) written by @Naereen
from https://github.com/Naereen/Jupyter-Notebook-OCaml
This software is still in development, please notify me of a bug at
https://github.com/Naereen/Jupyter-Notebook-OCaml/issues/new if you find one
*)

(* # Table of Contents
 <p><div class="lev1 toc-item"><a href="#Texte-d'oral-de-modélisation---Agrégation-Option-Informatique" data-toc-modified-id="Texte-d'oral-de-modélisation---Agrégation-Option-Informatique-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Texte d'oral de modélisation - Agrégation Option Informatique</a></div><div class="lev2 toc-item"><a href="#Préparation-à-l'agrégation---ENS-de-Rennes,-2016-17" data-toc-modified-id="Préparation-à-l'agrégation---ENS-de-Rennes,-2016-17-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Préparation à l'agrégation - ENS de Rennes, 2016-17</a></div><div class="lev2 toc-item"><a href="#À-propos-de-ce-document" data-toc-modified-id="À-propos-de-ce-document-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>À propos de ce document</a></div><div class="lev2 toc-item"><a href="#Question-de-programmation" data-toc-modified-id="Question-de-programmation-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Question de programmation</a></div><div class="lev3 toc-item"><a href="#Exercice" data-toc-modified-id="Exercice-131"><span class="toc-item-num">1.3.1&nbsp;&nbsp;</span>Exercice</a></div><div class="lev3 toc-item"><a href="#Besoin-de-plusieurs-exemples" data-toc-modified-id="Besoin-de-plusieurs-exemples-132"><span class="toc-item-num">1.3.2&nbsp;&nbsp;</span>Besoin de plusieurs exemples</a></div><div class="lev2 toc-item"><a href="#Solution" data-toc-modified-id="Solution-14"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Solution</a></div><div class="lev3 toc-item"><a href="#Représentation-du-graphe-et-de-la-proposition-d'éclairage" data-toc-modified-id="Représentation-du-graphe-et-de-la-proposition-d'éclairage-141"><span class="toc-item-num">1.4.1&nbsp;&nbsp;</span>Représentation du graphe et de la proposition d'éclairage</a></div><div class="lev3 toc-item"><a href="#Vérification" data-toc-modified-id="Vérification-142"><span class="toc-item-num">1.4.2&nbsp;&nbsp;</span>Vérification</a></div><div class="lev3 toc-item"><a href="#Exemples" data-toc-modified-id="Exemples-143"><span class="toc-item-num">1.4.3&nbsp;&nbsp;</span>Exemples</a></div><div class="lev4 toc-item"><a href="#Pour-des-éclairages-valides." data-toc-modified-id="Pour-des-éclairages-valides.-1431"><span class="toc-item-num">1.4.3.1&nbsp;&nbsp;</span>Pour des éclairages valides.</a></div><div class="lev4 toc-item"><a href="#Pour-des-éclairages-non-valides-:" data-toc-modified-id="Pour-des-éclairages-non-valides-:-1432"><span class="toc-item-num">1.4.3.2&nbsp;&nbsp;</span>Pour des éclairages non valides :</a></div><div class="lev3 toc-item"><a href="#Bonus-:-vérifier-que-le-graphe-est-valide" data-toc-modified-id="Bonus-:-vérifier-que-le-graphe-est-valide-144"><span class="toc-item-num">1.4.4&nbsp;&nbsp;</span>Bonus : vérifier que le graphe est valide</a></div><div class="lev2 toc-item"><a href="#Bonus-:-énumération-de-tous-les-éclairages-possibles" data-toc-modified-id="Bonus-:-énumération-de-tous-les-éclairages-possibles-15"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Bonus : énumération de tous les éclairages possibles</a></div><div class="lev3 toc-item"><a href="#Énumération-des-éclairages-possibles" data-toc-modified-id="Énumération-des-éclairages-possibles-151"><span class="toc-item-num">1.5.1&nbsp;&nbsp;</span>Énumération des éclairages possibles</a></div><div class="lev3 toc-item"><a href="#Liste-de-taille-minimale-parmi-une-liste-de-listes" data-toc-modified-id="Liste-de-taille-minimale-parmi-une-liste-de-listes-152"><span class="toc-item-num">1.5.2&nbsp;&nbsp;</span>Liste de taille minimale parmi une liste de listes</a></div><div class="lev3 toc-item"><a href="#Trouver-un-éclairage-optimal" data-toc-modified-id="Trouver-un-éclairage-optimal-153"><span class="toc-item-num">1.5.3&nbsp;&nbsp;</span>Trouver un éclairage optimal</a></div><div class="lev3 toc-item"><a href="#Exemples" data-toc-modified-id="Exemples-154"><span class="toc-item-num">1.5.4&nbsp;&nbsp;</span>Exemples</a></div><div class="lev2 toc-item"><a href="#Complexités-en-temps-et-espace-(bonus)" data-toc-modified-id="Complexités-en-temps-et-espace-(bonus)-16"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Complexités en temps et espace (bonus)</a></div><div class="lev3 toc-item"><a href="#En-temps" data-toc-modified-id="En-temps-161"><span class="toc-item-num">1.6.1&nbsp;&nbsp;</span>En temps</a></div><div class="lev3 toc-item"><a href="#En-espace" data-toc-modified-id="En-espace-162"><span class="toc-item-num">1.6.2&nbsp;&nbsp;</span>En espace</a></div><div class="lev2 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-17"><span class="toc-item-num">1.7&nbsp;&nbsp;</span>Conclusion</a></div><div class="lev3 toc-item"><a href="#Qualités" data-toc-modified-id="Qualités-171"><span class="toc-item-num">1.7.1&nbsp;&nbsp;</span>Qualités</a></div><div class="lev3 toc-item"><a href="#Défauts" data-toc-modified-id="Défauts-172"><span class="toc-item-num">1.7.2&nbsp;&nbsp;</span>Défauts</a></div><div class="lev3 toc-item"><a href="#Ouverture-?" data-toc-modified-id="Ouverture-?-173"><span class="toc-item-num">1.7.3&nbsp;&nbsp;</span>Ouverture ?</a></div> *)

(* # Texte d'oral de modélisation - Agrégation Option Informatique
## Préparation à l'agrégation - ENS de Rennes, 2016-17
- *Date* : 22 mai 2017
- *Auteur* : [Lilian Besson](https://GitHub.com/Naereen/notebooks/)
- *Texte*: Annale 2012, ["Éclairage graphe" (public2012-D1)](http://agreg.org/Textes/public2012-D1.pdf) *)

(* ## À propos de ce document
- Ceci est une *proposition* de correction, partielle et probablement non-optimale, pour la partie implémentation d'un [texte d'annale de l'agrégation de mathématiques, option informatique](http://Agreg.org/Textes/).
- Ce document est un [notebook Jupyter](https://www.Jupyter.org/), et [est open-source sous Licence MIT sur GitHub](https://github.com/Naereen/notebooks/tree/master/agreg/), comme les autres solutions de textes de modélisation que [j](https://GitHub.com/Naereen)'ai écrite cette année.
- L'implémentation sera faite en OCaml, version 4+ : *)

(* In[1]: *)


Sys.command "ocaml -version";;

(* ----
## Question de programmation
La question de programmation pour ce texte était donnée au tout début, à la page 2 :

### Exercice

> Dans le langage de votre choix, implémenter un programme qui étant donnés un graphe et une proposition d’éclairage des lampadaires teste si celle-ci est correcte, *i.e.*, si toutes les rues sont bien éclairées.

> Le tester sur différents exemples bien choisis (on pourra justifier la/les structures de données utilisée).

### Besoin de plusieurs exemples
Pour une fois, on voit bien que le jury *exige* de tester la fonction sur *plusieurs* exemples. *)

(* ----
## Solution
 *)

(* ### Représentation du graphe et de la proposition d'éclairage

Les graphes ici seront constitués de *places* (= sommets), reliés entre elles par des *rues* (= arêtes).

Pour vérifier un éclairage, donné sous forme d'une liste de places, on va devoir vérifier que chaque rue est connectée à une place éclairée.

Une approche très simple, en trois étapes :

1. compter le nombre de rues,
2. pour chaque place éclairée, compter le nombre de rues qui en partent (et qui sont donc éclairées),
3. s'il y a (au moins) une rue non éclairée, renvoyer `false`, sinon renvoyer `true`.

Pour être efficace, il faut pouvoir accéder efficacement aux rues qui partent de chaque place (et il suffit de les compter, si on sait qu'elles sont uniques dans la représentation).

$\implies$ À partir de ce constat, on opte pour une représentation du graphe par **liste d'adjacence**.

- Comme les graphes sont non orientés, chaque arête est présente deux fois dans la représentation du graphe : l'arête $u \leftrightarrow v$ est présente comme $v \in V[u]$ (les places voisines de $u$), et $u \in V[v]$ (les places voisines de $v$).

- Le fait que les graphes soient planaires n'apportent rien à la représentation.

- Par simplicité, on va représenter les places par leur numéros (on pourra aussi prendre des chaînes de caractères, comme `"Place de l'étoile"`, `"Nation"`, `"Champd de Mars"` etc, mais c'est plus long à écrire). *)

(* In[2]: *)


type place = int;;
type rues = place list;;

(* In[3]: *)


type ville = rues list;;

(* On donne tout de suite un exemple de graphe, en prenant le 3ème exemple de la Figure 1 du texte.

![Graphes de la Figure 1 du texte](images/ville_eclairee_1.png) *)

(* In[4]: *)


let graphe1 : ville = [
    [2];           (* place 0 *)
    [2; 3; 6];     (* place 1 *)
    [0; 1];        (* place 2 *)
    [1; 4];        (* place 3 *)
    [3; 5];        (* place 4 *)
    [1; 4; 6; 8];  (* place 5 *)
    [1; 5; 7];     (* place 6 *)
    [6; 8];        (* place 7 *)
    [5; 7];        (* place 8 *)
];;

(* On a besoin que les indices commence à $0$ et jusqu'à $n-1$ (où $n$ est le nombre de places), puisque la liste des rues utilisent implicitement la numérotation des places. *)

(* In[5]: *)


type eclairage = place list;;

(* Trois exemples d'éclairages, deux satisfaisant donc l'un trivialement, et l'autre non satisfaisant : *)

(* In[6]: *)


let eclairage1_sat : eclairage = [
    0; 1; 2; 3; 4; 5; 6; 7; 8
];;

let eclairage2_sat : eclairage = [
    1; 2; 3; 5; 6; 8
];;

(* In[7]: *)


let eclairage1_nonsat : eclairage = [
    2; 4; 8
];;

let eclairage2_nonsat : eclairage = [
    1; 2; 3; 5; 6
];;

(* ### Vérification

On pourrait écrire une première fonction pour vérifier que le graphe est bien valide, selon la représentation décrite ci-dessus, en vérifiant :
- que les places forment bien l'ensemble $\{0,\dots,n-1\}$,
- que chaque rue n'est présente qu'une fois dans les listes d'adjacences $V[u]$,
- qu'aucune place inconnue n'est dans une liste $V[u]$,
- et que le graphe est bien symétrique non-orienté, i.e., que $u \in V[u] \Leftrightarrow v \in V[u]$.

... Mais le sujet n'exige rien de tout ça, donc on passe directement à la question demandée. *)

(* Quelques fonctions utiles : *)

(* In[8]: *)


let somme =
    List.fold_left (+) 0
;;

(* On met en place, facilement, l'algorithme décrit plus haut.
Une approche très simple, en trois étapes :

1. compter le nombre de rues,
2. pour chaque place éclairée, compter le nombre de rues qui en partent (et qui sont donc éclairées),
3. s'il y a (au moins) une rue non éclairée, renvoyer `false`, sinon renvoyer `true`.
 *)

(* Il y a une finesse : en comptant une fois les rues dont les deux côtés sont éclairés, et deux fois les rues dont un seul côté est éclairé, on peut comparer au nombre de rues comptées doubles.

C'est légérement sous-optimal, comme on va devoir vérifier (en temps linéaire en taille la de l'éclairage) si chaque rue a un ou deux côté éclairés.
Mais on gagne en mémoire puisqu'on n'a pas à construire une représentation de toutes les rues. *)

(* In[9]: *)


let compte_simple_ou_double_0 (ici : place) (voisines : rues) (proposition : eclairage) =
    somme
    (List.map (fun voisine -> 
        if List.mem voisine proposition
        then 1
        else 2
    ) voisines)
;;

(* In[10]: *)


let verifie_eclairage_0 (graphe : ville) (proposition : eclairage) : bool =
    (* 1. compter le nombre de rues *)
    let nombre_rues =
        List.fold_left (fun a b -> a + (List.length b)) 0 (graphe)
        (* (List.length (List.flatten graphe)) *)
    in
    (* 2. pour chaque place *éclairée*, compter le nombre de rues qui en partent *)
    let nombre_rues_eclairees =
        somme
        (List.map (fun place_eclairee ->
            compte_simple_ou_double_0
            place_eclairee
            (List.nth graphe place_eclairee)
            proposition
        ) proposition)
    in
    (* 3. s'il y a (au moins) une rue non éclairée, renvoyer [false], sinon renvoyer [true] *)
    nombre_rues <= nombre_rues_eclairees
;;

(* Notez qu'on peut même faire mieux, puisque cet appel à `List.mem voisine proposition` est inefficace (au pire il est en $\mathcal{O}(n)$, et on le fait au pire $n-1$ fois).

En effet, on peut précalculer, dans la fonction `verifie_eclairage` un *tableau*, de taille $n$ fixée (et connue à l'avance), qui contient en indice $i$ le résultat de `List.mem i proposition` : sauf qu'au lieu d'appeler plusieurs fois la fonction `List.mem`, on a qu'à parcourir la liste `proposition` une fois, et remplir les cases du tableau. *)

(* In[14]: *)


let compte_simple_ou_double (_ : place) (voisines : rues) (est_eclairee : bool array) =
    somme
    (List.map (fun voisine -> 
        if est_eclairee.(voisine)
        then 1
        else 2
    ) voisines)
;;

(* Cette fonction précalcule, une seule fois, ce tableau. *)

(* In[15]: *)


let precalcule_places_eclairees (n : int) (proposition : eclairage) : bool array =
    let resultat = Array.make n false in
    List.iter (fun i -> 
        resultat.(i) <- true
    ) proposition;
    resultat
;;

(* Et enfin, on s'en sert pour la fonction `verifie_eclairage` plus rapide. *)

(* In[16]: *)


let verifie_eclairage (graphe : ville) (proposition : eclairage) : bool =
    (* 0. précalcul *)
    let n = List.length graphe in
    let est_eclairee = precalcule_places_eclairees n proposition in
    (* 1. compter le nombre de rues *)
    let nombre_rues =
        List.fold_left (fun a b -> a + (List.length b)) 0 (graphe)
        (* (List.length (List.flatten graphe)) *)
    in
    (* 2. pour chaque place *éclairée*, compter le nombre de rues qui en partent *)
    let nombre_rues_eclairees =
        somme
        (List.map (fun place_eclairee ->
            compte_simple_ou_double
            place_eclairee
            (List.nth graphe place_eclairee)
            est_eclairee
        ) proposition)
    in
    (* 3. s'il y a (au moins) une rue non éclairée, renvoyer [false], sinon renvoyer [true] *)
    nombre_rues <= nombre_rues_eclairees
;;

(* ### Exemples

Avec le graphe définit plus haut, et les deux propositions d'éclairages : *)

(* In[17]: *)


graphe1;;

(* #### Pour des éclairages valides.

- Le premier est trivialement valide, on éclaire toutes les places donc toutes les rues sont bien éclairées. *)

(* In[18]: *)


eclairage1_sat;;
List.map (fun place_eclairee -> List.nth graphe1 place_eclairee) eclairage1_sat;;

verifie_eclairage graphe1 eclairage1_sat;;    (* true *);;

(* - Le second est moins trivial, mais en vérifiant à la main sur le graphe on voit qu'il fonctionne.
  + On a juste éteint la place $0$, mais l'arête $0-1$ reste éclairée par la place $1$,
  + la place $4$ mais les arêtes $3-4$ et $4-5$ sont éclairées par les places $3$ et $5$,
  + et la place $7$ mais les arêtes $6-7$ et $7-8$ sont éclairées par les places $6$ et $8$. *)

(* In[19]: *)


eclairage2_sat;;
List.map (fun place_eclairee -> List.nth graphe1 place_eclairee) eclairage2_sat;;

verifie_eclairage graphe1 eclairage2_sat;;    (* true *);;

(* - On peut essayer un éclairage de seulement 5 villes. Est-ce optimal ? (on répondra plus tard, mais oui) *)

(* In[20]: *)


let eclairage3_sat : eclairage = [
    2; 3; 5; 6; 7;
];;

List.map (fun place_eclairee -> List.nth graphe1 place_eclairee) eclairage3_sat;;

verifie_eclairage graphe1 eclairage3_sat;;    (* true *);;

(* #### Pour des éclairages non valides :

- Clairement, le premier est trop gourmand et on a éteint trop de place. *)

(* In[21]: *)


eclairage1_nonsat;;
List.map (fun place_eclairee -> List.nth graphe1 place_eclairee) eclairage1_nonsat;;

verifie_eclairage graphe1 eclairage1_nonsat;;   (* false *);;

(* - Le second semble bon, mais la rue $8-9$ par exemple est éteinte. *)

(* In[22]: *)


eclairage2_nonsat;;
List.map (fun place_eclairee -> List.nth graphe1 place_eclairee) eclairage2_nonsat;;

verifie_eclairage graphe1 eclairage2_nonsat;;   (* false *);;

(* ### Bonus : vérifier que le graphe est valide
Bon... par acquis de conscience, on implémente l'étape de vérification évoquée plus haut.

D'abord, quelques fonctions utiles : *)

(* In[23]: *)


let max_liste (liste : int list) : int =
    List.fold_left max (-max_int) liste
;;

(* In[24]: *)


max_liste [123; 12; 1];;

(* In[25]: *)


let max_liste_liste (listeliste : int list list) : int =
    max_liste (List.map max_liste listeliste) 
;;

(* In[26]: *)


max_liste_liste [[123; 12; 1]; [1234; 13]];;

(* In[27]: *)


List.for_all (fun x -> (0 <= x) && (x <= 1234)) (List.flatten [[123; 12; 1]; [1234; 13]]);;

(* In[28]: *)


let compte_occurences (liste : int list) (x : int) =
    let rec aux xs x acc =
        match xs with
        | [] -> acc
        | y :: ys when y = x -> aux ys x (acc + 1)
        | _ :: ys -> aux ys x acc
    in
    aux liste x 0
;;

(* In[29]: *)


compte_occurences [1; 2; 3; 4; 5] 1;;
compte_occurences [1; 2; 3; 4; 5] 10;;
compte_occurences [1; 2; 3; 4; 5; 1; 6; 7] 1;;

(* Puis, la vérification annoncée : *)

(* In[30]: *)


let graphe_valide (graphe : ville) : bool =
    let n = max_liste_liste graphe in
    (* D'abord, on vérifie qu'il y a exactement n + 1 listes de places voisines *)
    let test1 =
        (List.length graphe) = (n + 1)
    in
    (* Ensuite, on vérifie que toutes les places voisines sont bien dans des places valides *)
    let test2 =
        List.for_all (
            fun x -> (0 <= x) && (x <= n)
        ) (List.flatten graphe)
    in
    (* Enfin, on vérifie qu'une place voisine v n'est présente qu'une fois dans V[u] *)
    let test3 =
        List.for_all (
            fun voisines -> List.for_all (
                fun place ->
                    (compte_occurences voisines place) = 1
            ) voisines
        ) graphe
    in
    (* test1, test2, test3 *)
    test1 && test2 && test3
;;

(* In[31]: *)


graphe1;;

(* In[32]: *)


graphe_valide graphe1;;

(* On doit aussi tester trois cas de graphes qui contredisent un de chaque test : *)

(* - S'il manque une place dans la liste d'adjacence : *)

(* In[33]: *)


let graphe2 : ville = [
    [2];           (* place 0 *)
    [2; 3; 6];     (* place 1 *)
    [0; 1];        (* place 2 *)
    [1; 3];        (* place 3 *)
    [3; 5];        (* place 4 *)
    [1; 4; 6; 8];  (* place 5 *)
    [1; 5; 7];     (* place 6 *)
    [6; 8];        (* place 7 *)
                   (* place 8 absente ! *)
];;

(* In[34]: *)


graphe_valide graphe2;;

(* - Si la liste d'adjacence est trop grande : *)

(* In[35]: *)


let graphe3 : ville = [
    [2];           (* place 0 *)
    [2; 3; 6];     (* place 1 *)
    [0; 1];        (* place 2 *)
    [1; 3];        (* place 3 *)
    [3; 5];        (* place 4 *)
    [1; 4; 6; 8];  (* place 5 *)
    [1; 5; 7];     (* place 6 *)
    [6; 8];        (* place 7 *)
    [5; 7];        (* place 8 absente ! *)
    [5; 7]         (* place 9 ?! *)
];;

(* In[36]: *)


graphe_valide graphe3;;

(* - Si une des places voisines n'est pas valide : *)

(* In[37]: *)


let graphe4 : ville = [
    [2];           (* place 0 *)
    [2; 3; 6];     (* place 1 *)
    [0; 1];        (* place 2 *)
    [1; 3];        (* place 3 *)
    [3; 5];        (* place 4 *)
    [1; 4; 6; 8];  (* place 5 *)
    [1; 5; 7];     (* place 6 *)
    [6; 8];        (* place 7 *)
    [50]           (* place 8 -> 50 ?! *)
];;

(* In[38]: *)


graphe_valide graphe4;;

(* - Et enfin, si une des listes d'adjacence contient deux fois la même place voisine : *)

(* In[39]: *)


let graphe5 : ville = [
    [2];           (* place 0 *)
    [2; 3; 6];     (* place 1 *)
    [0; 1];        (* place 2 *)
    [1; 3];        (* place 3 *)
    [3; 5];        (* place 4 *)
    [1; 4; 6; 8];  (* place 5 *)
    [1; 5; 7];     (* place 6 *)
    [6; 8];        (* place 7 *)
    [5; 7; 5]      (* place 8 -> 5 deux fois ! *)
];;

(* In[40]: *)


graphe_valide graphe5;;

(* ----
## Bonus : énumération de tous les éclairages possibles

Pour de tous petits graphes, on peut suivre l'approche naïve qui consiste à énumérer toutes les possibilités, et renvoyer celle de nombre de lampadaires minimal.

On pourra ensuite vérifier avec la fonction précédente que l'éclairage donné est bien valide. *)

(* ### Énumération des éclairages possibles

Un éclairage est un sous-ensemble, potentiellement vide, de $\{0,\dots,n-1\}$.
Il y en a $2^n$ en tout.

Comment les générer efficacement ? En fait, on s'en fiche, le reste du code sera déjà exponentiel en $n$...

- La fonction suivante prend une liste de liste, `acc`, et la dédouble en ajoutant `x` aux listes qui ne le contiennent pas encore, et en gardant une copie des listes d'avant.
En travaillant avec des listes toutes distinctes, la liste `acc` est toujours dédoublée. *)

(* In[41]: *)


let ajoute_ou_pas (x : 'a) (acc : 'a list list) =
    (List.map (fun liste ->
        if (List.mem x liste)
        then liste
        else x :: liste
    ) acc
    )
    @
    (List.filter (fun liste ->
        not (List.mem x liste)
    ) acc
    )
;;

(* In[42]: *)


ajoute_ou_pas 1 [[]];;
ajoute_ou_pas 2 [[1]; []];;

(* - Maintenant, il suffit d'itérer cette fonction, depuis la liste `[[]]` contenant juste la liste vide. *)

(* In[43]: *)


let tous_sous_ensembles (liste : 'a list) : 'a list list =
    let rec aux xs acc =
        match xs with
        | [] -> acc
        | y :: ys ->
            aux ys (ajoute_ou_pas y acc)
    in
    aux liste [ [] ]
;;

(* In[44]: *)


tous_sous_ensembles [];;
tous_sous_ensembles [1];;
tous_sous_ensembles [1; 2];;
tous_sous_ensembles [1; 2; 3];; (* taille 2^3 = 8 *);;

(* In[45]: *)


tous_sous_ensembles [0; 1; 2; 3];; (* taille 2^4 = 16 *)
tous_sous_ensembles [0; 1; 2; 3; 4];; (* taille 2^5 = 32 *)
tous_sous_ensembles [0; 1; 2; 3; 4; 5];; (* taille 2^6 = 64 *)
tous_sous_ensembles [0; 1; 2; 3; 4; 5; 6];; (* taille 2^7 = 128 *)
tous_sous_ensembles [0; 1; 2; 3; 4; 5; 6; 7];; (* taille 2^8 = 256 *)
tous_sous_ensembles [0; 1; 2; 3; 4; 5; 6; 7; 8];; (* taille 2^9 = 512 *)

assert ((List.length (tous_sous_ensembles [0; 1; 2; 3; 4; 5; 6; 7; 8])) = 512);;

(* > C'est [tellement plus simple en Python](https://stackoverflow.com/questions/374626/how-can-i-find-all-the-subsets-of-a-set-with-exactly-n-elements)... *)

(* Une autre fonction utile : *)

(* In[46]: *)


let range (n : int) : (int list) =
    let rec range_x (n : int) : (int list) =
    match n with
    | n when n < 0 -> []
    | 0 -> [0]
    | n -> n :: (range_x (n - 1))
    in
    List.rev (range_x n)
;;

(* In[47]: *)


range 0;;
range 1;;
range 5;;
range 10;;

(* In[48]: *)


let tous_les_eclairages_possibles (graphe : ville) : (eclairage list) =
    assert (graphe_valide graphe);
    let n = (List.length graphe) - 1 in
    let sommets = range n in
    tous_sous_ensembles sommets    
;;

(* In[49]: *)


tous_les_eclairages_possibles graphe1;;

(* ### Liste de taille minimale parmi une liste de listes *)

(* In[50]: *)


let min_liste (liste : int list) : int =
    List.fold_left min (max_int) liste
;;

(* In[51]: *)


min_liste [123; 12; 1];;

(* In[52]: *)


let taille_min (listes : int list list) : int =
    min_liste (List.map List.length listes)
;;

(* ### Trouver un éclairage optimal

Ca va être assez naïf :

1. on calcule tous les éclairages possibles,
2. on filtre les éclairages pour ne garder que ceux qui sont valides,
3. on calcule la longueur minimale,
4. tant qu'on y est, on filtre pour ne garder que ceux qui sont de longueur minimale (plutôt que d'en renvoyer un seul). *)

(* In[53]: *)


let eclairages_optimaux (graphe : ville) : (eclairage list) =
    let propositions =
        tous_les_eclairages_possibles graphe
    in
    let propositions_valides =
        List.filter (verifie_eclairage graphe) propositions
    in
    let taille_minimale = 
        taille_min propositions_valides
    in
    let propositions_minimales =
        List.filter (fun li ->
            (List.length li) = taille_minimale
        ) propositions_valides
    in
    propositions_minimales
;;

(* ### Exemples

- On commence avec un tout petit graphe, pour vérifier rapidement avant de passer sur un plus gros graphe : *)

(* In[54]: *)


let graphe2 : ville = [
    [1; 2];  (* place 0 -> 1 2 *)
    [0; 2];  (* place 1 -> 0 2 *)
    [0; 1]   (* place 2 -> 0 1 *)
] ;;

(* In[55]: *)


tous_les_eclairages_possibles graphe2;;

List.length (tous_les_eclairages_possibles graphe2);;

(* Il y a $8$ éclairages possibles ($2^3$) et les $3$ de taille $2$ sont optimaux : en effet sur un graphe complet à $n$ sommets, il faut et il suffit d'éclairer n'importe quel ensenble de $n-1$ places pour éclairer toutes les $n(n-1)$ arêtes. *)

(* In[56]: *)


eclairages_optimaux graphe2;;

(* - Et sur le graphe avec lequel on travaille depuis le début : *)

(* In[57]: *)


graphe1;;

(* In[58]: *)


tous_les_eclairages_possibles graphe1;;

List.length (tous_les_eclairages_possibles graphe1);;

(* In[59]: *)


eclairages_optimaux graphe1;;

(* On vérifie ici que l'éclairage à $5$ places qu'on avait proposé plus haut est bien optimal. *)

(* ----
## Complexités en temps et espace (bonus)

Il est toujours utile de préciser, rapidement à l'oral et/ou dans le code (un commentaire suffit) les complexité (ou ordre de grandeur) des fonctions exigées par l'énoncé.

> Le*s* complexité*s* ? Oui, il ne faut pas oublier l'espace (trop souvent négligé !).

Si vous n'êtes pas sûr ou ne savez pas comment le justifier, mieux vaut marquer :

> « En $\mathcal{O}(n^2)$ en temps et en espace. »

que de marquer quelque chose de difficilement justifiable comme :

> « Probablement en $\mathcal{O}(n)$ en temps et en espace. » *)

(* ### En temps

- La première fonction de vérification proposée `verifie_eclairage_0` est linéaire en temps, en $m$ le nombre de rues et $p$ le nombre de place éclairées, i.e., est en $\mathcal{O}(m p)$. C'est sous-optimal pour vérifier que toutes les rues sont bien éclairées, on devrait réussir à faire mieux en $\mathcal{O}(\max(n, m))$ !

- La deuxième fonction de vérification proposée `verifie_eclairage` est elle bien linéaire en temps, seulement en $m$ le nombre de rues, i.e., est en $\mathcal{O}(\max(n, m))$ (s'il y a moins de rues que de places, il faut quand même créer le tableau `est_eclairee` en $\mathcal{O}(n)$). C'est optimal pour vérifier que toutes les rues sont bien éclairées ! <span style="color:cyan;">Youpiiiiiii!!!!!!!!!!!</span>

- Les deux fonctions `tous_les_eclairages_possibles` et `eclairages_optimaux` sont en $\mathcal{O}(2^n)$ en temps, et c'est *beaucoup* ! *)

(* ### En espace (ou en mémoire)
- La première fonction de vérification proposée `verifie_eclairage` est aussi linéaire en espace en la taille du graphe.
- La deuxième fonction de vérification proposée `verifie_eclairage_0` est aussi linéaire en espace en la taille du graphe.

- Les deux fonctions `tous_les_eclairages_possibles` et `eclairages_optimaux` sont aussi en $\mathcal{O}(2^n)$ en mémoire, et c'est *beaucoup* ! A noter par contre que le résultat renvoyé par `eclairages_optimaux` est, lui, de taille bien plus raisonnables, mais toujours possiblement exponentielle (si le nombre minimal de places éclairées est $k$, alors ${n \choose k}$). *)

(* ----
## Conclusion

Voilà pour la question obligatoire de programmation, et un gros bonus.

### Qualités
- On a décomposé le problème en sous-fonctions,
- on a fait des exemples et *on les garde* dans ce qu'on présente au jury,
- on a testé la fonction exigée sur différents exemples.

### Défauts
- La première implémentation proposée de `verifie_eclairage_0` n'est pas optimale,
- La deuxième implémentation n'était pas immédiate,
- et on a pas testé sur des exemples très ambitieux.

### Ouverture ?
> Bien-sûr, ce petit notebook ne se prétend pas être une solution optimale, ni exhaustive. *)
