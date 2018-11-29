(*
This OCaml script was exported from a Jupyter notebook
using an open-source software (under the MIT License) written by @Naereen
from https://github.com/Naereen/Jupyter-Notebook-OCaml
This software is still in development, please notify me of a bug at
https://github.com/Naereen/Jupyter-Notebook-OCaml/issues/new if you find one
*)

(* # Table of Contents
 <p><div class="lev1 toc-item"><a href="#TP-4---Programmation-pour-la-préparation-à-l'agrégation-maths-option-info" data-toc-modified-id="TP-4---Programmation-pour-la-préparation-à-l'agrégation-maths-option-info-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>TP 4 - Programmation pour la préparation à l'agrégation maths option info</a></div><div class="lev1 toc-item"><a href="#Remise-en-forme-:-listes-associatives" data-toc-modified-id="Remise-en-forme-:-listes-associatives-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Remise en forme : listes associatives</a></div><div class="lev2 toc-item"><a href="#Exercice-1-:-appartient" data-toc-modified-id="Exercice-1-:-appartient-21"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Exercice 1 : <code>appartient</code></a></div><div class="lev2 toc-item"><a href="#Exercice-2-:-insere" data-toc-modified-id="Exercice-2-:-insere-22"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Exercice 2 : <code>insere</code></a></div><div class="lev2 toc-item"><a href="#Exercice-3-:-existe" data-toc-modified-id="Exercice-3-:-existe-23"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Exercice 3 : <code>existe</code></a></div><div class="lev2 toc-item"><a href="#Exercice-4-:-trouve" data-toc-modified-id="Exercice-4-:-trouve-24"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>Exercice 4 : <code>trouve</code></a></div><div class="lev2 toc-item"><a href="#Exercice-5-:-supprime" data-toc-modified-id="Exercice-5-:-supprime-25"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>Exercice 5 : <code>supprime</code></a></div><div class="lev2 toc-item"><a href="#Question-bonus-:-avec-des-tables-d'associations" data-toc-modified-id="Question-bonus-:-avec-des-tables-d'associations-26"><span class="toc-item-num">2.6&nbsp;&nbsp;</span>Question bonus : avec des tables d'associations</a></div><div class="lev1 toc-item"><a href="#Automates-finis-déterministes" data-toc-modified-id="Automates-finis-déterministes-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Automates finis déterministes</a></div><div class="lev2 toc-item"><a href="#Types-de-données" data-toc-modified-id="Types-de-données-31"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Types de données</a></div><div class="lev2 toc-item"><a href="#Affichage-(PAS-DANS-LE-TP)" data-toc-modified-id="Affichage-(PAS-DANS-LE-TP)-32"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Affichage (PAS DANS LE TP)</a></div><div class="lev2 toc-item"><a href="#Reconnaissance-d'un-mot" data-toc-modified-id="Reconnaissance-d'un-mot-33"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>Reconnaissance d'un mot</a></div><div class="lev3 toc-item"><a href="#Récursivement" data-toc-modified-id="Récursivement-331"><span class="toc-item-num">3.3.1&nbsp;&nbsp;</span>Récursivement</a></div><div class="lev3 toc-item"><a href="#Itérativement" data-toc-modified-id="Itérativement-332"><span class="toc-item-num">3.3.2&nbsp;&nbsp;</span>Itérativement</a></div><div class="lev2 toc-item"><a href="#Deux-exemples-d'automates" data-toc-modified-id="Deux-exemples-d'automates-34"><span class="toc-item-num">3.4&nbsp;&nbsp;</span>Deux exemples d'automates</a></div><div class="lev2 toc-item"><a href="#Exemple-de-lectures" data-toc-modified-id="Exemple-de-lectures-35"><span class="toc-item-num">3.5&nbsp;&nbsp;</span>Exemple de lectures</a></div><div class="lev2 toc-item"><a href="#Complétion-(DIFFICILE)" data-toc-modified-id="Complétion-(DIFFICILE)-36"><span class="toc-item-num">3.6&nbsp;&nbsp;</span>Complétion (DIFFICILE)</a></div><div class="lev2 toc-item"><a href="#Complémentaire-(plus-dur)" data-toc-modified-id="Complémentaire-(plus-dur)-37"><span class="toc-item-num">3.7&nbsp;&nbsp;</span>Complémentaire (plus dur)</a></div><div class="lev1 toc-item"><a href="#Expressions-régulières" data-toc-modified-id="Expressions-régulières-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Expressions régulières</a></div><div class="lev2 toc-item"><a href="#Exercice-10-:-regexp" data-toc-modified-id="Exercice-10-:-regexp-41"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Exercice 10 : <code>regexp</code></a></div><div class="lev2 toc-item"><a href="#Exercice-11-:-deux-regexp-pour-les-deux-automates-$A_1$,-$A_2$" data-toc-modified-id="Exercice-11-:-deux-regexp-pour-les-deux-automates-$A_1$,-$A_2$-42"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>Exercice 11 : deux regexp pour les deux automates <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-415-Frame" tabindex="0" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><msub><mi>A</mi><mn>1</mn></msub></math>" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-3024" style="width: 1.182em; display: inline-block;"><span style="display: inline-block; position: relative; width: 1.139em; height: 0px; font-size: 104%;"><span style="position: absolute; clip: rect(1.619em, 1001.14em, 2.668em, -999.998em); top: -2.402em; left: 0em;"><span class="mrow" id="MathJax-Span-3025"><span class="msubsup" id="MathJax-Span-3026"><span style="display: inline-block; position: relative; width: 1.139em; height: 0px;"><span style="position: absolute; clip: rect(3.236em, 1000.7em, 4.154em, -999.998em); top: -4.019em; left: 0em;"><span class="mi" id="MathJax-Span-3027" style="font-family: STIXMathJax_Normal-italic;">𝐴</span><span style="display: inline-block; width: 0px; height: 4.023em;"></span></span><span style="position: absolute; top: -3.888em; left: 0.701em;"><span class="mn" id="MathJax-Span-3028" style="font-size: 70.7%; font-family: STIXMathJax_Main;">1</span><span style="display: inline-block; width: 0px; height: 4.023em;"></span></span></span></span></span><span style="display: inline-block; width: 0px; height: 2.406em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.18em; border-left: 0px solid; width: 0px; height: 0.957em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>1</mn></msub></math></span></span><script type="math/tex" id="MathJax-Element-415">A_1</script>, <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-416-Frame" tabindex="0" data-mathml="<math xmlns=&quot;http://www.w3.org/1998/Math/MathML&quot;><msub><mi>A</mi><mn>2</mn></msub></math>" role="presentation" style="position: relative;"><nobr aria-hidden="true"><span class="math" id="MathJax-Span-3029" style="width: 1.182em; display: inline-block;"><span style="display: inline-block; position: relative; width: 1.139em; height: 0px; font-size: 104%;"><span style="position: absolute; clip: rect(1.619em, 1001.14em, 2.668em, -999.998em); top: -2.402em; left: 0em;"><span class="mrow" id="MathJax-Span-3030"><span class="msubsup" id="MathJax-Span-3031"><span style="display: inline-block; position: relative; width: 1.139em; height: 0px;"><span style="position: absolute; clip: rect(3.236em, 1000.7em, 4.154em, -999.998em); top: -4.019em; left: 0em;"><span class="mi" id="MathJax-Span-3032" style="font-family: STIXMathJax_Normal-italic;">𝐴</span><span style="display: inline-block; width: 0px; height: 4.023em;"></span></span><span style="position: absolute; top: -3.888em; left: 0.701em;"><span class="mn" id="MathJax-Span-3033" style="font-size: 70.7%; font-family: STIXMathJax_Main;">2</span><span style="display: inline-block; width: 0px; height: 4.023em;"></span></span></span></span></span><span style="display: inline-block; width: 0px; height: 2.406em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.18em; border-left: 0px solid; width: 0px; height: 0.957em;"></span></span></nobr><span class="MJX_Assistive_MathML" role="presentation"><math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>A</mi><mn>2</mn></msub></math></span></span><script type="math/tex" id="MathJax-Element-416">A_2</script></a></div><div class="lev2 toc-item"><a href="#Exercice-12-:-to_string" data-toc-modified-id="Exercice-12-:-to_string-43"><span class="toc-item-num">4.3&nbsp;&nbsp;</span>Exercice 12 : <code>to_string</code></a></div><div class="lev2 toc-item"><a href="#Exercice-13-:-est_vide" data-toc-modified-id="Exercice-13-:-est_vide-44"><span class="toc-item-num">4.4&nbsp;&nbsp;</span>Exercice 13 : <code>est_vide</code></a></div><div class="lev2 toc-item"><a href="#Exercice-14-:-est_fini" data-toc-modified-id="Exercice-14-:-est_fini-45"><span class="toc-item-num">4.5&nbsp;&nbsp;</span>Exercice 14 : <code>est_fini</code></a></div><div class="lev2 toc-item"><a href="#Exercice-15-:-pile_ou_face" data-toc-modified-id="Exercice-15-:-pile_ou_face-46"><span class="toc-item-num">4.6&nbsp;&nbsp;</span>Exercice 15 : <code>pile_ou_face</code></a></div><div class="lev2 toc-item"><a href="#Exercice-16-:-mot_aleatoire" data-toc-modified-id="Exercice-16-:-mot_aleatoire-47"><span class="toc-item-num">4.7&nbsp;&nbsp;</span>Exercice 16 : <code>mot_aleatoire</code></a></div><div class="lev1 toc-item"><a href="#Calcul-de-$\Sigma^k-\cap-L(A)$" data-toc-modified-id="Calcul-de-$\Sigma^k-\cap-L(A)$-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Calcul de <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-12-Frame" tabindex="0" style=""><nobr><span class="math" id="MathJax-Span-70" style="width: 4.44em; display: inline-block;"><span style="display: inline-block; position: relative; width: 4.255em; height: 0px; font-size: 104%;"><span style="position: absolute; clip: rect(1.629em, 1004.22em, 2.886em, -999.998em); top: -2.587em; left: 0em;"><span class="mrow" id="MathJax-Span-71"><span class="msubsup" id="MathJax-Span-72"><span style="display: inline-block; position: relative; width: 1.074em; height: 0px;"><span style="position: absolute; clip: rect(3.219em, 1000.59em, 4.107em, -999.998em); top: -3.992em; left: 0em;"><span class="mi" id="MathJax-Span-73" style="font-family: STIXMathJax_Main;">Σ</span><span style="display: inline-block; width: 0px; height: 3.996em;"></span></span><span style="position: absolute; top: -4.362em; left: 0.631em;"><span class="mi" id="MathJax-Span-74" style="font-size: 70.7%; font-family: STIXMathJax_Normal-italic;">𝑘</span><span style="display: inline-block; width: 0px; height: 3.996em;"></span></span></span></span><span class="mo" id="MathJax-Span-75" style="font-family: STIXMathJax_Main; padding-left: 0.261em;">∩</span><span class="mi" id="MathJax-Span-76" style="font-family: STIXMathJax_Normal-italic; padding-left: 0.261em;">𝐿</span><span class="mo" id="MathJax-Span-77" style="font-family: STIXMathJax_Main;">(</span><span class="mi" id="MathJax-Span-78" style="font-family: STIXMathJax_Normal-italic;">𝐴</span><span class="mo" id="MathJax-Span-79" style="font-family: STIXMathJax_Main;">)</span></span><span style="display: inline-block; width: 0px; height: 2.591em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.229em; border-left: 0px solid; width: 0px; height: 1.117em;"></span></span></nobr></span><script type="math/tex" id="MathJax-Element-12">\Sigma^k \cap L(A)</script></a></div><div class="lev2 toc-item"><a href="#Exercice-17-:-produit_cartesien" data-toc-modified-id="Exercice-17-:-produit_cartesien-51"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>Exercice 17 : <code>produit_cartesien</code></a></div><div class="lev2 toc-item"><a href="#Liste-de-tous-les-mots-de-$\Sigma^k$" data-toc-modified-id="Liste-de-tous-les-mots-de-$\Sigma^k$-52"><span class="toc-item-num">5.2&nbsp;&nbsp;</span>Liste de tous les mots de <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax" id="MathJax-Element-13-Frame" tabindex="0" style=""><nobr><span class="math" id="MathJax-Span-80" style="width: 1.139em; display: inline-block;"><span style="display: inline-block; position: relative; width: 1.095em; height: 0px; font-size: 104%;"><span style="position: absolute; clip: rect(1.444em, 1001.1em, 2.537em, -999.998em); top: -2.402em; left: 0em;"><span class="mrow" id="MathJax-Span-81"><span class="msubsup" id="MathJax-Span-82"><span style="display: inline-block; position: relative; width: 1.095em; height: 0px;"><span style="position: absolute; clip: rect(3.236em, 1000.61em, 4.154em, -999.998em); top: -4.019em; left: 0em;"><span class="mi" id="MathJax-Span-83" style="font-family: STIXMathJax_Main;">Σ</span><span style="display: inline-block; width: 0px; height: 4.023em;"></span></span><span style="position: absolute; top: -4.368em; left: 0.614em;"><span class="mi" id="MathJax-Span-84" style="font-size: 70.7%; font-family: STIXMathJax_Normal-italic;">𝑘</span><span style="display: inline-block; width: 0px; height: 4.023em;"></span></span></span></span></span><span style="display: inline-block; width: 0px; height: 2.406em;"></span></span></span><span style="display: inline-block; overflow: hidden; vertical-align: -0.043em; border-left: 0px solid; width: 0px; height: 0.957em;"></span></span></nobr></span><script type="math/tex" id="MathJax-Element-13">\Sigma^k</script></a></div><div class="lev2 toc-item"><a href="#Exercice-19-:-filtre" data-toc-modified-id="Exercice-19-:-filtre-53"><span class="toc-item-num">5.3&nbsp;&nbsp;</span>Exercice 19 : <code>filtre</code></a></div><div class="lev2 toc-item"><a href="#Exercice-20" data-toc-modified-id="Exercice-20-54"><span class="toc-item-num">5.4&nbsp;&nbsp;</span>Exercice 20</a></div><div class="lev1 toc-item"><a href="#Automate-produit-(PLUS-DUR)" data-toc-modified-id="Automate-produit-(PLUS-DUR)-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Automate produit (PLUS DUR)</a></div><div class="lev2 toc-item"><a href="#Exercice-21-:-bijection" data-toc-modified-id="Exercice-21-:-bijection-61"><span class="toc-item-num">6.1&nbsp;&nbsp;</span>Exercice 21 : <code>bijection</code></a></div><div class="lev2 toc-item"><a href="#Exercice-22" data-toc-modified-id="Exercice-22-62"><span class="toc-item-num">6.2&nbsp;&nbsp;</span>Exercice 22</a></div><div class="lev1 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Conclusion</a></div> *)

(* # TP 4 - Programmation pour la préparation à l'agrégation maths option info
TP 4 : Automates et langages réguliers. *)

(* - En OCaml. *)

(* In[32]: *)


let print = Printf.printf;;
Sys.command "ocaml -version";;

(* ----
# Remise en forme : listes associatives

Certaines de ces fonctions sont dans la bibliothèque standard dans le module `List`, avec des fonctions contenant `assoc` dans leur nom : *)

(* In[33]: *)


List.mem;;  (* appartient *);;

(* In[34]: *)


List.assoc;;  (* trouve *);;

(* In[35]: *)


List.mem_assoc;;  (* existe *);;

(* In[36]: *)


List.remove_assoc;;  (* supprime *);;

(* ## Exercice 1 : `appartient`

On propose plusieurs implémentations, toutes similaires mais de complexités différentes.
Je vous laisse trouver les différences de comportement (lesquelles sont tout le temps linéaire, au mieux $\mathcal{O}(1)$ etc). *)

(* In[37]: *)


(* En O(n) pour une liste de taille n (pire cas), en O(1) meilleur cas. *)
let rec appartient (x:'a) (l:'a list) : bool =
      match l with
      | [] -> false
      | y :: _ when x = y -> true
      | _ :: q -> appartient x q
;;

(* In[38]: *)


let liste1 = [ 1; 2; 3 ];;
let couple1 = (1, 2, 3) ;;

(* In[39]: *)


(* En O(n) pour une liste de taille n (pire cas), en O(1) meilleur cas. *)
let rec appartient (x:'a) (l:'a list) : bool =
      match l with
      | [] -> false
      | y :: q -> (x = y) || appartient x q
;;

(* In[40]: *)


(* En O(n) pour une liste de taille n (pire cas), en O(n) meilleur cas. *)
let rec appartient (x:'a) (l:'a list) : bool =
    match l with
    | [] -> false
    | y :: q -> appartient x q || x = y
;;

(* In[41]: *)


let appartient = List.mem;;

(* In[42]: *)


assert (appartient 3 [1;2;3;4;5]) ;;
assert (not (appartient 9 [1;2;3;4;5])) ;;

(* ## Exercice 2 : `insere`

On a envie d'écrire rapidement cela : *)

(* In[43]: *)


let insere (k:'a) (v:'b) (l: ('a*'b) list) : ('a*'b) list =
    (k,v) :: l
;;

(* Mais on peut réfléchir à la sémantique que l'on souhaite donner à cette fonction `insere` : si la clé `k` est déjà présente, doit-on échouer, ou ajouter une deuxième valeur associée à la même clé, ou écraser la valeur déjà associée à `k` ?
Vous pouvez essayer d'implémenter chacun des variantes ! *)

(* On construit un exemple de petite liste associative : *)

(* In[44]: *)


let justiceleague = insere "Superman" "Clark Kent" (insere "Batman" "Bruce Wayne" []);;

(* In[45]: *)


let communaute =
    insere "Aragorn" "rodeur" (
        insere "Gandalf" "magicien" (
            insere "Gimli" "nain" (
                insere "Legolas" "elfe" (
                    insere "Frodon" "hobbit"
                    []
                )
            )
        )
    )
;;

(* > La syntaxe est lourde, en comparaison d'un dictionnaire simple comme en Python...
> ```python
> communaute = { "Aragorn": "rodeur", "Gandalf": "magicien", "Gimli": "nain", "Legolas": "elfe", "Frodon": "hobbit" }
> ``` *)

(* ## Exercice 3 : `existe` *)

(* Première version, "à la main" : *)

(* In[46]: *)


let rec existe (cle : 'a) (l : ('a * 'b) list) : bool =
    match l with
    | [] -> false
    | (k, _) :: _ when cle = k -> true
    | _ :: q -> existe cle q
;;

(* In[47]: *)


assert (existe "Frodon" communaute) ;;
assert (not (existe "Boromir" communaute));;

(* En utilisant la bibliothèque standard : *)

(* In[48]: *)


let existe (cle : 'a) (l : ('a * 'b) list) : bool =
    List.exists (fun (k, _) -> cle = k) l
;;

(* In[49]: *)


assert (existe "Frodon" communaute) ;;
assert (not (existe "Boromir" communaute));;

(* In[50]: *)


let existe = List.mem_assoc;;

(* In[51]: *)


assert (existe "Frodon" communaute) ;;
assert (not (existe "Boromir" communaute));;

(* ## Exercice 4 : `trouve`
On doit déclencher une erreur si la clé n'est pas trouvée. Pour être consistent, on déclenche la même que la fonction de la bibliothèque standard, `Not_found` : *)

(* In[52]: *)


List.assoc "ok" [];;

(* In[53]: *)


let rec trouve (cle : 'a) (l : ('a * 'b) list) : 'b =
    match l with
    | [] -> raise Not_found
    | (k, v) :: _ when cle = k -> v
    | _ :: q -> trouve cle q
;;

(* In[54]: *)


assert ((trouve "Gandalf" communaute) = "magicien");;
assert (try (trouve "Boromir" communaute) = "guerrier" with Not_found -> true);;

(* Avec la bibliothèque standard : *)

(* In[55]: *)


let trouve = List.assoc;;

(* In[56]: *)


assert ((trouve "Gandalf" communaute) = "magicien");;
assert (try (trouve "Boromir" communaute) = "guerrier" with Not_found -> true);;

(* ## Exercice 5 : `supprime` *)

(* On choisit la sémantique suivante : l'exception `Not_found` est levée si la clé n'est pas présente.
On supprime sinon la *première* occurrence de la clé (rappel : `insere` ajoute `(cle, valeur)` même si `cle` est déjà présente). *)

(* In[57]: *)


let rec supprime (cle : 'a) (l : ('a*'b) list) : ('a*'b) list =
    match l with
    | [] -> raise Not_found
    | (k, _) :: q when cle = k -> q
    | p :: q -> p :: supprime cle q
;;

(* Par exemple : *)

(* In[58]: *)


communaute;;

(* In[59]: *)


supprime "Gandalf" [ ];;

(* In[60]: *)


let fin_film_1 = supprime "Gandalf" communaute;;

(* In[61]: *)


let dans100ans = supprime "Frodon" communaute;;

(* In[62]: *)


let debut_film_3 = insere "Gandalf" "magicien blanc" fin_film_1;;

(* ## Question bonus : avec des tables d'associations
La bibliothèque standard fournit le module [`Map`](http://caml.inria.fr/pub/docs/manual-ocaml/libref/Map.html#VALMake).
Il faut au préalable créer le bon module (syntaxe un peu difficile, avec un *foncteur*). *)

(* In[63]: *)


module M = Map.Make ( struct
       type t = int
       let compare = compare
    end);;

let t : string M.t = (M.add 1 "1" (M.add 2 "2" (M.add 3 "3" M.empty)));;

(* In[64]: *)


let _ = M.mem 1 t;;
let _ = M.mem 2 t;;
let _ = M.mem 4 t;;

let _ = M.find 1 t;;
let _ = M.find 2 t;;
let _ = M.find 4 t;;

let _ = M.remove 1 t;;
let _ = M.remove 2 t;;
let _ = M.remove 4 t;;

(* ----
# Automates finis déterministes *)

(* ## Types de données
Les listes d'association sont utilises pour stocker les transitions : pour chaque état, on stocke une liste de règle associant une lettre lue à l'état d'arrivée de la transition. *)

(* In[65]: *)


type ('a, 'b) assoc = ('a * 'b) list;;
type lettre = A | B | C;;

type mot = lettre list;; (* [lettre array] marche aussi bien ! *)
type langage = mot list;;
type etat = int;;

(* In[66]: *)


(* Automate fini déterministe *)
type afd = {
    taille : int;
    initial : etat;
    finals : etat list;
    (* on peut aussi utiliser : *)
    (* transition : (etat, (lettre, etat) assoc) assoc; *) (* comme une fonction q -> a -> q' *)
    (* transition : ((etat, lettre), etat) assoc; *) (* comme une fonction (q, a) -> q' *)
    transition : (lettre, etat) assoc array
};;

(* ## Affichage (PAS DANS LE TP)
On va utiliser le [langage dot](https://graphviz.readthedocs.io/en/stable/manual.html#using-raw-dot) pour afficher facilement des graphes, et donc ici, des automates.
Plutôt que d'utiliser une bibliothèque, on va écrire une fonction `dot` qui transforme un automate fini déterministe a en un fichier `out.dot` qui est ensuite converti en SVG (pour être affiché ici). *)

(* In[67]: *)


let string_of_lettre = function
    | A -> "A"
    | B -> "B"
    | C -> "C"
;;

(* In[68]: *)


let lettre_of_string = function
    | "A" -> A
    | "B" -> B
    | "C" -> C
    | _ -> failwith "Lettre pas dans Sigma"
;;

(* In[69]: *)


let dot (nom : string) (a : afd) : unit =
    let f = open_out nom in
    let print_edge i l = try
        let e = List.assoc l a.transition.(i) in
        Printf.fprintf f "  %d -> %d [label=%s]\n"
        i e (string_of_lettre l)
    with Not_found -> ()
    in
    Printf.fprintf f "digraph g {\n";
    Printf.fprintf f "  node [shape=circle];\n";
    for i = 0 to a.taille-1 do
        print_edge i A;
        print_edge i B;
        print_edge i C
    done;
    Printf.fprintf f "}\n";
    close_out f;
;;

(* ## Reconnaissance d'un mot

Une première approche est d'écrire une fonction récursive qui lit la première lettre du mot `m` et continue.
On peut aussi écrire une fonction itérative qui boucle sur les lettres du mot `m`, et garde un `q : etat ref` pour l'état courant.

On peut utiliser les fonctions `trouve` et `existe` que l'on a écrit plus haut, ou bien utiliser `List.mem_assoc` et `List.assoc` de la bibliothèque standard, comme on veut.

### Récursivement *)

(* In[70]: *)


let lecture (a : afd) (m : mot) : bool =
    let rec lire_lettre (e : etat) (m : mot) : bool =
        match m with
        | l::u ->
            if List.mem_assoc l a.transition.(e) then
                lire_lettre (List.assoc l a.transition.(e)) u
            else false
        | [] ->
            List.mem e a.finals
    in
    lire_lettre a.initial m
;;

(* ### Itérativement *)

(* In[74]: *)


let lecture2 (a : afd) (m : mot) : bool =
    let q = ref (a.initial) in
    List.iter (fun l -> begin
        if List.mem_assoc l a.transition.(!q) then
            q := List.assoc l a.transition.(!q)
        end
    ) m;
    List.mem !q a.finals;
;;

(* ## Deux exemples d'automates *)

(* In[75]: *)


let fin_ba = {
    taille = 3;
    initial = 0;
    finals = [2];
    (*transition = [ (* si ((etat * lettre) * etat) list *)
        ((0, A), 0); ((0, B), 1); ((0, C), 0));
        ((1, A), 2); ((1, B), 1); ((1, C), 0));
        ((2, A), 0); ((2, B), 1); ((2, C), 0));
    ]*)
    (*transition = [ (* si ((etat * (lettre * etat) list) list *)
        (0, [(A, 0); (B, 1); (C, 0)]);
        (1, [(A, 2); (B, 1); (C, 0)]);
        (2, [(A, 0); (B, 1); (C, 0)]);
    ])*)
    transition = [| (* si ((lettre, etat) list) array *)
        [(A, 0); (B, 1); (C, 0)]; (* état 0 *)
        [(A, 2); (B, 1); (C, 0)]; (* état 1 *)
        [(A, 0); (B, 1); (C, 0)]; (* état 1 *)
    |]
};;

(* In[76]: *)


dot "afd__fin_ba.dot" fin_ba;;
Sys.command "ls -larth afd__fin_ba.dot";;
Sys.command "cat afd__fin_ba.dot";;

(* In[77]: *)


Sys.command "dot -Tsvg -o afd__fin_ba.svg afd__fin_ba.dot";;
Sys.command "ls -larth afd__fin_ba.svg";;

(* ![Automate Fini Déterministe - Reconnaissance des mots finissants par BA](afd__fin_ba.svg) *)

(* Autre exemple : *)

(* In[78]: *)


let debut_ab = {
    taille = 3;
    initial = 0;
    finals = [2];
    transition = [|
        [(A, 1)];
        [(B, 2)];
        [(A, 2); (B, 2); (C, 2)]
    |]
};;

(* In[79]: *)


dot "afd__debut_ab.dot" debut_ab;;
Sys.command "ls -larth afd__debut_ab.dot";;
Sys.command "cat afd__debut_ab.dot";;

(* In[80]: *)


Sys.command "dot -Tsvg -o afd__debut_ab.svg afd__debut_ab.dot";;
Sys.command "ls -larth afd__debut_ab.svg";;

(* ![Automate Fini Déterministe - Reconnaissance des mots commençants par AB](afd__debut_ab.svg) *)

(* ## Exemple de lectures
On doit vérifier que ces deux automates reconnaissent bien respectivement les mots terminants par $ba$ et les mots commençants par $ab$. *)

(* In[81]: *)


let _ = lecture  fin_ba [A;B;A];;
let _ = lecture  fin_ba [A;B;A;A];;

let _ = lecture  debut_ab [A;B;A];;
let _ = lecture  debut_ab [B;A;A];;

(* In[82]: *)


let _ = lecture2  fin_ba [A;B;A];;
let _ = lecture2  fin_ba [A;B;A;A];;

let _ = lecture2  debut_ab [A;B;A];;
let _ = lecture2  debut_ab [B;A;A];;

(* ## Complétion (DIFFICILE) *)

(* In[40]: *)


let complete (a:afd) : afd =
    let puit = a.taille in
    let ajoute_arc (l : lettre) (e : etat) (asso : (lettre, etat) assoc) =
        if List.mem_assoc l a.transition.(e)
        then asso
        else (l, puit) :: asso
    in
    let complete_etat e =
        if e < a.taille then
            ajoute_arc A e
            (ajoute_arc B e
                (ajoute_arc C e
                    a.transition.(e)
                )
            )
        else
            [(A, puit); (B, puit); (C, puit)]
    in
    {
        a with
        taille = a.taille + 1;
        transition = Array.init (a.taille + 1) complete_etat
    }
;;

(* In[41]: *)


let com_debut_ab = complete debut_ab;;

(* In[42]: *)


dot "afd__com_debut_ab.dot" com_debut_ab;;
Sys.command "ls -larth afd__com_debut_ab.dot";;
Sys.command "cat afd__com_debut_ab.dot";;

(* In[43]: *)


Sys.command "dot -Tsvg -o afd__com_debut_ab.svg afd__com_debut_ab.dot";;
Sys.command "ls -larth afd__com_debut_ab.svg";;

(* ![Automate Fini Déterministe - Reconnaissance des mots finissants par BA](afd__com_debut_ab.svg) *)

(* ## Complémentaire (plus dur) *)

(* In[52]: *)


let complementaire (a : afd) : afd =
    let rec finals = function
        | n when n < 0 -> []
        | n when n != a.initial -> n :: finals (n-1)
        | n -> finals (n-1)
    in
    let a' = complete a in
    { 
        taille = a.taille +1;
        initial = a.initial;
        finals = finals (a.taille + 1);
        transition = a'.transition
    };;

(* In[53]: *)


let not_debut_ab = complementaire debut_ab;;

(* In[55]: *)


dot "afd__not_debut_ab.dot" not_debut_ab;;
Sys.command "ls -larth afd__not_debut_ab.dot";;
Sys.command "cat afd__not_debut_ab.dot";;

(* In[56]: *)


Sys.command "dot -Tsvg -o afd__not_debut_ab.svg afd__not_debut_ab.dot";;
Sys.command "ls -larth afd__not_debut_ab.svg";;

(* ![Automate Fini Déterministe - Reconnaissance des mots finissants par BA](afd__not_debut_ab.svg) *)

(* ----
# Expressions régulières

On se fixe $\Sigma = \{a, b, c\}$.

On rappelle la grammaire des expressions régulières :

    <exp> ::=
    | ∅
    | ε
    | a (lettre dans Sigma)
    | <exp> + <exp>
    | <exp> . <exp>
    | <exp>* *)

(* ## Exercice 10 : `regexp`

On représente ça le plus simplement possible, avec un type multiple : *)

(* In[84]: *)


type regexp =
  | Vide
  | Epsilon (* On peut faire sans ! *)
  | Lettre of lettre
  | Somme of (regexp * regexp)
  | Concat of (regexp * regexp)
  | Etoile of regexp;;

(* ## Exercice 11 : deux regexp pour les deux automates $A_1$, $A_2$

On peut définir des valeurs intermédiaires pour écrire les exemples plus rapidement : *)

(* In[85]: *)


let a = Lettre A;;
let b = Lettre B;;
let c = Lettre C;;

(* In[86]: *)


let sigma = Somme (Somme (a, b), c);;
let sigmaetoile = Etoile sigma;;

let la1 = Concat (sigmaetoile, Concat (a,b));;
let la2 = Concat (Concat (b, a), sigmaetoile);;

(* Un exemple plus long sera l'expression régulière reconnaissant $\Sigma^7\Sigma^*$ les mots de longueur au moins $7$. *)

(* In[88]: *)


let rec au_moins_longueur = function
    | 0 -> sigmaetoile
    | n -> Concat (sigma, au_moins_longueur (n - 1))
;;

let au_moins7 = au_moins_longueur 7;;

(* ## Exercice 12 : `to_string` *)

(* On peut faire une première version assez simple, qui sera assez moche puisqu'il y aura plein de parenthèses partout : *)

(* In[89]: *)


let rec regexp_to_string = function
    | Vide -> "{}"
    | Epsilon -> "Epsilon"
    | Lettre A -> "A"
    | Lettre B -> "B"
    | Lettre C -> "C"
    | Somme (r1, r2) ->
        "(" ^ (regexp_to_string r1) ^ " + " ^ (regexp_to_string r2) ^ ")"
    | Concat (r1, r2) ->
        "(" ^ (regexp_to_string r1) ^ " . " ^ (regexp_to_string r2) ^ ")"
    | Etoile r -> "(" ^ (regexp_to_string r) ^ ")*"
;;

(* In[64]: *)


let _ = regexp_to_string la1;;
let _ = regexp_to_string la2;;
let _ = regexp_to_string au_moins7;;

(* On peut chercher à faire un peu plus joli.
L'argument `last` garde en mémoire le dernier symbole binaire ou unaire lu, `Somme`, `Concat` ou `Etoile`. Cela permet de ne pas mettre des parenthèses quand on affiche `(A+B+C)` au lieu de `(A+(B+C))` et `(A.B.C)` au lieu de `(A.(B.C))`. *)

(* In[90]: *)


open Printf;;

let rec to_string last = function
    | Vide -> "{}"
    | Epsilon -> "Epsilon"
    | Lettre A -> "A"
    | Lettre B -> "B"
    | Lettre C -> "C"
    | Somme (r1, r2) ->
        if last="+" || last="*" then
            sprintf "%s + %s" (to_string "+" r1) (to_string "+" r2)
        else
            sprintf "(%s + %s)" (to_string "+" r1) (to_string "+" r2)
    | Concat (r1, r2) ->
        if last="." || last="*" then
            sprintf "%s . %s" (to_string "." r1) (to_string "." r2)
        else
            sprintf "(%s . %s)" (to_string "." r1) (to_string "." r2)
    | Etoile r -> sprintf "(%s)*" (to_string "*" r)
;;

let regexp_to_string = to_string "*";;

(* Exemples : *)

(* In[91]: *)


let _ = regexp_to_string Vide;;

(* In[92]: *)


let _ = regexp_to_string Epsilon;;

(* In[93]: *)


let _ = regexp_to_string (Etoile Epsilon);;

(* In[94]: *)


let _ = regexp_to_string la1;;
let _ = regexp_to_string la2;;
let _ = regexp_to_string au_moins7;;

(* ## Exercice 13 : `est_vide`

On teste si le langage généré par l'expression régulière est vide ou non.
Une étoile n'est jamais vide, même $\varepsilon^* = \emptyset^* = \{\varepsilon\}$.  *)

(* In[102]: *)


let rec est_vide = function
    | Vide -> true
    | Epsilon -> false
    | Lettre _ -> false
    | Somme (r1, r2) | Concat (r1, r2) -> est_vide r1 && est_vide r2
    | Etoile _ -> false (* piège ! *)
;;

(* In[103]: *)


let _ = est_vide Vide;;
let _ = est_vide sigma;;
let _ = est_vide la1;;
let _ = est_vide la2;;

(* In[104]: *)


let _ = est_vide (Etoile Vide);;
let _ = est_vide (Etoile Epsilon);;
let _ = est_vide Epsilon;;

(* ## Exercice 14 : `est_fini`

Pour tester si le langage généré est fini, il faut réfléchir un peu plus, parce qu'une étoile $e^*$ est infinie à condition que le langage généré par l'expression $e$ soit non vide **et pas réduit au sigleton $\{\varepsilon\}$**! *)

(* In[106]: *)


let rec est_vide_ou_epsilon = function
    | Vide -> true
    | Epsilon -> true
    | Lettre _ -> false
    | Somme (r1, r2) | Concat (r1, r2) -> est_vide_ou_epsilon r1 || est_vide_ou_epsilon r2
    | Etoile r -> est_vide_ou_epsilon r
;;

(* In[107]: *)


let rec est_fini = function
    | Vide -> true
    | Epsilon -> true
    | Lettre _ -> true
    | Somme (r1, r2) | Concat (r1, r2) -> est_fini r1 && est_fini r2
    | Etoile r -> est_vide_ou_epsilon r
    (* Piège car [Etoile Vide] est fini, [Etoile Epsilon] est fini aussi ! *)
;;

(* In[108]: *)


let _ = est_fini Vide;;
let _ = est_fini Epsilon;;
let _ = est_fini sigma;;
let _ = est_fini la1;;
let _ = est_fini la2;;

(* In[110]: *)


let _ = est_fini (Etoile Vide);;
let _ = est_fini (Etoile Epsilon);;
let _ = est_fini (Etoile (Somme (Epsilon, Epsilon)));;
let _ = est_fini (Etoile (Somme (Vide, Epsilon)));;
let _ = est_fini (Etoile (Somme (Vide, Vide)));;
let _ = est_fini (Etoile (Concat (Epsilon, Epsilon)));;
let _ = est_fini (Etoile (Concat (Vide, Epsilon)));;
let _ = est_fini (Etoile (Concat (Vide, Vide)));;
let _ = est_fini (Etoile sigma);;

(* ## Exercice 15 : `pile_ou_face`

On pense bien à initialiser le générateur de nombres pseudo aléatoires avec [`Random.self_init`](https://caml.inria.fr/pub/docs/manual-ocaml/libref/Random.html#VALself_init). *)

(* In[111]: *)


type piece = Pile | Face;;
Random.self_init ();;

let pile_ou_face () =
    match Random.int 2 with
    | 0 -> Pile
    | 1 -> Face
    | _ -> failwith "impossible"
;;

(* Par exemple : *)

(* In[113]: *)


let _ = Array.init 10 (fun _ -> pile_ou_face ());;

(* In[114]: *)


let _ = Array.init 10 (fun _ -> pile_ou_face ());;

(* In[115]: *)


let _ = Array.init 10 (fun _ -> pile_ou_face ());;

(* ## Exercice 16 : `mot_aleatoire`

Ce n'est pas trop compliqué : l'aléatoire est utilisé dans une somme, pour choisir l'un ou l'autre des expressions avec probabilité $1/2$, et dans une étoile.

En fait, il faut faire attention avec ces deux cas, parce que si l'un des deux morceaux est vide, il faut choisir l'autre (donc `est_fini` sera utile).

A noter que le choix d'implémentation de l'aléatoire dans l'étoile donne une distribution sur la longueur qui est non triviale.
Un bon exercice serait de trouver la distribution de la longueur d'un mot aléatoire généré par la fonction ci-dessous à partir de l'expression régulière $a^*$. (est-ce toujours 2 ? une variable aléatoire suivant une loi de Poisson de paramètre $\lambda=1/2$ ? une loi exponentielle ?). Envoyez moi vos réponsez [par mail](http://perso.crans.org/besson/callme) (ou [ce formulaire](http://perso.crans.org/besson/contact/)). *)

(* In[116]: *)


let rec mot_aleatoire = function
    | Vide -> failwith "langage vide"
    | Epsilon -> [] (* mot vide = liste de lettres vides *)
    | Lettre l -> [l]
    (* si une est vide on doit pas la choisir *)
    | Somme (r1, r2) when est_vide r1 -> mot_aleatoire r2
    | Somme (r1, r2) when est_vide r2 -> mot_aleatoire r1
    | Somme (r1, r2) -> begin
        match pile_ou_face() with
        | Pile -> mot_aleatoire r1
        | Face -> mot_aleatoire r2
    end
    | Concat (r1, r2) ->
        let m1 = mot_aleatoire r1 in
        let m2 = mot_aleatoire r2 in
        m1 @ m2
    (* Etoile (quelque chose qui est vide) devrait marcher et renvoyer vide *)
    | Etoile r when est_vide r -> [] (* mot vide *)
    | Etoile r -> begin
        match pile_ou_face() with
        | Pile -> []
        | Face -> (mot_aleatoire r) @ (mot_aleatoire (Etoile r))
    end
;;

(* On peut faire quelques exemples : *)

(* In[117]: *)


let _ = mot_aleatoire la1;;
let _ = mot_aleatoire la1;;
let _ = mot_aleatoire la1;;
let _ = mot_aleatoire la1;;
let _ = mot_aleatoire la1;;
let _ = mot_aleatoire la1;;
let _ = mot_aleatoire la1;;

(* In[118]: *)


let _ = mot_aleatoire la2;;
let _ = mot_aleatoire la2;;
let _ = mot_aleatoire la2;;
let _ = mot_aleatoire la2;;
let _ = mot_aleatoire la2;;
let _ = mot_aleatoire la2;;
let _ = mot_aleatoire la2;;

(* In[119]: *)


let _ = mot_aleatoire au_moins7;;
let _ = mot_aleatoire au_moins7;;
let _ = mot_aleatoire au_moins7;;
let _ = mot_aleatoire au_moins7;;
let _ = mot_aleatoire au_moins7;;
let _ = mot_aleatoire au_moins7;;
let _ = mot_aleatoire au_moins7;;

(* Ici, on pourrait faire des expériences numériques pour afficher une distribution (empirique) sur la longueur des mots générés pour une certaine expression régulière.

> Note : le mot "généré" s'applique plutôt à une grammaire, on dit généralement "reconnu" par une expression régulière et un automate. Mais cette fonction `mot_aleatoire` permet bien, elle, de générer des mots. *)

(* ----
# Calcul de $\Sigma^k \cap L(A)$ *)

(* ## Exercice 17 : `produit_cartesien`

C'est assez simple à faire, quand on ne s'embête pas à chercher à être très efficace (sur les concaténations).
Par contre, cette implémentation est efficace sur les appels récursifs, elle utilise cette fonction interne `aux` et un accumulateur `acc`.

Notez l'implémentation générique qui permet de transformer comme on veut couple d'éléments des deux listes, de type `'a` et `'b`, en un élément de type `'c`. En pratique, `fun a b -> (a, b)` sera utilisé pour faire le "vrai" produit cartésien. *)

(* In[14]: *)


let produit_cartesien (prod : 'a -> 'b -> 'c) (a : 'a list) (b : 'b list) : 'c list =
    let rec aux acc a =
    match a with
    | [] -> acc
    | va :: qa -> aux ((List.map (fun vb -> prod va vb) b) @ acc) qa
    in
    List.rev (aux [] a)
;;

(* Par exemple : *)

(* In[15]: *)


produit_cartesien (fun a b -> (a, b)) [1; 2] ["ok"; "pas"; "probleme"];;

(* ## Liste de tous les mots de $\Sigma^k$ *)

(* On peut commencer par construire $\Sigma^k$ comme une expression régulière, c'est très simple, mais ça ne sera pas suffisant : *)

(* In[121]: *)


let rec sigma_k (k : int) : regexp =
    match k with
    | n when n < 1 -> Vide
    | 1 -> sigma
    | n -> Concat (sigma, sigma_k (n - 1))
;;

(* In[122]: *)


regexp_to_string (sigma_k 0);;
regexp_to_string (sigma_k 1);;
regexp_to_string (sigma_k 4);;
regexp_to_string (sigma_k 12);;

(* On a besoin de créer une liste de mots, tous les mots dans $\Sigma^k$ (il y en a exactement $|\Sigma|^k$, attention ça grandit vite !) *)

(* In[123]: *)


let alphabet = [A; B; C];; (* Sigma *)

let rec tous_mots_sigma_k (alphabet : lettre list) (k : int) : mot list =
    match k with
    | k when k < 1 -> []
    | 1 -> List.map (fun lettre -> [lettre]) alphabet
    | k -> List.concat (
        List.map (
            fun lettre -> (
                List.map (fun mot -> lettre :: mot)
                (tous_mots_sigma_k alphabet (k - 1))
            )
        )
        alphabet
    )
;;

(* In[124]: *)


let _ = tous_mots_sigma_k alphabet 0;;
let _ = tous_mots_sigma_k alphabet 1;;
let _ = tous_mots_sigma_k alphabet 2;;
let _ = tous_mots_sigma_k alphabet 3;;

(* ## Exercice 19 : `filtre`

C'est très rapide, et c'est exactement la fonction `List.filter` de la bibliothèque standard. Attention, en français c'est filtre (tre) et en anglais (américain) c'est filter (ter). *)

(* In[126]: *)


let rec filtre (pred : 'a -> bool) (l : 'a list) : 'a list =
    match l with
    | [] -> []
    | h :: q when pred h -> h :: (filtre pred q)
    | _ :: q -> filtre pred q
;;

(* In[127]: *)


List.filter;;

(* In[97]: *)


filtre (fun x -> x mod 2 = 0) [1; 2; 3; 4];;

(* In[128]: *)


List.filter (fun x -> x mod 2 = 0) [1; 2; 3; 4];;

(* ## Exercice 20
C'est très facile ! Il suffit d'utiliser la fonction `lecture` comme un prédicat binaire : *)

(* In[98]: *)


lecture;;

(* In[124]: *)


let sigmak_inter_LA (k : int) (a : afd) : mot list =
    let s_k = tous_mots_sigma_k alphabet k in
    filtre (fun mot -> lecture a mot) s_k
;;

(* Exemples pour les deux automates du début tels que $L(A)$ soient $\Sigma^* b a$ et $a b \Sigma^*$.
Il y a $|\Sigma|^2 = 3^2 = 9$ mots dans les deux cas, puisque $2$ lettres parmi les $4$ (pour des mots de $\Sigma^4$) sont déjà fixées. *)

(* In[126]: *)


let _ = sigmak_inter_LA 4 fin_ba;;

let _ = sigmak_inter_LA 4 debut_ab;;

(* # Automate produit (PLUS DUR)
C'est plus dur mais assez guidé. *)

(* ## Exercice 21 : `bijection` *)

(* In[8]: *)


type f_intint_int = (int * int -> int);;
type f_int_intint = (int -> int * int);;

(* In[9]: *)


let bijection (p : int) (q : int) : f_intint_int * f_int_intint =
    let f (n, m) = m + n * q in
    let finv x =
        let m = x mod q and n = x / q in
        assert ((f (n, m)) = x);
        (n, m);
    in
    f, finv
;;

(* Il faut absolument la tester, au moins vérifier que $f^{-1}(f(n, m)) = (n, m)$ et $f(f^{-1}(x)) = x$ pour tout $n,m \in [0,p-1] \times [0,q-1]$ et $x \in [0, pq-1]$. *)

(* In[10]: *)


let p = 2 and q = 4;;
let f, finv = bijection 2 4;;

for n = 0 to p - 1 do
    flush_all();
    for m = 0 to q - 1 do
        Printf.printf "\n%i, %i -> %i" n m (f (n, m)); 
        assert ((n, m) = finv (f (n, m)));
    done;
    flush_all();
done;;

for x = 0 to p*q - 1 do
    flush_all();
    let n, m = finv x in
    Printf.printf "\n%i -> %i, %i" x n m ; 
    assert (x = f (finv x));
done;;

(* ## Exercice 22 *)

(* On utilise `produit_cartesien` pour les états finaux, une simple paire pour l'état initial, et un peu de calcul pour les transitions.
L'idée est d'utiliser cette bijection $f$ pour coder les paires comme des entiers simples (et donc produire un automate représenté par un `afd`). *)

(* In[18]: *)


let alphabet = [A; B; C];;

let automate_produit (a1 : afd) (a2 : afd) =
    let p, i1, f1, d1 = a1.taille, a1.initial, a1.finals, a1.transition in
    let q, i2, f2, d2 = a2.taille, a2.initial, a2.finals, a2.transition in
    (* les bijections *)
    let taille = p * q in
    let f, finv = bijection p q in
    (* état initial *)
    let initial = f (i1, i2) in
    (* peut contenir des doublons, pas grave *)
    let finals = List.map f (produit_cartesien (fun x y -> (x, y)) f1 f2) in
    (* et moins trivial pour les transitions *)
    let transition = Array.init taille (fun ij -> (* pour l'état (i, j) *)
        let i, j = finv ij in
        (* d1.(i) est une liste de (lettre, etat) = (a, q1) pour i --a-> q1 *)
        let transition_i_1 = d1.(i) in
        (* d2.(j) est une liste de (lettre, etat) = (b, q2) pour j --b-> q2 *)
        let transition_j_2 = d2.(j) in
        (* on doit trouver les transitions avec la meme lettre et produire i --a-> f q1 q2 *)
        List.concat (
            List.map (fun lettre ->
                (* pour cette lettre on cherche la transition jointe qui convient, si elle existe *)
                if (List.mem_assoc lettre transition_i_1) && (List.mem_assoc lettre transition_j_2) then
                begin
                    let q1 = List.assoc lettre transition_i_1 in
                    let q2 = List.assoc lettre transition_j_2 in
                    [(lettre, f(q1, q2))]
                end else []
            )
        alphabet)
    ) in
    { taille; initial; finals; transition }
;;

(* Exemple : *)

(* In[11]: *)


debut_ab;;
fin_ba;;

(* In[20]: *)


let test_produit = automate_produit debut_ab fin_ba;;

(* In[21]: *)


dot "afd__test_produit.dot" test_produit;;
Sys.command "ls -larth afd__test_produit.dot";;
Sys.command "cat afd__test_produit.dot";;

(* In[22]: *)


Sys.command "dot -Tsvg -o afd__test_produit.svg afd__test_produit.dot";;
Sys.command "ls -larth afd__test_produit.svg";;

(* ![Automate Fini Déterministe - automate produit](afd__test_produit.svg) *)

(* On peut vérifier qu'en partant de l'état $0$, on doit lire $A$ puis $B$, et ensuite on lit ce qu'on veut, puis on termine par $B$ puis $A$.

L'automate produit reconnait l'intersection des deux langages, donc $L(A \times B) = L(A) \cap L(B) = AB \Sigma^* \cap \Sigma^* BA = AB \Sigma^* BA$. *)

(* ----
# Conclusion

Fin. À la séance prochaine. Le TP5 traitera de lambda calcul (en février). *)
