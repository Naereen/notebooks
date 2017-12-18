(*
This OCaml script was exported from a Jupyter notebook
using an open-source software (under the MIT License) written by @Naereen
from https://github.com/Naereen/Jupyter-Notebook-OCaml
This software is still in development, please notify me of a bug at
https://github.com/Naereen/Jupyter-Notebook-OCaml/issues/new if you find one
*)

(* # Table of Contents
 <p><div class="lev1 toc-item"><a href="#Texte-d'oral-de-modélisation---Agrégation-Option-Informatique" data-toc-modified-id="Texte-d'oral-de-modélisation---Agrégation-Option-Informatique-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Texte d'oral de modélisation - Agrégation Option Informatique</a></div><div class="lev2 toc-item"><a href="#Préparation-à-l'agrégation---ENS-de-Rennes,-2017-18" data-toc-modified-id="Préparation-à-l'agrégation---ENS-de-Rennes,-2017-18-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Préparation à l'agrégation - ENS de Rennes, 2017-18</a></div><div class="lev2 toc-item"><a href="#À-propos-de-ce-document" data-toc-modified-id="À-propos-de-ce-document-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>À propos de ce document</a></div><div class="lev2 toc-item"><a href="#Question-de-programmation" data-toc-modified-id="Question-de-programmation-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Question de programmation</a></div><div class="lev3 toc-item"><a href="#Modélisation" data-toc-modified-id="Modélisation-131"><span class="toc-item-num">1.3.1&nbsp;&nbsp;</span>Modélisation</a></div><div class="lev3 toc-item"><a href="#Exercice" data-toc-modified-id="Exercice-132"><span class="toc-item-num">1.3.2&nbsp;&nbsp;</span>Exercice</a></div><div class="lev2 toc-item"><a href="#Solution" data-toc-modified-id="Solution-14"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Solution</a></div><div class="lev3 toc-item"><a href="#Types-et-représentations" data-toc-modified-id="Types-et-représentations-141"><span class="toc-item-num">1.4.1&nbsp;&nbsp;</span>Types et représentations</a></div><div class="lev3 toc-item"><a href="#Calcul-récursif-du-nombre-$\rho$" data-toc-modified-id="Calcul-récursif-du-nombre-$\rho$-142"><span class="toc-item-num">1.4.2&nbsp;&nbsp;</span>Calcul récursif du nombre <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-441-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mi>&amp;#x03C1;</mi></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-3069" role="math" style="width: 0.681em; display: inline-block;"><span style="display: inline-block; position: relative; width: 0.525em; height: 0px; font-size: 127%;"><span style="position: absolute; clip: rect(1.877em, 1000.49em, 2.786em, -1000em); top: -2.45em; left: 0em;"><span class="mrow" id="MathJax-Span-3070"><span class="mi" id="MathJax-Span-3071" style="font-family: STIXMathJax_Main; font-style: italic;">ρ</span></span><span style="display: inline-block; width: 0px; height: 2.45em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.316em; border-left: 0px solid; width: 0px; height: 0.932em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ρ</mi></math></span></span><script type="math/tex" id="MathJax-Element-441">\rho</script></a></div><div class="lev3 toc-item"><a href="#Algorithme-demandé-pour-décorer-l'arbre" data-toc-modified-id="Algorithme-demandé-pour-décorer-l'arbre-143"><span class="toc-item-num">1.4.3&nbsp;&nbsp;</span>Algorithme demandé pour décorer l'arbre</a></div><div class="lev2 toc-item"><a href="#Complexités" data-toc-modified-id="Complexités-15"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Complexités</a></div><div class="lev3 toc-item"><a href="#En-espace" data-toc-modified-id="En-espace-151"><span class="toc-item-num">1.5.1&nbsp;&nbsp;</span>En espace</a></div><div class="lev3 toc-item"><a href="#En-temps" data-toc-modified-id="En-temps-152"><span class="toc-item-num">1.5.2&nbsp;&nbsp;</span>En temps</a></div><div class="lev2 toc-item"><a href="#Implémentations-supplémentaires" data-toc-modified-id="Implémentations-supplémentaires-16"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Implémentations supplémentaires</a></div><div class="lev3 toc-item"><a href="#Évaluation-des-expressions" data-toc-modified-id="Évaluation-des-expressions-161"><span class="toc-item-num">1.6.1&nbsp;&nbsp;</span>Évaluation des expressions</a></div><div class="lev3 toc-item"><a href="#Evaluation-par-lecture-postfix-et-pile" data-toc-modified-id="Evaluation-par-lecture-postfix-et-pile-162"><span class="toc-item-num">1.6.2&nbsp;&nbsp;</span>Evaluation par lecture postfix et pile</a></div><div class="lev3 toc-item"><a href="#Affichage-dans-ce-langage-de-manipulation-de-registre" data-toc-modified-id="Affichage-dans-ce-langage-de-manipulation-de-registre-163"><span class="toc-item-num">1.6.3&nbsp;&nbsp;</span>Affichage dans ce langage de manipulation de registre</a></div><div class="lev3 toc-item"><a href="#Méthode-d'Ershov" data-toc-modified-id="Méthode-d'Ershov-164"><span class="toc-item-num">1.6.4&nbsp;&nbsp;</span>Méthode d'Ershov</a></div><div class="lev2 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-17"><span class="toc-item-num">1.7&nbsp;&nbsp;</span>Conclusion</a></div><div class="lev3 toc-item"><a href="#Qualités" data-toc-modified-id="Qualités-171"><span class="toc-item-num">1.7.1&nbsp;&nbsp;</span>Qualités</a></div><div class="lev3 toc-item"><a href="#Bonus" data-toc-modified-id="Bonus-172"><span class="toc-item-num">1.7.2&nbsp;&nbsp;</span>Bonus</a></div><div class="lev3 toc-item"><a href="#Défauts" data-toc-modified-id="Défauts-173"><span class="toc-item-num">1.7.3&nbsp;&nbsp;</span>Défauts</a></div> *)

(* # Texte d'oral de modélisation - Agrégation Option Informatique
## Préparation à l'agrégation - ENS de Rennes, 2017-18
- *Date* : 6 décembre 2017
- *Auteur* : [Lilian Besson](https://GitHub.com/Naereen/notebooks/)
- *Texte*: Annale 2018, ["Expressions arithmétiques" (public2018-D1)](http://agreg.org/Textes/public2018-D1.pdf) *)

(* ## À propos de ce document
- Ceci est une *proposition* de correction, partielle et probablement non-optimale, pour la partie implémentation d'un [texte d'annale de l'agrégation de mathématiques, option informatique](http://Agreg.org/Textes/).
- Ce document est un [notebook Jupyter](https://www.Jupyter.org/), et [est open-source sous Licence MIT sur GitHub](https://github.com/Naereen/notebooks/tree/master/agreg/), comme les autres solutions de textes de modélisation que [j](https://GitHub.com/Naereen)'ai écrite cette année.
- L'implémentation sera faite en OCaml, version 4+ : *)

(* In[1]: *)


Sys.command "ocaml -version";;
print_endline Sys.ocaml_version;;

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

(* In[2]: *)


type operateur = Plus | Moins | MoinsDroite | Mul | Div | DivDroite | Modulo | Expo ;;
(* On utilisera MoinsDroite et DivDroite pour la compilation avec la méthode d'Ershov *);;

(* In[3]: *)


type ('a, 'b) arbre_binaire = N of (('a,'b) arbre_binaire) * 'b * (('a,'b) arbre_binaire) | F of 'a;;

(* Par exemple pour l'expression $\frac{x - yz}{u - vw}$, c'est-à-dire `(x - y*z)/(u - v*w)` : *)

(* In[4]: *)


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

(* In[5]: *)


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

(* In[6]: *)


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

(* In[7]: *)


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

(* In[8]: *)


let rec hauteur (expr : ('a, 'b) arbre_binaire) : int =
    match expr with
    | F _ -> 0
    | N(t1, _, t2) ->
        let d1, d2 = hauteur t1, hauteur t2 in
        1 + (max d1 d2)
;;

(* Exemples qui concordent avec le texte : *)

(* In[9]: *)


let _ = hauteur exp1;;
let _ = nombre_rho exp1;;

(* In[10]: *)


let _ = hauteur exp2;;
let _ = nombre_rho exp2;;

(* In[11]: *)


let _ = hauteur exp3;;
let _ = nombre_rho exp3;;

(* ### Algorithme demandé pour décorer l'arbre *)

(* On choisit d'ajouter une *décoration* de type `'c` : *)

(* In[12]: *)


type ('a, 'b, 'c) arbre_binaire_decore = N2 of ('c * (('a, 'b, 'c) arbre_binaire_decore) * 'b * (('a, 'b, 'c) arbre_binaire_decore)) | F2 of 'a;;

(* On a besoin d'attacher à chaque noeud son paramètre $\rho$ et un drapeau binaire permettant de savoir si l'algorithme d'Ershov indique d'évaluer en premier le sous-arbre gauche (`premier_gauche = true`) ou droite (`= false`). *)

(* In[13]: *)


type decoration = {
    rho : int;
    premier_gauche : bool;
};;

(* In[14]: *)


let rec decore (expr : (('a, 'b) arbre_binaire)) : (('a, 'b, decoration) arbre_binaire_decore) =
    match expr with
    | F v -> F2 v
    | N (t1, o, t2) ->
        let d1, d2 = nombre_rho t1, nombre_rho t2 in
        let d = if d1 = d2 then d1 + 1 else max d1 d2 in
        N2({rho = d; premier_gauche = (d2<= d1)}, (decore t1), o, (decore t2))
;;

(* Dans nos exemples, on voit que l'évaluation favorise en premier (avec des `premier_gauche = false`) les expressions les plus profondes (à droite) au sens du paramètre $\rho$ : *)

(* In[15]: *)


decore exp1;;

(* In[16]: *)


decore exp2;;

(* In[17]: *)


decore exp3;;

(* ## Complexités *)

(* ### En espace
Les deux fonctions présentées ci-dessus n'utilisent pas d'autre espace que l'arbre décoré, et la pile d'appel récursif.

- Le calcul récursif de $\rho(t)$ prend donc un espace proportionnel au nombre d'appel récursif imbriqué, qui est borné par la taille du terme $t$ (définie comme le nombre de noeuds et de feuilles), donc est **linéaire**,
- Le calcul de la méthode d'Ershov est elle aussi **linéaire** puisque l'arbre décoré est de même taille que l'arbre initial. *)

(* ### En temps
Les deux fonctions présentées ci-dessus sont **linéaires** dans la taille de l'arbre. *)

(* ## Implémentations supplémentaires

On peut essayer d'implémenter une fonction qui afficherait ceci pour la méthode d'évaluation naturelle :

<img width="70%" alt="images/public2018-D1_ex1.png" src="images/public2018-D1_ex1.png">

Et ceci pour la méthode d'Ershov :

<img width="70%" alt="images/public2018-D1_ex2.png" src="images/public2018-D1_ex2.png">

Ce n'est pas trop difficile, mais ça prend un peu de temps :

- on va d'abord montrer comment évaluer les expressions, en lisant l'arbre et en effectuant des appels récursifs,
- puis on fera un parcours postfix de l'arbre afin d'utiliser l'évaluation avec une pile, avec la stratégie naïve,
- et enfin la méthode d'Ershov permettra de réduire la hauteur maximale de la pile, en passant de $h(t)$ (hauteur de l'arbre) à $\rho(t)$,
- en bonus, on affichera les instructions style "compilateur à registre", pour visualiser le gain apporté par la méthode d'Ershov.

> Bien sûr, tout cela fait beaucoup trop pour être envisagé le jour de l'oral ! Mais un des points aurait pû être implémenté rapidement. *)

(* ### Évaluation des expressions

Un premier objectif plus simple est d'évaluer les expressions, en fournissant un *contexte* (table associant une valeur à chaque variable). *)

(* In[18]: *)


type ('a, 'b) contexte = ('a * 'b) list;;
let valeur (ctx : ('a, 'b) contexte) (var : 'a) = List.assoc var ctx;;
(* une Hashtbl peut etre utilisee si besoin de bonnes performances *);;

(* In[19]: *)


let contexte1 : (string, int) contexte = [
    ("x", 1); ("y", 2); ("z", 3);
    ("u", 4); ("v", 5); ("w", 6)
];;

(* In[20]: *)


let intop_of_op (op : operateur) : (int -> int -> int) =
    match op with
    | Plus -> ( + )
    | Moins -> ( - )
    | MoinsDroite -> (fun v1 -> fun v2 -> v2 - v1)
    | Mul -> ( * )
    | Div -> ( / )
    | DivDroite -> (fun v1 -> fun v2 -> v2 / v1)
    | Modulo -> ( mod )
    | Expo ->
        (fun v1 -> fun v2 -> int_of_float ((float_of_int v1) ** (float_of_int v2)))
;;

(* In[21]: *)


let rec eval_int (ctx : (string, int) contexte) (expr : (string, operateur) arbre_binaire) : int =
    match expr with
    | F(s) -> valeur ctx s
    | N(t1, op, t2) ->
        let v1, v2 = eval_int ctx t1, eval_int ctx t2 in
        (intop_of_op op) v1 v2
;;

(* Par exemple, $x$ vaut $1$ dans le contexte d'exemple, et $x + y$ vaut $1 + 2 = 3$ : *)

(* In[22]: *)


let _ = eval_int contexte1 (F("x"));;

(* In[23]: *)


let _ = eval_int contexte1 (N(F("x"), Plus, F("y")));;

(* In[24]: *)


let _ = eval_int contexte1 exp1;;

(* In[25]: *)


let _ = eval_int contexte1 exp2;;

(* In[26]: *)


let _ = eval_int contexte1 exp3;;

(* On voit la faiblesse de l'interprétation avec des entiers, la division `/` est une division entière !

On peut aussi interpréter avec des flottants : *)

(* In[27]: *)


let contexte2 : (string, float) contexte = [
    ("x", 1.); ("y", 2.); ("z", 3.);
    ("u", 4.); ("v", 5.); ("w", 6.)
];;

(* In[28]: *)


let floatop_of_op (op : operateur) : (float -> float -> float) =
    match op with
    | Plus -> ( +. )
    | Moins -> ( -. )
    | MoinsDroite -> (fun v1 -> fun v2 -> v2 -. v1)
    | Mul -> ( *. )
    | Div -> ( /. )
    | DivDroite -> (fun v1 -> fun v2 -> v2 /. v1)
    | Modulo ->
        (fun v1 -> fun v2 -> float_of_int ((int_of_float v1) mod (int_of_float v2)))
    | Expo -> ( ** )
;;

(* In[29]: *)


let rec eval_float (ctx : (string, float) contexte) (expr : (string, operateur) arbre_binaire) : float =
    match expr with
    | F(s) -> valeur ctx s
    | N(t1, op, t2) ->
        let v1, v2 = eval_float ctx t1, eval_float ctx t2 in
        (floatop_of_op op) v1 v2
;;

(* Par exemple, $x$ vaut $1$ dans le contexte d'exemple, et $x + y$ vaut $1 + 2 = 3$ : *)

(* In[30]: *)


let _ = eval_float contexte2 (F("x"));;

(* In[31]: *)


let _ = eval_float contexte2 (N(F("x"), Plus, F("y")));;

(* In[32]: *)


let _ = eval_float contexte2 exp1;;

(* In[33]: *)


let _ = eval_float contexte2 exp2;;

(* In[34]: *)


let _ = eval_float contexte2 exp3;;

(* ### Evaluation par lecture postfix et pile
On va commencer par lire l'arbre en parcours postfix (cf. [TP2 @ ENS Rennes 2017/18](https://nbviewer.jupyter.org/github/Naereen/notebooks/tree/master/agreg/TP_Programmation_2017-18/TP2__OCaml.ipynb)) et ensuite l'évaluer grâce à une pile. *)

(* In[35]: *)


type ('a, 'b) lexem = O of 'b | V of 'a;;
type ('a, 'b) parcours = (('a, 'b) lexem) list;;

(* In[36]: *)


let parcours_postfix (expr : ('a, 'b) arbre_binaire) : (('a, 'b) parcours) =
    let rec parcours vus expr =
        match expr with
        | F(s) -> V(s) :: vus
        | N(t1, op, t2) -> O(op) :: (parcours (parcours vus t1) t2)
    in
    List.rev (parcours [] expr)
;;

(* On le teste : *)

(* In[37]: *)


parcours_postfix exp1;;

(* In[38]: *)


parcours_postfix exp3;;

(* In[39]: *)


let eval_int_2 (ctx : (string, int) contexte) (expr : (string, operateur) arbre_binaire) : int =
    let vus = parcours_postfix expr in
    let pile = Stack.create () in
    let aux lex =
        match lex with
        | V(s) -> Stack.push (valeur ctx s) pile;
        | O(op) ->
            let v1, v2 = Stack.pop pile, Stack.pop pile in
            Stack.push ((intop_of_op op) v1 v2) pile;
    in
    List.iter aux vus;
    Stack.pop pile
;;

(* Par exemple, $x - y*z$ avec $x = 1, y = 2, z = 3$ vaut $1 - 2 * 3 = -5$ : *)

(* In[40]: *)


let _ = exp1 ;;
let _ = eval_int_2 contexte1 exp1;;

(* In[41]: *)


let _ = exp2;;
let _ = eval_int_2 contexte1 exp2;;

(* On peut maintenant faire la même fonction mais qui va en plus afficher l'état successif de la pile (avec des valeurs uniquement). *)

(* In[42]: *)


let print f =
    let r = Printf.printf f in
    flush_all();
    r
;;

(* In[43]: *)


let print_pile pile =
    print "\nPile : ";
    Stack.iter (print "%i; ") pile;
    print "."
;;

(* In[44]: *)


let eval_int_3 (ctx : (string, int) contexte) (expr : (string, operateur) arbre_binaire) : int =
    let vus = parcours_postfix expr in
    let pile = Stack.create () in
    let aux lex =
        print_pile pile;
        match lex with
        | V(s) -> Stack.push (valeur ctx s) pile;
        | O(op) ->
            let v1, v2 = Stack.pop pile, Stack.pop pile in
            Stack.push ((intop_of_op op) v1 v2) pile;
    in
    List.iter aux vus;
    Stack.pop pile
;;

(* In[45]: *)


let _ = exp1 ;;
let _ = eval_int_3 contexte1 exp1;;

(* In[46]: *)


let _ = exp3;;
let _ = eval_int_3 contexte1 exp3;;

(* > Il y a un soucis dans l'ordre d'affichage des lignes, dû à Jupyter et pas à notre fonction. *)

(* On vérifie qu'on utilise au plus 4 valeurs sur la pile, comme représenté dans la figure de l'énoncé :

<img width="70%" alt="images/public2018-D1_ex3.png" src="images/public2018-D1_ex3.png"> *)

(* ### Affichage dans ce langage de manipulation de registre
On ne va pas trop formaliser ça, mais juste les afficher... *)

(* In[47]: *)


let print_aff (line : int) (i : int) (s : string) : unit =
    print "\n%02i: R[%d] := %s ;" line i s;
;;

(* In[48]: *)


let string_of_op (op : operateur) : string =
    match op with
    | Plus -> "+"
    | Moins | MoinsDroite -> "-"
    | Mul -> "*"
    | Div | DivDroite -> "/"
    | Modulo -> "%"
    | Expo -> "^"
;;

(* In[49]: *)


let print_op (line : int) (i : int) (j : int) (k : int) (op : operateur) : unit =
    match op with
    | MoinsDroite | DivDroite -> (* on gère ici les opérateurs "inverses" *)
        print "\n%02i: R[%d] := R[%d] %s R[%d] ;" line i k (string_of_op op) j;
    | _ ->
        print "\n%02i: R[%d] := R[%d] %s R[%d] ;" line i j (string_of_op op) k;
;;

(* In[50]: *)


let eval_int_4 (ctx : (string, int) contexte) (expr : (string, operateur) arbre_binaire) : int =
    let vus = parcours_postfix expr in
    let pile = Stack.create () in
    let ligne = ref 0 in
    let aux lex =
        incr ligne;
        match lex with
        | V(s) ->
            Stack.push (valeur ctx s) pile;
            print_aff !ligne ((Stack.length pile) - 1) s;
        | O(op) ->
            let v1, v2 = Stack.pop pile, Stack.pop pile in
            Stack.push ((intop_of_op op) v1 v2) pile;
            print_op !ligne ((Stack.length pile) - 1) ((Stack.length pile) - 1) (Stack.length pile) op;
    in
    List.iter aux vus;
    Stack.pop pile
;;

(* Essayons ça : *)

(* In[62]: *)


let _ = exp1 ;;
let _ = eval_int_4 contexte1 exp1;;

(* In[66]: *)


let _ = exp3;;
let _ = eval_int_4 contexte1 exp3;;

(* ### Méthode d'Ershov
Enfin, on va générer, en plus de l'évaluation, un affichage comme celui qu'on voulait, qui montre les affectations dans les registres, et permettra de visualiser que la méthode d'Ershov utilise un registre de moins sur le terme exemple qui calcule $(x - y*z)/(u - v*w)$. *)

(* On rappelle qu'on a obtenu un arbre binaire décoré, représenté comme tel : *)

(* In[53]: *)


decore exp1;;

(* On modifie notre parcours postfix pour prendre en compte la décoration et savoir si on calcul d'abord le sous-arbre gauche ou droit. *)

(* In[54]: *)


let parcours_postfix_decore (expr : ('a, 'b, decoration) arbre_binaire_decore) : (('a, 'b) parcours) =
    let rec parcours vus expr =
        match expr with
        | F2(s) -> V(s) :: vus
        | N2(dec, t1, Moins, t2) when dec.premier_gauche = false ->
            O(MoinsDroite) :: (parcours (parcours vus t2) t1)
        | N2(dec, t1, MoinsDroite, t2) when dec.premier_gauche = false ->
            O(Moins) :: (parcours (parcours vus t2) t1)
        | N2(dec, t1, Div, t2) when dec.premier_gauche = false ->
            O(DivDroite) :: (parcours (parcours vus t2) t1)
        | N2(dec, t1, DivDroite, t2) when dec.premier_gauche = false ->
            O(Div) :: (parcours (parcours vus t2) t1)
        | N2(dec, t1, op, t2) when dec.premier_gauche = false ->
            O(op) :: (parcours (parcours vus t2) t1)
        | N2(_, t1, op, t2) ->
            O(op) :: (parcours (parcours vus t1) t2)
    in
    List.rev (parcours [] expr)
;;

(* In[55]: *)


let eval_int_ershov (ctx : (string, int) contexte) (expr : (string, operateur) arbre_binaire) : int =
    let vus = parcours_postfix_decore (decore expr) in
    let pile = Stack.create () in
    let ligne = ref 0 in
    let aux lex =
        incr ligne;
        match lex with
        | V(s) ->
            Stack.push (valeur ctx s) pile;
            print_aff !ligne ((Stack.length pile) - 1) s;
        | O(op) ->
            let v1, v2 = Stack.pop pile, Stack.pop pile in
            Stack.push ((intop_of_op op) v1 v2) pile;
            print_op !ligne ((Stack.length pile) - 1) ((Stack.length pile) - 1) (Stack.length pile) op;
    in
    List.iter aux vus;
    Stack.pop pile
;;

(* Essayons ça : *)

(* In[56]: *)


let _ = exp1 ;;
let _ = eval_int_ershov contexte1 exp1;;

(* In[68]: *)


let _ = exp3;;
let _ = eval_int_ershov contexte1 exp3;;

(* Et voilà, ce n'était pas trop dur ! *)

(* ----
## Conclusion

Voilà pour la question obligatoire de programmation, et un petit bonus.

### Qualités
- On a décomposé le problème en sous-fonctions (d'abord le calcul de $\rho$ puis la méthode d'Ershov),
- On a fait des exemples et *on les garde* dans ce qu'on présente au jury,
- On a testé la fonction exigée sur de petits exemples et sur un exemple de taille réelle (venant du texte).

### Bonus
On a fait pas mal de bonus, en interprétant les termes, d'abord via l'arbre et des appels récursifs, ensuite par une lecture postfix et une pile, qui nous a permis de vérifier l'évolution de la pile et de sa hauteur (avec le même exemple que dans le texte), et ensuite avec une espèce de "compilation" en visualisant les affectations dans ces registres. La "compilation" n'est pas réelle, on a uniquement affiché des choses, mais elle permet de vérifier que la méthode de Ershov aide effectivement à réduire le nombre de registre requis.

### Défauts
- ?


> Bien-sûr, ce petit notebook ne se prétend pas être une solution optimale, ni exhaustive.

> Vous auriez pu choisir de modéliser le problème avec une autre approche, n'hésitez pas [à me contacter svp](http://perso.crans.org/besson/callme.html). *)

(* > C'est tout pour aujourd'hui les amis, allez voir [ici pour d'autres corrections](https://github.com/Naereen/notebooks/tree/master/agreg), et que la force soit avec vous ! *)
