
Sys.command "ocaml -version";;

(** Un échange T[i] <-> T[j]. Utilise une valeur temporaire *)
let swap tab i j =
    let tmp = tab.(i) in
    tab.(i) <- tab.(j);
    tab.(j) <- tmp
;;

let tri_bulle cmp tab =
    let n = Array.length tab in
    for i = n - 1 downto 1 do
        for j = 0 to i - 1 do
            if cmp tab.(j + 1) tab.(j) < 0 then
                swap tab (j + 1) j;
        done
    done
;;

let tri_bulle_opt cmp tab =
    let n = Array.length tab in
    let i = ref 0 in
    let last_swap = ref (-1) in
    while !i < n - 1 do
        (* séquence d'échanges sur T[i..n]: *)
        last_swap := n - 1;
        for j = n-1 downto !i + 1 do
            if cmp tab.(j) tab.(j-1) < 0 then begin
                swap tab j (j-1);
                last_swap := j - 1
            end;
            (* i avance "plus vite" :*)
            i := !last_swap + 1;
        done
    done
;;

(** Taille max des éléments dans les tableaux aléatoires *)
let maxint = int_of_float(1e3);;

(** Créer un tableau aléatoire. En O(n). *)
let rand_array length =
    Array.init length (fun _ -> Random.int maxint)
;; 

(** Vérifie que chaque élément du tableau n'y est qu'une seule fois (test l'égalité <> et pas !==).
    Mal codé, en O(n^2). *)
let isInjArray tab =
    try begin
        Array.iteri (fun i x -> 
            (Array.iteri (fun j y -> 
                assert( (x<>y) || (i=j) ) 
            ) tab) 
        ) tab;
        true
        end
    with _ -> false
;;

(** En moyenne, est en O(n^2) si [maxint] est bien plus grand que [n]. *)
let rand_array_inj = function
    | 0 -> [||]
    | length ->
        let tab = ref (rand_array length) in
        while not(isInjArray (!tab)) do
            tab := rand_array length;
        done;
        !tab
;;

rand_array_inj 12;;

rand_array_inj 12;;

rand_array_inj 12;;

let print = Printf.printf;; 

let testtri mysort cmp length nbrun () =
    print "Test d'un tri, %i simulations avec des tableaux de longueur %i.\n " nbrun length;
    for i = 0 to nbrun - 1 do
        let t1 = rand_array length in
        let t2 = Array.copy t1 in
        mysort cmp t1;
        Array.fast_sort cmp t2;
        try assert( t1 = t2 ) with _ -> begin
            print "Avec des tableaux de taille %i, le test numéro %i a échoué." length i;
            Format.printf "@[t1=[|"; Array.iter (fun i -> Format.printf " %i;" i) t1; Format.printf "|]@]@ ";
            Format.printf "@[t2=[|"; Array.iter (fun i -> Format.printf " %i;" i) t2; Format.printf "|]@]@ ";
        end;
    done;
    flush_all ();
;;

testtri Array.sort compare 10 10 ();;

testtri tri_bulle compare 10 10 ();;

testtri tri_bulle_opt compare 10 10 ();;

testtri tri_bulle compare 100 1000 ();;

let tri_cocktail cmp tab =
    let n = Array.length tab in
    let echange = ref true in
    while !echange do
        echange := false;
        (* Parcours croissant *)
        for j = 0 to n - 2 do
            if cmp tab.(j + 1) tab.(j) < 0 then begin
                swap tab (j + 1) j;
                echange := true
            end;
        done;
        (* Parcours decroissant *)
        for j = n - 2 downto 0 do
            if cmp tab.(j + 1) tab.(j) < 0 then begin
                swap tab (j + 1) j;
                echange := true
            end;
        done;
    done;
;;

let tri_cocktail_opt cmp tab =
    let n = Array.length tab in
    let echange = ref true in
    let debut = ref 0 and fin = ref (n - 2) in
    while !echange do
        echange := false;
        (* Parcours croissant *)
        for j = !debut to !fin do
            if cmp tab.(j + 1) tab.(j) < 0 then begin
                swap tab (j + 1) j;
                echange := true
            end;
        done;
        fin := !fin - 1;
        (* Parcours decroissant *)
        for j = !fin downto !debut do
            if cmp tab.(j + 1) tab.(j) < 0 then begin
                swap tab (j + 1) j;
                echange := true
            end;
        done;
        debut := !debut + 1;
    done;
;;

testtri tri_cocktail compare 10 10 ();;

testtri tri_cocktail_opt compare 10 10 ();;

testtri tri_cocktail compare 100 1000 ();;

let time f =
    let t = Sys.time() in
    let res = f () in
    Printf.printf "    Temps en secondes: %fs\n" (Sys.time() -. t);
    flush_all ();
    res
;;

time (testtri Array.sort compare 100 10000);;

time (testtri tri_bulle compare 100 10000);;

time (testtri tri_bulle_opt compare 100 10000);;

time (testtri tri_cocktail compare 100 10000);;

time (testtri tri_cocktail_opt compare 100 10000);;

time (testtri Array.sort compare 1000 1000);;

time (testtri tri_bulle compare 1000 1000);;

time (testtri tri_bulle_opt compare 1000 1000);;

time (testtri tri_cocktail compare 1000 1000);;

time (testtri tri_cocktail_opt compare 1000 1000);;
