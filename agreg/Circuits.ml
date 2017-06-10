(* # Texte d'oral de modélisation - Agrégation Option Informatique *)

(* ## Préparation à l'agrégation - ENS de Rennes, 2016-17 *)

(* - *Date* : 29 mai 2017 *)
(* - *Auteur* : [Lilian Besson](https://GitHub.com/Naereen/notebooks/) *)
(* - *Texte*: [Circuits (public2010-D1)](http://agreg.org/Textes/public2010-D1.pdf) *)

(* ## À propos de ce document *)

(* - Ceci est une *proposition* de correction, partielle et probablement non-optimale, pour la partie implémentation d'un [texte d'annale de l'agrégation de mathématiques, option informatique](http://Agreg.org/Textes/). *)
(* - Ce document est un [notebook Jupyter](https://www.Jupyter.org/), et [est open-source sous Licence MIT sur GitHub](https://github.com/Naereen/notebooks/tree/master/agreg/), comme les autres solutions de textes de modélisation que [j](https://GitHub.com/Naereen)'ai écrite cette année. *)
(* - L'implémentation sera faite en OCaml, version 4+ : *)


Sys.command "ocaml -version";;


(* > Notez que certaines fonctions des modules usuels [`List`](http://caml.inria.fr/pub/docs/manual-ocaml/libref/List.html) et [`Array`](http://caml.inria.fr/pub/docs/manual-ocaml/libref/List.html) ne sont pas disponibles en OCaml 3.12. *)
(* > J'essaie autant que possible de ne pas les utiliser, ou alors de les redéfinir si je m'en sers. *)

(* ---- *)

(* ## Question de programmation *)

(* La question de programmation pour ce texte était donnée en page 6, et était assez courte : *)

(* > "Écrire un programme prenant en entrée deux nombres $a$, $b$, représentés par des écritures en base $B$ avec des chiffres signés entre $-\beta$ et $\beta$, et retournant un résultat ternaire indiquant si $a < b$, si $a = b$ ou si $a > b$. On supposera que $\beta < B < 2 \beta$, et que les écritures de $a$ et $b$ ont même longueur." *)

(* ---- *)

(* ## Réponse à l'exercice requis *)

(* ### Structure de données *)

(* Pour représenter ces entiers, on stocke leur base et le tableau de leur coefficients. *)


type entier = {
    base : int;
    t : int array
}
;;


(* ### Exemples *)


let quatre = {
    base = 10;
    t = [| 4 |]
}


(* Le "bit" de poids faible est, par convention du texte, à gauche au début du tableau : *)


let quarantedeux = {
    base = 10;
    t = [| 2; 4 |]
}


(* Avec l'exemple du texte : *)


let n2006 = {
    base = 10;
    t = [| 6; 0; 0; 2 |]
}



let n2006 = {
    base = 10;
    t = [| 6; 0; 0; 2 |]
}



let n2006_2 = {
    base = 10;
    t = [| -4; 1; 0; 2 |]
}



let n2006_3 = {
    base = 10;
    t = [| 6; 0; 0; -8; 1 |]
}



let n2006_4 = {
    base = 10;
    t = [| -4; 1; 0; -8; 1 |]
}


(* ### Fonctions intermédiaires *)

(* Caml, dans sa toute beauté, ne permet pas de calculer $x^k$ facilement si $x$ est entier... *)


let rec puissance x k = 
    match k with
    | 0 -> 1
    | 1 -> x
    | k when k mod 2 = 0 ->
        (* x^k = x^(k/2 * 2) = (x^2)^(k/2) *)
        puissance (x * x) (k / 2)
    | k when k mod 2 = 1 ->
        (* x^k = x^((k-1)/2 * 2 + 1) = x * (x^2)^((k-1)/2) *)
        x * (puissance (x * x) ((k - 1) / 2))
;;



puissance 10 0;;
puissance 10 1;;
puissance 10 2;;
puissance 10 3;;
puissance 10 4;;


(* On va convertir un entier représenté sous cette forme en un entier machine de Caml : *)


let valeur {base=b; t=t} =
    let v = ref 0 in
    let n = Array.length t in
    for k = 0 to n - 1 do
        v := !v + (t.(k) * (puissance b k))
    done;
    !v
;;



valeur quatre;;



valeur quarantedeux;;



valeur n2006;;
valeur n2006_2;;
valeur n2006_3;;
valeur n2006_4;;


(* ### Résolution *)

(* Le texte ne demandait *pas* une approche particulièrement maligne, donc on va naïvement répondre à la question : on convertit les deux entiers en leur valeur, on les compare et VOILÀ. *)


let compare_entiers (a : entier) (b : entier) : int =
    let va = valeur a in
    let vb = valeur b in
    compare va vb
;;



compare_entiers quatre quarantedeux;;
compare_entiers quarantedeux quatre;;
compare_entiers quatre quatre;;
compare_entiers quarantedeux quarantedeux;;



compare_entiers n2006 quarantedeux;;


(* ---- *)
(* ## Bonus ? *)

(* <center><span style="color:red; font-size: xx-large;">FLEMME</span></center> *)

(* ---- *)
(* ## Conclusion *)

(* Voilà pour la question obligatoire de programmation : *)

(* - c'était facile. *)
(* - on a pas essayé d'en faire plus. *)

(* > Bien-sûr, ce petit notebook ne se prétend pas être une solution optimale, ni exhaustive. *)
