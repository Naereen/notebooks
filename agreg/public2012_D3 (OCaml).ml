(*
This OCaml script was exported from a Jupyter notebook
using an open-source software (under the MIT License) written by @Naereen
from https://github.com/Naereen/Jupyter-Notebook-OCaml
This software is still in development, please notify me of a bug at
https://github.com/Naereen/Jupyter-Notebook-OCaml/issues/new if you find one
*)

(* # Table des Matières
* [1. Agrégation externe de mathématiques, texte d’exercice diffusé en 2012](#1.-Agrégation-externe-de-mathématiques,-texte-d’exercice-diffusé-en-2012)
	* [1.1 Épreuve de modélisation, option informatique](#1.1-Épreuve-de-modélisation,-option-informatique)
	* [1.2 *Proposition* d'implémentation, en [OCaml](https://ocaml.org/)](#1.2-*Proposition*-d'implémentation,-en-[OCaml]%28https://ocaml.org/%29)
		* [1.2.1 Pour [l'option informatique (D)](http://www.dit.ens-rennes.fr/agregation-option-d/programme-de-l-option-informatique-de-l-agregation-de-mathematiques-48358.kjsp) de l'[agrégation de mathématiques](http://agreg.org/) (en France).](#1.2.1-Pour-[l'option-informatique-%28D%29]%28http://www.dit.ens-rennes.fr/agregation-option-d/programme-de-l-option-informatique-de-l-agregation-de-mathematiques-48358.kjsp%29-de-l'[agrégation-de-mathématiques]%28http://agreg.org/%29-%28en-France%29.)
	* [1.3 Jeux de Nim](#1.3-Jeux-de-Nim)
		* [1.3.1 Représentation des configurations](#1.3.1-Représentation-des-configurations)
		* [1.3.2 Fonction de Sprague-Grundy pour le jeu de Nim](#1.3.2-Fonction-de-Sprague-Grundy-pour-le-jeu-de-Nim)
		* [1.3.3 Déterminer un coup à jouer selon une stratégie gagnante (s'il y en a une)](#1.3.3-Déterminer-un-coup-à-jouer-selon-une-stratégie-gagnante-%28s'il-y-en-a-une%29)
			* [1.3.3.1 Stratégie optimale](#1.3.3.1-Stratégie-optimale)
		* [1.3.4 Stratégie stupide](#1.3.4-Stratégie-stupide)
	* [1.4 Deux exemples, manuellement](#1.4-Deux-exemples,-manuellement)
		* [1.4.1 Premier exemple](#1.4.1-Premier-exemple)
		* [1.4.2 Second exemple](#1.4.2-Second-exemple)
	* [1.5 Un bonus : *simulation du jeu*](#1.5-Un-bonus-:-*simulation-du-jeu*)
		* [1.5.1 Simulation de plusieurs étapes](#1.5.1-Simulation-de-plusieurs-étapes)
		* [1.5.2 Exemple :](#1.5.2-Exemple-:)
		* [1.5.3 Configuration aléatoire](#1.5.3-Configuration-aléatoire)
			* [Le joueur *optimal* gagne souvent...](#Le-joueur-*optimal*-gagne-souvent...)
			* [Le joueur *stupide* peut quand-même gagner ?](#Le-joueur-*stupide*-peut-quand-même-gagner-?)
	* [1.5 Conclusion](#1.5-Conclusion)
	* [1.6 Attention](#1.6-Attention-:)
 *)

(* # 1. Agrégation externe de mathématiques, texte d’exercice diffusé en 2012 *)

(* ## 1.1 Épreuve de modélisation, option informatique *)

(* > - Ce [notebook Jupyter](http://jupyter.org/), utilisant [OCaml](https://ocaml.org/) (via le [kernel IOcaml](https://github.com/andrewray/iocaml/#installation)), est une correction [non officielle](https://github.com/Naereen/notebooks/tree/master/agreg) d'un texte de modélisation pour l'option informatique de l'agrégation externe de mathématiques.
> - Il s'agit du texte [public2012-D3](http://agreg.org/Textes/public2012-D3.pdf).
> - Cette tentative de correction partielle a été rédigée par [Lilian Besson](http://perso.crans.org/besson/) ([sur GitHub ?](https://github.com/Naereen/), [sur Bitbucket ?](https://bitbucket.org/lbesson)), et [est open-source](https://github.com/Naereen/notebooks/blob/master/agreg/public2012_D3%20%28OCaml%29.ipynb).
> - Une autre version, en [Python 3](https://docs.python.org/3/), [est disponible (aussi sur GitHub)](https://github.com/Naereen/notebooks/blob/master/agreg/public2012_D3.ipynb).

> #### Feedbacks?
> - Vous avez trouvé un bug ? → [Signalez-le moi svp !](https://github.com/Naereen/notebooks/issues/new), merci d'avance.
> - Vous avez une question ? → [Posez la svp !](https://github.com/Naereen/ama.fr) [![Demandez moi n'importe quoi !](https://img.shields.io/badge/Demandez%20moi-n'%20importe%20quoi-1abc9c.svg)](https://GitHub.com/Naereen/ama.fr)

---- *)

(* ## 1.2 *Proposition* d'implémentation, en [OCaml](https://ocaml.org/) *)

(* ### 1.2.1 Pour [l'option informatique (D)](http://www.dit.ens-rennes.fr/agregation-option-d/programme-de-l-option-informatique-de-l-agregation-de-mathematiques-48358.kjsp) de l'[agrégation de mathématiques](http://agreg.org/) (en France). *)

(* **Attention** : ce document ne prétend pas être LA correction du texte, mais **un exemple de solution**.

---- *)

(* Initialisation du [générateur de nombres aléatoires](http://caml.inria.fr/pub/docs/manual-ocaml/libref/Random.html#VALinit) et d'une [fonction généralisée](https://ocaml.org/learn/tutorials/format.html) d'affichage. *)

(* In[1]: *)


Random.self_init ();;
let print = Format.printf;;

(* C'est un très bon réflexe d'utiliser `print = Format.printf` ainsi défini, elle permet d'afficher facilement du texte contenant des paramètres. Pour plus de détails, voir [la documentation de Printf.printf](http://caml.inria.fr/pub/docs/manual-ocaml/libref/Printf.html) et [des explications sur `Format`](https://ocaml.org/learn/tutorials/format.html#Printingtostdoutusingprintf).

Il suffit de retenir que `printf` s'utilise comme ça :  *)

(* In[2]: *)


print "Chaine de caractere\n";;

(* In[3]: *)


print "Chaine avec variables : il faut retenir %%i, %%f, %%s et %%c...\n" ;;
print "\n - %%i pour un entier : %i, " 1 ;;
print "\n - %%f pour un flottant : %f, " 3.1415 ;;
print "\n - %%s pour une string : %s, " "OK?" ;;
print "\n - %%c pour un caractère : %c\n" 'c' ;;

(* ## 1.3 Jeux de Nim *)

(* ### 1.3.1 Représentation des configurations *)

(* Pas besoin d'un type de données trop complexe : *)

(* In[4]: *)


type nim = int array;;

(* On va d'abord écrire une fonction toute simple qui affiche une configuration, en mode texte. *)

(* In[5]: *)


let print_nim =
  Array.iteri (fun case total -> begin
    print "\n%i: " case;
    for j = 1 to total do
      print "! ";
    done;
  end);;

(* On peut définir et afficher deux exemples de configuration d'un jeu de Nim, venant de la figure 1. *)

(* In[6]: *)


let a = [| 1; 3; 5 |] ;;
print "\n Configuration (a) de la Figure 1 :";
print_nim a;;

(* In[7]: *)


let b = [| 1; 3; 2 |] ;;
print "\n Configuration (b) de la Figure 1 :";
print_nim b;;

(* ### 1.3.2 Fonction de Sprague-Grundy pour le jeu de Nim *)

(* Elle est donnée par le corollaire 1. en page 6/7 du texte.
On a besoin du **xor** (*"ou exclusif"*, cf [cette page](https://fr.wikipedia.org/wiki/Fonction_OU_exclusif)) **bit à bit**, obtenu en OCaml avec l'opérateur [``lxor``](http://caml.inria.fr/pub/docs/manual-ocaml/libref/Pervasives.html#VAL(lxor)) :

$$ \gamma(\mathrm{Nim}(x_1, \dots, x_k)) := \bigoplus_{i=1}^{k} x_i = x_1 \oplus \dots \oplus x_k. $$ *)

(* Petit rappel sur cette fonction **xor** : *)

(* | Entrée      | |  Entrée  | Sortie  |
| ----- |:--------:| ----- | ------: |
| False | $\oplus$ | False | = False |
| False | $\oplus$ | True  | = True  |
| True  | $\oplus$ | False | = True  |
| True  | $\oplus$ | True  | = False | *)

(* On peut la définir avec l'opérateur infixe : *)

(* In[8]: *)


let somme_nim = ( lxor ) ;;

(* Ou bien plus simplement : *)

(* In[9]: *)


let somme_nim x y = x lxor y ;;

(* Quelques exemples, juste pour vérifier.

- D'abord, les valeurs pour les deux entiers `0` et `1` : *)

(* In[10]: *)


somme_nim 0 0;; (** = 0 *)
somme_nim 0 1;; (** = 1 *)
somme_nim 1 0;; (** = 1 *)
somme_nim 1 1;; (** = 0 *)

(* - Ensuite, d'autres valeurs, juste pour tester : *)

(* In[39]: *)


somme_nim 3 5;;  (** 3 xor 5  =  011_2 xor 101_2  = 111_2  = 6  *)
somme_nim 5 9;;  (** 5 xor 9  = 0101_2 xor 1001_2 = 1100_2 = 12 *)
somme_nim 12 1;; (** 12 xor 1 = 1100_2 xor 0001_2 = 1101_2 = 13 *)
somme_nim 12 2;; (** 12 xor 2 = 1100_2 xor 0010_2 = 1110_2 = 14 *)

(* D'après le corollaire 1., il suffit d'appliquer un **xor** bit à bit à chaque valeur du tableau pour calculer $\gamma$.

En OCaml, on peut faire ça avec une boucle, une fonction récursive, ou plus concisement avec `Array.fold_left`. *)

(* In[12]: *)


Array.fold_left ;;

(* *Rappel :* `fold_left` prend une fonction `f(x,y)` et `x0` calcule
`f( ... f( f( x0, a[0] ), a[1] ), a[n-1] )`.
Ici, pour `f = somme_nim`, il faut donner `x0 = 0` pour que le premier calcul `f(0, a[0]) = a[0]`. *)

(* In[13]: *)


let gamma = Array.fold_left somme_nim 0;;

(* In[14]: *)


print "\nGamma(a) = %i" (gamma(a));;
print "\nGamma(b) = %i" (gamma(b));;

(* ### 1.3.3 Déterminer un coup à jouer selon une stratégie gagnante (s'il y en a une) *)

(* On suit l'algorithme proposé par le texte, qui utilise la fonction $\gamma$ sur la configuration pour savoir s'il y a une stratégie ou non (d'après la proposition 5.), et ensuite si elle existe on doit trouver un coup qui ammene $\gamma$ à 0.

On a d'abord besoin d'une exception pour signaler s'il n'y a pas de stratégie gagnante. *)

(* In[15]: *)


exception Pas_de_Strat_Gagnante;;

(* #### 1.3.3.1 Stratégie optimale
L'algorithme va être assez naïf, depuis une configuration actuelle $c$ :
- si $\gamma(c)$ est $0$, on échoue (`Pas_de_Strat_Gagnante`),
- sinon, on explore toutes les configurations $c'$ atteignables en un coup depuis $c$, et on choisis la première qui amène à $\gamma(c') = 0$. *)

(* In[40]: *)


let next ?(id=0) config =
  let g = gamma config in
  (** La prop. 5 donne directement : si g(s_0) = 0 alors échec. *)
  if g = 0 then raise Pas_de_Strat_Gagnante;
  (** Sinon, on calcul les gamma des fils, et on pointe vers le fils avec un gamma nul. *)
  print "\n\nIl y a une stratégie gagnante :\n";
  (** En pratique, on aurait pas besoin de calculer chaque fils,
      comme on sait que g != 0, et on doit obtenir g' = 0,
      on peut s'arreter au premier coup qui donne g' = 0.
  *)
  let config' = Array.copy config in
  let colonne = ref 0 and
      nb      = ref 1 in
  (** Il suffit d'explorer toutes les configurations accessibles depuis l'état actuel : *)
  for   j = 0 to (Array.length config') - 1 do
    for i = 1 to config'.(j) do
      config'.(j) <- config'.(j) - i;  (** On essaie d'appliquer ce coup. *)
      if (gamma config') = 0 then begin
          (** On a trouvé un coup gagnant, on le stocke. *)
          colonne := j;
          nb := i;
      end;
      config'.(j) <- config'.(j) + i;  (** On annule ce coup. *)
    done;
  done;
  (**  On applique le coup retenu, dernier coup à donner gamma(c') = 0. *)
  print "\nLe joueur courant (numéro %i) doit enlever %i allumette à la %i-ième rangée." id !nb !colonne;
  config'.(!colonne) <- config.(!colonne) - !nb; (** On retire nb allumette sur cette colonne. *)
  (* assert ((gamma config') = 0); (** Si on veut vérifier *)  *)
  config'
;;

(* > *Note :* cette fonction utilise la notation `?(id=0)` dans sa définition pour définir un *argument optionnel avec valeur par défaut*.
> La fonction `next` peut être appelée de deux façons :
>
> - `next a` : sans spécifier `id`, qui vaudra donc `0`,
> - `next ~id:1 a` : en spécifiant `id=1`, qui vaut ici `1`.
>
> Cette astuce n'est pas requise, et c'est un peu de la "frime", inutile de la retenir et de se forcer à s'en servir. Néanmoins, ça peut être utile dans certaines situations. *)

(* ----
On peut tester cette fonction sur nos deux configuration a et b : *)

(* In[41]: *)


try
  print_nim (next ~id:0 a);
with _ -> print "\n\nBlocage durant la simulation 1 (sur a).";;

(* In[42]: *)


try
  print_nim (next ~id:1 b);
with _ -> print "\n\nBlocage durant la simulation 2 (sur b).";;

(* ### 1.3.4. Une stratégie "stupide" : complètement aléatoire *)

(* On a d'abord besoin de deux fonctions utilitaires :
 - `array_filter`, pour filtrer un tableau (comme [`List.filter`](http://caml.inria.fr/pub/docs/manual-ocaml/libref/List.html#VALfilter) mais pour un [`array`](http://caml.inria.fr/pub/docs/manual-ocaml/libref/Array.html)). On fait ça simplement en transformant le tableau en liste, on filtre la liste, puis la liste en tableau. Attention, la taille du tableau n'est *pas* préservée. 
 - et `choose` pour choisir un élément aléatoire (uniforme) dans un tableau. En Python, on aurait [`random.choice`](https://docs.python.org/3/library/random.html#random.choice). On fait ça simplement en tirant un entier `i` aléatoire uniformément parmi `0, ..., n-1` pour `n = Array.length a`, puis en renvoyant `a.(i)`.
 
> (Et oui, la libraire standard de OCaml est [assez limitée](http://sucre.syntaxique.fr/doku.php?id=ocaml#bibliotheque_standard))... *)

(* In[19]: *)


let array_filter pred a =
  Array.of_list (List.filter pred (Array.to_list a));;

let choose a
  = a.(Random.int (Array.length a));;

(* Dans le but de comparer cette fonction `next`, qui implémente une stratégie optimale, on implémente aussi une stratégie complétement aléatoire ("Dummy player").

La stratégie aléatoire fonctionne en trois étapes :
1. trouve les rangées qui ont encore des allumettes (en calculant leurs indices, via `array_filter`, dans le tableau `indices`),
2. choisi une rangée aléatoirement `i` (uniformément),
3. enlève un nombre aléatoire (uniforme) d'allumette entre `1` et `xi`, pour `xi` le nombre d'allumette dans la rangée `i` (i.e., `xi = config.(i)`). *)

(* In[20]: *)


(** Un adversaire stupide qui joue aléatoirement. *)
let random ?(id=1) config =
  print "\nLe joueur courant (numéro %i) joue aléatoirement.\n" id;
  let indices = array_filter ( fun i -> (config.(i) > 0) ) (Array.init (Array.length config) (fun i -> i)) in
  let i = choose indices in
  print "Le joueur (%i) choisi de regarder la %i-ième rangée.\n" id i;
  let nbAEnlever = 1 + Random.int config.(i) in
  print "Le joueur (%i) choisi d'enlever %i allumettes parmi les %i disponibles.\n" id nbAEnlever config.(i);
  let config' = Array.copy config in
  config'.(i) <- config.(i) - nbAEnlever;
  config';
;;

(* ## 1.4 Deux exemples, manuellement *)

(* ### 1.4.1 Premier exemple *)

(* On peut ainsi faire un exemple de début de partie entre deux joueurs "stupides" : *)

(* In[43]: *)


let a0 = a ;; (* Debut du jeu *)
print_nim a0 ;;
let a1 = random ~id:0 a0 ;;
print_nim a1 ;;
let a2 = random ~id:1 a1 ;;
print_nim a2 ;;
let a3 = random ~id:0 a2 ;;
print_nim a3 ;;
(* ... etc *)

(* ### 1.4.2 Second exemple *)

(* On peut aussi faire le même exemple de début de partie entre un joueur "optimal" et un joueur "stupide" : *)

(* In[44]: *)


let c = [| 2; 3; 2 |] ;;
let a0 = c ;; (* Debut du jeu *)
print_nim a0 ;;
let a1 = next ~id:0 a0 ;;
print_nim a1 ;;
let a2 = random ~id:1 a1 ;;
print_nim a2 ;;
let a3 = next ~id:0 a2 ;;
print_nim a3 ;;
(* ... etc *)

(* ## 1.5 Un bonus : *simulation du jeu* *)

(* Maintenant qu'on dispose d'un joueur stupide et d'un joueur optimal, on peut rapidement coder une petite fonction qui les fera s'affronter (même si c'est un peu cruel envers le pauvre joueur "stupide" purement aléatoire !). *)

(* In[23]: *)


exception Perdu of int;;

(* ### 1.5.1 Simulation de plusieurs étapes *)

(* La fonction ``kpas`` va jouer la partie, en partant de la configuration donnée, en commençant par le joueur ``id`` et pour un certain nombre de coups joués (``nbPas``).
Si on ne donne pas ce nombre de coups, le nombre total d'allumette est utilisé (sachant qu'une partie se termine souvent par une exception ``Pas_de_Strat_Gagnante`` lorsque le joueur optimal ne peut plus gagner). *)

(* In[45]: *)


let kpas config id nbPas =
  let id = ref id in
  let config' = ref (Array.copy config) in
  for i = 1 to nbPas do
    print "\nTour numéro %i." i;
    print_nim !config';
    print "\n";
    if (Array.fold_left ( + ) 0 !config') = 0 then raise (Perdu !id);
    begin
      if !id = 0 then (** Le joueur 0 joue bien. *)
        config' := next   ~id:(!id) !config'
      else (** Mais le joueur 1 joue aléatoirement. *)
        config' := random ~id:(!id) !config'
    end;
    id := 1 - !id; (** Juste pour alterner entre 0 et 1 : 0 -> 1, 1 -> 0 *)
  done;
  !config';
;;

(* On peut finalement implementer une jolie fonction qui simule en partant du joueur ``0`` (comme le vrai jeu de Nim) et interprète l'exception renvoyée pour afficher l'issue du jeu : *)

(* In[46]: *)


let simulation config =
  (** On compte le nombre total d'allumettes. *)
  let n = Array.fold_left (fun i j -> i + j + 1) 0 config in
  (** Puis on lance le joueur 0 avec au plus [n] pas. *)
  kpas config 0 n;
;;

(** Dernière fonction, [nim], qui lance [simulation] et rattrape les exceptions. *)
let nim a =
  let resultat =
    (* try ignore (simulation a) with *)
    try ignore(simulation a); None with
      | Perdu i -> (Some i)
      | Pas_de_Strat_Gagnante -> None
  in
  begin
    match resultat with
    | None -> print "Blocage à cause de la stratégie optimisée.\n\n"
    | Some i -> print "\n ==> Le joueur %i a perdu !\n\n" i
  end;
  resultat
;;

(* ### 1.5.2 Exemple : *)

(* In[47]: *)


nim a;;

(* In[48]: *)


nim b;;

(* > Pas très utile jusqu'ici... *)

(* In[49]: *)


nim c;;

(* ### 1.5.3 Générer des configurations aléatoires *)

(* On peut écrire une fonction qui génére une configuration aléatoire, et ensuite lancer notre simulation ``nim()`` dessus, pour voir ce que ça donne sur une configuration plus grande.

La fonction `randomstart(k, p)` va générer une configuration aléatoire :

- avec un nombre de lignes uniforme dans `{1, ..., k}`,
- et un nombre d'allumettes uniforme dans `{1, ..., p}` pour chaque ligne. *)

(* In[29]: *)


let randomstart k p () = Array.init (1 + Random.int k) (fun i -> 1 + Random.int p);;

(* Par exemple : *)

(* In[30]: *)


let c = randomstart 5 8 ();;
print_nim c;; 

(* #### Le joueur *optimal* (d'indice `0`) gagne toujours *)

(* In[31]: *)


let c = randomstart 5 8 () ;;
print "Configuration random c :" ;;
print_nim c;;
nim c;;

(* #### Le joueur *stupide* peut-il quand-même gagner ? *)

(* In[37]: *)


c = randomstart 5 8 () ;;
print "Configuration random c :" ;;
print_nim c ;;
nim c ;;

(* C'est effectivement possible que le joueur `0` (celui qui commence) perde, même en suivant sa stratégie gagnante.
Si le joueur aléatoire `1` a de la chance... *)

(* ---- *)

(* ## 1.5 Conclusion *)

(* C'est tout ce que j'avais eu le temps d'implémenter durant les 4h de préparation (c'est un des textes que j'avais préparé en juin 2014, dans les "vraies" conditions en oraux blanc, à l'ENS Cachan, et le code initial était en OCaml mais je n'ai rien changé à part l'écriture du notebook Jupyter).

Quelques remarques :

- durant l'épreuve de modélisation, vous êtes libres de faire ce que vous voulez, la seule partie requise est dans le paragraphe **Exercice de programmation** (ici, il s'agissait d'implémenter une fonction similaire à ``optimal()`` (cf. plus haut).
- les quelques développements supplémentaires traites ci-dessus (stratégie stupide, configuration aléatoire, simulation de jeu), ne sont qu'une suggestion de ce qui pouvait être fait sur ce texte,
- d'autres suggestions sont possibles, si vous avez des idées, [envoyez-moi vos notebooks !](https://github.com/Naereen/notebooks/pulls).

> *Edit :* j'avais une erreur dans mon calcul de `next`, corrigée le 11/01/17. *)

(* ## 1.6 Attention : *)

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
