(*
This OCaml script was exported from a Jupyter notebook
using an open-source software (under the MIT License) written by @Naereen
from https://github.com/Naereen/Jupyter-Notebook-OCaml
This software is still in development, please notify me of a bug at
https://github.com/Naereen/Jupyter-Notebook-OCaml/issues/new if you find one
*)

(* # Table of Contents
 <p><div class="lev1 toc-item"><a href="#TP-5---Programmation-pour-la-préparation-à-l'agrégation-maths-option-info" data-toc-modified-id="TP-5---Programmation-pour-la-préparation-à-l'agrégation-maths-option-info-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>TP 5 - Programmation pour la préparation à l'agrégation maths option info</a></div><div class="lev1 toc-item"><a href="#Représentation-des-$\lambda$-termes-en-OCaml" data-toc-modified-id="Représentation-des-$\lambda$-termes-en-OCaml-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Représentation des <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-480-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mi>&amp;#x03BB;</mi></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-3340" role="math" style="width: 0.587em; display: inline-block;"><span style="display: inline-block; position: relative; width: 0.462em; height: 0px; font-size: 125%;"><span style="position: absolute; clip: rect(1.691em, 1000.43em, 2.57em, -1000em); top: -2.462em; left: 0em;"><span class="mrow" id="MathJax-Span-3341"><span class="mi" id="MathJax-Span-3342" style="font-family: STIXMathJax_Main; font-style: italic;">λ</span></span><span style="display: inline-block; width: 0px; height: 2.462em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.058em; border-left: 0px solid; width: 0px; height: 0.944em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>λ</mi></math></span></span><script type="math/tex" id="MathJax-Element-480">\lambda</script>-termes en OCaml</a></div><div class="lev2 toc-item"><a href="#Grammaire" data-toc-modified-id="Grammaire-21"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Grammaire</a></div><div class="lev2 toc-item"><a href="#Ex1.-Ecrire-un-type-Caml-représentant-les-$\lambda$-termes" data-toc-modified-id="Ex1.-Ecrire-un-type-Caml-représentant-les-$\lambda$-termes-22"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Ex1. Ecrire un type Caml représentant les <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-447-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mi>&amp;#x03BB;</mi></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-3152" role="math" style="width: 0.602em; display: inline-block;"><span style="display: inline-block; position: relative; width: 0.469em; height: 0px; font-size: 126%;"><span style="position: absolute; clip: rect(1.703em, 1000.44em, 2.613em, -1000em); top: -2.489em; left: 0em;"><span class="mrow" id="MathJax-Span-3153"><span class="mi" id="MathJax-Span-3154" style="font-family: STIXMathJax_Main; font-style: italic;">λ</span></span><span style="display: inline-block; width: 0px; height: 2.489em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.066em; border-left: 0px solid; width: 0px; height: 0.965em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>λ</mi></math></span></span><script type="math/tex" id="MathJax-Element-447">\lambda</script>-termes</a></div><div class="lev2 toc-item"><a href="#Ex2.-Ecrire-une-fonction-qui-affiche-un-$\lambda$-terme-en-une-chaîne-de-caractère" data-toc-modified-id="Ex2.-Ecrire-une-fonction-qui-affiche-un-$\lambda$-terme-en-une-chaîne-de-caractère-23"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Ex2. Ecrire une fonction qui affiche un <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-452-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mi>&amp;#x03BB;</mi></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-3174" role="math" style="width: 0.602em; display: inline-block;"><span style="display: inline-block; position: relative; width: 0.469em; height: 0px; font-size: 126%;"><span style="position: absolute; clip: rect(1.703em, 1000.44em, 2.613em, -1000em); top: -2.489em; left: 0em;"><span class="mrow" id="MathJax-Span-3175"><span class="mi" id="MathJax-Span-3176" style="font-family: STIXMathJax_Main; font-style: italic;">λ</span></span><span style="display: inline-block; width: 0px; height: 2.489em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.066em; border-left: 0px solid; width: 0px; height: 0.965em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>λ</mi></math></span></span><script type="math/tex" id="MathJax-Element-452">\lambda</script>-terme en une chaîne de caractère</a></div><div class="lev2 toc-item"><a href="#Ex3.-Bonus-:-Ecrire-une-fonction-qui-transforme-un-$\lambda$-terme-en-une-chaîne-représentant-une-fonction-&quot;anonyme&quot;-exécutable-par-Python.-Rappel-:-lambda-x:-...-correspond-à-$\lambda-x.-<...>$" data-toc-modified-id="Ex3.-Bonus-:-Ecrire-une-fonction-qui-transforme-un-$\lambda$-terme-en-une-chaîne-représentant-une-fonction-&quot;anonyme&quot;-exécutable-par-Python.-Rappel-:-lambda-x:-...-correspond-à-$\lambda-x.-<...>$-24"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>Ex3. Bonus : Ecrire une fonction qui transforme un <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-444-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mi>&amp;#x03BB;</mi></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-3136" role="math" style="width: 0.602em; display: inline-block;"><span style="display: inline-block; position: relative; width: 0.469em; height: 0px; font-size: 126%;"><span style="position: absolute; clip: rect(1.703em, 1000.44em, 2.613em, -1000em); top: -2.489em; left: 0em;"><span class="mrow" id="MathJax-Span-3137"><span class="mi" id="MathJax-Span-3138" style="font-family: STIXMathJax_Main; font-style: italic;">λ</span></span><span style="display: inline-block; width: 0px; height: 2.489em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.066em; border-left: 0px solid; width: 0px; height: 0.965em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>λ</mi></math></span></span><script type="math/tex" id="MathJax-Element-444">\lambda</script>-terme en une chaîne représentant une fonction "anonyme" exécutable par Python. Rappel : <code>lambda x: ...</code> correspond à <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-445-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mi>&amp;#x03BB;</mi><mi>x</mi><mo>.</mo><mo>&amp;lt;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>&amp;gt;</mo></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-3139" role="math" style="width: 5.011em; display: inline-block;"><span style="display: inline-block; position: relative; width: 3.968em; height: 0px; font-size: 126%;"><span style="position: absolute; clip: rect(1.883em, 1003.9em, 2.802em, -1000em); top: -2.67em; left: 0em;"><span class="mrow" id="MathJax-Span-3140"><span class="mi" id="MathJax-Span-3141" style="font-family: STIXMathJax_Main; font-style: italic;">λ</span><span class="mi" id="MathJax-Span-3142" style="font-family: STIXMathJax_Main; font-style: italic;">x<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.003em;"></span></span><span class="mo" id="MathJax-Span-3143" style="font-family: STIXMathJax_Main;">.</span><span class="mo" id="MathJax-Span-3144" style="font-family: STIXMathJax_Main; padding-left: 0.188em;">&lt;</span><span class="mo" id="MathJax-Span-3145" style="font-family: STIXMathJax_Main;">.</span><span class="mo" id="MathJax-Span-3146" style="font-family: STIXMathJax_Main; padding-left: 0.188em;">.</span><span class="mo" id="MathJax-Span-3147" style="font-family: STIXMathJax_Main; padding-left: 0.188em;">.</span><span class="mo" id="MathJax-Span-3148" style="font-family: STIXMathJax_Main; padding-left: 0.188em;">&gt;</span></span><span style="display: inline-block; width: 0px; height: 2.67em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.076em; border-left: 0px solid; width: 0px; height: 0.975em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>λ</mi><mi>x</mi><mo>.</mo><mo>&lt;</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>&gt;</mo></math></span></span><script type="math/tex" id="MathJax-Element-445">\lambda x. <...></script></a></div><div class="lev1 toc-item"><a href="#Calculs-?" data-toc-modified-id="Calculs-?-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Calculs ?</a></div><div class="lev1 toc-item"><a href="#Quelques-termes-utiles-?" data-toc-modified-id="Quelques-termes-utiles-?-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Quelques termes utiles ?</a></div><div class="lev2 toc-item"><a href="#Une-valeur-&quot;nulle&quot;" data-toc-modified-id="Une-valeur-&quot;nulle&quot;-41"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Une valeur "nulle"</a></div><div class="lev2 toc-item"><a href="#Composition" data-toc-modified-id="Composition-42"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>Composition</a></div><div class="lev2 toc-item"><a href="#Conditionnelles" data-toc-modified-id="Conditionnelles-43"><span class="toc-item-num">4.3&nbsp;&nbsp;</span>Conditionnelles</a></div><div class="lev2 toc-item"><a href="#Nombres-entiers-en-codage-de-Chuch" data-toc-modified-id="Nombres-entiers-en-codage-de-Chuch-44"><span class="toc-item-num">4.4&nbsp;&nbsp;</span>Nombres entiers en codage de Chuch</a></div><div class="lev2 toc-item"><a href="#Successeur" data-toc-modified-id="Successeur-45"><span class="toc-item-num">4.5&nbsp;&nbsp;</span>Successeur</a></div><div class="lev2 toc-item"><a href="#Addition" data-toc-modified-id="Addition-46"><span class="toc-item-num">4.6&nbsp;&nbsp;</span>Addition</a></div><div class="lev2 toc-item"><a href="#Multiplication" data-toc-modified-id="Multiplication-47"><span class="toc-item-num">4.7&nbsp;&nbsp;</span>Multiplication</a></div><div class="lev2 toc-item"><a href="#Paires" data-toc-modified-id="Paires-48"><span class="toc-item-num">4.8&nbsp;&nbsp;</span>Paires</a></div><div class="lev2 toc-item"><a href="#Bonus-:-prédecesseur" data-toc-modified-id="Bonus-:-prédecesseur-49"><span class="toc-item-num">4.9&nbsp;&nbsp;</span>Bonus : prédecesseur</a></div><div class="lev2 toc-item"><a href="#Listes" data-toc-modified-id="Listes-410"><span class="toc-item-num">4.10&nbsp;&nbsp;</span>Listes</a></div><div class="lev2 toc-item"><a href="#Récursion-$U$" data-toc-modified-id="Récursion-$U$-411"><span class="toc-item-num">4.11&nbsp;&nbsp;</span>Récursion <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-501-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mi>U</mi></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-3518" role="math" style="width: 0.966em; display: inline-block;"><span style="display: inline-block; position: relative; width: 0.758em; height: 0px; font-size: 126%;"><span style="position: absolute; clip: rect(1.728em, 1000.76em, 2.615em, -1000em); top: -2.489em; left: 0em;"><span class="mrow" id="MathJax-Span-3519"><span class="mi" id="MathJax-Span-3520" style="font-family: STIXMathJax_Main; font-style: italic;">U<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.043em;"></span></span></span><span style="display: inline-block; width: 0px; height: 2.489em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.068em; border-left: 0px solid; width: 0px; height: 0.936em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>U</mi></math></span></span><script type="math/tex" id="MathJax-Element-501">U</script></a></div><div class="lev2 toc-item"><a href="#Point-fixe-$Y$" data-toc-modified-id="Point-fixe-$Y$-412"><span class="toc-item-num">4.12&nbsp;&nbsp;</span>Point fixe <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-500-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mi>Y</mi></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-3515" role="math" style="width: 0.784em; display: inline-block;"><span style="display: inline-block; position: relative; width: 0.613em; height: 0px; font-size: 126%;"><span style="position: absolute; clip: rect(1.728em, 1000.61em, 2.597em, -1000em); top: -2.489em; left: 0em;"><span class="mrow" id="MathJax-Span-3516"><span class="mi" id="MathJax-Span-3517" style="font-family: STIXMathJax_Main; font-style: italic;">Y<span style="display: inline-block; overflow: hidden; height: 1px; width: 0.077em;"></span></span></span><span style="display: inline-block; width: 0px; height: 2.489em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.045em; border-left: 0px solid; width: 0px; height: 0.914em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>Y</mi></math></span></span><script type="math/tex" id="MathJax-Element-500">Y</script></a></div><div class="lev2 toc-item"><a href="#Bonus-:-la-factorielle-en-$\lambda$-calcul" data-toc-modified-id="Bonus-:-la-factorielle-en-$\lambda$-calcul-413"><span class="toc-item-num">4.13&nbsp;&nbsp;</span>Bonus : la factorielle en <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-503-Frame" tabindex="0" style="position: relative;" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><mi>&amp;#x03BB;</mi></math>" role="presentation"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-3526" role="math" style="width: 0.602em; display: inline-block;"><span style="display: inline-block; position: relative; width: 0.469em; height: 0px; font-size: 126%;"><span style="position: absolute; clip: rect(1.703em, 1000.44em, 2.613em, -1000em); top: -2.489em; left: 0em;"><span class="mrow" id="MathJax-Span-3527"><span class="mi" id="MathJax-Span-3528" style="font-family: STIXMathJax_Main; font-style: italic;">λ</span></span><span style="display: inline-block; width: 0px; height: 2.489em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.066em; border-left: 0px solid; width: 0px; height: 0.965em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>λ</mi></math></span></span><script type="math/tex" id="MathJax-Element-503">\lambda</script>-calcul</a></div><div class="lev1 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Conclusion</a></div> *)

(* # TP 5 - Programmation pour la préparation à l'agrégation maths option info
TP 5 : Lambda calcul, représentations, calculs et quelques termes pratiques.

- Référence en théorie : [ce poly en français de Jean Goubault-Larrecqu (ENS Cachan)](http://www.lsv.fr/%7Egoubault/Lambda/lambda.pdf) ou le livre "Logique réduction résolution", par René Lalement.
- Pour la pratique : [ce post de blog en anglais](http://matt.might.net/articles/python-church-y-combinator/)
- Pour plus, [cette page wikipédia](https://fr.wikipedia.org/wiki/Lambda-calcul). *)

(* - En OCaml. *)

(* In[1]: *)


let print = Printf.printf;;
Sys.command "ocaml -version";;

(* ----
# Représentation des $\lambda$-termes en OCaml

## Grammaire

Avec une [grammaire BNF](https://fr.wikipedia.org/wiki/Forme_de_Backus-Naur), si `<var>` désigne un nom d'expression valide (on se limitera à des noms en miniscules consistitués des 26 lettres a,b,..,z) :

    <exp> ::= <var>
    | <exp>(<exp>)
    | fun <var> -> <exp>
    | (<exp>) *)

(* ## Ex1. Ecrire un type Caml représentant les $\lambda$-termes *)

(* In[3]: *)


type variable = string;;

type terme =
    | V of variable
    | A of terme * terme
    | F of variable * terme
;;

(* Par exemple, l'identité est le terme $\lambda x. x$. *)

(* In[5]: *)


let identite = F("x", V("x"));;

(* In[7]: *)


let identite_2 = F("y", V("y"));;

(* Les deux termes sont différents mais égaux à $\alpha$-renomage près. *)

(* Un autre exemple est le terme $\Omega = (\lambda x. xx)(\lambda x. xx)$ (qui est le plus petit terme dont l'exécution par $\beta$-réduction ne termine pas - cf [ce poly p7](http://www.lsv.fr/%7Egoubault/Lambda/lambda.pdf) si besoin). *)

(* In[11]: *)


let omega = A(F("x", A(V("x"), V("x"))), F("x", A(V("x"), V("x"))));;

(* ## Ex2. Ecrire une fonction qui affiche un $\lambda$-terme en une chaîne de caractère
C'est très rapide. *)

(* In[9]: *)


let sprintf = Format.sprintf;;

let rec string_of_terme = function
    | V(s) -> s
    | A(u, v) -> sprintf "(%s)(%s)" (string_of_terme u) (string_of_terme v)
    | F(s, u) -> sprintf "λ %s. (%s)" s (string_of_terme u)
;;

(* In[12]: *)


print_endline (string_of_terme identite);;
print_endline (string_of_terme identite_2);;
print_endline (string_of_terme omega);;

(* ## Ex3. Bonus : Ecrire une fonction qui transforme un $\lambda$-terme en une chaîne représentant une fonction "anonyme" exécutable par Python. Rappel : `lambda x: ...` correspond à $\lambda x. <...>$ *)

(* In[13]: *)


let sprintf = Format.sprintf;;

let rec python_of_terme = function
    | V(s) -> s
    | A(u, v) -> sprintf "(%s)(%s)" (python_of_terme u) (python_of_terme v)
    | F(s, u) -> sprintf "lambda %s: (%s)" s (python_of_terme u)
;;

(* In[15]: *)


print_endline (python_of_terme identite);;
print_endline (python_of_terme identite_2);;
print_endline (python_of_terme omega);;

(* On peut ensuite simplement appeler Python sur un terme et vérifier s'il s'exécute ou non. *)

(* In[35]: *)


let execute_python_string (s : string) : int =
    Sys.command (sprintf "python -c 'print(%s)'" s)
;;

(* In[36]: *)


execute_python_string (python_of_terme identite);;

(* On peut vérifier avec Python que ce terme $\Omega$ ne termine pas : *)

(* In[34]: *)


execute_python_string (python_of_terme omega);;

(* ----
# Calculs ? *)

(* ----
# Quelques termes utiles ?

On peut définir des $\lambda$-termes utiles avec notre représentation, et on vérifiera ensuite en les exécutant via Python qu'ils sont corrects. *)

(* ## Une valeur "nulle" *)

(* In[37]: *)


let none = F("x", V("x"));;

(* ## Composition *)

(* In[54]: *)


let compose u v = A(u, v);;

(* ## Conditionnelles
Ce n'est qu'un des encodages possibles. *)

(* In[38]: *)


let si = F("cond", F("v", F("f", A(A(V("cond"), V("v")), V("f")))));;

(* In[39]: *)


print_endline (string_of_terme si);;

(* In[40]: *)


let vrai = F("v", F("f", V("v")));;
let faux = F("v", F("f", V("f")));;

(* In[41]: *)


print_endline (string_of_terme vrai);;
print_endline (string_of_terme faux);;

(* ## Nombres entiers en codage de Chuch

On rappelle que pour $n \in \mathbb{N}$, $[n] = \lambda f. \lambda x. f^n(x)$ est son codage dit codage de Church dans les $\lambda$-termes. *)

(* In[45]: *)


let zero = F("f", F("x", V("x")));;
let un = F("f", F("x", A(V("f"), V("x"))));;

(* In[50]: *)


let terme_of_int (n : int) : terme =
    let rec aux = function
        | 0 -> V("x")
        | n -> A(V("f"), aux (n-1))
    in
    F("f", F("x", (aux n)))
;;

(* In[51]: *)


let deux = terme_of_int 2;;

(* In[53]: *)


print_endline (string_of_terme deux);;
execute_python_string (python_of_terme deux);;

(* On peut faire l'opération inverse, interpréter un entier de Church en Python. *)

(* In[55]: *)


let entier_natif_python = "lambda c: c(lambda x: x+1)(0)";;

(* In[56]: *)


execute_python_string (sprintf "(%s)(%s)" entier_natif_python (python_of_terme deux));;

(* > On est obligé de passer par une astuce, parce que $\lambda x. x + 1$ et $0$ ne sont pas des $\lambda$-termes. *)

(* In[58]: *)


execute_python_string (sprintf "(%s)(%s)" entier_natif_python (python_of_terme (terme_of_int 10)));;

(* Bien sûr, tout ça est très limité ! *)

(* In[66]: *)


execute_python_string (sprintf "(%s)(%s)" entier_natif_python (python_of_terme (terme_of_int 100)));;

(* ## Successeur *)

(* Le successeur s'écrit $\mathrm{succ} = \lambda n. \lambda f. \lambda z. f(n(f)(z))$. *)

(* In[72]: *)


let successeur = F("n", F("f", F("z", A(V("f"), A(A(V("n"), V("f")), V("z"))))));;

(* In[92]: *)


print_endline (string_of_terme successeur);;

(* In[70]: *)


let dix = terme_of_int 10;;
let onze = A(successeur, dix);;

(* A noter que ce terme `onze` ne sera pas le même que celui (plus court) obtenu par `terme_of_int 11` : *)

(* In[73]: *)


let onze2 = terme_of_int 11;;

(* Mais ils s'exécutent de la même façon : *)

(* In[74]: *)


execute_python_string (sprintf "(%s)(%s)" entier_natif_python (python_of_terme dix));;
execute_python_string (sprintf "(%s)(%s)" entier_natif_python (python_of_terme onze));;
execute_python_string (sprintf "(%s)(%s)" entier_natif_python (python_of_terme onze2));;

(* ## Addition *)

(* La somme s'écrit $\mathrm{somme} = \lambda n. \lambda m. \lambda f. \lambda z. n(f)(m(f)(z))$. *)

(* In[90]: *)


let somme = F("n", F("m", F("f", F("z", A((A(V("n"), V("f"))), A((A(V("m"), V("f"))), V("z")) )))));;

(* In[91]: *)


print_endline (string_of_terme somme);;

(* In[87]: *)


let trois = A(A(somme, un), deux);;

(* Comme pour le successeur, ce terme est bien plus compliqué que l'encodage de Church, mais ils s'exécutent de la même manière. *)

(* In[88]: *)


let trois2 = terme_of_int 3;;

(* In[89]: *)


execute_python_string (sprintf "(%s)(%s)" entier_natif_python (python_of_terme trois));;
execute_python_string (sprintf "(%s)(%s)" entier_natif_python (python_of_terme trois2));;

(* ## Multiplication *)

(* La multiplication est $\mathrm{mul} = \lambda n. \lambda m. \lambda f. \lambda z. m(n(f))(z)$. *)

(* In[122]: *)


let mul = F("n", F("m", F("f", F("z", A(A(V("m"), A(V("n"), V("f"))), V("z"))))));;

(* In[123]: *)


let trois = terme_of_int 3 ;;
let six = A(A(mul, trois), deux);;
let six2 = A(A(mul, deux), trois);;

(* Comme pour le successeur, ce terme est bien plus compliqué que l'encodage de Church, mais ils s'exécutent de la même manière. *)

(* In[124]: *)


execute_python_string (sprintf "(%s)(%s)" entier_natif_python (python_of_terme six));;
execute_python_string (sprintf "(%s)(%s)" entier_natif_python (python_of_terme six2));;
execute_python_string (sprintf "(%s)(%s)" entier_natif_python (python_of_terme (terme_of_int 6)));;

(* ## Paires *)

(* La représentation de la paire est simplement $\mathrm{pair} = \lambda a. \lambda b. \lambda f. f(a)(b)$. *)

(* In[127]: *)


let a = V("a") and b = V("b") and f = V("f");;
let pair = F("a", F("b", F("f", A(A(f, a), b))));;

(* Et ensuite les deux extracteurs sont immédiats : $\mathrm{gauche} = \lambda p. p(\lambda a. \lambda b. a)$  et $\mathrm{droite} = \lambda p. p(\lambda a. \lambda b. b)$.
(on retrouve `vrai` et `faux`) *)

(* In[130]: *)


let gauche = F("f", A(f, vrai));;
let droite = F("f", A(f, faux));;

(* In[133]: *)


let exemple_pair = A(A(pair, deux), trois);;

(* On vérifie qu'on peut extraire `[2]` et `[3]` de cette paire `[(2, 3)]` : *)

(* In[134]: *)


execute_python_string (sprintf "(%s)(%s)" entier_natif_python (python_of_terme (A(gauche, exemple_pair))));;
execute_python_string (sprintf "(%s)(%s)" entier_natif_python (python_of_terme (A(droite, exemple_pair))));;

(* ## Bonus : prédecesseur *)

(* > Avec les paires, c'est possible.
> Idée de l'algorithme : en ayant `[n]`, on commence par la paire `[(0, 0)]` et on itère la fonction `fun (a,b) -> (a+1, a)` exactement `n` fois (et ça c'est facile par définition du codage `[n]`, ce qui donne la paire `[(n, n-1)]` et en récupérant la deuxième coordonnée on a `[n-1]`.
> C'est corrigé en Exercice 12 du poly de Jean Goubault-Larrecqu.

On va découper ça en morceau : *)

(* In[137]: *)


let constructeur_pair u v = A(A(pair, u), v);;
let pi1 u = A(gauche, u);;
let pi2 u = A(droite, u);;
let constructeur_succ u = A(successeur, u);;

let pair_00 = constructeur_pair zero zero;;

(* In[139]: *)


let p = V("p");;
let succ_1 = F("p", constructeur_pair (constructeur_succ(pi1(p))) (pi1(p)));;

(* In[140]: *)


let n = V("n");;
let predecesseur = F("n", pi2(A(A(n, succ_1), pair_00)));;

(* In[142]: *)


let cinq = A(predecesseur, (terme_of_int 6));;
let cinq2 = terme_of_int 5;;

(* Comme pour le successeur, ce terme est bien plus compliqué que l'encodage de Church, mais ils s'exécutent de la même manière. *)

(* In[143]: *)


execute_python_string (sprintf "(%s)(%s)" entier_natif_python (python_of_terme cinq));;
execute_python_string (sprintf "(%s)(%s)" entier_natif_python (python_of_terme cinq2));;

(* On vérifie que `pred 0 = 0` : *)

(* In[146]: *)


let zero2 = A(predecesseur, zero);;

(* In[147]: *)


execute_python_string (sprintf "(%s)(%s)" entier_natif_python (python_of_terme zero2));;
execute_python_string (sprintf "(%s)(%s)" entier_natif_python (python_of_terme zero));;

(* ## Listes *)

(* ## Récursion $U$ *)

(* ## Point fixe $Y$ *)

(* ## Bonus : la factorielle en $\lambda$-calcul *)

(* ----
# Conclusion

Fin. À la séance prochaine. Le TP6 traitera de ?? (en février). *)
