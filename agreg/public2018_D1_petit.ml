(*
# Texte d'oral de modélisation - Agrégation Option Informatique
## Préparation à l'agrégation - ENS de Rennes, 2017-18
- Date : 6 décembre 2017
- Auteur : Lilian Besson (https://GitHub.com/Naereen/notebooks/)
- Texte: Annale 2018, "Expressions arithmétiques" (public2018-D1) (http://agreg.org/Textes/public2018-D1.pdf) *)

(* ## À propos de ce document
- Ceci est une proposition de correction, partielle et probablement non-optimale, pour la partie implémentation d'un texte d'annale de l'agrégation de mathématiques, option informatique (http://Agreg.org/Textes/).
- Ce document est un notebook Jupyter (https://www.Jupyter.org/), et est open-source sous Licence MIT sur GitHub (https://github.com/Naereen/notebooks/tree/master/agreg/), comme les autres solutions de textes de modélisation que j (https://GitHub.com/Naereen)'ai écrite cette année.
- L'implémentation sera faite en OCaml, version 4+ : *)


(* ----
## Question de programmation
La question de programmation pour ce texte était donnée en fin de page 6 :

### Modélisation
On est libre de choisir l'implémentation qui nous convient pour les expressions arithmétiques sous forme arborescente.

Je choisis de ne considérer que les variables et pas les valeurs (on aura des expressions en OCaml comme `F("x")` pour la variable $x$), et uniquement des arbres binaires.
Les noeuds `N(t1, op, t2)` sont étiquetées par un opérateur binaire `op`, dont on fournit à l'avance une liste fixée et finie, et les feuilles `F(s)` sont étiquetées par une variable `s`.

### Exercice
> « Écrire une fonction qui reçoit en argument une expression algébrique donnée sous forme
arborescente et décore cette expression en calculant pour chaque nœud interne quelle est
la valeur du paramètre ρ et quelle branche doit être évaluée en premier selon l’algorithme
d’Ershov. » *)

(* ----
## Solution

On va essayer d'être rapide et de faire simple, donc on choisit une algèbre de termes particulière, mais l'algorithme d'Ershov sera implémenté de façon générique (polymorphique, peu importe la valeur de `op`). *)

(* ### Types et représentations *)

type operateur = Plus | Moins | Mul | Div ;;

type ('a, 'b) arbre_binaire =
    | F of 'a
    | N of (('a,'b) arbre_binaire) * 'b * (('a,'b) arbre_binaire)
;;

(* Par exemple pour l'expression $\frac{x - yz}{u - vw}$, c'est-à-dire `(x - y*z)/(u - v*w)` : *)

(* exp1 = (x - y*z) *)
let exp1 =
N(
    F("x"),
    Moins,
    N(
        F("y"),
        Mul,
        F("z")
    )
)
;;

(* exp2 = (u - v*w) *)
let exp2 =
N(
    F("u"),
    Moins,
    N(
        F("v"),
        Mul,
        F("w")
    )
)
;;

(* exp3 = (x - y*z)/(u - v*w) *)
let exp3 =
N(
    exp1,
    Div,
    exp2
);;

(* ### Calcul récursif du nombre $\rho$

C'est assez immédiat, en suivant la définition récursive :
$\rho(F) = 0$ et $\rho(N(t_1, t_2)) = \rho(t_1) + 1$ si $\rho(t_1) = \rho(t_2)$ et $\max(\rho(t_1), \rho(t_2))$ si $\rho(t_1) \neq \rho(t_2)$.  *)

let rec nombre_rho (expr : ('a, 'b) arbre_binaire) : int =
    match expr with
    | F _ -> 0
    | N(t1, _, t2) ->
        let d1, d2 = nombre_rho t1, nombre_rho t2 in
        if d1 = d2 then
            d1 + 1
        else
            max d1 d2
;;

(* Pour comparer avec le calcul, plus simple, de la hauteur de l'arbre : *)

let rec hauteur (expr : ('a, 'b) arbre_binaire) : int =
    match expr with
    | F _ -> 0
    | N(t1, _, t2) ->
        let d1, d2 = hauteur t1, hauteur t2 in
        1 + (max d1 d2)
;;

(* Exemples qui concordent avec le texte : *)

hauteur exp1;;
nombre_rho exp1;;

hauteur exp2;;
nombre_rho exp2;;

hauteur exp3;;
nombre_rho exp3;;

(* ### Algorithme demandé pour décorer l'arbre *)

(* On choisit d'ajouter une *décoration* de type `'c` : *)

type ('a, 'b, 'c) arbre_binaire_decore =
    | F2 of 'a
    | N2 of ('c * (('a, 'b, 'c) arbre_binaire_decore) * 'b * (('a, 'b, 'c) arbre_binaire_decore))
;;

(* On a besoin d'attacher à chaque noeud son paramètre $\rho$ et un drapeau binaire permettant de savoir si l'algorithme d'Ershov indique d'évaluer en premier le sous-arbre gauche (`premier_gauche = true`) ou droite (`= false`). *)

type decoration = {
    rho : int;
    premier_gauche : bool;
};;

(* Complexité temporelle = O(n)
Complexité mémoire = O(log(n))
 *)
let rec decore (expr : (('a, 'b) arbre_binaire)) : (('a, 'b, decoration) arbre_binaire_decore) =
    match expr with
    | F v -> F2 v
    | N (t1, o, t2) ->
        let d1, d2 = nombre_rho t1, nombre_rho t2 in
        let d = if d1 = d2 then d1 + 1 else max d1 d2 in
        N2({rho = d; premier_gauche = (d2 <= d1)}, (decore t1), o, (decore t2))
;;

(* Dans nos exemples, on voit que l'évaluation favorise en premier (avec des `premier_gauche = false`) les expressions les plus profondes (à droite) au sens du paramètre $\rho$ : *)

decore exp1;;

decore exp2;;

decore exp3;;

(* ## Complexités *)

(* ### En espace
Les deux fonctions présentées ci-dessus n'utilisent pas d'autre espace que l'arbre décoré, et la pile d'appel récursif.

- Le calcul récursif de $\rho(t)$ prend donc un espace proportionnel au nombre d'appel récursif imbriqué, qui est borné par la taille du terme $t$ (définie comme le nombre de noeuds et de feuilles), donc est **linéaire**,
- Le calcul de la méthode d'Ershov est elle aussi **linéaire** puisque l'arbre décoré est de même taille que l'arbre initial. *)

(* ### En temps
Les deux fonctions présentées ci-dessus sont **linéaires** dans la taille de l'arbre. *)
