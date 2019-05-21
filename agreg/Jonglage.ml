(*
This OCaml script was exported from a Jupyter notebook
using an open-source software (under the MIT License) written by @Naereen
from https://github.com/Naereen/Jupyter-Notebook-OCaml
This software is still in development, please notify me of a bug at
https://github.com/Naereen/Jupyter-Notebook-OCaml/issues/new if you find one
*)

(* # Table of Contents
 <p><div class="lev1 toc-item"><a href="#Texte-d'oral-de-modélisation---Agrégation-Option-Informatique" data-toc-modified-id="Texte-d'oral-de-modélisation---Agrégation-Option-Informatique-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Texte d'oral de modélisation - Agrégation Option Informatique</a></div><div class="lev2 toc-item"><a href="#Préparation-à-l'agrégation---ENS-de-Rennes,-2018-19" data-toc-modified-id="Préparation-à-l'agrégation---ENS-de-Rennes,-2018-19-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Préparation à l'agrégation - ENS de Rennes, 2018-19</a></div><div class="lev2 toc-item"><a href="#À-propos-de-ce-document" data-toc-modified-id="À-propos-de-ce-document-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>À propos de ce document</a></div><div class="lev2 toc-item"><a href="#Question-de-programmation" data-toc-modified-id="Question-de-programmation-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Question de programmation</a></div><div class="lev2 toc-item"><a href="#Réponse-à-l'exercice-requis" data-toc-modified-id="Réponse-à-l'exercice-requis-14"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Réponse à l'exercice requis</a></div><div class="lev3 toc-item"><a href="#Structures-de-données" data-toc-modified-id="Structures-de-données-141"><span class="toc-item-num">1.4.1&nbsp;&nbsp;</span>Structures de données</a></div><div class="lev3 toc-item"><a href="#Vérifier-qu'un-mot-est-bien-une-permutation-de-$\{0,\dots,n-1\}$" data-toc-modified-id="Vérifier-qu'un-mot-est-bien-une-permutation-de-$\{0,\dots,n-1\}$-142"><span class="toc-item-num">1.4.2&nbsp;&nbsp;</span>Vérifier qu'un mot est bien une permutation de <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-459-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mo fence=&quot;false&quot; stretchy=&quot;false&quot;>{</mo><mn>0</mn><mo>,</mo><mo>&amp;#x2026;</mo><mo>,</mo><mi>n</mi><mo>&amp;#x2212;</mo><mn>1</mn><mo fence=&quot;false&quot; stretchy=&quot;false&quot;>}</mo></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-3289" style="width: 6.829em; display: inline-block;"><span style="display: inline-block; position: relative; width: 5.791em; height: 0px; font-size: 118%;"><span style="position: absolute; clip: rect(1.815em, 1005.69em, 2.959em, -1000em); top: -2.637em; left: 0em;"><span class="mrow" id="MathJax-Span-3290"><span class="mo" id="MathJax-Span-3291" style="font-family: STIXMathJax_Main;">{</span><span class="mn" id="MathJax-Span-3292" style="font-family: STIXMathJax_Main;">0</span><span class="mo" id="MathJax-Span-3293" style="font-family: STIXMathJax_Main;">,</span><span class="mo" id="MathJax-Span-3294" style="font-family: STIXMathJax_Main; padding-left: 0.188em;">…</span><span class="mo" id="MathJax-Span-3295" style="font-family: STIXMathJax_Main; padding-left: 0.188em;">,</span><span class="mi" id="MathJax-Span-3296" style="font-family: STIXMathJax_Normal; font-style: italic; padding-left: 0.188em;">𝑛</span><span class="mo" id="MathJax-Span-3297" style="font-family: STIXMathJax_Main; padding-left: 0.25em;">−</span><span class="mn" id="MathJax-Span-3298" style="font-family: STIXMathJax_Main; padding-left: 0.25em;">1</span><span class="mo" id="MathJax-Span-3299" style="font-family: STIXMathJax_Main;">}</span></span><span style="display: inline-block; width: 0px; height: 2.637em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.269em; border-left: 0px solid; width: 0px; height: 1.127em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mo fence="false" stretchy="false">{</mo><mn>0</mn><mo>,</mo><mo>…</mo><mo>,</mo><mi>n</mi><mo>−</mo><mn>1</mn><mo fence="false" stretchy="false">}</mo></math></span></span><script type="math/tex" id="MathJax-Element-459">\{0,\dots,n-1\}</script></a></div><div class="lev4 toc-item"><a href="#Fonction-quadratique" data-toc-modified-id="Fonction-quadratique-1421"><span class="toc-item-num">1.4.2.1&nbsp;&nbsp;</span>Fonction quadratique</a></div><div class="lev4 toc-item"><a href="#Fonction-linéaire" data-toc-modified-id="Fonction-linéaire-1422"><span class="toc-item-num">1.4.2.2&nbsp;&nbsp;</span>Fonction linéaire</a></div><div class="lev4 toc-item"><a href="#Comparaison-expérimentale" data-toc-modified-id="Comparaison-expérimentale-1423"><span class="toc-item-num">1.4.2.3&nbsp;&nbsp;</span>Comparaison expérimentale</a></div><div class="lev3 toc-item"><a href="#Construire-le-mot-$\omega$" data-toc-modified-id="Construire-le-mot-$\omega$-143"><span class="toc-item-num">1.4.3&nbsp;&nbsp;</span>Construire le mot <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-494-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mi>&amp;#x03C9;</mi></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-3544" style="width: 0.85em; display: inline-block;"><span style="display: inline-block; position: relative; width: 0.706em; height: 0px; font-size: 118%;"><span style="position: absolute; clip: rect(1.866em, 1000.69em, 2.6em, -1000em); top: -2.448em; left: 0em;"><span class="mrow" id="MathJax-Span-3545"><span class="mi" id="MathJax-Span-3546" style="font-family: STIXMathJax_Normal; font-style: italic;">𝜔</span></span><span style="display: inline-block; width: 0px; height: 2.448em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.069em; border-left: 0px solid; width: 0px; height: 0.644em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>ω</mi></math></span></span><script type="math/tex" id="MathJax-Element-494">\omega</script></a></div><div class="lev4 toc-item"><a href="#Transformer-une-chaîne-de-caractère-&quot;5241&quot;-en-un-mot" data-toc-modified-id="Transformer-une-chaîne-de-caractère-&quot;5241&quot;-en-un-mot-1431"><span class="toc-item-num">1.4.3.1&nbsp;&nbsp;</span>Transformer une chaîne de caractère "5241" en un <code>mot</code></a></div><div class="lev3 toc-item"><a href="#Test-de-la-permutation" data-toc-modified-id="Test-de-la-permutation-144"><span class="toc-item-num">1.4.4&nbsp;&nbsp;</span>Test de la permutation</a></div><div class="lev3 toc-item"><a href="#Test-de-la-moyenne" data-toc-modified-id="Test-de-la-moyenne-145"><span class="toc-item-num">1.4.5&nbsp;&nbsp;</span>Test de la moyenne</a></div><div class="lev2 toc-item"><a href="#Bonus-?" data-toc-modified-id="Bonus-?-15"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Bonus ?</a></div><div class="lev3 toc-item"><a href="#Complexité" data-toc-modified-id="Complexité-151"><span class="toc-item-num">1.5.1&nbsp;&nbsp;</span>Complexité</a></div><div class="lev3 toc-item"><a href="#Autres-idées" data-toc-modified-id="Autres-idées-152"><span class="toc-item-num">1.5.2&nbsp;&nbsp;</span>Autres idées</a></div><div class="lev2 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-16"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Conclusion</a></div> *)

(* # Texte d'oral de modélisation - Agrégation Option Informatique *)

(* ## Préparation à l'agrégation - ENS de Rennes, 2018-19 *)

(* - *Date* : 21 mai 2019
- *Auteur* : [Lilian Besson](https://GitHub.com/Naereen/notebooks/)
- *Texte*: [Jonglage (public2012-D2.pdf)](http://agreg.org/Textes/public2012-D2.pdf) *)

(* ## À propos de ce document *)

(* - Ceci est une *proposition* de correction, partielle et probablement non-optimale, pour la partie implémentation d'un [texte d'annale de l'agrégation de mathématiques, option informatique](http://Agreg.org/Textes/).
- Ce document est un [notebook Jupyter](https://www.Jupyter.org/), et [est open-source sous Licence MIT sur GitHub](https://github.com/Naereen/notebooks/tree/master/agreg/), comme les autres solutions de textes de modélisation que [j](https://GitHub.com/Naereen)'ai écrite cette année.
- L'implémentation sera faite en OCaml, version 4+ : *)

(* In[1]: *)


Sys.command "ocaml -version";;

(* > Notez que certaines fonctions des modules usuels [`List`](http://caml.inria.fr/pub/docs/manual-ocaml/libref/List.html) et [`Array`](http://caml.inria.fr/pub/docs/manual-ocaml/libref/List.html) ne sont pas disponibles en OCaml 3.12.
> J'essaie autant que possible de ne pas les utiliser, ou alors de les redéfinir si je m'en sers. *)

(* Merci à Pierre et Clarence, élèves de la préparation à l'agrégation en 2018/2019, de m'avoir autorisé à utiliser une partie de leur implémentation pour cette (proposition de) correction. *)

(* ---- *)

(* ## Question de programmation *)

(* La question de programmation pour ce texte était donnée en page 5, et était assez courte :

> "Implanter dans l’un des langages de programmation autorisés l’algorithme de test de permutation." *)

(* ---- *)

(* ## Réponse à l'exercice requis

Dans l'ordre, on va :

1. définir une structure de donnée (mot = tableau d'entier),
2. écrire une fonction qui vérifie qu'un tel tableau est bien une permutation de $\{0,\dots,n-1\}$,
3. transformer une chaîne comme `"5340"` en un mot `[|5;4;3;0|]`,
4. calculer le mot $\omega$ depuis un tel mot, `[|1;0;2;3|]`,
5. vérifier que ce mot $\omega$ est une permutation (c'est le **test de permutation**).

En bonus, on implémente aussi le **test de moyenne**, et on illustre le bon fonctionnement de notre implémentation sur les exemples du texte. *)

(* ### Structures de données

On travaille avec des **mots** représentés comme des tableaux d'entiers. *)

(* In[4]: *)


type mot = int array ;;

(* ### Vérifier qu'un mot est bien une permutation de $\{0,\dots,n-1\}$

On présente deux implémentations, la première n'est pas très réfléchie et se trouve être avoir une complexité temporelle en $\mathcal{O}(|mot|^2)$, tandis que la seconde est plus réfléchie et fonctionne en temps linéaire $\mathcal{O}(|mot|)$.

On va supposer que chaque valeur du mot d'entrée est bien dans $\{0,\dots,n-1\}$, et on vérifie simplement que chaque valeur est présente une et une seule fois (si $n=|mot|$). *)

(* #### Fonction quadratique

Pour chaque valeur $i\in\{0,\dots,n-1\}$, on parcourt le mot à la recherche d'une valeur $m[j]=i$. *)

(* In[6]: *)


let est_permut (m : mot) : bool =
  let p = Array.length m in
  let permut_bool = ref true in
  let i = ref 0 in
  while !i<p && !permut_bool do
    permut_bool := !permut_bool && ( Array.exists (fun x -> x = !i) m );
    incr i
  done;
  !permut_bool;;
(* Complexité temporelle au pire en O(p^2) *)
(* Complexité spatiale en O(p) *);;

(* In[7]: *)


est_permut [|3; 5; 1; 2; 4; 0|];; (* true ! *)
est_permut [|3; 5; 1; 3; 4; 0|];; (* false ! il manque le 2, il y a deux fois le 3 *);;

(* #### Fonction linéaire

Au lieu de parcourir les valeurs à trouver et de les chercher, on peut parcourir les valeurs directement ! *)

(* In[8]: *)


let est_permut_lineaire (m : mot) : bool =
  let p = Array.length m in
  let tous_vus = Array.make p false in
  Array.iter (fun mi ->
    tous_vus.(mi) <- true
  ) m;
  Array.for_all (fun b -> b) tous_vus
;;
(* Complexité temporelle au pire en O(p) *)
(* Complexité spatiale en O(p) *);;

(* In[9]: *)


est_permut_lineaire [|3; 5; 1; 2; 4; 0|];; (* true ! *)
est_permut_lineaire [|3; 5; 1; 3; 4; 0|];; (* false ! il manque le 2, il y a deux fois le 3 *);;

(* #### Comparaison expérimentale

On va faire quelques mesures empiriques du temps de calcul, entre la fonction linéaire et la fonction quadratique.
Cela illustre aussi l'utilisation de `Sys.time()` pour obtenir le temps système. *)

(* In[10]: *)


let echange t i j =
  let tmp = t.(i) in
  t.(i) <- t.(j);
  t.(j) <- tmp;
;;

(* In[11]: *)


Random.self_init ();;

(* On génère une permutation aléatoire facilement, en faisant plein d'échanges aléatoires (nombre et localisation aléatoires).
**Attention, on essaie pas de generer selon la loi uniforme dans $\Sigma_p$**, c'est beaucoup plus difficile ! *)

(* In[12]: *)


let permutation_aleatoire p =
  let m = Array.init p (fun i -> i) in
  for _ = 1 to Random.int (10*p) do
    echange m (Random.int p) (Random.int p);
  done;
  m
;;

(* In[13]: *)


permutation_aleatoire 10;;

(* In[13]: *)


permutation_aleatoire 10;;

(* In[13]: *)


permutation_aleatoire 10;;

(* Cette petite fonction permet de mesurer le temps machine mis pour calculer une fonction `f ()` : *)

(* In[14]: *)


let timeit f () =
  let debut = Sys.time () in
  let res = f () in
  let fin = Sys.time () in
  Printf.printf "\nTemps pour calculer f() = %f seconde(s)." (fin -. debut);
  res
;;

(* On va s'en servir avec cette fonction, qui test `nombre_test` fois la vérification `f_est_permut` sur une permutation aléatoire de taille `taille`. *)

(* In[17]: *)


let test f_est_permut nombre_test taille () =
  Printf.printf "\nDébut de %i tests de taille %i..." nombre_test taille;
  flush_all ();
  for _ = 1 to nombre_test do
    let m = permutation_aleatoire taille in
    assert (f_est_permut m);
  done
;;

(* - Pour la fonction qui devrait être linéaire, on observe bien un temps de calcul qui croît linéairement avec la taille de l'entrée ($p=1000,2000,4000$ ici). *)

(* In[26]: *)


timeit (test est_permut_lineaire 100 1000) ();;
timeit (test est_permut_lineaire 100 2000) ();;
timeit (test est_permut_lineaire 100 4000) ();;

Printf.printf "\n\n\n";;
flush_all();;

(* - Pour la fonction qui devrait être quadratique, on observe bien un temps de calcul qui croît quadratiquement avec la taille de l'entrée ($p=1000,2000,4000$ ici). *)

(* In[27]: *)


timeit (test est_permut 100 1000) ();;
timeit (test est_permut 100 2000) ();;
timeit (test est_permut 100 4000) ();;

Printf.printf "\n\n\n";;
flush_all();;

(* On peut afficher ces trois valeurs, juste pour mieux les visualiser : *)

(* ![](images/Jonglage_mesure_temps_calcul.png) *)

(* ---
### Construire le mot $\omega$
Cette fonction est toute simple, et est linéaire en temps et en mémoire. *)

(* In[37]: *)


let trouve_omega (m : mot) : mot =
  let p = Array.length m in
  let omega = Array.make p 0 in
  for i=0 to (p-1) do
    omega.(i) <- (i + m.(i)) mod p
  done;
  omega;;

(* In[36]: *)


trouve_omega [|4;4;1|];;
trouve_omega [|5;3;4;0|];;

(* Note : on peut être plus rapide avec une fonction `Array.init` au lieu de `Array.make` : *)

(* In[32]: *)


Array.make;;
Array.init;;

(* In[38]: *)


let trouve_omega (m : mot) : mot =
  let p = Array.length m in
  Array.init p (fun i -> ((i + m.(i)) mod p))
;;

(* In[ ]: *)


trouve_omega [|4;4;1|];;
trouve_omega [|5;3;4;0|];;

(* #### Transformer une chaîne de caractère "5241" en un `mot` *)

(* On a d'abord besoin de convertir un caractère comme `'5'` en un entier `5`.
Cela peut se faire manuellement comme ça : *)

(* In[ ]: *)


let entier (s : char) : int = match s with
  | '0'-> 0
  | '1'-> 1
  | '2'-> 2
  | '3'-> 3
  | '4'-> 4
  | '5'-> 5
  | '6'-> 6
  | '7'-> 7
  | '8'-> 8
  | '9'-> 9
;;

(* In[ ]: *)


let entier (s : char) : int =
  (int_of_char s) - (int_of_char '0')
;;

(* Pour la transformation de la chaîne en un mot, on peut le faire manuellement comme ça : *)

(* In[ ]: *)


let transfo_mot (m : string) : mot =
  let p = String.length m in
  let mot_tableau = Array.make p 0 in
  for i = 0 to (p - 1) do
    mot_tableau.(i) <- entier (m.[i])
  done;
  mot_tableau;;
(* Complexité temporelle et spatiale en O(p) *);;

(* In[ ]: *)


transfo_mot "5241";;

(* Mais on peut aussi accélérer un peu : *)

(* In[ ]: *)


Array.init;;

(* In[ ]: *)


let transfo_mot (m : string) : mot =
  Array.init (String.length m) (fun i -> (entier m.[i]))
(* Complexité temporelle et spatiale en O(p) *);;

(* In[47]: *)


transfo_mot "5241";;

(* ### Test de la permutation *)

(* In[48]: *)


let test_permut (m : string) : bool =
  est_permut (trouve_omega (transfo_mot m));;
(* Complexité temporelle en O(p) *);;

(* In[110]: *)


let test_permut_mot (m : mot) : bool =
  est_permut (trouve_omega m);;
(* Complexité temporelle en O(p) *);;

(* Quelques exemples : *)

(* In[49]: *)


test_permut "433";; (* pas jonglable *);;

(* In[52]: *)


test_permut "432";; (* pas jonglable *);;

(* In[53]: *)


test_permut "441";; (* jonglable *);;

(* In[50]: *)


test_permut "5241";; (* jonglable *);;

(* In[51]: *)


test_permut "9340";; (* jonglable *);;

(* ### Test de la moyenne

Cet autre test n'est pas une condition nécessaire et suffisante, mais il est rapide à implémenter : *)

(* In[67]: *)


let test_moyenne_mot (m : mot) (b : int) : bool =
  let p = Array.length m in
  let s = ref 0 in
  for i = 0 to (p - 1) do
    s:= !s + m.(i)
  done;
  !s / p = b (* on teste l'égalité *)
;;

(* In[68]: *)


test_moyenne_mot [|5;4;3;0|] 3;;

(* On va finir par quelques exemples : *)

(* In[69]: *)


let test_moyenne (m : string) (b : int) : bool =
  test_moyenne_mot (transfo_mot m) b;;

(* In[70]: *)


test_moyenne "433" 3;;

(* In[71]: *)


test_moyenne "443" 3;;

(* In[72]: *)


test_moyenne "432" 3;;

(* In[73]: *)


test_moyenne "5430" 3;;

(* ----
## Bonus ? *)

(* ### Complexité
- Sauf la fonction volontairement écrite pour être quadratique, toutes les fonctions suivantes sont linéaires, c'est à dire qu'elles ont une complexité en temps *et en mémoire* bornée par $\mathcal{O}(|mot|)$. *)

(* ### Autres idées *)

(* La fonction suivante donne la liste des mots de taille `p` commençant par `debut` (dont la somme des coefficients vaut `somme`) concaténée avec `acc`, en temps $\mathcal{O}(m^p)$. *)

(* In[114]: *)


let rec partition_aux balles p debut somme acc =
  let m = balles * p in
  let manque = Array.fold_left (fun c x -> if x = (-1) then c + 1 else c) 0 debut in
  if manque = 1 then
    let t = Array.copy debut in
    t.(p - 1) <- m - somme;
    t :: acc
  else
    let nacc = ref acc in
    for k = m - somme downto 0 do
      let ndebut = Array.copy debut in
      ndebut.(p - manque) <- k;
      nacc := partition_aux balles p ndebut (somme + k) !nacc
    done;
    !nacc
;;

(* In[115]: *)


let partition balles p =
  let debut = Array.make p (-1) in
  partition_aux balles p debut 0 []
;;

(* In[116]: *)


let bp balles p = List.filter test_permut_mot (partition balles p);;

(* Par exemples : *)

(* In[117]: *)


partition 3 3;;

(* In[118]: *)


bp 3 3;;

(* On voit que l'on retrouve les mots donnés en exemples dans le texte, 441, 423, 333 par exemple : *)

(* In[124]: *)


List.mem [|4; 4; 1|] (bp 3 3);;
List.mem [|4; 2; 3|] (bp 3 3);;
List.mem [|3; 3; 3|] (bp 3 3);;

(* Et le mot 433 n'est pas dans la liste calculée : *)

(* In[125]: *)


List.mem [|4; 3; 3|] (bp 3 3);;
;;

(* Pour $m=4$, on commence à avoir beaucoup plus de réponses : *)

(* In[121]: *)


partition 4 4;;

List.length (partition 4 4);;

(* In[123]: *)


bp 4 4;;

List.length (bp 4 4);;

(* ----
## Conclusion *)

(* Voilà pour les deux questions obligatoires de programmation :

- on a décomposé le problème en sous-fonctions,
- on a essayé d'être fainéant, en réutilisant les sous-fonctions,
- on a fait des exemples et *on les garde* dans ce qu'on présente au jury,
- on a testé la fonction exigée sur un exemple venant du texte,
- et on a essayé d'en faire un peu plus (au début).

> Bien-sûr, ce petit notebook ne se prétend pas être une solution optimale, ni exhaustive. *)
