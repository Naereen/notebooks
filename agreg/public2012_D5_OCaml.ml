(*
This OCaml script was exported from a Jupyter notebook
using an open-source software (under the MIT License) written by @Naereen
from https://github.com/Naereen/Jupyter-Notebook-OCaml
This software is still in development, please notify me of a bug at
https://github.com/Naereen/Jupyter-Notebook-OCaml/issues/new if you find one
*)

(* # Table of Contents
 <p><div class="lev1 toc-item"><a href="#Agrégation-externe-de-mathématiques,-texte-d’exercice-diffusé-en-2012" data-toc-modified-id="Agrégation-externe-de-mathématiques,-texte-d’exercice-diffusé-en-2012-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Agrégation externe de mathématiques, texte d’exercice diffusé en 2012</a></div><div class="lev2 toc-item"><a href="#Épreuve-de-modélisation,-option-informatique" data-toc-modified-id="Épreuve-de-modélisation,-option-informatique-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Épreuve de modélisation, option informatique</a></div><div class="lev2 toc-item"><a href="#Proposition-d'implémentation,-en-OCaml" data-toc-modified-id="Proposition-d'implémentation,-en-OCaml-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span><em>Proposition</em> d'implémentation, en <a href="https://ocaml.org/" target="_blank">OCaml</a></a></div><div class="lev3 toc-item"><a href="#Pour-l'option-informatique-(D)-de-l'agrégation-de-mathématiques-(en-France)." data-toc-modified-id="Pour-l'option-informatique-(D)-de-l'agrégation-de-mathématiques-(en-France).-121"><span class="toc-item-num">1.2.1&nbsp;&nbsp;</span>Pour <a href="http://www.dit.ens-rennes.fr/agregation-option-d/programme-de-l-option-informatique-de-l-agregation-de-mathematiques-48358.kjsp" target="_blank">l'option informatique (D)</a> de l'<a href="http://agreg.org/" target="_blank">agrégation de mathématiques</a> (en France).</a></div><div class="lev2 toc-item"><a href="#Exercice-requis" data-toc-modified-id="Exercice-requis-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Exercice requis</a></div><div class="lev2 toc-item"><a href="#Choix-de-structure-de-données" data-toc-modified-id="Choix-de-structure-de-données-14"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Choix de structure de données</a></div><div class="lev3 toc-item"><a href="#En-OCaml" data-toc-modified-id="En-OCaml-141"><span class="toc-item-num">1.4.1&nbsp;&nbsp;</span>En OCaml</a></div><div class="lev3 toc-item"><a href="#En-Python" data-toc-modified-id="En-Python-142"><span class="toc-item-num">1.4.2&nbsp;&nbsp;</span>En Python</a></div><div class="lev2 toc-item"><a href="#Réponse" data-toc-modified-id="Réponse-15"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Réponse</a></div><div class="lev3 toc-item"><a href="#On-fait-quelques-exemples..." data-toc-modified-id="On-fait-quelques-exemples...-151"><span class="toc-item-num">1.5.1&nbsp;&nbsp;</span>On fait quelques exemples...</a></div><div class="lev3 toc-item"><a href="#Si-une-hypothèse-n'est-pas-vérifié" data-toc-modified-id="Si-une-hypothèse-n'est-pas-vérifié-152"><span class="toc-item-num">1.5.2&nbsp;&nbsp;</span>Si une hypothèse n'est pas vérifié</a></div><div class="lev2 toc-item"><a href="#Bonus-:-deux-autres-méthodes-(droites-inférieure-et-supérieure)" data-toc-modified-id="Bonus-:-deux-autres-méthodes-(droites-inférieure-et-supérieure)-16"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Bonus : deux autres méthodes (droites inférieure et supérieure)</a></div><div class="lev2 toc-item"><a href="#Illustration" data-toc-modified-id="Illustration-17"><span class="toc-item-num">1.7&nbsp;&nbsp;</span>Illustration</a></div><div class="lev3 toc-item"><a href="#Par-la-sélection-de-Bresenham" data-toc-modified-id="Par-la-sélection-de-Bresenham-171"><span class="toc-item-num">1.7.1&nbsp;&nbsp;</span>Par la sélection de Bresenham</a></div><div class="lev3 toc-item"><a href="#Par-la-sélection-inférieure" data-toc-modified-id="Par-la-sélection-inférieure-172"><span class="toc-item-num">1.7.2&nbsp;&nbsp;</span>Par la sélection inférieure</a></div><div class="lev3 toc-item"><a href="#Par-la-sélection-supérieure" data-toc-modified-id="Par-la-sélection-supérieure-173"><span class="toc-item-num">1.7.3&nbsp;&nbsp;</span>Par la sélection supérieure</a></div><div class="lev2 toc-item"><a href="#Autres-bonus-:-calculer-le-mot-binaire-codant-les-déplacements" data-toc-modified-id="Autres-bonus-:-calculer-le-mot-binaire-codant-les-déplacements-18"><span class="toc-item-num">1.8&nbsp;&nbsp;</span>Autres bonus : calculer le mot binaire codant les déplacements</a></div><div class="lev2 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-19"><span class="toc-item-num">1.9&nbsp;&nbsp;</span>Conclusion</a></div><div class="lev2 toc-item"><a href="#Attention" data-toc-modified-id="Attention-110"><span class="toc-item-num">1.10&nbsp;&nbsp;</span>Attention</a></div> *)

(* # Agrégation externe de mathématiques, texte d’exercice diffusé en 2012 *)

(* ## Épreuve de modélisation, option informatique *)

(* > - Ce [notebook Jupyter](http://jupyter.org/), utilisant [OCaml](https://ocaml.org/) (via le [kernel Ocaml](https://github.com/akabe/ocaml-jupyter/)), est une correction [non officielle](https://github.com/Naereen/notebooks/tree/master/agreg) d'un texte de modélisation pour l'option informatique de l'agrégation externe de mathématiques.
> - Il s'agit du texte [public2012-D5](http://agreg.org/Textes/public2012-D5.pdf).
> - Cette tentative de correction partielle a été rédigée par [Lilian Besson](http://perso.crans.org/besson/) ([sur GitHub ?](https://github.com/Naereen/), [sur Bitbucket ?](https://bitbucket.org/lbesson)), et [est open-source](https://github.com/Naereen/notebooks/blob/master/agreg/public2012_D5_OCaml.ipynb).
> - J'avais déjà rédigé une solution, pendant ma propre préparation à l'agrégation en 2013/2014, voir [ce fichier](https://perso.crans.org/besson/agreg/m/29-04/code_Public2012-D5.html).

> Retour ?
> - Vous avez trouvé un bug ? → [Signalez-le moi svp !](https://github.com/Naereen/notebooks/issues/new), merci d'avance.
> - Vous avez une question ? → [Posez la svp !](https://github.com/Naereen/ama.fr) [![Demandez moi n'importe quoi !](https://img.shields.io/badge/Demandez%20moi-n'%20importe%20quoi-1abc9c.svg)](https://GitHub.com/Naereen/ama.fr)

---- *)

(* ## *Proposition* d'implémentation, en [OCaml](https://ocaml.org/) *)

(* ### Pour [l'option informatique (D)](http://www.dit.ens-rennes.fr/agregation-option-d/programme-de-l-option-informatique-de-l-agregation-de-mathematiques-48358.kjsp) de l'[agrégation de mathématiques](http://agreg.org/) (en France). *)

(* **Attention** : ce document ne prétend pas être LA correction du texte, mais **un exemple de solution**.

Je me suis inspiré des propositions d'implémentations rédigées par les élèves qui ont préparé ce texte en 3h50 le lundi 13 mai 2019.

---- *)

(* ## Exercice requis

L'exercice de programmation était en page 2/8 du texte, après l'explication du problème et de l'algorithme de Bresenham.

> Écrire un programme permettant de représenter le segment $[A B]$, où $A= (a_1,a_2)$ et $B=(b_1,b_2)$, en suivant l'algorithme de Bresenham.
> On supposera que $a_1<b_1$, $a_2 \leq b_2$ et que la pente $\alpha$ de la droite est inférieure à $1$.
> La sortie du programme sera la liste des couples $(x_i,y_i)$ des points représentant le segment.

Attention, on rappelle que le rapport du jury précise explicitement que dans les exercices de programmation **liste de …** signifie *liste* <span style="color:red;">OU</span> *tableau*, au choix du candidat ou de la candidate. *)

(* ---- *)

(* ## Choix de structure de données

Soit $n = b_1 - a_1 \in\mathbb{N}$.
Ici, on connaît à l'avance le nombre de points que doit contenir la solution, donc utiliser un tableau de $n+1$ points est une bonne idée.

### En OCaml
On va préférer :

```ocaml
let segment = Array.make (n+1) (a1, a2) in
...

for i = 1 to n do
    let xi, yi = ..., ... in
    segment.(i) <- (xi, yi);
done
```

à :

```ocaml
let segment = ref [(a1, a2)] in
...

for i = 1 to n do
    let xi, yi = ..., ... in
    segment := (xi, yi) :: !segment;
done
```

### En Python
On pourrait de même créer un tableau dès le début.
On va préférer :

```python
segment = [ (0,0) for i in range(n+1) ]
segment = [ (0,0) ] * (n+1)
...
for i in range(n):
    xi, yi = ..., ...
    segment[i] = (xi, yi)
```

à :

```python
segment = [ (a1, a2) ]
...
for i in range(n):
    xi, yi = ..., ...
    segment.append(xi, yi)
``` *)

(* ---- *)

(* ## Réponse *)

(* On utilise un type `point` pour représenter les points de coordonées entières $(x, y) \in\mathbb{Z}^2$, cela facilitera l'affichage des signatures : *)

(* In[3]: *)


type point = (int * int);;

let point_a : point = (0, 0)
and point_b : point = (4, 3);;

(* In[5]: *)


type segment = point array;;

(* La fonction suivante renvoie un tableau de $n+1$ points, représentant le segment $[a, b]$ obtenus avec l'algorithme de Bresenham.

- Complexité temporelle : $\mathcal{O}(n)$
- Complexité mémoire : $\mathcal{O}(n)$, où n = b1 - a1.
  (dans tous les cas) *)

(* In[50]: *)


let bresenham (a : point) (b : point) : segment =
  let a1, a2 = a
  and b1, b2 = b in
  let n = b1 - a1 in
  let segment_ab = Array.make (n+1) a in
  let alpha_normalisee = b2 - a2 in (* pente normalisée, ie alpha*n dans *)
  let erreur = ref 0 in
  let y_tilde = ref a2 in
  for i = 1 to n-1 do
    if 2 * (!erreur + alpha_normalisee) <= n then
      erreur := !erreur + alpha_normalisee
    else begin
      erreur := !erreur + alpha_normalisee - n;
      y_tilde := !y_tilde + 1;
    end;
    segment_ab.(i) <- (a1 + i, !y_tilde);
  done;
  segment_ab.(n) <- b;
  segment_ab
;;

(* ### On fait quelques exemples... *)

(* In[51]: *)


bresenham (0, 0) (5, 2);;

(* In[52]: *)


bresenham (0, 0) (5, 5);;

(* ### Si une hypothèse n'est pas vérifié *)

(* On vérifie que l'ordre des arguments est important, le programme exige que $a_1 < b_1$ et $a_2 \leq b_2$ : *)

(* In[53]: *)


bresenham (0, 0) (-5, 2);;

(* Si la pente est $\alpha>1$, le programme ne fait pas ce qu'on espérait, car ses hypothèses ne sont pas respectées : *)

(* In[54]: *)


bresenham (0, 0) (0, 2);;

(* ---- *)

(* ## Bonus : deux autres méthodes (droites inférieure et supérieure)

Ce n'est pas exigé dans le texte, mais on pouvait facilement implémenter la méthode qui longe la droite au plus près inférieurement, et au plus près supérieurement.

- Pour la première, c'est assez facile et on peut aussi travailler uniquement avec des entiers :

  - Complexité temporelle : $\mathcal{O}(n)$
  - Complexité mémoire : $\mathcal{O}(n)$, où n = b1 - a1.
    (dans tous les cas) *)

(* In[55]: *)


let au_plus_pres_inferieurement (a : point) (b : point) : segment =
  let a1, a2 = a
  and b1, b2 = b in
  let n = b1 - a1 in
  let segment_ab = Array.make (n+1) a in
  let alpha_normalisee = b2 - a2 in (* pente normalisée, ie alpha*n dans *)
  for i = 1 to n-1 do
    (* on laisse la division entière faire la partie inférieure *)
    segment_ab.(i) <- (a1 + i, (alpha_normalisee * i + a2 * (b1-a1)) / (b1 -a1));
  done;
  segment_ab.(n) <- b;
  segment_ab
;;

(* Sur les mêmes exemples, on voit la différence, quand la pente est $\alpha<1$ : *)

(* In[56]: *)


bresenham (0, 0) (5, 2);;
au_plus_pres_inferieurement (0, 0) (5, 2);;

(* In[57]: *)


bresenham (0, 0) (5, 5);;
au_plus_pres_inferieurement (0, 0) (5, 5);;

(* - Pour la droite au plus près supérieurement, on va illustrer l'utilisation d'arithmétique flottante et de la fonction `ceil`

  - Complexité temporelle : $\mathcal{O}(n)$
  - Complexité mémoire : $\mathcal{O}(n)$, où n = b1 - a1.
    (dans tous les cas) *)

(* In[58]: *)


ceil;;

(* In[59]: *)


let ceil_to_int x = int_of_float (ceil x);;

(* In[60]: *)


let au_plus_pres_superieurement (a : point) (b : point) : segment =
  let a1, a2 = a
  and b1, b2 = b in
  let n = b1 - a1 in
  let segment_ab = Array.make (n+1) a in
  let alpha = (float_of_int (b2 - a2)) /. (float_of_int n) in (* pente normalisée, ie alpha*n dans *)
  for i = 1 to n-1 do
    segment_ab.(i) <- (a1 + i, ceil_to_int ((float_of_int a2) +. alpha *. (float_of_int i)));
  done;
  segment_ab.(n) <- b;
  segment_ab
;;

(* Sur les mêmes exemples, on voit la différence, quand la pente est $\alpha<1$ : *)

(* In[61]: *)


bresenham (0, 0) (5, 2);;
au_plus_pres_superieurement (0, 0) (5, 2);;

(* In[62]: *)


bresenham (0, 0) (5, 5);;
au_plus_pres_superieurement (0, 0) (5, 5);;

(* ---- *)

(* ## Illustration

En bonus, on montre une illustration (on ferait des dessins au tableau).

### Par la sélection de Bresenham

![](images/public2012_D5_OCaml__selection_Bresenham.png)

### Par la sélection inférieure

![](images/public2012_D5_OCaml__selection_inferieure.png)

### Par la sélection supérieure

![](images/public2012_D5_OCaml__selection_superieure.png) *)

(* ---- *)

(* ## Autres bonus : calculer le mot binaire codant les déplacements

Si on utilise par exemple la droite longeant au plus près inférieurement, la fonction suivante renvoie la suite des déplacements horizontaux ou diagonaux
pour longer le segment $[a, b]$. *)

(* In[63]: *)


type mot_binaire = bool array;;

(* In[69]: *)


let deplacements (a : point) (b : point) : mot_binaire =
  let a1, a2 = a
  and b1, b2 = b in
  let n = b1 - a1 in
  let mot_binaire_ab : mot_binaire = Array.make n false in
  let alpha_normalisee = b2 - a2 in (* pente normalisée, ie alpha*n dans *)
  let y0 = ref 0 and y1 = ref 0 in
  for i = 1 to n do
    y0 := !y1;
    (* on laisse la division entière faire la partie inférieure *)
    y1 := (alpha_normalisee * i + a2 * (b1-a1)) / (b1 -a1);
    mot_binaire_ab.(i-1) <- !y0 != !y1;
  done;
  mot_binaire_ab
;;

(* Sur les mêmes exemples, on voit la différence, quand la pente est $\alpha<1$ : *)

(* In[70]: *)


au_plus_pres_inferieurement (0, 0) (5, 2);;
deplacements (0, 0) (5, 2);;

(* Le mot renvoyé est $(0 0 1 0 1)$, comme prévu. *)

(* Et si la pente est $\alpha=1$, le mot sera $(11111)$. *)

(* In[71]: *)


au_plus_pres_inferieurement (0, 0) (5, 5);;
deplacements (0, 0) (5, 5);;

(* ---- *)

(* ## Conclusion *)

(* ## Attention *)

(* Les 35/40 minutes de passage au tableau ne doivent PAS être uniquement consacrée à la présentation de vos expériences sur l'ordinateur !

Il faut aussi :

- faire une introduction générale (citer des mots clés),
- présenter le plan de votre présentation,
- introduire les notations, les objectifs et les résultats donnés par le texte,
- prouver ou exposer des développements **theoriques** personnels (à choisir parmi la liste proposée, mais pas seulement),
- etc. *)

(* ----

> *C'est tout pour aujourd'hui les amis !*
> [Allez voir d'autres notebooks](https://github.com/Naereen/notebooks/tree/master/agreg) si vous voulez. *)
