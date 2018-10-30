(*
This OCaml script was exported from a Jupyter notebook
using an open-source software (under the MIT License) written by @Naereen
from https://github.com/Naereen/Jupyter-Notebook-OCaml
This software is still in development, please notify me of a bug at
https://github.com/Naereen/Jupyter-Notebook-OCaml/issues/new if you find one
*)

(* # Table of Contents
 <p><div class="lev1 toc-item"><a href="#TP-7---Programmation-pour-la-préparation-à-l'agrégation-maths-option-info" data-toc-modified-id="TP-7---Programmation-pour-la-préparation-à-l'agrégation-maths-option-info-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>TP 7 - Programmation pour la préparation à l'agrégation maths option info</a></div><div class="lev2 toc-item"><a href="#Algorithme-de-Dijkstra---avec-des-files-non-mutables" data-toc-modified-id="Algorithme-de-Dijkstra---avec-des-files-non-mutables-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Algorithme de Dijkstra - avec des files non mutables</a></div><div class="lev3 toc-item"><a href="#Files-de-priorité-min" data-toc-modified-id="Files-de-priorité-min-111"><span class="toc-item-num">1.1.1&nbsp;&nbsp;</span>Files de priorité min</a></div><div class="lev3 toc-item"><a href="#Graphe-par-tableau-de-listes-d'adjacence" data-toc-modified-id="Graphe-par-tableau-de-listes-d'adjacence-112"><span class="toc-item-num">1.1.2&nbsp;&nbsp;</span>Graphe par tableau de listes d'adjacence</a></div><div class="lev3 toc-item"><a href="#Exemple-de-visualisation-de-graphe" data-toc-modified-id="Exemple-de-visualisation-de-graphe-113"><span class="toc-item-num">1.1.3&nbsp;&nbsp;</span>Exemple de visualisation de graphe</a></div><div class="lev3 toc-item"><a href="#Dijkstra" data-toc-modified-id="Dijkstra-114"><span class="toc-item-num">1.1.4&nbsp;&nbsp;</span>Dijkstra</a></div><div class="lev3 toc-item"><a href="#Contre-exemples" data-toc-modified-id="Contre-exemples-115"><span class="toc-item-num">1.1.5&nbsp;&nbsp;</span>Contre-exemples</a></div><div class="lev4 toc-item"><a href="#Un-graphe-non-connexe" data-toc-modified-id="Un-graphe-non-connexe-1151"><span class="toc-item-num">1.1.5.1&nbsp;&nbsp;</span>Un graphe non connexe</a></div><div class="lev4 toc-item"><a href="#Un-graphe-avec-un-poids-négatif" data-toc-modified-id="Un-graphe-avec-un-poids-négatif-1152"><span class="toc-item-num">1.1.5.2&nbsp;&nbsp;</span>Un graphe avec un poids négatif</a></div><div class="lev2 toc-item"><a href="#Algorithme-de-Dijkstra---avec-des-files-mutables" data-toc-modified-id="Algorithme-de-Dijkstra---avec-des-files-mutables-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Algorithme de Dijkstra - avec des files mutables</a></div><div class="lev3 toc-item"><a href="#Files-de-priorité-min-mutables" data-toc-modified-id="Files-de-priorité-min-mutables-121"><span class="toc-item-num">1.2.1&nbsp;&nbsp;</span>Files de priorité min mutables</a></div><div class="lev3 toc-item"><a href="#Dijkstra,-2ème-version" data-toc-modified-id="Dijkstra,-2ème-version-122"><span class="toc-item-num">1.2.2&nbsp;&nbsp;</span>Dijkstra, 2ème version</a></div><div class="lev3 toc-item"><a href="#Exemples" data-toc-modified-id="Exemples-123"><span class="toc-item-num">1.2.3&nbsp;&nbsp;</span>Exemples</a></div><div class="lev2 toc-item"><a href="#Arbres-couvrants-de-poids-minimal" data-toc-modified-id="Arbres-couvrants-de-poids-minimal-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Arbres couvrants de poids minimal</a></div><div class="lev3 toc-item"><a href="#Algorithme-de-Prim" data-toc-modified-id="Algorithme-de-Prim-131"><span class="toc-item-num">1.3.1&nbsp;&nbsp;</span>Algorithme de Prim</a></div><div class="lev3 toc-item"><a href="#Exemple" data-toc-modified-id="Exemple-132"><span class="toc-item-num">1.3.2&nbsp;&nbsp;</span>Exemple</a></div><div class="lev2 toc-item"><a href="#Tas-binaire-min" data-toc-modified-id="Tas-binaire-min-14"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Tas binaire min</a></div><div class="lev2 toc-item"><a href="#Codage-de-Huffman" data-toc-modified-id="Codage-de-Huffman-15"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Codage de Huffman</a></div><div class="lev3 toc-item"><a href="#Fréquences-de-lettres-dans-un-texte" data-toc-modified-id="Fréquences-de-lettres-dans-un-texte-151"><span class="toc-item-num">1.5.1&nbsp;&nbsp;</span>Fréquences de lettres dans un texte</a></div><div class="lev3 toc-item"><a href="#Structure-de-tas-binaire-min" data-toc-modified-id="Structure-de-tas-binaire-min-152"><span class="toc-item-num">1.5.2&nbsp;&nbsp;</span>Structure de tas binaire min</a></div><div class="lev3 toc-item"><a href="#Exemple-d'un-codage-préfixe-(Figure-16.4-p378-du-Cormen)" data-toc-modified-id="Exemple-d'un-codage-préfixe-(Figure-16.4-p378-du-Cormen)-153"><span class="toc-item-num">1.5.3&nbsp;&nbsp;</span>Exemple d'un codage préfixe (Figure 16.4 p378 du Cormen)</a></div><div class="lev3 toc-item"><a href="#Algorithme-glouton-de-codage-préfixe-optimal-de-Huffman" data-toc-modified-id="Algorithme-glouton-de-codage-préfixe-optimal-de-Huffman-154"><span class="toc-item-num">1.5.4&nbsp;&nbsp;</span>Algorithme glouton de codage préfixe optimal de Huffman</a></div><div class="lev2 toc-item"><a href="#Coloration-de-graphes" data-toc-modified-id="Coloration-de-graphes-16"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Coloration de graphes</a></div><div class="lev3 toc-item"><a href="#Représentation-des-graphes" data-toc-modified-id="Représentation-des-graphes-161"><span class="toc-item-num">1.6.1&nbsp;&nbsp;</span>Représentation des graphes</a></div><div class="lev3 toc-item"><a href="#Et-des-coloriages" data-toc-modified-id="Et-des-coloriages-162"><span class="toc-item-num">1.6.2&nbsp;&nbsp;</span>Et des coloriages</a></div><div class="lev3 toc-item"><a href="#Exemple" data-toc-modified-id="Exemple-163"><span class="toc-item-num">1.6.3&nbsp;&nbsp;</span>Exemple</a></div><div class="lev3 toc-item"><a href="#Algorithme-glouton-pour-le-coloriage" data-toc-modified-id="Algorithme-glouton-pour-le-coloriage-164"><span class="toc-item-num">1.6.4&nbsp;&nbsp;</span>Algorithme glouton pour le coloriage</a></div><div class="lev3 toc-item"><a href="#Exemples" data-toc-modified-id="Exemples-165"><span class="toc-item-num">1.6.5&nbsp;&nbsp;</span>Exemples</a></div><div class="lev2 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-17"><span class="toc-item-num">1.7&nbsp;&nbsp;</span>Conclusion</a></div> *)

(* # TP 7 - Programmation pour la préparation à l'agrégation maths option info
TP 5 : Algorithmes gloutons et files de priorité. *)

(* - En OCaml. *)

(* In[1]: *)


let print = Printf.printf;;
Sys.command "ocaml -version";;

(* In[2]: *)


print_endline;;

(* ----
## Algorithme de Dijkstra - avec des files non mutables

Déjà vu, on le retraite ici. *)

(* ### Files de priorité min *)

(* In[3]: *)


(* file de priorité version non-mutable *)
type 'a priopqueue = (int * 'a) list;;

(* In[4]: *)


(* file vide *)
let vide : 'a priopqueue = [ ];;

(* In[5]: *)


(* [inserer x clef q] insere l'element [x] dans la file [q]
   avec le clef [x], et renvoie la nouvelle file ainsi créée.
   Termine avec une exception si la file contient déjà [x]  *)
let inserer (x:'a) (clef:int) (q:'a priopqueue) : 'a priopqueue =
    if List.exists (fun (_, v) -> x = v) q
    then failwith "l'element est déjà dans la file"
    else (clef,x) :: q
;;

(* In[6]: *)


(* [est_vide q] teste si la file [q] est vide *)
let est_vide (q:'a priopqueue) : bool = (q = [ ]);;

(* In[7]: *)


(* [trouve_min_aux min_val min_clef q] renvoie un couple de clef minimale
     dans (min_val,min_clef)::q *)
let rec trouve_min_aux (min_val:'a) (min_clef:int) (q:'a priopqueue) : int * 'a =
    match q with
    | [ ] -> (min_clef, min_val)
    | (clef, _) :: q when clef > min_clef -> trouve_min_aux min_val min_clef q
    | (clef, v) :: q -> trouve_min_aux v clef q
;;

(* In[8]: *)


(* [trouve_min q] renvoie un élément de clef minimale la file [q].
   Lance une exception si la liste est vide *)
let trouve_min (q:'a priopqueue) : 'a =
    match q with
    | [ ] -> failwith "trouve_min: la file est vide"
    | (clef, v) :: q -> snd (trouve_min_aux v clef q)
;;

(* In[9]: *)


let _ = trouve_min (inserer '1' 1 (inserer '2' 2 (inserer '3' 3 vide)));;
let _ = trouve_min (inserer '1' 4 (inserer '2' 2 (inserer '3' 3 vide)));;

(* In[10]: *)


(* [supprime v q] renvoie une file contenant les éléments de [q], sauf [x].
   [x] doit apparaitre une et une seule fois dans la file. *)
let rec supprime (x:'a) (q:'a priopqueue) : 'a priopqueue =
    match q with
    | [ ] -> [ ]
    | (_, v) :: q when v=x -> q
    | (clef, v) :: q -> (clef, v) :: (supprime x q)
;;

(* In[11]: *)


(* [extraire_min q] renvoie un élément de q, de clef minimal,
   ainsi que la nouvelle file obtenue en supprimant cet
   élément; termine avec une exception si la file est vide  *)
let extraire_min (q:'a priopqueue) : 'a * 'a priopqueue =
    if q = [ ] then
        failwith "extraire_min: file vide"
    else
        let min = trouve_min q in
        (min, supprime min q)
;;

(* In[12]: *)


let _ = extraire_min (inserer '1' 1 (inserer '2' 2 (inserer '3' 3 vide)));;
let _ = extraire_min (inserer '1' 4 (inserer '2' 2 (inserer '3' 3 vide)));;

(* In[13]: *)


(* [diminuer_clef q clef x] modifie la clef de l'élément [x]
   dans la file q en lui associant la nouvelle clef [clef], qui
   doit être inferieur à la clef actuelle de [x].
   Termine avec une exception si la file ne contient pas [x]  *)
let rec diminuer_clef (x:'a) (clef:int) (q:'a priopqueue) : 'a priopqueue =
    match q with
    | [ ] -> failwith "diminuer_clef : l'élément n'est pas présent"
    | (_, v) :: q when v=x -> (clef, x) :: q
    | (c, v) :: q -> (c, v) :: diminuer_clef x clef q
;;

(* In[14]: *)


let f =  inserer '1' 1 (inserer '2' 2 (inserer '3' 3 vide));;
let _ = diminuer_clef '3' 0 f;;
let _ = diminuer_clef '2' 0 f;;

(* ### Graphe par tableau de listes d'adjacence *)

(* In[15]: *)


type sommet = int;;
type graph = {
    taille: int; (* les sommets sont des entiers entre 0 et taille-1 *)
    adj: (int * sommet) list array;
    entree: sommet
};;

(* Ce qui suit est purement optionnel, ce n'était pas demandé, ne vous embêtez pas à chercher à tout comprendre, c'est simplement pour visualiser les graphes et les afficher ensuite. *)

(* In[16]: *)


let print = Printf.fprintf;;

let dot outname (g:graph) (bold:(int*int) list) : unit =
    let f = open_out (outname ^ ".dot") in
    print f "digraph G {\n";
    for i=0 to g.taille-1 do
        print f "  som%d [label=\"%d\"];\n" i i
    done;
    for i=0 to g.taille-1 do
        List.iter (fun (c,j) ->
            let option = if List.mem (i,j) bold then ",style=bold" else "" in
            print f "  som%d -> som%d [label=\"%d\"%s];\n" i j c option
        ) g.adj.(i);
    done;
    print f "}\n";
    close_out f
;;

let dot2svg outname =
    Sys.command (Printf.sprintf "dot -Tsvg %s.dot > %s.svg" outname outname);;;

(* ### Exemple de visualisation de graphe *)

(* In[17]: *)


let s = 0
and a = 1
and b = 2
and c = 3
and d = 4;;
let g1 = {
    taille = 5;
    entree = s;
    adj = [|
        [(2,a); (4,b); (2,c)]; (* adj(s) *)
        [(1,d)]; (* adj(A) *)
        [(4,d)]; (* adj(B) *)
        [(1,b)]; (* adj(C) *)
        [ ]; (* adj(D) *)
    |]
};;

(* In[18]: *)


let _ = dot "TP7__g1" g1 [ ];;
dot2svg "TP7__g1";;

(* In[19]: *)


Sys.command "cat TP7__g1.dot";;

(* ![TP7__g1.svg](TP7__g1.svg) *)

(* Le second argument permet d'afficher un certain chemin : *)

(* In[20]: *)


let _ = dot "TP7__g2" g1 [(0,3);(3,2);(2,4)];;

(* In[21]: *)


Sys.command "cat TP7__g2.dot";;
dot2svg "TP7__g2";;

(* ![](TP7__g2.svg) *)

(* ### Dijkstra *)

(* Une fois qu'on dispose de tout ça, écrire l'algorithme de Dijkstra est relativement rapide.

- Voir [ce site](https://www.cs.usfca.edu/~galles/visualization/Dijkstra.html) pour de belles visualisations de l'algorithme de Dijkstra.
- Et [cette page](https://jilljenn.github.io/tryalgo/tryalgo/tryalgo.html#module-tryalgo.dijkstra) pour une implémentation propre en Python ([lien direct vers le code](https://jilljenn.github.io/tryalgo/_modules/tryalgo/dijkstra.html#dijkstra)). *)

(* In[22]: *)


let dijkstra g =
    let q = ref vide in
    let dist = Array.init g.taille (fun i ->
        if i=g.entree then 0 else max_int
    ) in
    for i=0 to g.taille - 1 do (* initialisation de la file *)
        q := inserer i dist.(i) !q
    done;
    while not (est_vide !q) do
        let (x, q') = extraire_min !q in
        q := q';  (* ne pas oublier de mettre à jour la file *)
        (* on regarde les adjacents de x *)
        List.iter (fun (c,y) ->
            if dist.(y) > dist.(x) + c
            then begin
                dist.(y) <- dist.(x) + c;
                q := diminuer_clef y dist.(y) !q
            end
        ) g.adj.(x)
    done;
    dist
;;

(* In[23]: *)


let _ = dijkstra g1;;

(* ### Contre-exemples

Trouver des cas simples faisant échouer l’algorithme si une des hypothèses n'est pas satisfaite : par exemple un graphe non connexe, ou un graphe avec une arête de poids négatif. *)

(* #### Un graphe non connexe *)

(* In[32]: *)


let s = 0
and a = 1
and b = 2
and c = 3
and d = 4
and e = 5
and f = 6;;
let g2 = {
    taille = 7;
    entree = s;
    adj = [|
        [(2,a); (4,b); (2,c)]; (* adj(s) *)
        [(1,d)]; (* adj(A) *)
        [(4,d)]; (* adj(B) *)
        [(1,b)]; (* adj(C) *)
        [ ]; (* adj(D) *)
        [(5,f)]; (* adj(E) *)
        [ ]; (* adj(F) *)
    |]
};;

(* In[33]: *)


let _ = dijkstra g2;;

(* Oups, ça n'a pas l'air correct ! *)

(* #### Un graphe avec un poids négatif *)

(* In[44]: *)


let s = 0
and a = 1
and b = 2
and c = 3
and d = 4;;
let g3 = {
    taille = 5;
    entree = s;
    adj = [|
        [(2,a); (-4,b); (2,c)]; (* adj(s) *)
        [(1,d)]; (* adj(A) *)
        [(-4,d)]; (* adj(B) *)
        [(1,b)]; (* adj(C) *)
        [(2,b)]; (* adj(D) *)
    |]
};;

(* In[45]: *)


let _ = dijkstra g3;;

(* Oups, ça n'a pas l'air correct non plus ! *)

(* ----
## Algorithme de Dijkstra - avec des files mutables

Déjà vu, on le retraite ici. *)

(* ### Files de priorité min mutables *)

(* In[46]: *)


(* file de priorité version non-mutable *)
type 'a priopqueue = (int * 'a) list ref;;

(* In[47]: *)


(* file vide *)
let vide () : 'a priopqueue = ref [ ];;

(* In[48]: *)


(* [inserer x clef q] insere l'element [x] dans la file [q]
   avec le clef [x].
   Termine avec une exception si la file contient déjà [x]  *)
let inserer (x:'a) (clef:int) (q:'a priopqueue) : unit =
    if List.exists (fun (_, v) -> x=v) !q
    then failwith "l'element est déjà dans la file"
    else q := (clef,x) :: !q
;;

(* In[49]: *)


(* [est_vide q] teste si la file [q] est vide *)
let est_vide (q:'a priopqueue) : bool = (!q = [ ]);;

(* In[50]: *)


(* [trouve_min_aux min_val min_clef q] renvoie un couple de clef minimale
     dans (min_val,min_clef)::q *)
let rec trouve_min_aux (min_val:'a) (min_clef:int) (q:(int*'a) list) : int * 'a =
    match q with
    | [ ] -> (min_clef, min_val)
    | (clef, _) :: q when clef > min_clef -> trouve_min_aux min_val min_clef q
    | (clef, v) :: q -> trouve_min_aux v clef q
;;

(* In[51]: *)


(* [trouve_min q] renvoie un élément de clef minimale la file [q].
   Lance une exception si la liste est vide *)
let trouve_min (q:(int*'a) list) : 'a =
    match q with
    | [ ] -> failwith "trouve_min: la file est vide"
    | (clef, v) :: q -> snd (trouve_min_aux v clef q)
;;

(* In[52]: *)


(* [supprime v q] renvoie une file contenant les éléments de [q], sauf [x].
   [x] doit apparaitre une et une seule fois dans la file. *)
let rec supprime (x:'a) (q:(int*'a) list) : (int*'a) list =
    match q with
    | [ ] -> [ ]
    | (_, v) :: q when v=x -> q
    | (clef, v) :: q -> (clef,v) :: (supprime x q)
;;

(* In[53]: *)


(* [extraire_min q] renvoie un élément de q, de clef minimal,
   et met à jour la file; termine avec une exception si la file est vide  *)
let extraire_min (q:'a priopqueue) : 'a =
    if !q = [ ] then failwith "extraire_min: file vide"
    else
        let min = trouve_min !q in
        q :=  supprime min !q;
        min
;;

(* In[54]: *)


(* [diminuer_clef q clef x] modifie la clef de l'élément [x]
   dans la file q en lui associant la nouvelle clef [clef], qui
   doit être inferieur à la clef actuelle de [x].
   Termine avec une exception si la file ne contient pas [x]  *)
let diminuer_clef (x:'a) (clef:int) (q:'a priopqueue) : unit =
    let rec diminuer_aux (l:(int*'a) list) : (int*'a) list =
        match l with
        | [ ] -> failwith "diminuer_clef : l'élément n'est pas présent"
        | (_, v) :: q when v=x -> (clef, x) :: q
        | (c, v) :: q -> (c, v) :: diminuer_aux q in
    q := diminuer_aux !q
;;

(* ### Dijkstra, 2ème version *)

(* C'est aussi assez direct : *)

(* In[55]: *)


let dijkstra g =
    let q = vide () in
    let dist = Array.init g.taille (fun i ->
        if i=g.entree then 0 else max_int
    ) in
    let pere = Array.init g.taille (fun i -> i) in
    for i=0 to g.taille - 1 do (* initialisation de la file *)
        inserer i dist.(i) q;
    done;
    while not (est_vide q) do
        let x = extraire_min q in
        (* on regarde les adjacents de x *)
        List.iter (fun (c,y) ->
            if dist.(y) > dist.(x) + c
            then begin
                pere.(y) <- x;
                dist.(y) <- dist.(x) + c;
                diminuer_clef y dist.(y) q
        end) g.adj.(x)
    done;
    dist, pere
;;

(* ### Exemples *)

(* In[56]: *)


let _ = dijkstra g1;;

(* Et les contre-exemples maintenant : *)

(* In[57]: *)


let _ = dijkstra g2;;

(* In[58]: *)


let _ = dijkstra g3;;

(* ----
## Arbres couvrants de poids minimal

On ne traite que l'algorithme de Prim. L'algorithme de Kruskal n'est pas plus compliqué, il utilise une autre structure de données (Union-Find, déjà traité aussi). *)

(* ### Algorithme de Prim *)

(* In[37]: *)


let prim g =
    let q = vide () in
    let poids = Array.init g.taille (fun i ->
        if i=g.entree then 0 else max_int
    ) in
    let pere = Array.init g.taille (fun i -> i) in
    for i=0 to g.taille-1 do (* initialisation de la file *)
        inserer i poids.(i) q;
    done;
    while not (est_vide q) do
        let x = extraire_min q in
        (* on regarde les adjacents de x *)
        List.iter (fun (c,y) ->
            if poids.(y) > c
            then begin
                pere.(y) <- x;
                poids.(y) <- c;
                diminuer_clef y poids.(y) q
        end)
        g.adj.(x)
    done;
    Array.iteri (fun i p ->
        if i != p then Printf.printf " (%d, %d)\n" i p
    ) pere;
    poids, pere;
;;

(* ### Exemple *)

(* In[38]: *)


let _ = prim g1;;

(* ---
## Tas binaire min *)

(* In[39]: *)


(** {2 Leftist heaps, by Jean-Christophe Filliâtre} *)

(**************************************************************************)
(*                                                                        *)
(*  Copyright (C) Jean-Christophe Filliâtre                               *)
(*                                                                        *)
(*  This software is free software; you can redistribute it and/or        *)
(*  modify it under the terms of the GNU Library General Public           *)
(*  License version 2.1, with the special exception on linking            *)
(*  described in file LICENSE.                                            *)
(*                                                                        *)
(*  This software is distributed in the hope that it will be useful,      *)
(*  but WITHOUT ANY WARRANTY; without even the implied warranty of        *)
(*  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.                  *)
(*                                                                        *)
(**************************************************************************)

(* Leftist heaps.

   See for instance Chris Okasaki's "Purely Functional Data Structures" *)

module type Ordered = sig
  type t
  val le: t -> t -> bool
end

exception Empty

module Make(X : Ordered) :
sig
  type t
  val empty : t
  val is_empty : t -> bool
  val insert : X.t -> t -> t
  val min : t -> X.t
  val extract_min : t -> X.t * t
  val merge : t -> t -> t
  val length : t -> int
end
=
struct

  type t = E | T of int * X.t * t * t

  let rank = function E -> 0 | T (r,_,_,_) -> r

  let rec length = function E -> 0 | T (_,_,t1,t2) -> 1 + (length t1) + (length t2)

  let make x a b =
    let ra = rank a and rb = rank b in
    if ra >= rb then T (rb + 1, x, a, b) else T (ra + 1, x, b, a)

  let empty = E

  let is_empty = function E -> true | T _ -> false

  let rec merge h1 h2 = match h1,h2 with
    | E, h | h, E ->
        h
    | T (_,x,a1,b1), T (_,y,a2,b2) ->
        if X.le x y then make x a1 (merge b1 h2) else make y a2 (merge h1 b2)

  let insert x h = merge (T (1, x, E, E)) h

  let min = function E -> raise Empty | T (_,x,_,_) -> x

  let extract_min = function
    | E -> raise Empty
    | T (_,x,a,b) -> x, merge a b

end;;

(* ----
## Codage de Huffman

C'est un grand classique pour les leçons "Programmation dynamique" et "Algorithmique du texte".
Le présenter en développement sans l'avoir implémenter est difficilement pardonnable. *)

(* <center><span style="color:red;">TODO : utiliser une file de priorité mutable plutôt qu'un tas min ? Je n'ai pas encore eu le temps de terminer cette correction.</span></center> *)

(* ### Fréquences de lettres dans un texte *)

(* In[40]: *)


(** Calcule l'alphabet du texte [text] ainsi que son tableau de fréquence.
    Linéaire en temps et espace dans la taille du texte. *)
let frequencies text =
    let n = String.length text in
    let f = Hashtbl.create 128 in
    for i = 0 to n-1 do
        if Hashtbl.mem f text.[i] then
            Hashtbl.replace f text.[i] (1 + Hashtbl.find f text.[i])
        else Hashtbl.add f text.[i] 1;
    done;
    f
;;

(* In[41]: *)


(** Renvoie juste l'alphabet qui compose le texte [text]. *)
let alphabet text =
    let f = frequencies text in
    let alp = ref [ ] in
    Hashtbl.iter (fun carct _ -> alp := carct :: !alp) f;
    !alp
;;

(* In[51]: *)


(** Un exemple. https://www.un.org/fr/universal-declaration-human-rights/index.html *)
let text1 = "https://www.un.org/fr/universal-declaration-human-rights/index.html : Article premier\n\nTous les etres humains naissent libres et egaux en dignite et en droits. Ils sont doues de raison et de conscience et doivent agir les uns envers les autres dans un esprit de fraternite.\nArticle 2\n\n1. Chacun peut se prevaloir de tous les droits et de toutes les libertes proclames dans la presente Declaration, sans distinction aucune, notamment de race, de couleur, de sexe, de langue, de religion, d'opinion politique ou de toute autre opinion, d'origine nationale ou sociale, de fortune, de naissance ou de toute autre situation.\n2. De plus, il ne sera fait aucune distinction fondee sur le statut politique, juridique ou international du pays ou du territoire dont une personne est ressortissante, que ce pays ou territoire soit independant, sous tutelle, non autonome ou soumis a une limitation quelconque de souverainete.";;
let _ = alphabet text1;;

(* In[52]: *)


(** Pour affiche facilement. *)
let print = Format.printf;;

(** Pour visualiser un tableau des fréquences ainsi calculée. *)
let print_frequencies f =
  flush_all();
  print "\n\nTable des fréquences f :\n";
  flush_all();
  Hashtbl.iter (fun carct freq -> print "%C: %i, " carct freq) f;
  flush_all();
;;

(* In[73]: *)


print_frequencies (frequencies text1);;

(* ### Structure de tas binaire min *)

(* In[55]: *)


(* #use "Heap.ml";; *)
(* open Heap;; *)

type codage =
    | F of char * int | N of (int * codage * codage);;

let freq = function F (_, i) -> i | N (i,_ , _) -> i;;

module CodageFreq = struct
    type t = codage
    let le c1 c2 = (freq c1) <= (freq c2)
end;;

module MinHeap = Make(CodageFreq);;

let rec check_freq = function
    | F(_,i) -> assert( (i >= 0) )
    | N(i, c1, c2) -> assert( (i >= 0) && (i = (freq c1) + (freq c2)) ); check_freq c1; check_freq c2;
;;

(* ### Exemple d'un codage préfixe (Figure 16.4 p378 du Cormen) *)

(* In[56]: *)


let sigma_fromlist l =
    let h = Hashtbl.create (List.length l) in
    List.iter (fun (c, f) -> Hashtbl.add h c f) l;
    h
;;

let sigma1 = sigma_fromlist [('f', 5); ('e', 9); ('c', 12); ('b', 13); ('d', 16); ('a', 45) ];;

let codage1 = N(100,
    F('a', 45),
    N(55,
    N(25,
        F('c',12),
        F('b',13)
    ),
    N(30,
        N(14,
        F('f',5),
        F('e',9)
        ),
        F('d',16)
    )
)
);;

(* In[57]: *)


let _ = check_freq codage1;;

(* In[58]: *)


(** Calcul du nombre de bits nécessaires pour stocker le fichier. *)
let rec coutx prof = function
  | F(c, f) -> begin
    print "\nFeuille %C de profondeur %i et de fréquence %i." c prof f;
    (f * prof);
  end
  | N(_, c1, c2) -> (coutx (prof+1) c1) + (coutx (prof+1) c2)
;;

(** Il faudrait rajouter la taille du codage lui-même. *)
let cout = coutx 1;;

let _ = cout codage1;;

(* ### Algorithme glouton de codage préfixe optimal de Huffman *)

(* On commence avec une fonction auxiliaire : *)

(* In[59]: *)


let huffmanx sigma =
    let n = Hashtbl.length sigma in
    let q = ref (MinHeap.empty) in
    Hashtbl.iter (fun c f -> q := (MinHeap.insert (F(c,f)) !q) ) sigma;
    for i = 1 to n-1 do
        flush_all();
        print "\n\nHuffmanx : %i-ième étape. La file q est de taille %i." i (MinHeap.length !q);
        let x, q2 = MinHeap.extract_min (!q) in
        flush_all();
        print "\nOn retire à q le noeud x de fréquence minimale (= %i)." (freq x);
        let y, q3 = MinHeap.extract_min q2 in
        flush_all();
        print "\nOn retire à q second noeud y de fréquence minimale (= %i)." (freq y);
        q := q3;
        let z = N( (freq x) + (freq y), x, y) in
        flush_all();
        print "\nOn les fusionne en z un nouveau noeud de fréquence %i, de fils gauche = x et droit = y." ( freq z );
        q := MinHeap.insert z !q;
        flush_all();
        print "\nOn ajoute ce noeud z a la file de priorité min q.";
    done;
    MinHeap.min !q
;;

(* In[62]: *)


(* Vérification sur l'exemple. *)
assert(codage1 = (huffmanx sigma1));;

(* In[61]: *)


(** Pour un texte entier, on calcule directement le codage. *)
let huffman text =
    let freq = frequencies text in
    huffmanx freq
;;

let sigma2 = sigma_fromlist [ ('a',1); ('b',1); ('c',2); ('d',3); ('e',5); ('f',8); ('g',13); ('h',21) ];;
let _ = huffmanx sigma2;;

(* In[74]: *)


let _ = huffman text1;;

(* ----
## Coloration de graphes

Voyons une approche gloutonne.

On va trier les sommets par degrés décroissants, et attribuer à chaque sommet une couleur, soit la plus petite possible parmi celles non utilisées par ces voisins, soit une nouvelle.

On représente un graphe par tableau de listes d'adjacence. Notre exemple sera le graphe suivant, sans considérer les étiquettes des arêtes et en le considérant non orienté : *)

(* ![TP7__g1.svg](TP7__g1.svg) *)

(* ### Représentation des graphes *)

(* In[2]: *)


type sommet = int ;;
type graphe = (sommet list) array;;

(* In[3]: *)


let nb_sommet (g : graphe) = Array.length g;;

(* ### Et des coloriages *)

(* In[4]: *)


type couleur = int;;
type coloriage = couleur array;; (* c.(i) est la couleur du sommet i... *);;

(* In[5]: *)


let verifie_coloriage (g : graphe) (c : coloriage) =
    let res = ref true in
    let n = nb_sommet g in
    for i = 0 to n-1 do
        if c.(i) < 0 || c.(i) >= n then res := false;
        List.iter (fun j ->
            if c.(i) == c.(j) then res := false;
        ) g.(i)
    done;
    !res
;;

(* ### Exemple *)

(* In[6]: *)


let g1 : graphe = [|
    [1; 2; 3]; (* voisins de 0 *)
    [0; 4]; (* voisins de 1 *)
    [0; 3; 4]; (* voisins de 2 *)
    [0; 2]; (* voisins de 3 *)
    [1; 2]  (* voisins de 4 *)
|];;

(* In[7]: *)


let coloriage1 = [|0; 1; 1; 1; 0|];;
let _ = verifie_coloriage g1 coloriage1;; (* 3 -> 2 mais ont la même couleur *)

let coloriage2 = [|0; 1; 2; 1; 0|];;
let _ = verifie_coloriage g1 coloriage2;;

(* On a bien sûr une approche naïve : *)

(* In[8]: *)


let coloriage_naif (g : graphe) : coloriage =
    let n = nb_sommet g in
    Array.init n (fun i -> i);
;;

(* In[9]: *)


let coloriage3 = coloriage_naif g1;;
let _ = verifie_coloriage g1 coloriage3;;

(* C'est une borne supérieure triviale sur le nombre minimal de couleur requis pour colorier un graphe. *)

(* ### Algorithme glouton pour le coloriage

Pour plus de détails, voir par exemple [cette page là](http://jean-paul.davalan.pagesperso-orange.fr/graphs/col/index.html). *)

(* In[10]: *)


let degres (g : graphe) : int array =
    Array.map List.length g
;;

(* In[11]: *)


let _ = degres g1;;

(* In[12]: *)


type permutation = int array;;

let trie_par_degres (g : graphe) : permutation =
    let n = nb_sommet g in
    let indices = Array.init n (fun i -> i) in
    let d = degres g in
    let cmp_deg i j = Pervasives.compare d.(j) d.(i) in
    Array.stable_sort cmp_deg indices;
    indices
;;

(* In[13]: *)


let _ = trie_par_degres g1;;

(* In[14]: *)


let plus_petite_couleur_libre (n : int) (cs : couleur list) : couleur =
    let rep = ref 0 in
    while List.mem !rep cs do
        incr rep
    done;
    assert (!rep < n);
    !rep
;;

(* In[15]: *)


let coloriage_glouton (g : graphe) : coloriage =
    let n = nb_sommet g in
    let c = Array.make n (-1) in
    let perm = trie_par_degres g in
    for i = 0 to n-1 do
        (* on regarde le sommet perm.(i) *)
        let couleurs_voisins = List.map (fun j -> c.(j)) g.(perm.(i)) in
        c.(perm.(i)) <- plus_petite_couleur_libre n couleurs_voisins;
    done;
    c
;;

(* In[20]: *)


let coloriage_glouton_pas_trie (g : graphe) : coloriage =
    let n = nb_sommet g in
    let c = Array.make n (-1) in
    for i = 0 to n-1 do
        (* on regarde le sommet i *)
        let couleurs_voisins = List.map (fun j -> c.(j)) g.(i) in
        c.(i) <- plus_petite_couleur_libre n couleurs_voisins;
    done;
    c
;;

(* ### Exemples *)

(* In[16]: *)


let coloriage4 = coloriage_glouton g1;;
let _ = verifie_coloriage g1 coloriage4;;

(* In[21]: *)


let coloriage5 = coloriage_glouton_pas_trie g1;;
let _ = verifie_coloriage g1 coloriage5;;

(* On remarque que la procédure gloutonne a ici trouvé un coloriage minimal et optimal mais différent de celui proposé plus haut.

- Comment peut-on vérifier que c'est un coloriage minimal ? Il faudrait essayer chaque changement de couleur (ce n'est pas simple)
- Et comment vérifier l'optimalité ? Il faudrait tester *tous* les coloriages à `c-1` couleurs (si celui là en a `c`) et montrer qu'aucun ne convient (ce n'est pas simple non plus, il y a beaucoup de coloriages possibles).

Note : une première indication est qu'ici on a utilisé `c=3` couleurs avec un graphe de degré maximum $\delta_{\max} = 3$. *)

(* Pour un contre exemple : *)

(* In[22]: *)


let g2 : graphe = [|
    [1; 2; 3; 4; 5]; (* voisins de 0 *)
    [0; 2; 3; 4; 5]; (* voisins de 1 *)
    [0; 1; 3; 4]; (* voisins de 2 *)
    [0; 1; 2; 5]; (* voisins de 3 *)
    [0; 1; 2];  (* voisins de 4 *)
    [0; 1; 3]  (* voisins de 5 *)
|];;

(* In[23]: *)


let coloriage6 = coloriage_glouton g2;;
let _ = verifie_coloriage g2 coloriage6;;

(* In[24]: *)


let coloriage6 = coloriage_glouton_pas_trie g2;;
let _ = verifie_coloriage g2 coloriage6;;

(* Et en changeant l'ordre des sommets : *)

(* In[26]: *)


let g3 : graphe = [|
    [5; 4; 2];  (* voisins de 0 *)
    [5; 4; 3];  (* voisins de 1 *)
    [5; 4; 3; 0]; (* voisins de 2 *)
    [5; 4; 2; 1]; (* voisins de 3 *)
    [5; 3; 2; 1; 0]; (* voisins de 4 *)
    [4; 3; 2; 1; 0] (* voisins de 5 *)
|];;

(* In[29]: *)


let coloriage6 = coloriage_glouton g3;;
let _ = verifie_coloriage g3 coloriage6;;

(* Là on vérifie que l'ordre des sommets est important, par exemple si on ne trie pas les sommets par degrés décroissants, l'algorithme glouton trouche un coloriage sous-optimal (avec 5 couleurs ici) : *)

(* In[28]: *)


let coloriage6 = coloriage_glouton_pas_trie g3;;
let _ = verifie_coloriage g3 coloriage6;;

(* Je n'ai pas trouvé de contre exemple qui donne un coloriage sous-optimal pour la première version (avec tri par degrés décroissants) de l'algorithme.
Si vous en avez un, [envoyez le moi !](https://perso.crans.org/besson/contact/) *)

(* ----
## Conclusion

Fin. À la séance prochaine. Le dernier TP (TP8) traitera de programmation logique (en mai).

> En attendant, essayez de finir ce sujet TP#7 et aussi la partie 2 (avec Python) du TP#6 sur le $\lambda$-calcul. *)
