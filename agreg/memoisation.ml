(* 
    Mémoïsation en OCaml
 *)

let sprintf = Format.sprintf;;
let sleep n = Sys.command (sprintf "sleep %i" n);;


(* Deux exemples de fonctions à mémoïser *)

let f1 n =
    ignore (sleep 3);
    n + 2
;;

let _ = f1 10;; (* 13, après 3 secondes *)

let f2 n =
    ignore (sleep 4);
    n * n
;;

let _ = f2 10;; (* 100, après 4 secondes *)


(* Implémentation générique d'un décorateur de mémoïsation *)

let memo f =
      let memoire = Hashtbl.create 128 in (* taille 128 par defaut *)
      let memo_f n =
          if Hashtbl.mem memoire n then
             Hashtbl.find memoire n
          else begin
             let res = f n in
             Hashtbl.add memoire n res;
             res
          end
      in
      memo_f
;;

let memo_f1 = memo f1 ;;
let _ = memo_f1 10 ;; (* 3 secondes *)
let _ = memo_f1 10 ;; (* instantanné *)

let memo_f2 = memo f2 ;;
let _ = memo_f2 10 ;; (* 4 secondes *)
let _ = memo_f2 10 ;; (* instantanné *)

(* Et voilà ! *)
