(*
This OCaml script was exported from a Jupyter notebook
using an open-source software (under the MIT License) written by @Naereen
from https://github.com/Naereen/Jupyter-Notebook-OCaml
This software is still in development, please notify me of a bug at
https://github.com/Naereen/Jupyter-Notebook-OCaml/issues/new if you find one
*)

(* # Table of Contents
 <p><div class="lev1 toc-item"><a href="#TP-7---Programmation-pour-la-préparation-à-l'agrégation-maths-option-info" data-toc-modified-id="TP-7---Programmation-pour-la-préparation-à-l'agrégation-maths-option-info-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>TP 7 - Programmation pour la préparation à l'agrégation maths option info</a></div><div class="lev2 toc-item"><a href="#Algorithme-de-Dijkstra---avec-des-files-non-mutables" data-toc-modified-id="Algorithme-de-Dijkstra---avec-des-files-non-mutables-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Algorithme de Dijkstra - avec des files non mutables</a></div><div class="lev3 toc-item"><a href="#Files-de-priorité-min" data-toc-modified-id="Files-de-priorité-min-111"><span class="toc-item-num">1.1.1&nbsp;&nbsp;</span>Files de priorité min</a></div><div class="lev3 toc-item"><a href="#Graphe-par-tableau-de-listes-d'adjacence" data-toc-modified-id="Graphe-par-tableau-de-listes-d'adjacence-112"><span class="toc-item-num">1.1.2&nbsp;&nbsp;</span>Graphe par tableau de listes d'adjacence</a></div><div class="lev3 toc-item"><a href="#Exemple-de-visualisation-de-graphe" data-toc-modified-id="Exemple-de-visualisation-de-graphe-113"><span class="toc-item-num">1.1.3&nbsp;&nbsp;</span>Exemple de visualisation de graphe</a></div><div class="lev3 toc-item"><a href="#Dijkstra" data-toc-modified-id="Dijkstra-114"><span class="toc-item-num">1.1.4&nbsp;&nbsp;</span>Dijkstra</a></div><div class="lev2 toc-item"><a href="#Algorithme-de-Dijkstra---avec-des-files-mutables" data-toc-modified-id="Algorithme-de-Dijkstra---avec-des-files-mutables-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Algorithme de Dijkstra - avec des files mutables</a></div><div class="lev3 toc-item"><a href="#Files-de-priorité-min-mutables" data-toc-modified-id="Files-de-priorité-min-mutables-121"><span class="toc-item-num">1.2.1&nbsp;&nbsp;</span>Files de priorité min mutables</a></div><div class="lev3 toc-item"><a href="#Dijkstra,-2ème-version" data-toc-modified-id="Dijkstra,-2ème-version-122"><span class="toc-item-num">1.2.2&nbsp;&nbsp;</span>Dijkstra, 2ème version</a></div><div class="lev3 toc-item"><a href="#Exemple" data-toc-modified-id="Exemple-123"><span class="toc-item-num">1.2.3&nbsp;&nbsp;</span>Exemple</a></div><div class="lev2 toc-item"><a href="#Arbres-couvrants-de-poids-minimal" data-toc-modified-id="Arbres-couvrants-de-poids-minimal-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Arbres couvrants de poids minimal</a></div><div class="lev3 toc-item"><a href="#Algorithme-de-Prim" data-toc-modified-id="Algorithme-de-Prim-131"><span class="toc-item-num">1.3.1&nbsp;&nbsp;</span>Algorithme de Prim</a></div><div class="lev3 toc-item"><a href="#Exemple" data-toc-modified-id="Exemple-132"><span class="toc-item-num">1.3.2&nbsp;&nbsp;</span>Exemple</a></div><div class="lev2 toc-item"><a href="#Codage-de-Huffman" data-toc-modified-id="Codage-de-Huffman-14"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Codage de Huffman</a></div><div class="lev2 toc-item"><a href="#Coloration-de-graphes" data-toc-modified-id="Coloration-de-graphes-15"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Coloration de graphes</a></div><div class="lev2 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-16"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Conclusion</a></div> *)

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


let _ = dot "g1" g1 [ ];;
dot2svg "g1";;

(* In[19]: *)


Sys.command "cat g1.dot";;

(* ![](g1.svg) *)

(* Le second argument permet d'afficher un certain chemin : *)

(* In[20]: *)


let _ = dot "g2" g1 [(0,3);(3,2);(2,4)];;

(* In[21]: *)


Sys.command "cat g2.dot";;
dot2svg "g2";;

(* ![](g2.svg) *)

(* ### Dijkstra *)

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

(* ----
## Algorithme de Dijkstra - avec des files mutables

Déjà vu, on le retraite ici. *)

(* ### Files de priorité min mutables *)

(* In[24]: *)


(* file de priorité version non-mutable *)
type 'a priopqueue = (int * 'a) list ref;;

(* In[25]: *)


(* file vide *)
let vide () : 'a priopqueue = ref [ ];;

(* In[26]: *)


(* [inserer x clef q] insere l'element [x] dans la file [q]
   avec le clef [x].
   Termine avec une exception si la file contient déjà [x]  *)
let rec inserer (x:'a) (clef:int) (q:'a priopqueue) : unit =
    if List.exists (fun (_, v) -> x=v) !q
    then failwith "l'element est déjà dans la file"
    else q := (clef,x) :: !q
;;

(* In[27]: *)


(* [est_vide q] teste si la file [q] est vide *)
let est_vide (q:'a priopqueue) : bool = (!q = [ ]);;

(* In[28]: *)


(* [trouve_min_aux min_val min_clef q] renvoie un couple de clef minimale
     dans (min_val,min_clef)::q *)
let rec trouve_min_aux (min_val:'a) (min_clef:int) (q:(int*'a) list) : int * 'a =
    match q with
    | [ ] -> (min_clef,min_val)
    | (_, v) :: q when clef > min_clef -> trouve_min_aux min_val min_clef q
    | (clef, v) :: q -> trouve_min_aux v clef q
;;

(* In[29]: *)


(* [trouve_min q] renvoie un élément de clef minimale la file [q].
   Lance une exception si la liste est vide *)
let trouve_min (q:(int*'a) list) : 'a =
    match q with
    | [ ] -> failwith "trouve_min: la file est vide"
    | (clef, v) :: q -> snd (trouve_min_aux v clef q)
;;

(* In[30]: *)


(* [supprime v q] renvoie une file contenant les éléments de [q], sauf [x].
   [x] doit apparaitre une et une seule fois dans la file. *)
let rec supprime (x:'a) (q:(int*'a) list) : (int*'a) list =
    match q with
    | [ ] -> [ ]
    | (_, v) :: q when v=x -> q
    | (clef, v) :: q -> (clef,v) :: (supprime x q)
;;

(* In[31]: *)


(* [extraire_min q] renvoie un élément de q, de clef minimal,
   et met à jour la file; termine avec une exception si la file est vide  *)
let extraire_min (q:'a priopqueue) : 'a =
    if !q = [ ] then failwith "extraire_min: file vide"
    else
        let min = trouve_min !q in
        q :=  supprime min !q;
        min
;;

(* In[39]: *)


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

(* In[33]: *)


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

(* ### Exemple *)

(* In[34]: *)


let _ = dijkstra g1;;

(* ----
## Arbres couvrants de poids minimal

On ne traite que l'algorithme de Prim. L'algorithme de Kruskal n'est pas plus compliqué, il utilise une autre structure de données (Union-Find, déjà traité aussi). *)

(* ### Algorithme de Prim *)

(* In[40]: *)


let prim g =
    let q = vide () in
    let poid = Array.init g.taille (fun i ->
        if i=g.entree then 0 else max_int
    ) in
    let pere = Array.init g.taille (fun i -> i) in
    for i=0 to g.taille-1 do (* initialisation de la file *)
        inserer i poid.(i) q;
    done;
    while not (est_vide q) do
        let x = extraire_min q in
        (* on regarde les adjacents de x *)
        List.iter (fun (c,y) ->
            if poid.(y) > c
            then begin
                pere.(y) <- x;
                poid.(y) <- c;
                diminuer_clef y poid.(y) q
        end)
        g.adj.(x)
    done;
    Array.iteri (fun i p ->
        if i != p then Printf.printf " (%d, %d)\n" i p
    ) pere;
    poid, pere;
;;

(* ### Exemple *)

(* In[41]: *)


let _ = prim g1;;

(* ----
## Codage de Huffman

C'est un grand classique pour les leçons "Programmation dynamique" et "Algorithmique du texte".
Le présenter en développement sans l'avoir implémenter est difficilement pardonnable. *)

(* In[37]: *)


Printf.printf "\nTODO\n";;

(* ----
## Coloration de graphes

On a déjà travaillé sur ça en novembre. Voyons une approche gloutonne. *)

(* In[38]: *)


Printf.printf "\nTODO\n";;

(* ----
## Conclusion

Fin. À la séance prochaine. Le dernier TP8 traitera de programmation logique (en mai). *)
