(*
This OCaml script was exported from a Jupyter notebook
using an open-source software (under the MIT License) written by @Naereen
from https://github.com/Naereen/Jupyter-Notebook-OCaml
This software is still in development, please notify me of a bug at
https://github.com/Naereen/Jupyter-Notebook-OCaml/issues/new if you find one
*)

(* # Table of Contents
 <p><div class="lev1 toc-item"><a href="#Lambda-calcul-implémenté-en-OCaml" data-toc-modified-id="Lambda-calcul-implémenté-en-OCaml-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Lambda-calcul implémenté en OCaml</a></div><div class="lev2 toc-item"><a href="#Expressions" data-toc-modified-id="Expressions-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Expressions</a></div><div class="lev2 toc-item"><a href="#But-?" data-toc-modified-id="But-?-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>But ?</a></div><div class="lev2 toc-item"><a href="#Grammaire" data-toc-modified-id="Grammaire-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Grammaire</a></div><div class="lev2 toc-item"><a href="#L'identité" data-toc-modified-id="L'identité-14"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>L'identité</a></div><div class="lev2 toc-item"><a href="#Conditionnelles" data-toc-modified-id="Conditionnelles-15"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Conditionnelles</a></div><div class="lev2 toc-item"><a href="#Nombres" data-toc-modified-id="Nombres-16"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Nombres</a></div><div class="lev2 toc-item"><a href="#Test-d'inégalité" data-toc-modified-id="Test-d'inégalité-17"><span class="toc-item-num">1.7&nbsp;&nbsp;</span>Test d'inégalité</a></div><div class="lev2 toc-item"><a href="#Successeurs" data-toc-modified-id="Successeurs-18"><span class="toc-item-num">1.8&nbsp;&nbsp;</span>Successeurs</a></div><div class="lev2 toc-item"><a href="#Prédecesseurs" data-toc-modified-id="Prédecesseurs-19"><span class="toc-item-num">1.9&nbsp;&nbsp;</span>Prédecesseurs</a></div><div class="lev2 toc-item"><a href="#Addition" data-toc-modified-id="Addition-110"><span class="toc-item-num">1.10&nbsp;&nbsp;</span>Addition</a></div><div class="lev2 toc-item"><a href="#Multiplication" data-toc-modified-id="Multiplication-111"><span class="toc-item-num">1.11&nbsp;&nbsp;</span>Multiplication</a></div><div class="lev2 toc-item"><a href="#Paires" data-toc-modified-id="Paires-112"><span class="toc-item-num">1.12&nbsp;&nbsp;</span>Paires</a></div><div class="lev2 toc-item"><a href="#Prédécesseurs,-deuxième-essai" data-toc-modified-id="Prédécesseurs,-deuxième-essai-113"><span class="toc-item-num">1.13&nbsp;&nbsp;</span>Prédécesseurs, deuxième essai</a></div><div class="lev2 toc-item"><a href="#Listes" data-toc-modified-id="Listes-114"><span class="toc-item-num">1.14&nbsp;&nbsp;</span>Listes</a></div><div class="lev2 toc-item"><a href="#La-fonction-U" data-toc-modified-id="La-fonction-U-115"><span class="toc-item-num">1.15&nbsp;&nbsp;</span>La fonction U</a></div><div class="lev2 toc-item"><a href="#La-récursion-via-la-fonction-Y" data-toc-modified-id="La-récursion-via-la-fonction-Y-116"><span class="toc-item-num">1.16&nbsp;&nbsp;</span>La récursion via la fonction Y</a></div><div class="lev2 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-117"><span class="toc-item-num">1.17&nbsp;&nbsp;</span>Conclusion</a></div> *)

(* # Lambda-calcul implémenté en OCaml

Ce notebook est inspiré de [ce post de blog du Professeur Matt Might](http://matt.might.net/articles/python-church-y-combinator/), qui implémente un mini langage de programmation en $\lambda$-calcul, en Python.
Je vais faire la même chose en OCaml.

## Expressions
On rappelle que les expressions du [Lambda calcul](https://fr.wikipedia.org/wiki/Lambda-calcul), ou $\lambda$-calcul, sont les suivantes :
$$ \begin{cases}
x, y, z & \text{(des variables)} \\
u v & \text{(application de deux termes}\, u, v\; \text{)} \\
\lambda x. v & \text{(lambda-function prenant la variable}\; x \;\text{et le terme}\; v \;\text{)}
\end{cases} $$

## But ?
Le but ne va pas être de les représenter comme ça avec des types formels en Caml, mais plutôt d'utiliser les constructions de Caml, respectivement `u(v)` et `fun x -> v` pour l'application et les fonctions anonymes, et encoder des fonctionnalités de plus haut niveau dans ce langage réduit.

## Grammaire
Avec une grammaire BNF, si `<var>` désigne un nom d'expression valide (on se limitera à des noms en miniscules consistitués des 26 lettres `a,b,..,z`) :

    <exp> ::= <var>
    | <exp>(<exp>)
    | fun <var> -> <exp>
    | (<exp>) *)

(* ----
## L'identité *)

(* In[3]: *)


let identite = fun x -> x ;;

(* In[4]: *)


let vide = fun x -> x ;;

(* ## Conditionnelles
La conditionnelle est `si cond alors valeur_vraie sinon valeur_fausse`. *)

(* In[13]: *)


let si = fun cond valeur_vraie valeur_fausse -> cond valeur_vraie valeur_fausse ;;

(* C'est très simple, du moment qu'on s'assure que `cond` est soit `vrai` soit `faux` tels que définis par leur comportement :

    si vrai e1 e2 == e1
    si faux e1 e2 == e2 *)

(* In[14]: *)


let vrai = fun valeur_vraie valeur_fausse -> valeur_vraie ;;
let faux = fun valeur_vraie valeur_fausse -> valeur_fausse ;;

(* La négation est facile ! *)

(* In[15]: *)


let non = fun v x y -> v y x;;

(* En fait, on va forcer une évaluation paresseuse, comme ça si l'une des deux expressions ne terminent pas, l'évaluation fonctionne quand même. *)

(* In[16]: *)


let vrai_paresseux = fun valeur_vraie valeur_fausse -> valeur_vraie () ;;
let faux_paresseux = fun valeur_vraie valeur_fausse -> valeur_fausse () ;;

(* Pour rendre paresseux un terme, rien de plus simple ! *)

(* In[17]: *)


let paresseux = fun f -> fun () -> f ;;

(* ## Nombres
La représentation de Church consiste a écrire $n$ comme $\lambda f. \lambda z. f^n z$. *)

(* In[18]: *)


type 'a nombres = ('a -> 'a) -> 'a -> 'a;;  (* inutilisé *)
type entiers_church = (int -> int) -> int -> int;;

(* $0$ est trivialement $\lambda f. \lambda z. z$ : *)

(* In[34]: *)


let zero = fun (f : ('a -> 'a)) (z : 'a) -> z ;;

(* $1$ est $\lambda f. \lambda z. f z$ : *)

(* In[35]: *)


let un = fun (f : ('a -> 'a)) -> f ;;

(* Avec l'opérateur de composition, l'écriture des entiers suivants est facile. *)

(* In[36]: *)


let compose = fun f g x -> f (g x);;

(* In[37]: *)


let deux = fun f -> compose f f;;  (* == compose f (un f) *)
let trois = fun f -> compose f (deux f) ;;
let quatre = fun f -> compose f (trois f) ;;
(* etc *);;

(* On peut généraliser ça, avec une fonction qui transforme un entier (`int`) de Caml en un entier de Church : *)

(* In[38]: *)


let rec entierChurch (n : int) =
    fun f z -> if n = 0 then z else f ((entierChurch (n-1)) f z)
;;

(* Par exemple : *)

(* In[39]: *)


(entierChurch 0) (fun x -> x + 1) 0;; (* 0 *)
(entierChurch 7) (fun x -> x + 1) 0;; (* 7 *)
(entierChurch 3) (fun x -> 2*x) 1;; (* 8 *);;

(* Et une fonction qui fait l'inverse (note : cette fonction n'est *pas* un $\lambda$-terme) : *)

(* In[40]: *)


let entierNatif c : int =
    c (fun x -> x + 1) 0
;;

(* Un petit test : *)

(* In[41]: *)


entierNatif (si vrai zero un);; (* 0 *)
entierNatif (si faux zero un);; (* 1 *);;

(* In[42]: *)


entierNatif (entierChurch 100);; (* 100 *);;

(* ## Test d'inégalité
On a besoin de pouvoir tester si $n \leq 0$ (ou $n = 0$) en fait. *)

(* In[43]: *)


(* prend un lambda f lambda z. ... est donne vrai ssi n = 0 ou faux sinon *)
let estnul = fun n -> n (fun z -> faux) (vrai);;

(* In[44]: *)


(* prend un lambda f lambda z. ... est donne vrai ssi n > 0 ou faux sinon *)
let estnonnul = fun n -> n (fun z -> vrai) (faux);;

(* On peut proposer cette autre implémentation, qui "fonctionne" pareil (au sens calcul des $\beta$-réductions) mais est plus compliquée : *)

(* In[45]: *)


let estnonnul2 = fun n -> non (estnul n);;

(* In[46]: *)


entierNatif (si (estnul zero) zero un);; (* 0 *)
entierNatif (si (estnul un)   zero un);; (* 1 *)
entierNatif (si (estnul deux) zero un);; (* 1 *);;

(* In[47]: *)


entierNatif (si (estnonnul zero) zero un);; (* 0 *)
entierNatif (si (estnonnul un)   zero un);; (* 1 *)
entierNatif (si (estnonnul deux) zero un);; (* 1 *);;

(* In[48]: *)


entierNatif (si (non (estnul zero)) zero un);; (* 0 *)
entierNatif (si (non (estnul un))   zero un);; (* 1 *)
entierNatif (si (non (estnul deux)) zero un);; (* 1 *);;

(* ## Successeurs
Vue la représentation de Churc, $n+1$ consiste a appliquer l'argument $f$ une fois de plus :
$f^{n+1}(z) = f (f^n(z))$. *)

(* In[49]: *)


let succ = fun n f z -> f ((n f) z) ;;

(* In[50]: *)


entierNatif (succ un);; (* 2 *);;

(* In[51]: *)


deux;;
succ un;;

(* On remarque qu'ils ont le même typage, mais OCaml indique qu'il a moins d'informations à propos du deuxième : ce `'_a` signifie que le type est *contraint*, il sera fixé dès la première utilisation de cette fonction.

C'est assez mystérieux, mais il faut retenir le point suivant : `deux` était écrit manuellement, donc le système a vu le terme en entier, il le connaît et saît que `deux = fun f -> fun x -> f (f x))`, pas de surprise. Par contre, `succ un` est le résultat d'une évaluation *partielle* et vaut `fun f z -> f ((deux f) z)`. Sauf que le système ne calcule pas tout et laisse l'évaluation partielle ! (heureusement !) *)

(* Si on appelle `succ un` à une fonction, le `'_a` va être contraint, et on ne pourra pas s'en reservir : *)

(* In[54]: *)


let succ_de_un = succ un;;

(* In[55]: *)


(succ_de_un) (fun x -> x + 1);;

(* In[56]: *)


(succ_de_un) (fun x -> x ^ "0");;

(* In[57]: *)


(succ un) (fun x -> x ^ "0");;
(* une valeur fraîchement calculée, sans contrainte *);;

(* ## Prédecesseurs
Vue la représentation de Church, $\lambda n. n-1$ n'existe pas... mais on peut tricher. *)

(* In[30]: *)


let pred = fun n ->
    if (entierNatif n) > 0 then entierChurch ((entierNatif n) - 1)
    else zero
;;

(* In[31]: *)


entierNatif (pred deux);; (* 1 *);;

(* In[32]: *)


entierNatif (pred trois);; (* 2 *);;

(* ## Addition

Pour ajouter $n$ et $m$, il faut appliquer une fonction $f$ $n$ fois puis $m$ fois : $f^{n+m}(z) = f^n(f^m(z))$. *)

(* In[33]: *)


let somme = fun n m f z -> n(f)( m(f)(z));;

(* In[34]: *)


let cinq = somme deux trois ;;

(* In[35]: *)


entierNatif cinq;;

(* In[36]: *)


let sept = somme cinq deux ;;

(* In[37]: *)


entierNatif sept;;

(* ## Multiplication

Pour multiplier $n$ et $m$, il faut appliquer le codage de $n$ exactement $m$ fois : $f^{nm}(z) = (f^n(f^n(...(f^n(z))...))$. *)

(* In[38]: *)


let produit = fun n m f z -> m(n(f))(z);;

(* On peut faire encore mieux avec l'opérateur de composition : *)

(* In[39]: *)


let produit = fun n m -> compose m n;;

(* In[40]: *)


let six = produit deux trois ;;

(* In[41]: *)


entierNatif six;;

(* In[42]: *)


let huit = produit deux quatre ;;

(* In[43]: *)


entierNatif huit;;

(* ## Paires

On va écrire un constructeur de paires, `paire a b` qui sera comme `(a, b)`, et deux destructeurs, `gauche` et `droite`, qui vérifient :

    gauche (paire a b) == a
    droite (paire a b) == b *)

(* In[75]: *)


let paire = fun a b -> fun f -> f(a)(b);;

(* In[76]: *)


let gauche = fun p -> p(fun a b -> a);;
let droite = fun p -> p(fun a b -> b);;

(* In[77]: *)


entierNatif (gauche (paire zero un));;
entierNatif (droite (paire zero un));;

(* ## Prédécesseurs, deuxième essai

Il y a une façon, longue et compliquée ([source](http://gregfjohnson.com/pred/)) d'y arriver, avec des paires. *)

(* In[78]: *)


let pred n suivant premier =
    let pred_suivant = paire vrai premier in
    let pred_premier = fun p ->
        si (gauche p)
        (paire faux premier)
        (paire faux (suivant (droite p)))
    in
    let paire_finale = n pred_suivant pred_premier in
    droite paire_finale
;;

(* Malheureusement, ce n'est pas bien typé. *)

(* In[79]: *)


entierNatif (pred deux);; (* 1 *);;

(* ## Listes

Pour construire des listes (simplement chaînées), on a besoin d'une valeur pour la liste vide, `listevide`, d'un constructeur pour une liste `cons`, un prédicat pour la liste vide `estvide`, un accesseur `tete` et `queue`, et avec les contraintes suivantes (avec `vrai`, `faux` définis comme plus haut) :

    estvide (listevide) == vrai
    estvide (cons tt qu) == faux
    
    tete (cons tt qu) == tt
    queue (cons tt qu) == qu

On va stocker tout ça avec des fonctions qui attendront deux arguments (deux fonctions - rappel tout est fonction en $\lambda$-calcul), l'une appellée si la liste est vide, l'autre si la liste n'est pas vide. *)

(* In[58]: *)


let listevide = fun survide surpasvide -> survide;;

(* In[59]: *)


let cons = fun hd tl -> fun survide surpasvide -> surpasvide hd tl;;

(* Avec cette construction, `estvide` est assez simple : `survide` est `() -> vrai` et `surpasvide` est `tt qu -> faux`. *)

(* In[60]: *)


let estvide = fun liste -> liste (vrai) (fun tt qu -> faux);;

(* Deux tests : *)

(* In[61]: *)


entierNatif (si (estvide (listevide)) un zero);; (* estvide listevide == vrai *)
entierNatif (si (estvide (cons un listevide)) un zero);; (* estvide (cons un listevide) == faux *);;

(* Et pour les deux extracteurs, c'est très facile avec cet encodage. *)

(* In[62]: *)


let tete = fun liste -> liste (vide) (fun tt qu -> tt);;
let queue = fun liste -> liste (vide) (fun tt qu -> qu);;

(* In[69]: *)


entierNatif (tete (cons un listevide));;
entierNatif (tete (queue (cons deux (cons un listevide))));;
entierNatif (tete (queue (cons trois (cons deux (cons un listevide)))));;

(* Visualisons les types que Caml trouve a des listes de tailles croissantes : *)

(* In[70]: *)


cons un (cons un listevide);;  (* 8 variables pour une liste de taille 2 *);;

(* In[71]: *)


cons un (cons un (cons un (cons un listevide)));;  (* 14 variables pour une liste de taille 4 *);;

(* In[72]: *)


cons un (cons un (cons un (cons un (cons un (cons un (cons un (cons un listevide)))))));;  (* 26 variables pour une liste de taille 7 *);;

(* Pour ces raisons là, on se rend compte que le type donné par Caml à une liste de taille $k$ croît linéairement *en taille* en fonction de $k$ !

Aucun espoir donc (avec cet encodage) d'avoir un type générique pour les listes représentés en Caml.

Et donc nous ne sommes pas surpris de voir cet essai échouer : *)

(* In[68]: *)


let rec longueur liste =
    liste (zero) (fun t q -> succ (longueur q))
;;

(* <span style="color:red;">En effet, `longueur` devrait être bien typée et `liste` et `q` devraient avoir le même type, or le type de `liste` est strictement plus grand que celui de `q`...</span> *)

(* On peut essayer de faire une fonction `ieme`.
On veut que `ieme zero liste = tete` et `ieme n liste = ieme (pred n) (queue liste)`.

En écrivant en haut niveau, on aimerait pouvoir faire : *)

(* In[87]: *)


let pop liste =
    si (estvide liste) (listevide) (queue liste)
;;

(* In[86]: *)


let ieme n liste =
    tete (n pop liste)
;;

(* ## La fonction U

C'est le premier indice que le $\lambda$-calcul peut être utilisé comme modèle de calcul : le terme $U : f \to f(f)$ ne termine pas si on l'applique à lui-même.

Mais ce sera la faiblesse de l'utilisation de Caml : ce terme ne peut être correctement typé ! *)

(* In[55]: *)


let u = fun f -> f (f);;

(* A noter que même dans un langage non typé (par exemple Python), on peut définir $U$ mais son exécution échouera, soit à caude d'un dépassement de pile, soit parce qu'elle ne termine pas. *)

(* ## La récursion via la fonction Y

La fonction $Y$ trouve le point fixe d'une autre fonction.
C'est très utile pour définir des fonctions par récurrence.

Par exemple, la factorielle est le point fixe de la fonction suivante :
"$\lambda f. \lambda n. 1$ si $n \leq 0$ sinon $n * f(n-1)$" (écrite dans un langage plus haut niveau, pas en $\lambda$-calcul).

$Y$ satisfait ces contraintes : $Y(F) = f$ et $f = F(f)$.
Donc $Y(F) = F(Y(F))$ et donc $Y = \lambda F. F(Y(F))$. Mais ce premier essai ne marche pas. *)

(* In[56]: *)


let rec y = fun f -> f (y(f));;

(* In[57]: *)


let fact = y(fun f n -> si (estnul n) (un) (produit n (f (pred n))));;

(* On utilise la $\eta$-expansion : si $e$ termine, $e$ est équivalent (ie tout calcul donne le même terme) à $\lambda x. e(x)$. *)

(* In[58]: *)


let rec y = fun f -> f (fun x -> y(f)(x));;

(* Par contre, le typage n'arrive toujours pas à trouver que l'expression suivante devrait être bien définie : *)

(* In[59]: *)


let fact = y(fun f n -> si (estnul n) (un) (produit n (f (pred n))));;

(* ## Conclusion

Je n'ai pas réussi à traduire intégralement la prouesse initiale, écrite en Python, par Matt Might.
Dommage, le typage de Caml est trop strict pour cet exercice. *)
