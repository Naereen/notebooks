#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Février-2021-un-mini-challenge-arithmético-algorithmique" data-toc-modified-id="Février-2021-un-mini-challenge-arithmético-algorithmique-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Février 2021 un mini challenge arithmético-algorithmique</a></span><ul class="toc-item"><li><span><a href="#Challenge-:" data-toc-modified-id="Challenge-:-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Challenge :</a></span></li><li><span><a href="#Réponse-en-Java-(par-un-de-mes-élèves-de-L3-SIF)" data-toc-modified-id="Réponse-en-Java-(par-un-de-mes-élèves-de-L3-SIF)-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Réponse en Java (par <a href="http://www.dit.ens-rennes.fr/" target="_blank">un de mes élèves de L3 SIF</a>)</a></span></li><li><span><a href="#Réponse-en-Bash-(par-Lilian-Besson)-?" data-toc-modified-id="Réponse-en-Bash-(par-Lilian-Besson)-?-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Réponse en Bash (par <a href="https://perso.crans.org/besson/" target="_blank">Lilian Besson</a>) ?</a></span></li><li><span><a href="#Réponse-en-Python-(par-Lilian-Besson)" data-toc-modified-id="Réponse-en-Python-(par-Lilian-Besson)-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Réponse en Python (par <a href="https://perso.crans.org/besson/" target="_blank">Lilian Besson</a>)</a></span></li><li><span><a href="#Réponse-en-OCaml-(par-Lilian-Besson)" data-toc-modified-id="Réponse-en-OCaml-(par-Lilian-Besson)-1.5"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Réponse en OCaml (par <a href="https://perso.crans.org/besson/" target="_blank">Lilian Besson</a>)</a></span></li><li><span><a href="#Réponse-en-Rust-(par-un-de-mes-élèves-(Théo-Degioanni))" data-toc-modified-id="Réponse-en-Rust-(par-un-de-mes-élèves-(Théo-Degioanni))-1.6"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Réponse en Rust (par <a href="https://github.com/Moxinilian" target="_blank">un de mes élèves (Théo Degioanni)</a>)</a></span></li><li><span><a href="#Conclusion" data-toc-modified-id="Conclusion-1.7"><span class="toc-item-num">1.7&nbsp;&nbsp;</span>Conclusion</a></span></li><li><span><a href="#Challenge-(pour-les-futurs-agrégs-maths)" data-toc-modified-id="Challenge-(pour-les-futurs-agrégs-maths)-1.8"><span class="toc-item-num">1.8&nbsp;&nbsp;</span>Challenge (pour les futurs agrégs maths)</a></span><ul class="toc-item"><li><span><a href="#Une-première-réponse" data-toc-modified-id="Une-première-réponse-1.8.1"><span class="toc-item-num">1.8.1&nbsp;&nbsp;</span>Une première réponse</a></span></li></ul></li></ul></li></ul></div>

# # Février 2021 un mini challenge arithmético-algorithmique
# ## Challenge :
# Le lundi 01 février 2021, j'ai donné à mes élèves de L3 et M1 du département informatique de l'ENS Rennes le challenge suivant :
# 
# > Mini challenge algorithmique pour les passionnés en manque de petits exercices de code : (optionnel)
# Vous avez dû observer que ce mois de février est spécial parce que le 1er février est un lundi, et qu'il a exactement 4 lundis, 4 mardis, 4 mercredis, 4 jeudis, 4 vendredis, 4 samedis et 4 dimanches.
# 
# > **Question** : Comptez le nombre de mois de février répondant à ce critère (je n'ai pas trouvé de nom précis), depuis l'année de création de l'ENS Rennes (1994, enfin pour Cachan antenne Bretagne) jusqu'à 2077 (1994 et 2077 inclus).

# - Auteur : [Lilian Besson](https://perso.crans.org/besson/)
# - License : [MIT](https://lbesson.mit-license.org/)
# - Date : 01/02/2021
# - Cours : [ALGO2](http://people.irisa.fr/Francois.Schwarzentruber/algo2/) @ [ENS Rennes](http://www.dit.ens-rennes.fr/)

# <span style="color:red;">Attention : ce notebook est déclaré avec le kernel Python, mais certaines sections (Java, OCaml et Rust) ont été exécutées avec le kernel correspondant. La coloration syntaxique multi-langage n'est pas (encore?) supportée, désolé d'avance.</span>

# ---
# ## Réponse en Java (par [un de mes élèves de L3 SIF](http://www.dit.ens-rennes.fr/))
# 
# > Oui, on peut utiliser Java dans des notebooks ! Voir [ce poste de blogue](https://blog.frankel.ch/teaching-java-jupyter-notebooks/), et [ce kernel IJava](https://github.com/SpencerPark/IJava).
# Moi je trouve ça chouette, [et je m'en suis servi en INF1 au semestre dernier](https://perso.crans.org/besson/teach/INF1_L1_Rennes1_2020-21/)
# 
# Il en avait trouvé 9.
# 
# - Date et heure : lundi 01 février, 20h32.

# In[15]:


(/, ceci, est, du, code, Java, 9, et, pas, Python, !)
(/, On, a, besoin, des, dépendances, suivantes, :)
import java.util.Calendar;           // pour Calendar.FEBRUARY, .YEAR, .MONDAY
import java.util.GregorianCalendar;  // pour 
import java.util.stream.IntStream;   // pour cet IntStream


# In[16]:


(/, ceci, est, du, code, Java, 9, et, pas, Python, !)
IntStream.rangeClosed(1994, 2077)
         (/.parallel(), //, ce, .parallel(), est, inutile,, il, y, a, trop, peu, de, valeurs)
         .mapToObj(i -> new GregorianCalendar(i, Calendar.FEBRUARY, 1))
         .filter(calendar -> !calendar.isLeapYear(calendar.get(Calendar.YEAR)))
         .filter(calendar -> calendar.get(Calendar.DAY_OF_WEEK) == Calendar.MONDAY)
         .count();


# Si les cellules précédentes ne s'exécute pas, a priori c'est normal : ce notebook est déclaré en Python !
# Il faudrait utiliser une des astuces suivantes, mais flemme.

# In[5]:


System.out.println("Test d'une cellule en Java dans un notebook déclaré comme Java");
(/, ==>, ça, marche, !)


# In[3]:


get_ipython().run_cell_magic('java', '', 'System.out.println("Test d\'une cellule en Java dans un notebook déclaré comme Python");\n// cela ne marche pas !')


# In[6]:


# On peut aussi écrire une cellule Python qui fait appel à une commande Bash
get_ipython().system('echo \'System.out.println("\\nTest d\\\'une ligne de Java dans un notebook déclaré comme Python");\' | jshell -q')


# In[8]:


get_ipython().run_cell_magic('bash', '', '# voir une commande Bash directement !\n# mais uniquement depuis un notebook Python\necho \'System.out.println("\\nok");\' | jshell -q')


# ---
# ## Réponse en Bash (par [Lilian Besson](https://perso.crans.org/besson/)) ?
# 
# En bidouillant avec des programmes en lignes de commandes tels que `cal` et des grep on devrait pouvoir s'en sortir facilement. Ça tient même en une ligne !
# 
# - Date et heure : 01/02/2021, 21h16

# In[5]:


get_ipython().run_cell_magic('bash', '', 'ncal February 2021')


# En recherchant exactement cette chaîne "lu  1  8 15 22" et en excluant 29 des lignes trouvées, on obtient la réponse :

# In[6]:


get_ipython().run_cell_magic('bash', '', "time for ((annee=1994; annee<=2077; annee+=1)); do\n    ncal February $annee \\\n    | grep 'lu  1  8 15 22' \\\n    | grep -v 29;\ndone \\\n| wc -l")


# In[7]:


get_ipython().run_cell_magic('bash', '', "for ((annee=1994; annee<=2077; annee+=1)); do ncal February $annee | grep 'lu  1  8 15 22' | grep -v 29; done | wc -l")


# ---
# ## Réponse en Python (par [Lilian Besson](https://perso.crans.org/besson/))
# 
# Avec le module [calendar](https://www.geeksforgeeks.org/python-calendar-module/) on pourrait faire comme en Bash : imprimer les calendriers, et rechercher des chaînes particulières... mais ce n'est pas très propre.
# Essayons avec ce même module mais en écrivant une solution fonctionnelle !
# 
# - Date et heure : lundi 01 février, 21h40.

# In[1]:


import calendar


# In[2]:


def filter_annee(annee):
    return (
        set(calendar.Calendar(annee).itermonthdays2(annee, 2))
        & {(1,0), (28, 6), (29, 0)}
    ) == {(1, 0), (28, 6)}


# In[3]:


filter_annee(2020), filter_annee(2021), filter_annee(2022)


# Et donc on a juste à compter les années, de 1994 à 2077 inclus, qui ne sont pas des années bissextiles et qui satisfont le filtre :

# In[4]:


get_ipython().run_cell_magic('time', '', "len(list(filter(filter_annee, ( annee\n        for annee in range(1994, 2077 + 1)\n        # if not calendar.isleap(annee) # en fait c'est inutile\n    )\n)))")


# ---
# ## Réponse en OCaml (par [Lilian Besson](https://perso.crans.org/besson/))
# 
# En installant et utilisant [ocaml-calendar](https://github.com/ocaml-community/calendar) cela ne doit pas être trop compliqué. On peut s'inspirer du code Java ci-dessus, qui a une approche purement fonctionnelle.
# 
# - Date et heure : ?

# In[1]:


(* cette cellule est en OCaml *)
(* avec la solution en Bash et Sys.command... *)
Sys.command "bash -c \"for ((annee=1994; annee<=2077; annee+=1)); do ncal February \\$annee | grep 'lu  1  8 15 22' | grep -v 29; done | wc -l\"";;
(* mais ça ne compte pas ! *)


# On pourrait faire en calculant manuellement les quantièmes du 01/01/YYYY pour YYYY entre 1994 et 2077.

# In[2]:


type day = int
and  dayofweek = int
and  month = int
and  year = int
(";")
type date = { d: day; q: dayofweek; m: month; y: year };;


# In[3]:


let is_not_bissextil (y: year) : bool =
    (y mod 4 != 0) || (y mod 100 == 0 && y mod 400 != 0)
(";")


# In[4]:


is_not_bissextil 2019;;
is_not_bissextil 2020;;
is_not_bissextil 2021;;


# In[7]:


(* Ce Warning:8 est volontaire ! *)
let length_of_month (m: month) (y: year) : int =
    match m with
    | 4 | 6 | 9 | 11 -> 30
    | 1 | 3 | 5 | 7 | 8 | 10 | 12 -> 31
    | 2 -> if is_not_bissextil(y) then 28 else 29
(";")


# In[8]:


length_of_month 2 2019;; (* 28 *)
length_of_month 2 2020;; (* 29 *)
length_of_month 2 2021;; (* 28 *)


# In[9]:


let next_dayofweek (q: dayofweek) =
    1 + (q mod 7)
(";")


# In[10]:


next_dayofweek 1;; (* Monday => Tuesday *)
next_dayofweek 2;; (* Tuesday => Wednesday *)
next_dayofweek 3;; (* Wednesday => Thursday *)
next_dayofweek 4;; (* Thursday => Friday *)
next_dayofweek 5;; (* Friday => Saturday *)
next_dayofweek 6;; (* Saturday => Sunday *)
next_dayofweek 7;; (* Sunday => Monday *)


# In[11]:


let next_day { d; q; m; y } =
    let l_o_m = length_of_month m y in
    if (d = 31 && m = 12) then
        { d=1; q=next_dayofweek q; m=1; y=y+1 }
    else begin
        if (d = l_o_m) then
            { d=1; q=next_dayofweek q; m=m+1; y=y }
        else
            { d=d+1; q=next_dayofweek q; m=m; y=y }
    end
(";")


# In[12]:


let rec iterate (n: int) (f: 'a -> 'a) (x: 'a): 'a =
    match n with
    | 0 -> x (* identité *)
    | 1 -> f(x)
    | n -> iterate (n-1) f (f(x))
;;


# In[13]:


let start_of_next_month { d; q; m; y } =
    let l_o_m = length_of_month m y in
    let nb_nextday = l_o_m - d + 1 in
    if (m = 12) then
        { d=1; q=iterate nb_nextday next_dayofweek q; m=1; y=y+1 }
    else
        { d=1; q=iterate nb_nextday next_dayofweek q; m=m+1; y=y }
(";")


# Je vais tricher un peu et utiliser la connaissance que le 01/01/1994 est un samedi :

# In[14]:


Sys.command "ncal Jan 1994 | grep '  1'";


# In[15]:


let start_date = {d=1; q=6; m=1; y=1994};; (* 01/01/1994 était un samedi, q=6 *)
(* let start_date = {d=1; q=3; m=1; y=2020};; (* 01/01/2020 était un mercredi, q=3 *) *)

let end_date   = {d=31; q=0; m=1; y=2077};; (* on se fiche du quantième ici ! *)
(* let end_date   = {d=31; q=0; m=1; y=2021};; (* on se fiche du quantième ici ! *) *)

let aujourdhui = ref start_date;; (* les champs sont pas mutables, go reference *)
let nb_bon_mois_fevrier = ref 0;;
let aujourdhuis = ref [];;
let solutions = ref [];;

while (!aujourdhui.y <= end_date.y || !aujourdhui.y <= end_date.y || !aujourdhui.y <= end_date.y) do
    if (!aujourdhui.d = 1 && !aujourdhui.m = 2) then begin
        (* on a un début de février, est-ce qu'il vérifie les critères ? *)
        let date_suivante    = iterate 27 next_day !aujourdhui in
        let date_suivante_p1 = next_day date_suivante in
        if (
               date_suivante.d = 28 && date_suivante.m = 2
            && date_suivante_p1.d != 29 (* année pas bisextile *)
            && !aujourdhui.q = 1        (* mois février commence par lundi *)
        ) then begin
            solutions := !aujourdhui :: !solutions;
            incr nb_bon_mois_fevrier;
        end;
    end;
    (* on a un jour quelconque, on avance d'un mois *)
    aujourdhui := start_of_next_month !aujourdhui;
    aujourdhuis := !aujourdhui :: !aujourdhuis;
done;;

get_ipython().system('nb_bon_mois_fevrier;;')


# On peut même facilement vérifier les années qui ont été trouvées, et donc vérifier que 2021 est dedans.
# 
# J'ai aussi eu la chance d'observer ce phénomène en 1999 (mais je ne me souviens pas l'avoir remarqué, j'avais 6 ans !) et en 2010 (et je me *souviens* l'avoir remarqué, normal j'étais en MP* et on adore ce genre de coïncidences).

# In[16]:


get_ipython().system('solutions')


# (le kernel [ocaml-jupyter](https://github.com/akabe/ocaml-jupyter/) est génial, mais [plante un peu](https://github.com/akabe/ocaml-jupyter/issues/160), j'ai galéré à écrire cette douzaine de cellules sans devoir relancer Jupyter plusieurs fois... bug signalé, résolution en cours...)

# ---
# ## Réponse en Rust (par [un de mes élèves (Théo Degioanni)](https://github.com/Moxinilian))
# 
# Le code Rust proposé peut être executé depuis le [bac à sable Rust]() :
# https://play.rust-lang.org/?version=stable&mode=debug&edition=2018&gist=2ab9c57e9d114a344363e21f9493bf22
# 
# Mais on peut aussi utiliser [le kernel Jupyter proposé par le projet evcxr de Google](https://github.com/google/evcxr/blob/master/evcxr_jupyter/README.md) :
# 
# 1. il faut installer Rust, je n'avais jamais fait j'ai donc suivi [rustup.rs](https://rustup.rs/) le site officiel de présentation de l'installation de Rust ;
# 2. puis j'ai suivi les explications pour installer le kernel [sur GitHub @google/evcxr](https://github.com/google/evcxr/blob/master/evcxr_jupyter/README.md) ;
# 3. puis j'ai écrit cette cellule ci-dessous, j'ai changé le Noyau en Rust, et j'ai exécuté la cellule ;
# 4. notez qu'avec l'extension [jupyter nbextension ExecuteTime](https://jupyter-contrib-nbextensions.readthedocs.io/en/latest/nbextensions/execute_time/readme.html), j'ai vu que la première cellule avait pris quasiment 10 secondes... mais je pense qu'il s'agit du temps d'installer et de compilation du module `chrono` (je ne suis pas encore très familier avec Rust).
#    - Les exécutions suivantes prennent environ 300ms pour la définition (y a-t-il recompilation même si le texte ne change pas ?) de la fonction ;
#    - Et environ 700ms pour l'exécution. C'est bien plus lent que les 35 ms de mon code naïf en OCaml (qui est juste interprété et pas compilé), que les 10 ms de Python, ou les 100 ms de Bash. Mais pas grave !
# 
# - Date et heure : lundi 01/02/2021, 21h20

# In[8]:


:dep chrono = "0.4"
use chrono::TimeZone;
use chrono::Datelike;

fn main() {
    let n = (1994..=2077)
        .filter(|n| chrono::Utc.ymd_opt(*n, 2, 29) == chrono::LocalResult::None)
        .map(|n| chrono::Utc.ymd(n, 2, 1))
        .filter(|t| t.weekday() == chrono::Weekday::Mon)
        .count();
        
    println!("{}", n);
}


# In[9]:


main()


# On trouve la même réponse que les autres langages, parfait.

# ---
# ## Conclusion
# 
# En utilisant bien la librairie standard de votre langage favori, ce n'est pas très difficile.
# 
# Curieux de plus ? Voir [cet article](https://www.truthorfiction.com/february-2017-4-day-first-time-823-years/) et [celui là](https://www.tecatips.com/february-happens-every-823-years/) qui expliquent que ce n'est pas si rare (comme vous venez de le calculer), contrairement à une rumeur qui semble circuler régulièrement sur les réseaux sociaux. La rumeur dirait que ces mois de février n'arrivent qu'une fois tous les 823 ans...
# 
# ## Challenge (pour les futurs agrégs maths)
# 
# **Bonus spécial** : si quelqu'un trouve un calcul de maths qui permette de trouver la réponse "à la main", ou en tous cas sans un programme informatique.

# ### Une première réponse
# 
# - Date : lundi 01/02/2021, 22h32
# 
# > - Sur 28 ans, chaque année on décale d'un jour, sauf les bissextiles où c'est de 2 (car 365%7 = 1).
# > - Donc il y a 7 années bissextiles et comme 7 et 4 sont premiers entre eux, autant de chacun des jours, donc 3 cas (une des commençant lundi ayant 5 lundis).
# > - Aucunes années non bissextiles en 4 entre 94 et 77
# > - On a donc 83 années = 3x28-1.
# > - 2020-28 = 1992 donc 1993 (l'année manquante pour tomber rond) n'était pas un cas de lundi.
# > - Le nombre de cas semblable est donc de 3x3 = **9** (réponse correcte).

# > C'est tout pour ce notebook, [allez voir ce projet](https://github.com/Naereen/notebooks/) pour d'autres notebooks.
