(*
This OCaml script was exported from a Jupyter notebook
using an open-source software (under the MIT License) written by @Naereen
from https://github.com/Naereen/Jupyter-Notebook-OCaml
This software is still in development, please notify me of a bug at
https://github.com/Naereen/Jupyter-Notebook-OCaml/issues/new if you find one
*)

(* # Table of Contents
 <p><div class="lev1 toc-item"><a href="#TP-5---Programmation-pour-la-préparation-à-l'agrégation-maths-option-info" data-toc-modified-id="TP-5---Programmation-pour-la-préparation-à-l'agrégation-maths-option-info-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>TP 5 - Programmation pour la préparation à l'agrégation maths option info</a></div><div class="lev1 toc-item"><a href="#Représentation" data-toc-modified-id="Représentation-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Représentation</a></div><div class="lev2 toc-item"><a href="#Trois-représentations" data-toc-modified-id="Trois-représentations-21"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Trois représentations</a></div><div class="lev3 toc-item"><a href="#Matrice-d'adjacence" data-toc-modified-id="Matrice-d'adjacence-211"><span class="toc-item-num">2.1.1&nbsp;&nbsp;</span>Matrice d'adjacence</a></div><div class="lev3 toc-item"><a href="#Listes-d'adjancence" data-toc-modified-id="Listes-d'adjancence-212"><span class="toc-item-num">2.1.2&nbsp;&nbsp;</span>Listes d'adjancence</a></div><div class="lev3 toc-item"><a href="#Listes-d'arêtes" data-toc-modified-id="Listes-d'arêtes-213"><span class="toc-item-num">2.1.3&nbsp;&nbsp;</span>Listes d'arêtes</a></div><div class="lev2 toc-item"><a href="#Nombres-de-sommets-et-d'arcs" data-toc-modified-id="Nombres-de-sommets-et-d'arcs-22"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Nombres de sommets et d'arcs</a></div><div class="lev3 toc-item"><a href="#Matrice-d'adjacence" data-toc-modified-id="Matrice-d'adjacence-221"><span class="toc-item-num">2.2.1&nbsp;&nbsp;</span>Matrice d'adjacence</a></div><div class="lev3 toc-item"><a href="#Listes-d'adjacence" data-toc-modified-id="Listes-d'adjacence-222"><span class="toc-item-num">2.2.2&nbsp;&nbsp;</span>Listes d'adjacence</a></div><div class="lev3 toc-item"><a href="#Listes-d'arêtes" data-toc-modified-id="Listes-d'arêtes-223"><span class="toc-item-num">2.2.3&nbsp;&nbsp;</span>Listes d'arêtes</a></div><div class="lev2 toc-item"><a href="#Graphes-pondérés" data-toc-modified-id="Graphes-pondérés-23"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Graphes pondérés</a></div><div class="lev3 toc-item"><a href="#Matrice-d'adjacence" data-toc-modified-id="Matrice-d'adjacence-231"><span class="toc-item-num">2.3.1&nbsp;&nbsp;</span>Matrice d'adjacence</a></div><div class="lev3 toc-item"><a href="#Listes-d'adjacence" data-toc-modified-id="Listes-d'adjacence-232"><span class="toc-item-num">2.3.2&nbsp;&nbsp;</span>Listes d'adjacence</a></div><div class="lev3 toc-item"><a href="#Listes-d'arêtes" data-toc-modified-id="Listes-d'arêtes-233"><span class="toc-item-num">2.3.3&nbsp;&nbsp;</span>Listes d'arêtes</a></div><div class="lev2 toc-item"><a href="#Graphes-colorés" data-toc-modified-id="Graphes-colorés-24"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>Graphes colorés</a></div><div class="lev3 toc-item"><a href="#Matrice-d'adjacence" data-toc-modified-id="Matrice-d'adjacence-241"><span class="toc-item-num">2.4.1&nbsp;&nbsp;</span>Matrice d'adjacence</a></div><div class="lev3 toc-item"><a href="#Listes-d'adjacence" data-toc-modified-id="Listes-d'adjacence-242"><span class="toc-item-num">2.4.2&nbsp;&nbsp;</span>Listes d'adjacence</a></div><div class="lev3 toc-item"><a href="#Listes-d'arêtes" data-toc-modified-id="Listes-d'arêtes-243"><span class="toc-item-num">2.4.3&nbsp;&nbsp;</span>Listes d'arêtes</a></div><div class="lev2 toc-item"><a href="#Degrés" data-toc-modified-id="Degrés-25"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>Degrés</a></div><div class="lev3 toc-item"><a href="#Matrice-d'adjacence" data-toc-modified-id="Matrice-d'adjacence-251"><span class="toc-item-num">2.5.1&nbsp;&nbsp;</span>Matrice d'adjacence</a></div><div class="lev3 toc-item"><a href="#Listes-d'adjacence" data-toc-modified-id="Listes-d'adjacence-252"><span class="toc-item-num">2.5.2&nbsp;&nbsp;</span>Listes d'adjacence</a></div><div class="lev3 toc-item"><a href="#Listes-d'arêtes" data-toc-modified-id="Listes-d'arêtes-253"><span class="toc-item-num">2.5.3&nbsp;&nbsp;</span>Listes d'arêtes</a></div><div class="lev1 toc-item"><a href="#Parcours-de-graphes" data-toc-modified-id="Parcours-de-graphes-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Parcours de graphes</a></div><div class="lev2 toc-item"><a href="#Parcours-en-profondeur-et-largeur" data-toc-modified-id="Parcours-en-profondeur-et-largeur-31"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Parcours en profondeur et largeur</a></div><div class="lev3 toc-item"><a href="#En-profondeur-:-avec-une-pile-(Stack)" data-toc-modified-id="En-profondeur-:-avec-une-pile-(Stack)-311"><span class="toc-item-num">3.1.1&nbsp;&nbsp;</span>En profondeur : avec une pile (<code>Stack</code>)</a></div><div class="lev3 toc-item"><a href="#En-largeur-:-avec-une-file-(Queue)" data-toc-modified-id="En-largeur-:-avec-une-file-(Queue)-312"><span class="toc-item-num">3.1.2&nbsp;&nbsp;</span>En largeur : avec une file (<code>Queue</code>)</a></div><div class="lev2 toc-item"><a href="#est_connexe" data-toc-modified-id="est_connexe-32"><span class="toc-item-num">3.2&nbsp;&nbsp;</span><code>est_connexe</code></a></div><div class="lev2 toc-item"><a href="#est_arbre" data-toc-modified-id="est_arbre-33"><span class="toc-item-num">3.3&nbsp;&nbsp;</span><code>est_arbre</code></a></div><div class="lev2 toc-item"><a href="#composantes_connexes" data-toc-modified-id="composantes_connexes-34"><span class="toc-item-num">3.4&nbsp;&nbsp;</span><code>composantes_connexes</code></a></div><div class="lev2 toc-item"><a href="#2-coloriage" data-toc-modified-id="2-coloriage-35"><span class="toc-item-num">3.5&nbsp;&nbsp;</span>2-coloriage</a></div><div class="lev1 toc-item"><a href="#Cycles-eulériens" data-toc-modified-id="Cycles-eulériens-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Cycles eulériens</a></div><div class="lev2 toc-item"><a href="#existe_cycle_eulerien" data-toc-modified-id="existe_cycle_eulerien-41"><span class="toc-item-num">4.1&nbsp;&nbsp;</span><code>existe_cycle_eulerien</code></a></div><div class="lev2 toc-item"><a href="#La-suite" data-toc-modified-id="La-suite-42"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>La suite</a></div><div class="lev1 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Conclusion</a></div> *)

(* # TP 5 - Programmation pour la préparation à l'agrégation maths option info
TP 5 : Graphes. *)

(* - En OCaml. *)

(* In[2]: *)


let print = Printf.printf;;
Sys.command "ocaml -version";;

(* In[3]: *)


print_endline;;

(* ----
# Représentation *)

(* On prend un petit exemple de graphe avec lequel on va travailler, pour vérifier que chaque représentation permet bien de le représenter.

Graphe :

    0 - 1
    0 - 2

![TP5__exemple_graphe.svg](TP5__exemple_graphe.svg) *)

(* ## Trois représentations *)

(* In[4]: *)


type sommet = int;;

(* On supposera que les sommets sont toujours numérotés de $0$ à $n-1$. *)

(* Pour des graphes non orientés, on doit stocker deux fois chaque arête : $a \to b$ et $b \to a$.

<span style="color:red;">On suppose aussi que des arêtes de la forme $a - a$ ne sont pas considérées : pas de boucle sur soi-même ! Ca simplifie les codes...</span> *)

(* ### Matrice d'adjacence *)

(* Plutôt que d'utiliser des `bool`, on utilise `0` et `1` pour facilement compter le nombre d'arêtes en sommant le nombre de `1`.
(en plus, ça s'écrit plus vite !) *)

(* In[5]: *)


type graphe_mat = int array array;;

(* In[6]: *)


let g1__mat : graphe_mat = [|
        [| 0; 1; 1 |];  (* 0 -- 1 et 0 -- 2 *)
        [| 1; 0; 0 |];  (* 1 -- 0 *)
        [| 1; 0; 0 |]   (* 2 -- 0 *)
    |]
;;

(* ### Listes d'adjancence *)

(* In[7]: *)


type graphe_adj = (sommet list) array;;

(* In[8]: *)


let g1__adj : graphe_adj = [|
    [1; 2]; (* 0 -- 1 et 0 -- 2 *)
    [0]; (* 1 -- 0 *)
    [0]  (* 2 -- 0 *)
|];;

(* ### Listes d'arêtes *)

(* In[9]: *)


type arete = sommet * sommet;;
type graphe_art = arete list;;

(* In[10]: *)


let g1__art : graphe_art = [
    (0, 1); (0, 2); (* 0 -- 1 et 0 -- 2 *)
    (1, 0); (* 1 -- 0 *)
    (2, 0)  (* 2 -- 0 *)
];;

(* ## Nombres de sommets et d'arcs *)

(* ### Matrice d'adjacence *)

(* Pour `graphe_mat`, `nb_sommets` est en $\mathcal{O}(1)$ et `nb_arcs` est en $\mathcal{O}(n^2)$. *)

(* In[11]: *)


let somme_tableau = Array.fold_left (+) 0;;
let somme_matrice = Array.fold_left (fun x a -> x + (somme_tableau a)) 0;;

(* In[12]: *)


let nb_sommets__mat (g : graphe_mat) : int = Array.length g ;;
nb_sommets__mat g1__mat;;

let nb_arcs__mat (g : graphe_mat) : int = (somme_matrice g) / 2 ;;
nb_arcs__mat g1__mat;;

(* ### Listes d'adjacence *)

(* Pour `graphe_adj`, `nb_sommets` est en $\mathcal{O}(1)$ et `nb_arcs` est en $\mathcal{O}(n)$. *)

(* In[13]: *)


let somme_list = List.fold_left (+) 0;;

(* In[14]: *)


let nb_sommets__adj (g : graphe_adj) : int = Array.length g ;;
nb_sommets__adj g1__adj;;


let nb_arcs__adj (g : graphe_adj) : int = (somme_list (Array.to_list (Array.map List.length g))) / 2 ;;
nb_arcs__adj g1__adj;;

(* ### Listes d'arêtes *)

(* Pour `graphe_art`, `nb_sommets` est en $\mathcal{O}(n)$ et `nb_arcs` est en $\mathcal{O}(1)$. *)

(* In[15]: *)


let max_list = List.fold_left max min_int;;
max_list [1; 3; 4; 19];;

(* In[16]: *)


let max_list_couple l =
    let g, d = List.split l in
    max (max_list g) (max_list d)
;;

(* In[17]: *)


let nb_sommets__art (g : graphe_art) : int = 1 + (max_list_couple g);;
nb_sommets__art g1__art;;

let nb_arcs__art (g : graphe_art) : int = (List.length g) / 2 ;;
nb_arcs__art g1__art;;

(* ## Graphes pondérés *)

(* La définition des types est assez explicite. On utilise le même exemple de graphe :

    0 -[2]- 1
    0 -[3]- 2

![TP5__exemple_graphe2.svg](TP5__exemple_graphe2.svg) *)

(* In[18]: *)


type poids = int;;

(* ### Matrice d'adjacence *)

(* `None` indique une absence d'arête, `Some x` une arête pondérée par `x`.
Aucune raison qu'on ne puisse pas pondérer par `0`, donc utiliser seulement `0` pour indiquer une absence d'arête ne marchera pas. *)

(* In[19]: *)


type graphe_mat_pond = (poids option) array array;;

(* In[20]: *)


let g1__mat_pond : graphe_mat_pond = [|
        [| None; Some 2; Some 3 |];  (* 0 -[2]- 1 et 0 -[3]- 2 *)
        [| Some 2; None; None |];  (* 1 -[2]- 0 *)
        [| Some 3; None; None |]   (* 2 -[3]- 0 *)
    |]
;;

(* ### Listes d'adjacence *)

(* C'est plus facile : *)

(* In[21]: *)


type graphe_adj_pond = ((sommet * poids) list) array;;

(* In[22]: *)


let g1__adj_pond : graphe_adj_pond = [|
    [(1, 2); (2, 3)]; (* 0 -[2]- 1 et 0 -[3]- 2 *)
    [(0, 2)]; (* 1 -[2]- 0 *)
    [(0, 3)]  (* 2 -[3]- 0 *)
|];;

(* ### Listes d'arêtes *)

(* C'est très facile : *)

(* In[23]: *)


type arete_pond = sommet * poids * sommet;;
type graphe_art_pond = arete_pond list;;

(* In[24]: *)


let g1__art_pond : graphe_art_pond = [
    (0, 2, 1); (0, 3, 2); (* 0 -[2]- 1 et 0 -[3]- 2 *)
    (1, 2, 0); (* 1 -[2]- 0 *)
    (2, 3, 0)  (* 2 -[3]- 0 *)
];;

(* ## Graphes colorés *)

(* La définition des types est assez explicite. On utilise le même exemple de graphe :

    0 [rouge] -- 1 [bleu]
    0 [rouge] -- 2 [vert]

![TP5__exemple_graphe3.svg](TP5__exemple_graphe3.svg) *)

(* In[25]: *)


type couleur = int;;
let rouge : couleur = 1 and bleu : couleur = 2 and vert : couleur = 3;;

(* ### Matrice d'adjacence *)

(* C'est moins facile ! On est obligé d'ajouter une structure qui contient la liste des couleurs séparément... Et donc ce n'est pas très intéressant... *)

(* In[26]: *)


type graphe_mat_color = { mat : int array array; couleurs : couleur array } ;;

(* In[27]: *)


let g1__mat_color : graphe_mat_color = { mat = [|
        [| 0; 1; 1 |];  (* 0 -- 1 et 0 -- 2 *)
        [| 1; 0; 0 |];  (* 1 -- 0 *)
        [| 1; 0; 0 |]   (* 2 -- 0 *)
    |];
    couleurs = [| rouge; bleu; vert |]
};;

(* ### Listes d'adjacence *)

(* In[28]: *)


type graphe_adj_color = { adj : (sommet list) array; couleurs : couleur array } ;;

(* In[29]: *)


let g1__adj_color : graphe_adj_color = { adj = [|
        [1; 2]; (* 0 -- 1 et 0 -- 2 *)
        [0]; (* 1 -- 0 *)
        [0]  (* 2 -- 0 *)
    |];
    couleurs = [| rouge; bleu; vert |]
};;

(* ### Listes d'arêtes *)

(* In[30]: *)


type graphe_art_color = { art : arete list; couleurs : couleur array } ;;

(* In[31]: *)


let g1__art_color : graphe_art_color = { art = [
        (0, 1); (0, 2); (* 0 -- 1 et 0 -- 2 *)
        (1, 0); (* 1 -- 0 *)
        (2, 0)  (* 2 -- 0 *)
    ];
    couleurs = [| rouge; bleu; vert |]
};;

(* ## Degrés *)

(* ### Matrice d'adjacence *)

(* Pour `graphe_mat`, `degres` est en $\mathcal{O}(n^2)$. *)

(* In[32]: *)


let degres__mat (g : graphe_mat) : int array = Array.map somme_tableau g ;;
degres__mat g1__mat;;

(* ### Listes d'adjacence *)

(* Pour `graphe_adj`, `degres` est en $\mathcal{O}(n)$. *)

(* In[33]: *)


let degres__adj (g : graphe_adj) : int array = Array.map List.length g ;;
degres__adj g1__adj;;

(* ### Listes d'arêtes *)

(* Pour `graphe_art`, `degres` est en $\mathcal{O}(n^2)$. *)

(* In[34]: *)


g1__art;;

(* In[35]: *)


let degres__art (g : graphe_art) : int array =
    let n = nb_sommets__art g in
    Array.init n (fun i ->
        List.length (List.filter (fun (a, _) -> a = i) g)
    )
;;
degres__art g1__art;;

(* ----
# Parcours de graphes *)

(* Pour la suite, on choisit les représentations qui sont les plus adaptées aux algorithmes qu'on doit écrire. *)

(* ## Parcours en profondeur et largeur *)

(* Pour les deux parcours, l'implémentation sous forme de listes d'adjacence fonctionne très bien.

Les deux algorithmes sont très similaires, et sont en $\mathcal{O}(|A|)$ ($|A|$ étant le nombre d'arêtes, si $G=(S,A)$), si on utilise une structure de pile/file qui est efficace (insertion, suppression en $\mathcal{O}(1)$).

On va être un peu fainéant, et ces deux parcours *ne renverront rien*, ils vont juste afficher les sommets dans l'ordre dans lesquels on les voit.
On pourrait utiliser une référence d'une liste (`list ref`) pour ajouter les sommets un à un. *)

(* ### En profondeur : avec une pile (`Stack`) *)

(* In[36]: *)


let profondeur_iter (g : graphe_adj) (debut : sommet) : unit =
    let vu = Array.make (nb_sommets__adj g) false in
    let pile = Stack.create () in
    Stack.push debut pile;
    vu.(debut) <- true;
    while not (Stack.is_empty pile) do
        let i = Stack.pop pile in
        Printf.printf "visite(%d)\n" i;
        flush_all();
        (* Complexité O(deg(i)) pour le sommet i *)
        List.iter (fun j -> if not vu.(j) then begin
            Stack.push j pile;
            vu.(j) <- true
            end)
        g.(i)
    done
    (* donc en tout, complexité en Sigma_i O(deg(i)) = |E| *)
;;

(* On remarque qu'on parcourt les sommets de "la droite vers la gauche" dans cet exemple. *)

(* In[37]: *)


g1__adj;;

(* In[38]: *)


profondeur_iter g1__adj 0;;

(* ### En largeur : avec une file (`Queue`) *)

(* C'est magique, le code est *exactement* le même, avec `Queue` en lieu et place de `Stack`.

> On a déjà vu tout ça, vous devriez être capable de le réécrire rapidement ! *)

(* In[39]: *)


let largeur_iter (g : graphe_adj) (debut : sommet) : unit =
    let vu = Array.make (nb_sommets__adj g) false in
    let file = Queue.create () in
    Queue.push debut file;
    vu.(debut) <- true;
    while not (Queue.is_empty file) do
        let i = Queue.pop file in
        Printf.printf "visite(%d)\n" i;
        flush_all();
        List.iter (fun j -> if not vu.(j) then begin
            Queue.push j file;
            vu.(j) <- true
            end)
        g.(i)
    done
;;

(* On remarque qu'on parcourt les sommets de "la gauche vers la droite" dans cet exemple. *)

(* In[40]: *)


g1__adj;;

(* In[41]: *)


largeur_iter g1__adj 0;;

(* > Vous pouvez aussi faire des versions récursives de ces parcours. *)

(* ## `est_connexe` *)

(* Un graphe est connexe *si et seulement si* chaque sommet est relié à tout autre sommet (par un chemin de longueur un ou plus).
On écrit d'abord une fonction qui vérifie que tous les sommets sont accessibles depuis un sommet, puis on vérifiera que ce prédicat est vrai pour tous les sommets. *)

(* In[42]: *)


let tous_vrais = Array.fold_left (&&) true;;

(* In[43]: *)


let tous_accessibles (g : graphe_adj) (debut : sommet) : bool =
    let vu = Array.make (nb_sommets__adj g) false in
    let file = Queue.create () in
    Queue.push debut file;
    vu.(debut) <- true;  (* on ne peut pas se passer du tableau vu *)
    while not (Queue.is_empty file) do
        let i = Queue.pop file in
        List.iter (fun j -> if not vu.(j) then begin (* car utile ici *)
            Queue.push j file;
            vu.(j) <- true
            end)
        g.(i)
    done;
    (* mais a la fin on s'en sert juste pour ce test *)
    tous_vrais vu
;;

(* In[44]: *)


tous_accessibles g1__adj 0;;
tous_accessibles g1__adj 1;;
tous_accessibles g1__adj 2;;

(* In[45]: *)


let est_connexe (g : graphe_adj) : bool =
    let n = nb_sommets__adj g in
    tous_vrais (Array.init n (fun i -> tous_accessibles g i));
;;

(* In[46]: *)


est_connexe g1__adj;;

(* Et avec un exemple de graphe non connexe :

![TP5__exemple_graphe4.svg](TP5__exemple_graphe4.svg) *)

(* In[47]: *)


let g2__adj : graphe_adj = [|
    [1; 2]; (* 0 -- 1 et 0 -- 2 *)
    [0]; (* 1 -- 0 *)
    [0]; (* 2 -- 0 *)
    [4]; (* 3 -- 4 *)
    [3]; (* 4 -- 3 *)
|];;

(* In[48]: *)


largeur_iter g2__adj 0;;

largeur_iter g2__adj 3;;

(* In[49]: *)


est_connexe g2__adj;;

(* ## `est_arbre` *)

(* Un arbre est un graphe connexe acyclique.

1. on sait déjà vérifier la connexité.
2. on doit vérifier l'absence de cycle.

Je vous laisse réfléchir par vous-même pour le second point. ([Exemple](http://www.geeksforgeeks.org/detect-cycle-undirected-graph/))

Si besoin, voici une correction. *)

(* In[64]: *)


let rec est_cyclique_aux (g : graphe_adj) (v : sommet) (vu : bool array) (parent : sommet) =
    vu.(v) <- true; (* v est vu ! *)
    let res = ref false in
    let indice = ref 0 in
    let gv = Array.of_list g.(v) in (* la conversion prend un temps O(deg(v)) une fois *)
    while (not !res) && (!indice < Array.length gv) do
        let i = gv.(!indice) in (* comme ca cette lecture prend O(1) chaque fois *)
        incr indice;
        if not vu.(i) then begin
            if (est_cyclique_aux g i vu v) then
                res := true;
        end
        else begin
            if parent != i then
                res := true
        end
    done;
    !res    
;;

(* In[65]: *)


let est_cyclique (g : graphe_adj) : bool =
    let n = nb_sommets__adj g in
    let vu = Array.make n false in
    let res = ref false in
    for i = 0 to n - 1 do
        if not vu.(i) then begin
            if est_cyclique_aux g i vu (-1) then
                res := true;
        end
    done;
    !res
;;

(* In[66]: *)


let absence_cycle (g : graphe_adj) : bool =
    not (est_cyclique g)
;;

(* In[67]: *)


let est_arbre (g : graphe_adj) : bool =
    (est_connexe g) && (absence_cycle g)
;;

(* In[68]: *)


est_cyclique g1__adj;;
est_arbre g1__adj;;

(* In[69]: *)


est_cyclique g2__adj;;
est_arbre g2__adj;;

(* Et avec un exemple de graphe connexe mais avec un cycle : *)

(* In[70]: *)


let g3__adj : graphe_adj = [|
    [1; 2]; (* 0 -- 1 et 0 -- 2 *)
    [0; 2]; (* 1 -- 0 et 1 -- 2 *)
    [0; 1]; (* 2 -- 0 et 2 -- 1 *)
|];;

(* In[71]: *)


est_connexe g3__adj;;
est_arbre g3__adj;;

(* ## `composantes_connexes` *)

(* Pour chaque sommet, on fait un parcours en largeur, et on ajoute tous les sommets visités dans la même composante connexe.
Dès qu'un nouveau sommet n'a pas encore été visité, on commence une nouvelle composante connexe.

Cet algorithme est en $\mathcal{O}(n)$, au pire chaque sommet est visité exactement une fois. *)

(* In[72]: *)


let composantes_connexes (g : graphe_adj) : sommet list list =
    let n = nb_sommets__adj g in
    let vu = Array.make n false in
    let cc_courante = ref [] in
    let rec visite (i : sommet) : unit =
        Printf.printf "visite(%d)\n" i; (* permet de vérifier que chaque sommet n'est visité qu'une seule fois ! *)
        flush_all();
        vu.(i) <- true;
        cc_courante := i :: !cc_courante;
        (* cette opération est linéaire en deg(i) le degré de i *)
        List.iter (fun j -> if not vu.(j) then visite j) g.(i) 
    in
    let cc = ref [] in
    for i = 0 to n - 1 do
        (* au pire, on est en O(somme deg(i)) = O(n^2) *)
        (* mais en fait un sommet deja vu ne sera pas considere par la suite *)
        (* donc on est en O(n) en fait ! *)
        if not vu.(i) then begin
            visite i; (* au pire, chaque visite est en O(deg(i)) *)
            cc := !cc_courante :: !cc;
            cc_courante := []
        end
    done;
    !cc
;;

(* In[73]: *)


composantes_connexes g1__adj;;

(* In[74]: *)


composantes_connexes g2__adj;;

(* ## 2-coloriage

Le $2$-coloriage est très facile : si un seul sommet a un degré $\geq 3$, ce n'est pas possible.
Si tous les sommets ont un degrés $\leq 2$, on part d'un sommet (pour chaque composante connexe) et on alterne entre deux couleurs en parcourant la composante connexe...

Cet algorithme est aussi en $\mathcal{O}(n)$. *)

(* In[77]: *)


type deuxcouleur = Blanc | Noir;; (* on pourrait utiliser bool *);;

(* In[78]: *)


let alterne_couleur = function  (* avec bool, cette fonction serait... juste not *)
    | Blanc -> Noir
    | Noir -> Blanc
;;

(* In[63]: *)


let max_array = Array.fold_left max min_int;;

(* In[81]: *)


let deuxcoloriage (g : graphe_adj) : deuxcouleur array =
    let n = nb_sommets__adj g in
    let vu = Array.make n false in
    let couleurs = Array.make n Blanc in
    let cc = composantes_connexes g in
    let rec visite_et_colorie_en_alternance (c : deuxcouleur) (i : sommet) : unit =
        Printf.printf "visite(%d)\n" i;
        flush_all();
        vu.(i) <- true;
        couleurs.(i) <- c;
        List.iter (fun j ->
            if not vu.(j) then
                visite_et_colorie_en_alternance (alterne_couleur c) j
            else begin
                if couleurs.(j) = c then failwith "2-coloriage impossible."
            end
        ) g.(i)
    in
    List.iter (visite_et_colorie_en_alternance Blanc) (List.map List.hd cc);
    couleurs
;;

(* In[82]: *)


deuxcoloriage g1__adj;;

(* Pour le deuxième exemple, on voit que la seconde composante connexe $\{3, 4\}$ est coloriée avec deux couleurs aussi. *)

(* In[83]: *)


deuxcoloriage g2__adj;;

(* In[84]: *)


let g3__adj : graphe_adj = [|
    [1; 2; 3]; (* 0 -- 1 et 0 -- 2 et 0 -- 3 *)
    [0]; (* 1 -- 0 *)
    [0]; (* 2 -- 0 *)
    [0]; (* 3 -- 0 *)
|];;

(* In[85]: *)


deuxcoloriage g3__adj;;

(* Et un graphe non coloriable, avec une 3-clique $0 - 1 - 2$ : *)

(* In[86]: *)


let g4__adj : graphe_adj = [|
    [1; 2; 3]; (* 0 -- 1 et 0 -- 2 et 0 -- 3 *)
    [0; 2]; (* 1 -- 0 et 1 -- 2 *)
    [0; 1]; (* 2 -- 0 et 2 -- 1 *)
    [0]; (* 3 -- 0 *)
|];;

(* In[87]: *)


deuxcoloriage g4__adj;;

(* ----
# Cycles eulériens

Je vous laisse lire [cette page](http://perso.crans.org/besson/agreg/modelisation/projet_2/)
(`perso.crans.org/besson/agreg/modelisation/projet_2/`).
[Cherchez en ligne](https://duckduckgo.com/?q=parcours+eul%C3%A9rien+algorithme+de+rosenstielh&t=canonical&ia=web) pour plus d'informations. *)

(* ## `existe_cycle_eulerien` *)

(* On compte le nombre de sommets de degrés impairs, et un chemin eulérien existe si et seulement s'il y en a zéros ou deux. *)

(* In[106]: *)


let existe_cycle_eulerien (g : graphe_adj) : bool =
    let deg = Array.to_list (degres__adj g) in
    let nb_deg_impair = List.length (List.filter (fun i -> i mod 2 = 0) deg) in
    nb_deg_impair = 0 || nb_deg_impair = 2
;;

(* In[107]: *)


existe_cycle_eulerien g1__adj;;

(* In[108]: *)


existe_cycle_eulerien g2__adj;;

(* In[109]: *)


existe_cycle_eulerien g3__adj;;

(* ## La suite *)

(* Pour trouver un chemin eulérien, on applique l'algorithme suivant (dû à Rosentielh, aussi attribué à [Hierholzer (1873)](https://en.wikipedia.org/wiki/Eulerian_path#Hierholzer.27s_algorithm)).

- Compter le nombre de sommets de degré impair,
- Si :
  + c'est 0 : construire un cycle partant du premier sommet (choix arbitraire),
  + c'est 2 : construire un chemin entre les deux sommets en question,
  + sinon, il n'y a pas de chemin eulérien (on répond non).
- parcourir le chemin déjà construit : à chaque sommet :
  + tant qu'il reste des arêtes partant de ce sommet dans le graphe :
     - construire un cycle partant de ce sommet,
     - puis l'insérer dans le chemin.

Étant donné les conditions sur le graphe, construire un chemin ou un cycle n'est pas compliqué : il suffit de partir de l'origine, de prendre la première arête rencontrée et de recommencer récursivement. *)

(* ----
# Conclusion

Fin. À la séance prochaine. Le TP6 traitera de Lambda calcul (en février). *)
