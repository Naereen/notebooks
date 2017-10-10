(*
This OCaml script was exported from a Jupyter notebook
using an open-source software (under the MIT License) written by @Naereen
from https://github.com/Naereen/Jupyter-Notebook-OCaml
This software is still in development, please notify me of a bug at
https://github.com/Naereen/Jupyter-Notebook-OCaml/issues/new if you find one
*)

(* # Table of Contents
 <p><div class="lev1 toc-item"><a href="#TP-4---Programmation-pour-la-préparation-à-l'agrégation-maths-option-info" data-toc-modified-id="TP-4---Programmation-pour-la-préparation-à-l'agrégation-maths-option-info-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>TP 4 - Programmation pour la préparation à l'agrégation maths option info</a></div><div class="lev1 toc-item"><a href="#Remise-en-forme-:-listes-associatives" data-toc-modified-id="Remise-en-forme-:-listes-associatives-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Remise en forme : listes associatives</a></div><div class="lev2 toc-item"><a href="#Exercice-1-:-appartient" data-toc-modified-id="Exercice-1-:-appartient-21"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Exercice 1 : <code>appartient</code></a></div><div class="lev2 toc-item"><a href="#Exercice-2-:-insere" data-toc-modified-id="Exercice-2-:-insere-22"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Exercice 2 : <code>insere</code></a></div><div class="lev2 toc-item"><a href="#Exercice-3-:-existe" data-toc-modified-id="Exercice-3-:-existe-23"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Exercice 3 : <code>existe</code></a></div><div class="lev2 toc-item"><a href="#Exercice-4-:-trouve" data-toc-modified-id="Exercice-4-:-trouve-24"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>Exercice 4 : <code>trouve</code></a></div><div class="lev2 toc-item"><a href="#Exercice-5-:-supprime" data-toc-modified-id="Exercice-5-:-supprime-25"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>Exercice 5 : <code>supprime</code></a></div><div class="lev2 toc-item"><a href="#Question-bonus-:-avec-des-tables-d'associations" data-toc-modified-id="Question-bonus-:-avec-des-tables-d'associations-26"><span class="toc-item-num">2.6&nbsp;&nbsp;</span>Question bonus : avec des tables d'associations</a></div><div class="lev1 toc-item"><a href="#Automates-finis-déterministes" data-toc-modified-id="Automates-finis-déterministes-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Automates finis déterministes</a></div><div class="lev2 toc-item"><a href="#Types-de-données" data-toc-modified-id="Types-de-données-31"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Types de données</a></div><div class="lev2 toc-item"><a href="#Affichage" data-toc-modified-id="Affichage-32"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Affichage</a></div><div class="lev2 toc-item"><a href="#Reconnaissance-d'un-mot" data-toc-modified-id="Reconnaissance-d'un-mot-33"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>Reconnaissance d'un mot</a></div><div class="lev2 toc-item"><a href="#Deux-exemples-d'automates" data-toc-modified-id="Deux-exemples-d'automates-34"><span class="toc-item-num">3.4&nbsp;&nbsp;</span>Deux exemples d'automates</a></div><div class="lev2 toc-item"><a href="#Exemple-de-lectures" data-toc-modified-id="Exemple-de-lectures-35"><span class="toc-item-num">3.5&nbsp;&nbsp;</span>Exemple de lectures</a></div><div class="lev2 toc-item"><a href="#Complétion" data-toc-modified-id="Complétion-36"><span class="toc-item-num">3.6&nbsp;&nbsp;</span>Complétion</a></div><div class="lev2 toc-item"><a href="#Complémentaire-(plus-dur)" data-toc-modified-id="Complémentaire-(plus-dur)-37"><span class="toc-item-num">3.7&nbsp;&nbsp;</span>Complémentaire (plus dur)</a></div><div class="lev1 toc-item"><a href="#Expressions-régulières" data-toc-modified-id="Expressions-régulières-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Expressions régulières</a></div><div class="lev2 toc-item"><a href="#Exercuce-10-:-regexp" data-toc-modified-id="Exercuce-10-:-regexp-41"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Exercuce 10 : <code>regexp</code></a></div><div class="lev2 toc-item"><a href="#Exercice-11-:-deux-regexp-pour-les-deux-automates-$A_1$,-$A_2$" data-toc-modified-id="Exercice-11-:-deux-regexp-pour-les-deux-automates-$A_1$,-$A_2$-42"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>Exercice 11 : deux regexp pour les deux automates <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax MathJax_Processing" id="MathJax-Element-5-Frame" tabindex="0"></span><script type="math/tex" id="MathJax-Element-5">A_1</script>, <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax MathJax_Processing" id="MathJax-Element-6-Frame" tabindex="0"></span><script type="math/tex" id="MathJax-Element-6">A_2</script></a></div><div class="lev2 toc-item"><a href="#Exercice-12-:-to_string" data-toc-modified-id="Exercice-12-:-to_string-43"><span class="toc-item-num">4.3&nbsp;&nbsp;</span>Exercice 12 : <code>to_string</code></a></div><div class="lev2 toc-item"><a href="#Exercice-13-:-est_vide" data-toc-modified-id="Exercice-13-:-est_vide-44"><span class="toc-item-num">4.4&nbsp;&nbsp;</span>Exercice 13 : <code>est_vide</code></a></div><div class="lev2 toc-item"><a href="#Exercice-14-:-est_fini" data-toc-modified-id="Exercice-14-:-est_fini-45"><span class="toc-item-num">4.5&nbsp;&nbsp;</span>Exercice 14 : <code>est_fini</code></a></div><div class="lev2 toc-item"><a href="#Exercice-15-:-pile_ou_face" data-toc-modified-id="Exercice-15-:-pile_ou_face-46"><span class="toc-item-num">4.6&nbsp;&nbsp;</span>Exercice 15 : <code>pile_ou_face</code></a></div><div class="lev2 toc-item"><a href="#Exercice-16-:-mot_aleatoire" data-toc-modified-id="Exercice-16-:-mot_aleatoire-47"><span class="toc-item-num">4.7&nbsp;&nbsp;</span>Exercice 16 : <code>mot_aleatoire</code></a></div><div class="lev1 toc-item"><a href="#Calcul-de-$\Sigma^k-\cap-L(A)$" data-toc-modified-id="Calcul-de-$\Sigma^k-\cap-L(A)$-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Calcul de <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax MathJax_Processing" id="MathJax-Element-12-Frame" tabindex="0"></span><script type="math/tex" id="MathJax-Element-12">\Sigma^k \cap L(A)</script></a></div><div class="lev2 toc-item"><a href="#Exercice-17-:-produit_cartesien" data-toc-modified-id="Exercice-17-:-produit_cartesien-51"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>Exercice 17 : <code>produit_cartesien</code></a></div><div class="lev2 toc-item"><a href="#Liste-de-tous-les-mots-de-$\Sigma^k$" data-toc-modified-id="Liste-de-tous-les-mots-de-$\Sigma^k$-52"><span class="toc-item-num">5.2&nbsp;&nbsp;</span>Liste de tous les mots de <span class="MathJax_Preview" style="color: inherit;"></span><span class="MathJax MathJax_Processing" id="MathJax-Element-13-Frame" tabindex="0"></span><script type="math/tex" id="MathJax-Element-13">\Sigma^k</script></a></div><div class="lev2 toc-item"><a href="#Exercice-19-:-filtre" data-toc-modified-id="Exercice-19-:-filtre-53"><span class="toc-item-num">5.3&nbsp;&nbsp;</span>Exercice 19 : <code>filtre</code></a></div><div class="lev2 toc-item"><a href="#Exercice-20" data-toc-modified-id="Exercice-20-54"><span class="toc-item-num">5.4&nbsp;&nbsp;</span>Exercice 20</a></div><div class="lev1 toc-item"><a href="#Automate-produit" data-toc-modified-id="Automate-produit-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Automate produit</a></div><div class="lev2 toc-item"><a href="#Exercice-21-:-bijection" data-toc-modified-id="Exercice-21-:-bijection-61"><span class="toc-item-num">6.1&nbsp;&nbsp;</span>Exercice 21 : <code>bijection</code></a></div><div class="lev2 toc-item"><a href="#Exercice-22" data-toc-modified-id="Exercice-22-62"><span class="toc-item-num">6.2&nbsp;&nbsp;</span>Exercice 22</a></div><div class="lev1 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Conclusion</a></div> *)

(* # TP 4 - Programmation pour la préparation à l'agrégation maths option info
TP 4 : Automates et langages réguliers. *)

(* - En OCaml. *)

(* In[1]: *)


let print = Printf.printf;;
Sys.command "ocaml -version";;

(* ----
# Remise en forme : listes associatives

Certaines de ces fonctions sont dans la bibliothèque standard dans le module `List`, avec des fonctions contenant `assoc` dans leur nom : *)

(* In[11]: *)


List.mem;;  (* appartient *);;

(* In[7]: *)


List.assoc;;  (* trouve *);;

(* In[6]: *)


List.mem_assoc;;  (* existe *);;

(* In[70]: *)


List.remove_assoc;;  (* supprime *);;

(* ## Exercice 1 : `appartient`

On propose plusieurs implémentations, toutes similaires mais de complexités différentes.
Je vous laisse trouver les différences de comportement (lesquelles sont tout le temps linéaire, au mieux $\mathcal{O}(1)$ etc). *)

(* In[8]: *)


let rec appartient (x:'a) (l:'a list) : bool =
      match l with
      | [] -> false
      | y :: _ when x = y -> true
      | _ :: q -> appartient x q
;;

(* In[9]: *)


let rec appartient (x:'a) (l:'a list) : bool =
      match l with
      | [] -> false
      | y :: q -> (x = y) || appartient x q
;;

(* In[10]: *)


let rec appartient (x:'a) (l:'a list) : bool =
    match l with
    | [] -> false
    | y :: q -> appartient x q || x = y
;;

(* In[12]: *)


let appartient = List.mem;;

(* In[14]: *)


assert (appartient 3 [1;2;3;4;5]) ;;
assert (not (appartient 9 [1;2;3;4;5])) ;;

(* ## Exercice 2 : `insere`

On a envie d'écrire rapidement cela : *)

(* In[15]: *)


let insere (k:'a) (v:'b) (l: ('a*'b) list) : ('a*'b) list =
    (k,v) :: l
;;

(* Mais on peut réfléchir à la sémantique que l'on shouaite donner à cette fonction `insere` : si la clé `k` est déjà présente, doit-on échouer, ou ajouter une deuxième valeur associée à la même clé, ou écraser la valeur déjà associée à `k` ?
Vous pouvez essayer d'implémenter chacun des variantes ! *)

(* On construit un exemple de petite liste associative : *)

(* In[20]: *)


let justiceleague = insere "Superman" "Clark Kent" (insere "Batman" "Bruce Wayne" []);;

(* In[24]: *)


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

(* In[52]: *)


let rec existe (cle : 'a) (l : ('a * 'b) list) : bool =
    match l with
    | [] -> false
    | (k, _) :: _ when cle = k -> true
    | _ :: q -> existe cle q
;;

(* In[53]: *)


assert (existe "Frodon" communaute) ;;
assert (not (existe "Boromir" communaute));;

(* En utilisant la bibliothèque standard : *)

(* In[58]: *)


let existe (cle : 'a) (l : ('a * 'b) list) : bool =
    List.exists (fun (k, _) -> cle = k) l
;;

(* In[59]: *)


assert (existe "Frodon" communaute) ;;
assert (not (existe "Boromir" communaute));;

(* In[60]: *)


let existe = List.mem_assoc;;

(* In[61]: *)


assert (existe "Frodon" communaute) ;;
assert (not (existe "Boromir" communaute));;

(* ## Exercice 4 : `trouve`
On doit déclencher une erreur si la clé n'est pas trouvée. Pour être consistent, on déclenche la même que la fonction de la bibliothèque standard : *)

(* In[37]: *)


List.assoc "ok" [];;

(* In[62]: *)


let rec trouve (cle : 'a) (l : ('a * 'b) list) : 'b =
    match l with
    | [] -> raise Not_found
    | (k, v) :: _ when cle = k -> v
    | _ :: q -> trouve cle q
;;

(* In[67]: *)


assert ((trouve "Gandalf" communaute) = "magicien");;
assert (try (trouve "Boromir" communaute) = "guerrier" with Not_found -> true);;

(* Avec la bibliothèque standard : *)

(* In[65]: *)


let trouve = List.assoc;;

(* In[68]: *)


assert ((trouve "Gandalf" communaute) = "magicien");;
assert (try (trouve "Boromir" communaute) = "guerrier" with Not_found -> true);;

(* ## Exercice 5 : `supprime` *)

(* In[71]: *)


let rec supprime (cle : 'a) (l : ('a*'b) list) : ('a*'b) list =
    match l with
    | [] -> raise Not_found
    | (k, _) :: q when cle = k -> q
    | p :: q -> p :: supprime cle q
;;

(* In[72]: *)


let fin_film_1 = supprime "Gandalf" communaute;;

(* In[73]: *)


let debut_film_3 = insere "Gandalf" "magicien blanc" fin_film_1;;

(* ## Question bonus : avec des tables d'associations
La bibliothèque standard fournit le module [`Map`](http://caml.inria.fr/pub/docs/manual-ocaml/libref/Map.html#VALMake).
Il faut au préalable créer le bon module (syntaxe un peu difficile, avec un *foncteur*). *)

(* In[75]: *)


module M = Map.Make ( struct
       type t = int
       let compare = compare
    end);;

let t : string M.t = (M.add 1 "1" (M.add 2 "2" (M.add 3 "3" M.empty)));;

(* In[76]: *)


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

(* In[1]: *)


type ('a, 'b) assoc = ('a * 'b) list;;
type lettre = A | B | C;;
type mot = lettre list;;
type langage = mot list;;
type etat = int;;

(* Automate fini déterministe *)
type afd = {
    taille : int;
    initial : etat;
    finals : etat list;
(*    transition : (etat, (lettre, etat) assoc) assoc;
      transition : ((etat, lettre), etat) assoc; *)
    transition : (lettre, etat) assoc array
};;

(* ## Affichage
On va utiliser le [langage dot](http://graphviz.readthedocs.io/en/stable/manual.html#using-raw-dot) pour afficher facilement des graphes, et donc ici, des automates.
Plutôt que d'utiliser une bibliothèque, on va écrire une fonction `dot` qui transforme un automate fini déterministe a en un fichier `out.dot` qui est ensuite converti en SVG (pour être affiché ici). *)

(* In[2]: *)


let string_of_lettre = function
    | A -> "A"
    | B -> "B"
    | C -> "C"
;;

(* In[3]: *)


let lettre_of_string = function
    | "A" -> A
    | "B" -> B
    | "C" -> C
    | _ -> failwith "Lettre pas dans Sigma"
;;

(* In[4]: *)


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
    (* ignore (Sys.command "dot -Tsvg -o out.pdf out.svg") *)
;;

(* ## Reconnaissance d'un mot *)

(* In[5]: *)


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

(* ## Deux exemples d'automates *)

(* In[6]: *)


let fin_ba = {
    taille = 3;
    initial = 0;
    finals = [2];
    transition = [|
        [(A, 0); (B, 1); (C, 0)];
        [(A, 2); (B, 1); (C, 0)];
        [(A, 0); (B, 1); (C, 0)];
    |]
};;

(* In[27]: *)


dot "afd__fin_ba.dot" fin_ba;;
Sys.command "ls -larth afd__fin_ba.dot";;
Sys.command "cat afd__fin_ba.dot";;

(* In[28]: *)


Sys.command "dot -Tsvg -o afd__fin_ba.svg afd__fin_ba.dot";;
Sys.command "ls -larth afd__fin_ba.svg";;

(* ![Automate Fini Déterministe - Reconnaissance des mots finissants par BA](afd__fin_ba.svg) *)

(* Autre exemple : *)

(* In[7]: *)


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

(* In[33]: *)


dot "afd__debut_ab.dot" debut_ab;;
Sys.command "ls -larth afd__debut_ab.dot";;
Sys.command "cat afd__debut_ab.dot";;

(* In[34]: *)


Sys.command "dot -Tsvg -o afd__fin_ba.svg afd__fin_ba.dot";;
Sys.command "ls -larth afd__fin_ba.svg";;

(* ![Automate Fini Déterministe - Reconnaissance des mots finissants par BA](afd__fin_ba.svg) *)

(* ## Exemple de lectures
On doit vérifier que ces deux automates reconnaissent bien respectivement les mots terminants par $ba$ et les mots commençants par $ab$. *)

(* In[58]: *)


let _ = lecture  fin_ba [A;B;A];;
let _ = lecture  fin_ba [A;B;A;A];;

let _ = lecture  debut_ab [A;B;A];;
let _ = lecture  debut_ab [B;A;A];;

(* ## Complétion *)

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
    | <exp>*

On représente ça le plus simplement possible : *)

(* ## Exercuce 10 : `regexp` *)

(* In[59]: *)


type regexp =
  | Vide
  | Epsilon
  | Lettre of lettre
  | Somme of (regexp * regexp)
  | Concat of (regexp * regexp)
  | Etoile of regexp;;

(* ## Exercice 11 : deux regexp pour les deux automates $A_1$, $A_2$ *)

(* In[61]: *)


let sigma = Somme (Somme (Lettre A, Lettre B), Lettre C);;

let la1 = Concat (Etoile sigma, Concat (Lettre A, Lettre B));;
let la2 = Concat (Concat (Lettre B, Lettre A), Etoile sigma);;

(* Un exemple plus long sera l'expression régulière reconnaissant $\Sigma^7\Sigma^*$ les mots de longueur au moins $7$. *)

(* In[77]: *)


let rec au_moins_longueur = function
    | 0 -> Etoile sigma
    | n -> Concat (sigma, au_moins_longueur (n - 1))
;;

let au_moins7 = au_moins_longueur 7;;

(* ## Exercice 12 : `to_string` *)

(* In[92]: *)


open Printf;;

let rec to_string last = function
    | Vide -> "∅"
    | Epsilon -> "ε"
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

(* In[93]: *)


let _ = regexp_to_string la1;;
let _ = regexp_to_string la2;;
let _ = regexp_to_string au_moins7;;

(* ## Exercice 13 : `est_vide` *)

(* In[64]: *)


let rec est_vide = function
    | Vide -> true
    | Epsilon -> false
    | Lettre _ -> false
    | Somme (r1, r2) -> est_vide r1 && est_vide r2
    | Concat (r1, r2) -> est_vide r1 && est_vide r2
    | Etoile r -> est_vide r
;;

(* In[71]: *)


let _ = est_vide Vide;;
let _ = est_vide sigma;;
let _ = est_vide la1;;
let _ = est_vide la2;;

(* ## Exercice 14 : `est_fini` *)

(* In[69]: *)


let rec est_fini = function
    | Vide -> true
    | Epsilon -> true
    | Lettre _ -> true
    | Somme (r1, r2) -> est_fini r1 && est_fini r2
    | Concat (r1, r2) -> est_fini r1 && est_fini r2
    | Etoile _ -> false
;;

(* In[70]: *)


let _ = est_fini Vide;;
let _ = est_fini sigma;;
let _ = est_fini la1;;
let _ = est_fini la2;;

(* ## Exercice 15 : `pile_ou_face` *)

(* In[67]: *)


type piece = Pile | Face;;
Random.self_init ();;

let pile_ou_face () =
    match Random.int 2 with
    | 0 -> Pile
    | 1 -> Face
    | _ -> failwith "impossible"
;;

(* Par exemple : *)

(* In[72]: *)


let _ = Array.init 10 (fun _ -> pile_ou_face ());;

(* ## Exercice 16 : `mot_aleatoire`

Ce n'est pas trop compliqué : l'aléatoire est utilisé dans une somme, pour choisir l'un ou l'autre des expressions avec probabilité $1/2$, et dans une étoile.

A noter que le choix d'implémentation de l'aléatoire dans l'étoile donne une distribution sur la longueur qui est non triviale.
Un bon exercice serait de trouver la distribution de la longueur d'un mot aléatoire généré par la fonction ci-dessous à partir de l'expression régulière $a^*$. (est-ce toujours 2 ? une variable aléatoire suivant une loi de Poisson de paramètre $\lambda=1/2$ ? une loi exponentielle ?). Envoyez moi vos réponsez [par mail](http://perso.crans.org/besson/callme) (ou [ce formulaire](http://perso.crans.org/besson/contact/)). *)

(* In[73]: *)


let rec mot_aleatoire = function
    | Vide -> failwith "langage vide"
    | Epsilon -> []
    | Lettre l -> [l]
    | Somme (r1, r2) -> begin
        match pile_ou_face() with
        | Pile -> mot_aleatoire r1
        | Face -> mot_aleatoire r2
    end
    | Concat (r1, r2) ->
        let m1 = mot_aleatoire r1 in
        let m2 = mot_aleatoire r2 in
        m1 @ m2
    | Etoile r -> begin
        match pile_ou_face() with
        | Pile -> []
        | Face -> (mot_aleatoire r) @ (mot_aleatoire (Etoile r))
    end
;;

(* In[81]: *)


let _ = mot_aleatoire la1;;
let _ = mot_aleatoire la1;;
let _ = mot_aleatoire la1;;

(* In[82]: *)


let _ = mot_aleatoire la2;;
let _ = mot_aleatoire la2;;
let _ = mot_aleatoire la2;;

(* In[83]: *)


let _ = mot_aleatoire au_moins7;;
let _ = mot_aleatoire au_moins7;;
let _ = mot_aleatoire au_moins7;;

(* ----
# Calcul de $\Sigma^k \cap L(A)$ *)

(* ## Exercice 17 : `produit_cartesien` *)

(* In[14]: *)


let produit_cartesien (prod : 'a -> 'b -> 'c) (a : 'a list) (b : 'b list) : 'c list =
    let rec aux acc a =
    match a with
    | [] -> acc
    | va :: qa -> aux ((List.map (fun vb -> prod va vb) b) @ acc) qa
    in
    List.rev (aux [] a)
;;

(* In[15]: *)


produit_cartesien (fun a b -> (a, b)) [1; 2] ["ok"; "pas"; "probleme"];;

(* ## Liste de tous les mots de $\Sigma^k$ *)

(* On peut commencer par construire $\Sigma^k$ comme une expression régulière, mais ça ne sera pas suffisant : *)

(* In[89]: *)


let rec sigma_k (k : int) : regexp =
    match k with
    | n when n < 1 -> Vide
    | 1 -> sigma
    | n -> Concat (sigma, sigma_k (n - 1))
;;

(* In[94]: *)


regexp_to_string (sigma_k 4);;

(* On a besoin de créer une liste de mots, tous les mots dans $\Sigma^k$ (il y en a exactement $|\Sigma|^k$, attention ça grandit vite !) *)

(* In[121]: *)


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

(* In[122]: *)


let _ = tous_mots_sigma_k alphabet 0;;
let _ = tous_mots_sigma_k alphabet 1;;
let _ = tous_mots_sigma_k alphabet 2;;
let _ = tous_mots_sigma_k alphabet 3;;

(* ## Exercice 19 : `filtre` *)

(* In[96]: *)


let rec filtre (pred : 'a -> bool) (l : 'a list) : 'a list =
    match l with
    | [] -> []
    | h :: q when pred h -> h :: (filtre pred q)
    | _ :: q -> filtre pred q
;;

(* In[97]: *)


filtre (fun x -> x mod 2 = 0) [1; 2; 3; 4];;

(* ## Exercice 20
C'est très facile en utilisant la fonction `lecture` comme un prédicat binaire : *)

(* In[98]: *)


lecture;;

(* In[124]: *)


let sigmak_inter_LA (k : int) (a : afd) : mot list =
    let s_k = tous_mots_sigma_k alphabet k in
    filtre (fun mot -> lecture a mot) s_k
;;

(* Exemples pour les deux automates du début tels que $L(A)$ soient $\Sigma^* b a$ et $a b \Sigma^*$.
Il y a $|\Sigma|^2 = 3^2 = 9$ mots dans les deux cas. *)

(* In[126]: *)


let _ = sigmak_inter_LA 4 fin_ba;;

let _ = sigmak_inter_LA 4 debut_ab;;

(* # Automate produit
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
