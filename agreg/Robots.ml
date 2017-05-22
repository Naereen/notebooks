(*  # Texte d'oral de modélisation - Agrégation Option Informatique *)
(*  ## Préparation à l'agrégation - ENS de Rennes, 2016-17 *)
(*  - *Date* : 12 mai 2017 *)
(*  - *Auteur* : [Lilian Besson](https://GitHub.com/Naereen/notebooks/) *)
(*  - *Texte*: Annale 2008, ["Robots"](http://agreg.org/Textes/pub2008-D1.pdf) *)

(*  ## À propos de ce document *)
(*  - Ceci est une *proposition* de correction, partielle et probablement non-optimale, pour la partie implémentation d'un [texte d'annale de l'agrégation de mathématiques, option informatique](http://Agreg.org/Textes/). *)
(*  - Ce document est un [notebook Jupyter](https://www.Jupyter.org/), et [est open-source sous Licence MIT sur GitHub](https://github.com/Naereen/notebooks/tree/master/agreg/), comme les autres solutions de textes de modélisation que [j](https://GitHub.com/Naereen)'ai écrite cette année. *)
(*  - L'implémentation sera faite en OCaml, version 4+ : *)

Sys.command "ocaml -version";;


(*  ---- *)
(*  ## Question de programmation *)
(*  La question de programmation pour ce texte était donnée au milieu, en page 3 : *)

(*  > « On suppose donnés les tableaux $T_i$. Un état du système est représenté par un vecteur $U$ de longueur $n$, dont la $i$-ème composante contient la position du robot $R_i$ (sous forme du numéro $j$ du lieu $L_j$ où il se trouve). » *)

(*  > « Écrire une fonction/procédure/méthode transition qui transforme $U$ en un état suivant du système (on admettra que les données sont telles qu’il existe un état suivant). *)
(*  Simuler le système de robots pendant $n$ unités de temps. On prendra comme état initial du robot $R_i$ le premier élément du tableau $T_i$ . » *)

(*  ### Plus ou moins de liberté dans le choix de modélisation ? *)
(*  Vous remarquez que même avec une question bien précise comme celle-là, on dispose d'une relative liberté : la question n'impose pas le choix de modélisation ! *)

(*  Elle pourrait être traitée avec un automate ou graphe produit non simplifié (1ère solution ci-dessous), ou un graphe produit plus réduit (2ème solution), mais on aurait tout aussi pu utiliser une approche probabiliste, avec des chaînes de Markov par exemple (3ème solution). *)

(*  ---- *)
(*  ## Réponse à l'exercice requis, première approche *)

(*  Cette première solution, assez longue, est telle quelle celle que j'avais implémentée en novembre 2013, durant [ma préparation à l'agrégation en 2013-14](http://perso.crans.org/besson/agreg-2014/). *)

(*  Elle est assez longue, mais montre beaucoup de techniques différentes dans les fonctions intermédiaires. *)

let print = Format.printf;;


(*  ### Représentations d'un graphe *)

(*  Les sommets d'un graphe seront des entiers, et les poids des arêtes seront aussi des entiers. *)
(*  Les graphes sont stockés par liste d'adjacence. *)

type sommet = int;;

type poids = int;;

type graphe = (sommet list) * ( (sommet * poids * sommet) list);;


(*  ### Fonctions utilitaires *)

(*  Pour créer une liste de sommets. *)

(** range n = [1; 2; ...; n] *)
let range (n : int) : int list =
    let rec aux = function  (* Tail recursive : OK *)
        0 -> [] | n -> n :: (aux (n-1))
    in
    List.rev (aux n)
;;

(** Tests *)
range 14;;
range 4;;


(*  On a besoin de tester si `element` est dans le tableau `tab`, en $\mathcal{O}(n)$ si `n = Array.length tab`. *)

let arraymem (element : 'a) (tab : 'a array) : bool =
    List.mem element (Array.to_list tab)
;;

(** Tests *)
arraymem 11 (Array.of_list (range 12));;  (* true *)
arraymem 14 (Array.of_list (range 12));;  (* false *)


(*  On peut onstruire un graphe en liste d'adjacence, à partir d'une matrice d'adjacence `tabs`, facilement : *)

let construire_graphe (n : int) (tabs : poids array array) : graphe =
    let sommets = range n
    and res = ref []  (** Accumulateur pour la liste des arêtes. *)
    in
    for i = 0 to n-1 do
        for j = 0 to n-1 do
            for k = 0 to n-1 do
                if ( (arraymem k tabs.(i)) && (arraymem k tabs.(j)) ) then
                    res := (i, k, j) :: !res;
            done;
        done;
    done;
    (sommets, !res);
;;


(*  > On utilise un accumulateur `res = ref []` qui est une *référence* sur une liste, d'abord vide, puis complétée petit à petit (en ajoutant une valeur en tête de liste, pour rester efficace). *)


(*  ### Automates finis et automates multiples *)

(*  On représente un *automate fini* avec le type abstrait, venant tout droit de la définition formelle mathématique, $A = < Q, I, F, \delta >$. *)

type arete = (sommet * sommet);;

type automate = (sommet list) * (sommet list) * (sommet list) * (arete list) ;;


(*  On peut calculer la liste des paires $(t_i, t_j)$ pour $t_i$,$t_j$ dans $\mathrm{tab}$ et $i < j$. *)

let liste_des_paires (tab : 'a array) : (('a * 'a) list) =
    let n = Array.length tab
    and res = ref [] in
    for i=0 to n-1 do
        for j=i+1 to n-1 do
            res := (tab.(i), tab.(j)) :: !res;
        done;
    done;
    !res @ [(tab.(n-1), tab.(0))];
;;


(*  On peut construire l'automate donné par ses sommets : *)

let construire_automate (tab: sommet array) : automate =
    ( (Array.to_list tab), [tab.(0)], [], (liste_des_paires tab) )
;;


(*  Et maintenant, on va devoir travailler avec des multi-automates, venant du produit des automates de chaque robot. *)

type multisommet = sommet list ;;
type multiarete = (multisommet * multisommet);;


(*  Le type représentant un multi automate fini est simplement $A = < QQ, II, FF, \delta' >$, où $QQ, II, FF$ sont des listes de multi-sommets, qui sont eux-mêmes des couples (des listes) de sommets. *)

type multiautomate =
    (multisommet list)     (* QQ, états *)
    * (multisommet list)   (* II, états initiaux *)
    * (multisommet list)   (* FF, états finaux *)
    * (multiarete list)    (* multi-transitions *)
;;


(*  On peut travailler avec les paires de multi-sommets et de multi-arêtes, pour construire le multi-automate. *)

let rec paires_multisommet (l1 : 'a list) (l2 : 'a list list) : 'a list list =
    match l2 with
    | [] -> []
    | a :: l2' ->
        (List.map (fun e -> (e :: a)) l1) @ (paires_multisommet l1 l2')
;;


(*  En faisant pareil avec les multi-arêtes. *)

let multisommet_of_sommet (l1 : 'a list) : 'a list list =
    List.map (fun e -> [e]) l1
;;


let rec paires_multiarete
        (l1 : ('a * 'b) list)
        (l2 : (('a list) * ('b list)) list)
        : ((('a list) * ('b list)) list) =
    match l2 with
    | [] -> []
    | (u, v) :: l2' ->
        (List.map (
            fun (uu, vv) -> (uu :: u, vv :: v)
        ) l1)
        @ (paires_multiarete l1 l2')
;;


let multiarete_of_arete (l2 : ('a * 'b) list)
    : (('a list * 'b list) list) =
    List.map (fun (u,v) -> ([u], [v])) l2
;;


(*  ### Automate produit *)
(*  Maintenant, on peut calculer explicitement l'automate produit, *sans simplification*. *)

(*  La fonction suivante est assez simple, mais longue : il s'agit juste de créer des couples d'états, pour $QQ, II, FF$ et $\delta'$. *)

let rec automate_produit (autlist: automate list) : multiautomate =
    match autlist with
    | [] ->
        ( [], [], [], [] )  (** automate vide *)
    | [(q1, i1, f1, d1)] ->
        (   (** Produit d'un seul automate. *)
            (multisommet_of_sommet q1),
            (multisommet_of_sommet i1),
            (multisommet_of_sommet f1),
            (multiarete_of_arete   d1)
        )
    | (q1, i1, f1, d1) :: autlist2 ->
        (* Pas récursif terminal, pas grave *)
        let (qq2, ii2, ff2, dd2) = (automate_produit autlist2) in
        (
            (paires_multisommet q1 qq2),
            (paires_multisommet i1 ii2),
            (paires_multisommet f1 ff2),
            (paires_multiarete  d1 dd2)
        )
;;


(*  Calculer l'automate produit depuis tabs est rapide : *)

let construire_automate_produit (tabs: sommet array array) : multiautomate =
  automate_produit (Array.to_list (Array.map construire_automate tabs))
;;


(*  On peut ensuite vérifier s'il sera bloqué, simplement en vérifiant qu'il existe (au moins) une transition à chaque état. *)

let nest_pas_bloque (maut : multiautomate) : bool =
  let (qq, _, _, dd) = maut in
  List.for_all (fun qi -> List.mem_assoc qi dd) qq
;;


(*  ### Transitions et simulations *)

(*  La fonction suivante lit la table de multi-transition $\delta'$ du multi-automate et renvoie l'état correspondant à $u$, l'état courant. *)

(*  En fait, c'est la fonction cruciale de la solution implémentée dans cette partie. *)

(*  Notez que deux tests sont effectués, avec `assert`, pour être sûr qu'une transition existe (et d'après la modélisation et les hypothèses du texte, une unique transition existe à chaque état). *)

let transition (maut: multiautomate) u =
    (** On ignore les états initiaux et finaux... *)
    let (qq, _, _, dd) = maut in
    assert (List.mem u qq);
    assert (List.mem_assoc u dd);
    List.assoc u dd
;;


(*  On a besoin de récupérer l'état initial. *)

let etat_initial tabs = Array.to_list (Array.map (fun tab -> tab.(0)) tabs) ;;


(*  Pour visualiser les transitions, on va afficher une représentation simplifiée de l'automate, à l'étape $i$. *)

let affiche_etat i u =
  print "Etape i = %i: " i;
  List.iter (fun x -> (print "%i, " x)) u;
  print "\n"
;;


(*  ### Il faut simuler l'évolution de l'automate durant n étapes *)

(*  C'est très facile, il suffit d'enchaîner $n$ fois la fonction `transition`. *)
(*  Pas besoin d'une fonction récursive, une boucle `for` suffit ! *)

let simule (n : int) (tabs : sommet array array) () : multisommet =
    print "\nDébut simulations :  \n";
    let maut = construire_automate_produit tabs in
    let u = ref (etat_initial tabs) in
    for i = 0 to n-1 do
        affiche_etat i !u;
        print "  --> transition\n";
        u := transition maut !u;
    done;
    affiche_etat n !u;
    !u
;;


(*  ### Exemple 1 *)

(*  On commence avec le premier exemple du texte, avec trois robots $R_1, R_2, R_3$, qui ont comme tableaux de rendez-vous $T_1 = [1, 3]$, $T_2 = [2, 1]$ et $T_3 = [3, 2]$. *)

(*  Ce système n'est pas bloqué, mais aucun rendez-vous n'est réalisé. *)

(*  ![Premier exemple de robots](images/robots_exemple1.png) *)

print "\nSimulation 1:\n=============";;
let n = 3
and tabs = [| [|1; 3|]; [|2; 1|]; [|3; 2|]|]
in simule n tabs ();;


(*  ### Exemple 2 *)

(*  On peut aussi s'intéresser au second exemple du texte : *)

(*  ![Second exemple de robots](images/robots_exemple2.png) *)

(*  Là aussi, aucun rendez-vous n'est réalisé si on commence aux mauvais états. *)

print "\nSimulation 2:\n=============";;
let n = 4
and tabs = [| [|1; 4|]; [|2; 1|]; [|3; 2|]; [|4; 3|]|]
in simule n tabs ();;


(*  Par contre, avec l'ordre des rendez-vous par indice croissants : *)

print "\nSimulation 3:\n=============";;
let n = 4
and tabs = [| [|1; 4|]; [|1; 2|]; [|2; 3|]; [|3; 4|]|]
in simule n tabs ();;


(*  - Là, le rendez-vous $L_1$ est effectué, une fois sur deux (entre $R_1$ et $R_2$), et le rendez-vous $L_4$ est effectué, une fois sur deux aussi (entre $R_1$ et $R_4$). *)
(*  - Les rendez-vous $L_2$ et $L_3$ ne sont pas effectués. *)

(*  ---- *)
(*  ## Réponse à l'exercice requis, seconde approche *)
(*  > Merci à Romain Dubourg (2017) pour son code, à peine modifié ici. *)

(*  Cette deuxième solution est bien plus concise, en utilisant une approche plus directe. *)

(*  ### Choix des structures de données *)
(*  En utilisant des tableaux, `int array`, au lieu de listes, pour représenter les états $u$ on peut modifier l'état *en place* ! *)

type etat = int array;;
type liste_rdv = (int array) array;;


(*  On peut facilement trouver la première position de `x` dans une liste et dans un tableau et `-1` sinon. *)

let trouve (x : int) (a : int list) : int =
    let rec aux (x : int) (a : int list) (i : int) : int =
        match a with
        | [] -> -1
        | t :: _ when (t = x) -> i
        | _ :: q -> aux x q (i+1)
    in
    aux x a 0
;;


let trouve_array (x : int) (a : int array) : int =
    trouve x (Array.to_list a)
;;


(*  On a besoin de pouvoir obtenir la liste des paires de robots pouvant réaliser un rendez-vous. *)

let rdv (u : etat) : ((int * int) list) = 
    let n = Array.length u in
    let ls = ref [] in
    for k = 0 to n - 1 do
        let i = trouve_array u.(k)
            (Array.sub u (k + 1) (n - (k + 1)))
        in
        if i >= 0 then
            ls := (k, i + k + 1) :: !ls;
    done;
    !ls
;;


(*  Étant donné un état et une paire de robots pouvant réaliser un rendez-vous, la fonction suivante le réalise, en modifiant *en place* l'état $u$. *)

(*  C'est bien plus simple que de traiter avec une approche fonctionnelle. *)

(*  Pour une fonction comme ça, il faut absolument : *)

(*  - utiliser des variables intermédiaires, *)
(*  - et des noms de variables un peu explicites (attention aux `1`, `i`, `I` et `l` qui se ressemblent beaucoup au tableau !). *)

let realise_rdv (xy : int * int) (u : etat) (lr : liste_rdv) : etat =
  let x, y = xy in
  let ux = u.(x) and uy = u.(y) in
  let rx, ry = lr.(x), lr.(y) in
  u.(x) <- rx.(((trouve_array ux rx) + 1) mod (Array.length rx));
  u.(y) <- ry.(((trouve_array uy ry) + 1) mod (Array.length ry));
  u
;;


(*  ### Fonction `transition` *)
(*  Et enfin, on calcule l'état suivant $u_2$ à partir de l'état $u_1$, en appliquant la fonction `realise_rdv` à chaque état qui peut être modifié. *)

let transition (u1 : etat) (l : liste_rdv) : etat =
    let ls = rdv u1 in
    let rec aux (u2 : etat) (l1 : (int * int) list) (l2 : liste_rdv) : etat =
        match l1 with
        | [] -> u2
        | t :: q -> aux (realise_rdv t u2 l2) q l2
    in
    aux u1 ls l
;;


(*  On effectue `n` transitions successives, non pas avec une approche récursive (qui ne serait pas récursive terminale, et donc avec une mémoire de pile d'appel linéaire en $\mathcal{O}(n)$), mais avec une simple boucle `for`. *)

let rec n_transitions_trop_couteux (u : etat) (l : liste_rdv) (n : int) : etat =
    if (n = 0) then
        u
    else
        n_transitions_trop_couteux (transition u l) l (n-1)
;;


let n_transitions (u : etat) (l : liste_rdv) (n : int) : etat =
    let u0 = ref u in
    for _ = 1 to n do
        u0 := transition u l  (* u est changé en place *)
    done;
    !u0
;;


(*  ### Plein d'exemples *)

(*  Avec l'exemple donné à l'oral, qui est un peu différent de celui du texte. *)

(*  Quatre robots, $R_0$, $R_1$, $R_2$, $R_3$, ont comme liste de rendez-vous successifs, $T_0 = [0, 1, 2]$, $T_1 = [0]$, $T_2 = [1, 3]$ et $T_3 = [2, 3]$. *)

let ex1 = [| [|0; 1; 2|]; [|0|]; [|1; 3|]; [|2; 3|] |];;

let ex1_1 = [| 0; 0; 1; 2 |];;
let _ = n_transitions ex1_1 ex1 3;;


(*  C'est trivial, mais il peut être utile de vérifier que `n_transitions 3` fait pareil que trois appels à `transition` : *)

let ex1_1 = [| 0; 0; 1; 2 |];;
let _ = transition ex1_1 ex1;;
let _ = transition ex1_1 ex1;;
let _ = transition ex1_1 ex1;;


(*  Avec un autre état initial : *)

let ex1_2 = [| 0; 0; 3; 2 |];;

let _ = transition ex1_2 ex1;;
let _ = transition ex1_2 ex1;; (* On bloque !*)
let _ = transition ex1_2 ex1;; (* On bloque !*)


(*  Et avec encore un autre état initial : *)

let ex1_3 = [| 0; 0; 3; 3 |];;

let _ = transition ex1_3 ex1;;
let _ = transition ex1_3 ex1;;
let _ = transition ex1_3 ex1;; (* On a un cycle de taille 3 *)
let _ = transition ex1_3 ex1;;


(*  Enfin, un dernier exemple, pour visualiser le fonctionnement de la fonction `realise_rdv`. *)

let ex = [| 1; 2; 1; 4; 4 |];;
let _ = rdv ex 


let u = [| 0; 0; 1 |];;
let l = [| [|0; 2|]; [|1; 2|]; [|2; 0|] |];;
let _ = realise_rdv (0, 1) u l


(*  ---- *)
(*  ## Conclusion *)

(*  Voilà pour la question obligatoire de programmation : *)

(*  - on a adopté la modélisation du texte (dans la 1ère approche) et aussi une autre modélisation (2ème approche), *)
(*  - on a traité l'exemple du texte, ou un exemple très proche. *)
(*  - on a fait des exemples et *on les garde* dans ce qu'on présente au jury. *)
(*  - on n'a pas essayé de faire *un peu plus*, mais on aurait très bien pu (avec les chaînes de Markov ou les temps d'attentes, par exemple). *)

(*  > Bien-sûr, ce petit notebook ne se prétend pas être une solution optimale, ni exhaustive. *)

(*  > Merci à Romain pour son implémentation, sur laquelle la seconde approche est basée. *)

(* ---- *)
(* ## Une autre approche avec des chaînes de Markov *)

(* Voici une troisième modélisation, avec des matrices et des [chaînes de Markov](https://fr.wikipedia.org/wiki/Cha%C3%AEne_de_Markov). *)

(* L'idée de base vient de l'observation suivante : ajouter de l'aléa dans les déplacements des robots devraient permettre de s'assurer (avec forte probabilité) que tous les rendez-vous sont bien effectués. *)

(* ### Opérations matrice-vecteur (inutile ici) *)
(* Avec un produit scalaire simple, et un appel à `Array.init`, on peut facilement effectuer un produit matrice-vecteur. *)

(* $$ \mathrm{dot}(\mathbf{x}, \mathbf{y}) := \mathbf{x} . \mathbf{y} = \sum_{i=0}^{n-1} x_i \times y_i $$ *)
(* $$ \mathbf{A} \times \mathbf{x} := \begin{bmatrix} *)
(*     A_0 . \mathbf{x} \\ *)
(*     \dots \\ *)
(*     A_{n-1} . \mathbf{x} \\ *)
(* \end{bmatrix}. $$ *)

let dot (x : float array) (y : float array) : float =
    let n = Array.length x in
    let acc = ref 0. in
    for i = 0 to n - 1 do
        acc := (!acc) +. (x.(i) *. y.(i))
    done;
    !acc
;;


dot [| 1.; 2.; 3. |] [| 1.; 2.; 3. |];;
(* = 14 = 1 * 1 + 2 * 2 + 3 * 3 = 1 + 4 + 9 *)


(* Et maintenant pour le produit matrice-vecteur : *)

let right_mult (a : float array array) (x : float array) : float array =
    Array.init (Array.length x) (fun i ->
        dot a.(i) x
    )
;;


(* Par exemple, définissons une matrice et un vecteur, utilisés ici et après pour nos tests. *)

let a = [|
            [| 0.4; 0.3; 0.3 |];
            [| 0.3; 0.4; 0.3 |];
            [| 0.3; 0.3; 0.4 |]
    |]
;;

let x = [| 0.; 1.; 0. |];;  (* etat 2 *)
let y = [| 0.2; 0.3; 0.5 |];;


right_mult a x;;
right_mult a y;;


(* ### Échantillonage pondéré *)
(* Le module [`Random`](http://caml.inria.fr/pub/docs/manual-ocaml/libref/Random.html) va être utile. *)

Random.self_init ();;


(* Etant donné une distribution discrète $\pi = (\pi_1,\dots,\pi_N)$ sur $\{1,\dots,N\}$, la fonction suivante permet de générer un indice $i$ tel que *)
(* $$ \mathbb{P}(i = k) = \pi_k, \forall k \in \{1,\dots,N\}.$$ *)

let weight_sampling (pi : float array) () =
    let p = Random.float 1. in
    let i = ref (-1) in
    let acc = ref 0. in
    while !acc < p do
        incr i;
        acc := (!acc) +. pi.(!i);
    done;
    !i
;;


(* Par exemple, tirer 100 échantillons suivant la distribution $\pi = [0.5, 0.1, 0.4]$ devrait donner environ $50$ fois $0$, $10$ fois $1$ et $40$ fois $2$ : *)

let compte (a : 'a array) (x : 'a) : int =
    Array.fold_left (fun i y -> if y = x then i + 1 else i) 0 a
;;
    
let echantillons = Array.init 100
    (fun i -> weight_sampling [| 0.5; 0.1; 0.4 |] ())
;;

compte echantillons 0;;
compte echantillons 1;;
compte echantillons 2;;


(* ### Simuler une étape d'une chaîne de Markov ? *)
(* On peut utiliser cette fonction pour suivre une transition, aléatoire, sur une chaîne de Markov. *)

let markov_1 (a : float array array) (i : int) : int =
    let pi = a.(i) in
    weight_sampling pi ()
;;


(* Avec l'exemple définit ci-dessus, on peut voir le résultat de $100$ transitions différentes depuis l'état $0$ : *)

for _ = 0 to 100 do
    print_int (markov_1 a 0);
done;;


(* On peut suivre plusieurs transitions : *)

let markov_n (a : float array array) (etat : int) (n : int) : int =
    let u = ref etat in
    for _ = 0 to n-1 do
        u := markov_1 a !u;
    done;
    !u
;;


markov_n a 0 10;;


(* Et pour plusieurs robots, c'est pareil : chaque robots a un état (`robots.(i)`) et une matrice de transition (`a.(i)`) : *)

let markovs_n (a : float array array array) (robots : int array) (n : int) : int array =
    Array.mapi (fun i u -> markov_n a.(i) u n) robots
;;


(* Si par exemple chaque état a la même matrice de transition : *)

markovs_n [|a; a; a|] [|0; 1; 2|] 10;;


(* ### Modéliser nos robots avec des chaînes de Markov *)

(* Plutôt que d'imposer à chaque robot un ordre fixe de ses rendez-vous, on va leur donner une probabilité uniforme d'aller, après un rendez-vous, à n'importe lequel de leur rendez-vous. *)

(* - Cela demande de transformer la liste $T_1,\dots,T_n$ de rendez-vous en $n$ matrices de transition de chaînes de Markov, une par robot. *)
(* - Et ensuite de simuler chaque chaîne de Markov, parant d'un état initial $T_i[0]$. *)

(* Fonctions utiles *)
Array.init;;
Array.make_matrix;;
Array.iter;;


let mat_proba_depuis_rdv (ts : int array array) : (float array array) array =
    let n = Array.length ts in
    let a = Array.init n (fun i -> Array.make_matrix n n 0.) in
    for i = 0 to n-1 do
        (* Pour le robot R_i, ses rendez-vous T_i sont ts.(i) *)
        let r = ts.(i) in
        let m = Array.length r in
        let p_i = 1. /. (float_of_int m) in
        (* Pour chaque rendez-vous L_j dans T_i,
           remplir a.(j).(k) par 1/m,
           et aussi a.(k).(j) par 1/m
           pour chaque autre k dans L_j
        *)
        for j = 0 to m-1 do
            for k = 0 to m-1 do
                a.(i).(r.(j)).(r.(k)) <- p_i;
                a.(i).(r.(k)).(r.(j)) <- p_i;
            done;
        done;
    done;
    a
;;


(* Avec les fonctions précédentes, on peut faire évoluer le système. *)

let simule_markov_robots (ts : int array array)
    (etats : int array) (n : int)
    : int array =
    let a = mat_proba_depuis_rdv ts in
    markovs_n a etats n
;;


(* ### Exemple 1 *)
(* On commence avec le premier exemple du texte, avec trois robots $R_1, R_2, R_3$, qui ont comme tableaux de rendez-vous $T_1 = [1, 3]$, $T_2 = [2, 1]$ et $T_3 = [3, 2]$. *)

(* Ce système n'est pas bloqué, mais aucun rendez-vous n'est réalisé avec l'approche statique. *)
(* L'approche probabiliste permettra, espérons, de résoudre ce problème. *)

(* ![Premier exemple de robots](images/robots_exemple1.png) *)

let rdv = [| [|0; 2|]; [|1; 0|]; [|2; 1|]|] ;;


(* On peut écrire une fonction qui récupère l'état initial dans lequel se trouve chaque robot (le texte donnait comme convention d'utiliser le premier de chaque liste). *)

let premier_etat (rdvs : int array array) : int array =
    Array.init (Array.length rdvs) (fun i -> rdvs.(i).(0))
;;


let etat = premier_etat rdv;;


(* On vérifie la matrice de transition produite par `mat_proba_depuis_rdv` : *)

mat_proba_depuis_rdv rdv;;


(* On peut vérifier que ces chaînes de Markov représentent bien le comportement des robots, par exemple le premier robot $R_1$ a $T_1 = [1, 3]$, donc il alterne entre l'état $0$ et $2$, avec la matrice de transition *)
(* $$ \mathbf{A}_i := \begin{bmatrix} *)
(*     1/2 & 0 & 1/2 \\ *)
(*     0 & 0 & 0 \\ *)
(*     1/2 & 0 & 1/2 *)
(* \end{bmatrix}. $$ *)

(* Et enfin on peut simuler le système, par exemple pour juste une étape, plusieurs fois (pour bien visualiser). *)

simule_markov_robots rdv etat 0;;  (* rien à faire ! *)


simule_markov_robots rdv etat 1;;


(* Pour mieux comprendre le fonctionnement, on va afficher les états intermédiaires. *)

let print = Printf.printf;;


let affiche_etat (etat : int array) =
    Array.iter (fun u -> print "%i " u) etat;
    print "\n";
;;


affiche_etat etat;;


let u = ref etat in
for _ = 0 to 10 do
    affiche_etat !u;
    u := simule_markov_robots rdv !u 1;
done;;


(* On constate que des rendez-vous ont bien été effectués ! *)
(* Pas à chaque fois, mais presque. *)

(* En tout cas, ça fonctionne mieux que l'approche naïve, peu importe l'état initial. *)

let u = ref [| 0; 1; 1 |] in
for _ = 0 to 10 do
    affiche_etat !u;
    u := simule_markov_robots rdv !u 1;
done;;


(* Sur 11 états, le rendez-vous 0 a été fait 1 fois, le 1 a été fait 4 fois, et le 2 a été fait 4 fois aussi. Soit 9 sur 11 étapes utiles ! Pas mal ! *)

(* ### Exemple 2 *)
(* Puis le second exemple : *)

(* ![Premier exemple de robots](images/robots_exemple2.png) *)

let rdv = [| [|0; 3|]; [|0; 1|]; [|1; 2|]; [|2; 3|] |];;


let etat = premier_etat rdv;;


(* On vérifie la matrice de transition produite par `mat_proba_depuis_rdv` : *)

mat_proba_depuis_rdv rdv;;


(* Et enfin on peut simuler le système, par exemple pour juste une étape, plusieurs fois (pour bien visualiser). *)

simule_markov_robots rdv etat 0;;  (* rien à faire ! *)


simule_markov_robots rdv etat 1;;


let u = ref etat in
for _ = 0 to 10 do
    affiche_etat !u;
    u := simule_markov_robots rdv !u 1;
done;;


(* Sur 11 états, le rendez-vous 0 a été fait 5 fois, le 1 a été fait 2 fois, le 2 a été fait 3 fois, et le 3 a été fait 3 fois aussi. *)
(* Soit plus d'un rendez-vous par étape réussi en moyenne, et tous les rendez-vous ont été vus. *)

(* ### Conclusion de cette approche par des chaînes de Markov *)

(* On ne pas en faire plus, mais cela suffit de montrer la pertinence de cette autre approche. *)


(* > Merci d'avoir lu jusque là ! *)

(* ---- *)
(* N'hésitez pas à aller voir [ce dépôt GitHub](https://GitHub.com/Naereen/notebooks/) pour d'autres notebooks, notamment [cette page](https://nbviewer.jupyter.org/github/Naereen/notebooks/tree/master/agreg/) pour d'autres notebooks corrigeant des textes de modélisation (option D, informatique théorique) pour l'agrégation de mathématiques. *)
