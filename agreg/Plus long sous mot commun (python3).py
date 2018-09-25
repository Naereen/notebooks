
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#Table-des-matières" data-toc-modified-id="Table-des-matières-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Table des matières</a></div><div class="lev1 toc-item"><a href="#1.-Agrégation-externe-de-mathématiques" data-toc-modified-id="1.-Agrégation-externe-de-mathématiques-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>1. Agrégation externe de mathématiques</a></div><div class="lev2 toc-item"><a href="#1.1-Leçon-orale,-option-informatique" data-toc-modified-id="1.1-Leçon-orale,-option-informatique-21"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>1.1 Leçon orale, option informatique</a></div><div class="lev4 toc-item"><a href="#Feedbacks?" data-toc-modified-id="Feedbacks?-2101"><span class="toc-item-num">2.1.0.1&nbsp;&nbsp;</span>Feedbacks?</a></div><div class="lev1 toc-item"><a href="#2.-Calcul-du-plus-long-sous-mot-commun" data-toc-modified-id="2.-Calcul-du-plus-long-sous-mot-commun-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>2. Calcul du plus long sous mot commun</a></div><div class="lev3 toc-item"><a href="#2.0.1-Implémentation-d'un-développement-pour-les-leçons-906,-907." data-toc-modified-id="2.0.1-Implémentation-d'un-développement-pour-les-leçons-906,-907.-301"><span class="toc-item-num">3.0.1&nbsp;&nbsp;</span>2.0.1 Implémentation d'un développement pour les leçons 906, 907.</a></div><div class="lev3 toc-item"><a href="#2.0.2-Références-:" data-toc-modified-id="2.0.2-Références-:-302"><span class="toc-item-num">3.0.2&nbsp;&nbsp;</span>2.0.2 Références :</a></div><div class="lev3 toc-item"><a href="#2.0.3-Applications,-généralisations-:" data-toc-modified-id="2.0.3-Applications,-généralisations-:-303"><span class="toc-item-num">3.0.3&nbsp;&nbsp;</span>2.0.3 Applications, généralisations :</a></div><div class="lev1 toc-item"><a href="#3.-Algorithme-naïf-(exponentiel)" data-toc-modified-id="3.-Algorithme-naïf-(exponentiel)-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>3. Algorithme naïf (exponentiel)</a></div><div class="lev2 toc-item"><a href="#3.1-Détecter-si-$u$-est-sous-mot-de-$y$" data-toc-modified-id="3.1-Détecter-si-$u$-est-sous-mot-de-$y$-41"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>3.1 Détecter si <span class="MathJax_Preview" style="color: inherit;"><span class="MJXp-math" id="MJXp-Span-112"><span class="MJXp-mi MJXp-italic" id="MJXp-Span-113">u</span></span></span><script type="math/tex" id="MathJax-Element-19">u</script> est sous mot de <span class="MathJax_Preview" style="color: inherit;"><span class="MJXp-math" id="MJXp-Span-114"><span class="MJXp-mi MJXp-italic" id="MJXp-Span-115">y</span></span></span><script type="math/tex" id="MathJax-Element-20">y</script></a></div><div class="lev2 toc-item"><a href="#3.2-Trouver-un-sous-mot-de-longueur-k" data-toc-modified-id="3.2-Trouver-un-sous-mot-de-longueur-k-42"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>3.2 Trouver <em>un</em> sous-mot de longueur <code>k</code></a></div><div class="lev2 toc-item"><a href="#3.3-Sous-mot-de-longueur-maximale-(version-naïve)" data-toc-modified-id="3.3-Sous-mot-de-longueur-maximale-(version-naïve)-43"><span class="toc-item-num">4.3&nbsp;&nbsp;</span>3.3 Sous-mot de longueur maximale (version naïve)</a></div><div class="lev1 toc-item"><a href="#4.-Méthode-gloutonne-(programmation-dynamique)" data-toc-modified-id="4.-Méthode-gloutonne-(programmation-dynamique)-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>4. Méthode gloutonne (programmation dynamique)</a></div><div class="lev2 toc-item"><a href="#4.1-Programmation-dynamique,-sans-optimisation-mémoire" data-toc-modified-id="4.1-Programmation-dynamique,-sans-optimisation-mémoire-51"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>4.1 Programmation dynamique, sans optimisation mémoire</a></div><div class="lev2 toc-item"><a href="#4.2-Utilisation-d'une-matrice-creuse" data-toc-modified-id="4.2-Utilisation-d'une-matrice-creuse-52"><span class="toc-item-num">5.2&nbsp;&nbsp;</span>4.2 Utilisation d'une matrice <em>creuse</em></a></div><div class="lev3 toc-item"><a href="#4.2.1-Version-condensée" data-toc-modified-id="4.2.1-Version-condensée-521"><span class="toc-item-num">5.2.1&nbsp;&nbsp;</span>4.2.1 Version condensée</a></div><div class="lev1 toc-item"><a href="#5.-Calcule-de-la-plus-longue-sous-séquence-commune" data-toc-modified-id="5.-Calcule-de-la-plus-longue-sous-séquence-commune-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>5. Calcule de la plus longue sous-séquence commune</a></div><div class="lev2 toc-item"><a href="#5.1-Vérifier-qu'une-sous-séquence-est-une-bonne-sous-séquence" data-toc-modified-id="5.1-Vérifier-qu'une-sous-séquence-est-une-bonne-sous-séquence-61"><span class="toc-item-num">6.1&nbsp;&nbsp;</span>5.1 Vérifier qu'une sous-séquence est une bonne sous-séquence</a></div><div class="lev2 toc-item"><a href="#5.2-Algorithme-pour-la-plus-longue-sous-séquence" data-toc-modified-id="5.2-Algorithme-pour-la-plus-longue-sous-séquence-62"><span class="toc-item-num">6.2&nbsp;&nbsp;</span>5.2 Algorithme pour la plus longue sous-séquence</a></div><div class="lev3 toc-item"><a href="#5.2.1-Exemple,-venant-du-développement" data-toc-modified-id="5.2.1-Exemple,-venant-du-développement-621"><span class="toc-item-num">6.2.1&nbsp;&nbsp;</span>5.2.1 Exemple, venant du développement</a></div><div class="lev3 toc-item"><a href="#5.2.2-Autres-exemples" data-toc-modified-id="5.2.2-Autres-exemples-622"><span class="toc-item-num">6.2.2&nbsp;&nbsp;</span>5.2.2 Autres exemples</a></div>

# # Table des matières
# * [1. Agrégation externe de mathématiques](#1.-Agrégation-externe-de-mathématiques)
# 	* [1.1 Leçon orale, option informatique](#1.1-Leçon-orale,-option-informatique)
# * [2. Calcul du plus long sous mot commun](#2.-Calcul-du-plus-long-sous-mot-commun)
# 	* &nbsp;
# 		* [2.0.1 Implémentation d'un développement pour les leçons 906, 907.](#2.0.1-Implémentation-d'un-développement-pour-les-leçons-906,-907.)
# 		* [2.0.2 Références :](#2.0.2-Références-:)
# 		* [2.0.3 Applications, généralisations :](#2.0.3-Applications,-généralisations-:)
# * [3. Algorithme naïf (exponentiel)](#3.-Algorithme-naïf-%28exponentiel%29)
# 	* [3.1 Détecter si $u$ est sous mot de $y$](#3.1-Détecter-si-$u$-est-sous-mot-de-$y$)
# 	* [3.2 Trouver *un* sous-mot de longueur ``k``](#3.2-Trouver-*un*-sous-mot-de-longueur-k)
# 	* [3.3 Sous-mot de longueur maximale (version naïve)](#3.3-Sous-mot-de-longueur-maximale-%28version-naïve%29)
# * [4. Méthode gloutonne (programmation dynamique)](#4.-Méthode-gloutonne-%28programmation-dynamique%29)
# 	* [4.1 Programmation dynamique, sans optimisation mémoire](#4.1-Programmation-dynamique,-sans-optimisation-mémoire)
# 	* [4.2 Utilisation d'une matrice *creuse*](#4.2-Utilisation-d'une-matrice-*creuse*)
# 		* [4.2.1 Version condensée](#4.2.1-Version-condensée)
# * [5. Calcule de la plus longue sous-séquence commune](#5.-Calcule-de-la-plus-longue-sous-séquence-commune)
# 	* [5.1 Vérifier qu'une sous-séquence est une bonne sous-séquence](#5.1-Vérifier-qu'une-sous-séquence-est-une-bonne-sous-séquence)
# 	* [5.2 Algorithme pour la plus longue sous-séquence](#5.2-Algorithme-pour-la-plus-longue-sous-séquence)
# 		* [5.2.1 Exemple, venant du développement](#5.2.1-Exemple,-venant-du-développement)
# 		* [5.2.2 Autres exemples](#5.2.2-Autres-exemples)
# 

# # 1. Agrégation externe de mathématiques

# ## 1.1 Leçon orale, option informatique

# > - Ce [notebook Jupyter](http://jupyter.org/) est une implémentation d'un algorithme constituant un développement pour l'option informatique de l'agrégation externe de mathématiques.
# > - Il s'agit du calcul du [plus long sous mot commun](https://fr.wikipedia.org/wiki/Plus_longue_sous-séquence_commune).
# > - Cette implémentation (partielle) a été rédigée par [Lilian Besson](http://perso.crans.org/besson/) ([sur GitHub ?](https://github.com/Naereen/), [sur Bitbucket ?](https://bitbucket.org/lbesson)), et [est open-source](https://github.com/Naereen/notebooks/blob/master/agreg/Plus%20long%20sous%20mot%20commun%20%28python3%29.ipynb).
# 
# > #### Feedbacks?
# > - Vous avez trouvé un bug ? → [Signalez-le moi svp !](https://github.com/Naereen/notebooks/issues/new), merci d'avance.
# > - Vous avez une question ? → [Posez la svp !](https://github.com/Naereen/ama.fr) [![Demandez moi n'importe quoi !](https://img.shields.io/badge/Demandez%20moi-n'%20importe%20quoi-1abc9c.svg)](https://GitHub.com/Naereen/ama.fr)
# 
# ----

# # 2. Calcul du plus long sous mot commun

# ### 2.0.1 Implémentation d'un développement pour les leçons 906, 907.

# On présente ici un algorithme de programmation dynamique pour **le calcul du plus long sous mot commun** (attention, c'est différent de la plus longue sous séquence commune !).
# 
# Étant donnés deux mots $X = x_1 \dots x_m$ et $Y = y_1 \dots y_n$ sur un alphabet $\Sigma$, on cherche à savoir quel est le plus long sous-mot commun à $X$ et $Y$.
# Un sous-mot correspond à un morceau commun aux deux mots : on extraie de **façon consécutive** une sous-séquence de $x$ et $y$ et elles doivent être égales : $u = x_{i_0} \dots x_{i_0 + k} = y_{j_0} \dots y_{j_0 + k} = v$ !
# 
# La solution naïve est d’énumérer tous les sous-mots de $X$, et de regarder ensuite s'ils sont aussi sous-mots de
# $Y$, mais cette solution est inefficace : il y a $\mathcal{O}(2^m)$ sous-mots de X...
# 
# L'objectif est donc d'obtenir un algorithme plus efficace, si possible polynomial en $m = |X|$ et $n = |Y|$ (il sera en $\mathcal{O}(m n)$).

# ### 2.0.2 Références :

# - Bien traité dans ["Cormen", Ch15.4 p341](https://catalogue.ens-cachan.fr/cgi-bin/koha/opac-detail.pl?biblionumber=15671),
# - Esquissé dans ["Aho, Hopcroft, Ullman", Ch5.6 p192](https://catalogue.ens-cachan.fr/cgi-bin/koha/opac-detail.pl?biblionumber=35831),
# - [Dévéloppement tapé en PDF ici](http://minerve.bretagne.ens-cachan.fr/images/Dvt_plsc.pdf).

# ### 2.0.3 Applications, généralisations :

# - Un généralisation est le calcul de la plus longue sous-sequence commune, pour lequel on ne se restreint plus à extraire de façon consécutive (ca semble plus compliqué, mais le même algorithme permet de régler le problème avec la même complexité, en fait).
# - On peut citer en application la comparaison de chaînes d'ADN, mais aussi la commande ``diff`` des systèmes GNU/Linux.
# - Généralisation : aucune chance d'avoir un algorithme aussi efficace s'il s'agit de trouver le plus long sous mot commun à $K$ chaînes de caractères (et en fait, le probleme général est $\mathcal{NP}$, en le nombre de chaînes, [comme expliqué ici (en anglais)](https://en.wikipedia.org/wiki/Longest_common_subsequence_problem#Complexity)).
# 
# ----

# # 3. Algorithme naïf (exponentiel)

# On va d'abord montrer rapidement une implémentation simple de l'algorithme naïf, pour ensuite vérifier que l'algorithme plus complexe fonctionne aussi bien.

# ## 3.1 Détecter si $u$ est sous mot de $y$

# L'objectif de toutes les fonctions suivantes est de proscrire toute recopie de chaines (*slicing*, ``x[i:j]``), qui sont très couteuse.

# In[1]:


def indiceSousMotAux(u, n, k, y, m, i, delta=0):
    """ Fonction tail-récursive qui trouve l'indice j tel que u[k:k+n] = y[i+j:i+j+n], ou -1 en cas d'échec."""
    # print("{}indiceSousMotAux(u = {}, n = {}, k = {}, y = {}, m = {}, i = {}, delta = {})".format('  '*delta, u, n, k, y, m, i, delta))  # DEBUG
    if n == 0:  # Mot vide, commun partout, par defaut on donne 0
        return 0
    else:       # Mot pas vide
        if k >= len(u) or i >= m:  # On a cherché trop loin, échec
            return -1         # -1 signifie échec
        elif u[k] == y[i]:    # Lettre en commun
            if delta == n - 1:    # On a fini, on a trouvé !
                return i - n + 1  # i est l'indice de la derniere lettre ici
            else:  # On continue de chercher, une lettre de moins
                return indiceSousMotAux(u, n, k + 1, y, m, i + 1, delta=delta+1)
        else:      # On recommence a chercher en i+1
            return indiceSousMotAux(u, n, k - delta, y, m, i + 1)


def indiceSousMot(u, y):
    """ En O(|u|), trouve l'indice j tel que u = y[j:j+|u|], ou -1 en cas d'échec."""
    return indiceSousMotAux(u, len(u), 0, y, len(y), 0)


def estSousMot(u, y):
    """ Vérifie en O(|u|) si u est sous-mot de y."""
    return indiceSousMotAux(u, len(u), 0, y, len(y), 0) >= 0


# Quelques tests :

# In[2]:


def test_estSousMot(u, y):
    """ Teste et affiche. """
    i = indiceSousMot(u, y)
    if i >= 0:
        print("Le mot u = '{}' est sous-mot de y = '{}', a partir de l'indice i = {}.".format(u, y, i))
    else:
        print("Le mot u = '{}' n'est pas sous-mot de y = '{}'.".format(u, y))        


u = "cde"
y1 = "abcdefghijklmnopqrstuvwxyz"
test_estSousMot(u, y1)  # True

y2 = "abcDefghijklmnopqrstuvwxyz"
test_estSousMot(u, y2)  # False


# ## 3.2 Trouver *un* sous-mot de longueur ``k``

# On peut chercher **tous** les sous-mots de longueur ``k`` dans ``x`` et regarder si l'**un d'entre eux** est inclus dans y (on s'arrête dès qu'on en a trouvé un) :

# In[3]:


def aSousMotDeLongueur(x, y, k):
    """ Trouve le premier sous-mot de x de longueur k et renvoit i, j, u, ou échoue avec une ValueError. """
    imax = len(x) - k + 1
    # Les sous mots seront x0..xk-1, .., ximax-1,..,xn-1
    for debut in range(imax):
        j = indiceSousMotAux(x, k, debut, y, len(y), 0)
        if j >= 0:
            return debut, debut + j, x[debut:debut+k]
    # Pas trouvé !
    raise ValueError("Aucun sous-mot de longueur k = {} de x = '{}' n'est dans y = '{}'.".format(k, x, y))


# Un test :

# In[4]:


def test_aSousMotDeLongueur(x, y, k):
    """ Teste et affiche. """
    try:
        i, j, u = aSousMotDeLongueur(x, y, k)
        print("==> Sous-mot de longueur k = {} de x = '{}' dans y = '{}' : u = '{}' en indice i = {} pour x et j = {} pour y.".format(k, x, y, u, i, j))
    except ValueError:
        print("==> Aucun sous-mot de longueur k = {} de x = '{}' n'est dans y = '{}'.".format(k, x, y))

x = "aabcde"
y = "aABcdE"
for k in range(0, min(len(x), len(y)) + 1):
    test_aSousMotDeLongueur(x, y, k)

x = "aabffcde"
y = "aABGGGGGcdE"
for k in range(0, min(len(x), len(y)) + 1):
    test_aSousMotDeLongueur(x, y, k)


# ## 3.3 Sous-mot de longueur maximale (version naïve)

# In[5]:


def _sousMotMax(x, y, verb=True):
    """ |x| doit etre plus petit que |y|."""
    k = len(x)
    while k >= 0:
        if verb:
            print("  On essaie de trouver un sous-mot commun à x = '{}' et y = '{}' de taille k = {} ...".format(x, y, k))
        try:
            i, j, u = aSousMotDeLongueur(x, y, k)
            if verb:
                print("  ==> On a un sous-mot commun à x = '{}' et y = '{}' de taille k = {} : u = '{}' (i = {}, j = {}) !".format(x, y, k, u, i, j))
            return i, j, u
        except ValueError:
            if verb:
                print("  ==> Aucun sous-mot commun à x = '{}' et y = '{}' de taille k = {} ...".format(x, y, k))
        k -= 1

            
def sousMotMax(x, y, verb=True):
    """ Trouve un sous-mot de longueur maximale (le plus à gauche possible de x et y), en temps exponentiel en n = |x|."""
    if len(x) <= len(y):
        return _sousMotMax(x, y, verb=verb)
    else:
        return _sousMotMax(y, x, verb=verb)


# Quelques tests :

# In[6]:


x = "abcABCabc123456abcABCabc99"
y = "abcDEFdef123456abcDEFdef9999"
sousMotMax(x, y, verb=False)


# In[7]:


x = "abcABCabc"
y = "abcDEFdef"
sousMotMax(x, y)


# # 4. Méthode gloutonne (programmation dynamique)

# On passe désormais à la seconde approche, qui sera bien plus efficace (et qui montrera que le probleme du plus long sous-mot commun de deux mots est dans $\mathcal{P}$).

# Cette approche a l'avantage d'être bien plus efficace, mais aussi plus simple à coder.
# On a juste besoin d'une matrice de taille $(|x|+1)(|y|+1)$ (un ``numpy.array``, pour être plus efficace qu'une liste de liste), et quelques boucles ``for``.

# In[8]:


# On a besoin du module numpy. Cf. http://numpy.org/ pour l'installer si besoin
import numpy as np


# ## 4.1 Programmation dynamique, sans optimisation mémoire

# La fonction ci-dessous procède en 4 étapes :
# 
# 1. Initialisation de la matrice ``longueurs``, pleine de $0$ et de taille $(n+1) \times (m+1)$ où $y := |x|$ et $m := |y|$,
# 2. Calcul "bottom-up" de la matrice ``longueurs``, par l'équation suivante :
#     $$ \mathrm{longueurs}[i, j] = 1 + \mathrm{longueurs}[i-1, j-1] \; \text{si} \; x[i-1] = y[i-1]. $$
# 3. Calcul de la longueur maximale d'une correspondance entre ``x`` et ``y``, par un simple parcours (``longueur_max``), et calcul des indices de début de cette coresspondance maximale (= plus long sous-mot !), ``idebut`` et ``jdebut``.
# 4. (optionnel) On vérifie que ``x[idebut : idebut + longueur_max]`` = ``y[jdebut : jdebut + longueur_max]``.
# 
# 
# On commence en utilisant une matrice, pleine de $0$ (ie. une matrice nulle).
# Comme on va le voir dans les exemples ci-dessous, en pratique cette matrice restera presque "vide", consommant beaucoup de memoire ($\mathcal{O}(n m)$) inutilement.
# La version suivante sera optimisée (en utilisant une matrice *sparse*, ie. creuse).

# Cet algorithme sera en :
# 
# - $\mathcal{O}(n m)$ en mémoire, dans tous les cas (mais on peut faire mieux),
# - $\mathcal{O}(n m)$ en temps, dans tous les cas (et on ne peut pas faire mieux).
# 
# ----

# In[9]:


def sousMotMaxGlouton(x, y, verb=False, verifie=True):
    """ Calcule le plus long sous-mot commun a x et y, par programmation dynamique.
    
        - affiche un peu ce qu'il se passe si verb=True,
        - vérifie que le sous-mot commun est bien un bon sous-mot commun si verifie=True.
    """
    def message(*args):
        if verb:
            print(*args) 
    # 1. et 2. Initialisation et construction Matrice longueurs
    n = len(x)
    m = len(y)
    message("\n1. Initialisation de la look-up matrice longueurs de taille (n+1, m+1) : n = {} m = {} ...".format(n, m))
    longueurs = np.zeros((n+1, m+1), dtype=int)
    message("2. Construction bottom-up de la loop-up matrice longueurs ...")
    for i in range(1, n+1):
        for j in range(1, m+1):
            if x[i-1] == y[j-1]:
                longueurs[i, j] = 1 + longueurs[i-1, j-1]
                message("      Correspondance en cours, u[{}] = {} et v[{}] = {}, de longueur courante {} ...".format(i-1, x[i-1], j-1, y[j-1], longueurs[i, j]))
    # 3. Utilisation de la matrice longueurs
    iFin, jFin = 0, 0
    longueur_max = -1  # Pas encore
    message("3. Calcul de la position du plus long sous mot via la matrice longueurs ...")
    for i in range(0, n+1):
        for j in range(0, m+1):
            if longueur_max < longueurs[i, j]:
                longueur_max = longueurs[i, j]
                iFin, jFin = i, j
    # Note : avec les fonctions numpy np.max et np.argmax on pourrait faire ça plus vite (pour des matrices) :
    # longueur_max = np.max(longueurs)
    # iFin, jFin = np.unravel_index(np.argmax(longueurs), np.shape(longueurs))
    # Calcul des indices de debut
    iDebut, jDebut = iFin - longueur_max, jFin - longueur_max
    message("4. On a obtenu iDebut = {} et jDebut = {} et longueur_max = {} ...".format(iDebut, jDebut, longueur_max))

    # 4. Vérification
    if verifie:
        xSous = x[iDebut: iDebut + longueur_max]
        ySous = y[jDebut: jDebut + longueur_max]
        message("      Sous-mot dans x = {}, et sous-mot dans y = {} ...".format(xSous, ySous))
        assert xSous == ySous, "Erreur, xSous et ySous sont différents !"
    
    leSousMot = x[iDebut: iDebut + longueur_max]
    return iDebut, jDebut, leSousMot, longueurs


# On peut faire quelques tests, comme pour l'approche initiale.

# In[10]:


x = "BDCABA"
y = "ABCBDAB"
sousMotMaxGlouton(x, y, verb=True)


# In[11]:


x = "abcABCabc123456abcABCabc99"
y = "abcDEFdef123456abcDEFdef9999"
sousMotMaxGlouton(x, y, verb=True)


# On commence à constater que la matrice `longueurs` est toujours presque remplie de zéros, même après tous les calculs ! Peut-être qu'on peut faire mieux, niveau espace de stockage (complexité en mémoire), pour éviter de stocker un nombre trop grand de zéros inutiles. Une version améliorée est présentée ci-dessous, on parvient à diminuer grandement la complexité (moyenne) en mémoire en utilisant une structure intelligente de matrice *"creuse"*.

# In[12]:


x = "abcZZdeFG597"
y = "AbCdEFG413ZAQCWQ"
sousMotMaxGlouton(x, y, verb=True)


# ## 4.2 Utilisation d'une matrice *creuse*

# On va utiliser le module [``scipy.sparse``](https://docs.scipy.org/doc/scipy/reference/sparse.html) pour utiliser un codage efficace pour cette matrice ``longueurs`` : un codage dit creux qui permettra de ne pas stocker tous ces zéros inutiles.

# In[13]:


from scipy.sparse import lil_matrix


# On utilise la structure ``lil_matrix`` (``lil`` pour *"LInked List"*), car c'est la plus efficace quant la matrice change de structure *sparse* (on rajoute des valeurs non-nulles au fur et à mesure de sa construction).
# 
# Exemple :

# In[14]:


print("I_12 pleine :\n", np.eye(12))
I12 = lil_matrix(np.eye(12))
print("I_12 creuse :\n", I12)
I12


# In[15]:


print("Taille de I_12 creuse =", I12.size)


# On peut prendre exactement la même fonction, et changer la ligne qui crée la matrice ``longueurs`` : on ajoute un appel à ``lil_matrix`` pour en faire une matrice creuse.
# 
# Et voilà comment on passe, en une ligne, de $\mathcal{O}(n m)$ en mémoire dans tous les cas à un $\mathcal{O}(n m)$ dans le pire des cas et $\mathcal{O}(\sum \text{longueur des sous-mots de x et y})$ dans tous les cas (en moyenne, ce sera $\mathcal{O}(\min(n, m))$ au pire).
# Notez que ce sera un poil moins efficace, mais on garde la complexité en temps en $\mathcal{O}(n m)$ de toute façon.

# In[16]:


def sousMotMaxGloutonCreux(x, y, verb=False, verifie=True):
    """ Calcule le plus long sous-mot commun a x et y, par programmation dynamique.
    
        - affiche un peu ce qu'il se passe si verb=True,
        - vérifie que le sous-mot commun est bien un bon sous-mot commun si verifie=True.
    """
    def message(*args):
        if verb:
            print(*args) 
    # 1. et 2. Initialisation et construction Matrice longueurs
    n = len(x)
    m = len(y)
    message("\n1. Initialisation de la look-up matrice longueurs, creuse de taille (n+1, m+1) : n = {} m = {} ...".format(n, m))
    longueurs = lil_matrix(np.zeros((n+1, m+1), dtype=int))
    message("2. Construction bottom-up de la loop-up matrice longueurs ...")
    for i in range(1, n+1):
        for j in range(1, m+1):
            if x[i-1] == y[j-1]:
                longueurs[i, j] = 1 + longueurs[i-1, j-1]
                message("      Correspondance en cours, u[{}] = {} et v[{}] = {}, de longueur courante {} ...".format(i-1, x[i-1], j-1, y[j-1], longueurs[i, j]))
    # 3. Utilisation de la matrice longueurs
    iFin, jFin = 0, 0
    longueur_max = -1  # Pas encore
    message("3. Calcul de la position du plus long sous mot via la matrice longueurs ...")
    for i in range(0, n+1):
        for j in range(0, m+1):
            if longueur_max < longueurs[i, j]:
                longueur_max = longueurs[i, j]
                iFin, jFin = i, j
    # Calcul des indices de debut
    iDebut, jDebut = iFin - longueur_max, jFin - longueur_max
    message("4. On a obtenu iDebut = {} et jDebut = {} et longueur_max = {} ...".format(iDebut, jDebut, longueur_max))

    # 4. Vérification
    if verifie:
        xSous = x[iDebut: iDebut + longueur_max]
        ySous = y[jDebut: jDebut + longueur_max]
        message("      Sous-mot dans x = {}, et sous-mot dans y = {} ...".format(xSous, ySous))
        assert xSous == ySous, "Erreur, xSous et ySous sont différents !"
    
    leSousMot = x[iDebut: iDebut + longueur_max]
    return iDebut, jDebut, leSousMot, longueurs


# On peut faire quelques exemples en plus, et on calcule aussi la taille de la matrice creuse ``longueurs`` (pour comparer a la taille de la matrice pleine de la fonction d'avant) :

# In[17]:


x = "ab0cABC0abc123456abcABCabc99"
y = "abZQXCVQDScD0EFd0ef123456abcDEFdef9999"
iDebut, jDebut, sousxy, longueurs = sousMotMaxGloutonCreux(x, y, verb=True)
print("Taille de la matrice pleine = (n+1)(m+1) =", (len(x) + 1) * (len(y) + 1))
print("Taille de la matrice creuse longueurs =", longueurs.size)


# Ici, sur deux mots de tailles raisonnables (``x = "ab0cABC0abc123456abcABCabc99"`` et ``y = "abZQXCVQDScD0EFd0ef123456abcDEFdef9999"``), on passe d'une matrice pleine de taille ``1131`` entiers à une matrice creuse de taille ``44`` entiers : le gain est considérable ! 

# In[18]:


x = "abcZZdeFG597"
y = "AbCdEFG413ZAQCWQ"
iDebut, jDebut, sousxy, longueurs = sousMotMaxGloutonCreux(x, y, verb=True)
print("Taille de la matrice pleine = (n+1)(m+1) =", (len(x) + 1) * (len(y) + 1))
print("Taille de la matrice creuse longueurs =", longueurs.size)


# Avec des mots ``x`` et ``y`` plus longs, le gain en mémoire induit par le codage creux est encore plus impressionnant :

# In[19]:


x = "ab0cABC0abc123456abcABCabc99abcZZdeFG597abcZZdeFG597abcZZdeFG597abcZZdeFG597aethjrynghù*ejgodknùebjtzinhmodgkùjihrznhumbajzdgihbjmnaekrzùdbnvkzriùnodgkl ojzirnùodk bùgbznùod1249721325414765132486513486565465klfrzinhbùodfskl p*bjùdkl nbdnù"
y = "abZQXCVQDScD0EFd0ef123456abcDEFdef9999AbCdEFG413ZAQCWQAbCdEFG413ZAQCWQAbCdEFG413ZAQCWQAbCdEFG413ZAQCWQAbCdEFG413ZAQCWQzrthekĝbùpbgmhbgdmv hubznemr1249721325414765132486513486565465ebgd"
iDebut, jDebut, sousxy, longueurs = sousMotMaxGloutonCreux(x, y, verb=False)
print("Taille de la matrice pleine = (n+1)(m+1) =", (len(x) + 1) * (len(y) + 1))
print("Taille de la matrice creuse longueurs =", longueurs.size)


# ### 4.2.1 Version condensée

# Le code de cette fonction `sousMotMaxGloutonCreux` peut sembler un peu long, mais sans messages ni commentaires il est vraiment court et simple :

# In[20]:


def sousMotMaxGloutonCreux2(x, y):
    n = len(x)
    m = len(y)
    
    longueurs = lil_matrix(np.zeros((n+1, m+1), dtype=int))
    for i in range(1, n+1):
        for j in range(1, m+1):
            if x[i-1] == y[j-1]:
                longueurs[i, j] = 1 + longueurs[i-1, j-1]
    
    iFin, jFin = 0, 0
    longueur_max = -1  # Pas encore
    for i in range(0, n+1):
        for j in range(0, m+1):
            if longueur_max < longueurs[i, j]:
                longueur_max = longueurs[i, j]
                iFin, jFin = i, j
    iDebut, jDebut = iFin - longueur_max, jFin - longueur_max

    leSousMot = x[iDebut: iDebut + longueur_max]
    return iDebut, jDebut, leSousMot, longueurs


# Et le même exemple donne pareil :

# In[21]:


x = "ab0cABC0abc123456abcABCabc99abcZZdeFG597abcZZdeFG597abcZZdeFG597abcZZdeFG597aethjrynghù*ejgodknùebjtzinhmodgkùjihrznhumbajzdgihbjmnaekrzùdbnvkzriùnodgkl ojzirnùodk bùgbznùod1249721325414765132486513486565465klfrzinhbùodfskl p*bjùdkl nbdnù"
y = "abZQXCVQDScD0EFd0ef123456abcDEFdef9999AbCdEFG413ZAQCWQAbCdEFG413ZAQCWQAbCdEFG413ZAQCWQAbCdEFG413ZAQCWQAbCdEFG413ZAQCWQzrthekĝbùpbgmhbgdmv hubznemr1249721325414765132486513486565465ebgd"
iDebut, jDebut, sousxy, longueurs = sousMotMaxGloutonCreux2(x, y)
print("Taille de la matrice pleine = (n+1)(m+1) =", (len(x) + 1) * (len(y) + 1))
print("Taille de la matrice creuse longueurs =", longueurs.size)
print("Sous-mot :", sousxy)


# ----

# # 5. Calcule de la plus longue sous-séquence commune

# Maintenant qu'on a fait tout ca, on peut implementer, de facon tres semblable, l'algorithme glouton pour le calcul de la plus longue sous-séquence commune.
# 
# Dans cet autre problème, on cherche des sous-séquences et plus des sous-mots, donc on peut extraire de facon non consécutives.
# Le développement d'agrégation devrait concerner le second problème, qui est plus intéressant:
# Par exemple, voici une version tapée en PDF : http://minerve.bretagne.ens-cachan.fr/images/Dvt_plsc.pdf.

# ## 5.1 Vérifier qu'une sous-séquence est une bonne sous-séquence

# On commencer par écrire une petite fonction qui permet de vérifier rapidement qu'une chaine est une sous-séquence d'une autre, juste en regardant la définition.

# In[22]:


def estSousSeq(seq, x, verb=True, indices=True):
    """ Verifie en temps O(|seq| |x|) que seq est une bonne sous-sequence de x.
    """
    result = False
    indices_x = []
    try:
        i = -1
        for l in seq:
            j = i+1 + x[i+1:].index(l)
            indices_x.append(j)
            i = j
        result = True
    except Exception as e:
        if verb:
            print("Erreur dans estSousSeq(seq = {}, x = {}):\n{}".format(seq, x, e))
    if indices:
        return result, indices_x
    else:
        return result


# ## 5.2 Algorithme pour la plus longue sous-séquence

# On adapte l'algorithme du plus long sous-mot pour détecter les séquences aussi.
# Cf. le PDF page 2/3.
# 
# TODO meilleures explications

# In[23]:


def utiliseTableOrigines_x(x, origines, i, j, accu=''):
    """ Renvoie la sous-séquence de x codée dans la table origines. Cf. PDF (Algorithme 2).
    
        - Calcul tail récursif (stocké dans la variable accu).
    """
    # print("  utiliseTableOrigines(x = {}, origines, i = {}, j = {}, accu = {}) : origines[i, j] = {} ...".format(x, i, j, accu, origines[i, j]))  # DEBUG
    if i == 0 or j == 0:
        return accu
    if origines[i, j] == '↖':    # Vraie correspondance, on ajoute une lettre !
        return utiliseTableOrigines_x(x, origines, i-1, j-1, x[i-1] + accu)
    elif origines[i, j] == '↑':  # Fausse correspondance, on continue a gauche...
        return utiliseTableOrigines_x(x, origines, i-1, j, accu)
    elif origines[i, j] == '←':  # Fausse correspondance, on continue en haut...
        return utiliseTableOrigines_x(x, origines, i, j-1, accu)
    else:
        raise ValueError("Erreur dans la table 'origines', invalide pour le mot x = {} ...".format(x))


def utiliseTableOrigines_y(x, origines, i, j, accu=''):
    """ Renvoie la sous-séquence de y codée dans la table origines. Cf. PDF (Algorithme 2).
    
        - Calcul tail récursif (stocké dans la variable accu).
    """
    # print("  utiliseTableOrigines(y = {}, origines, i = {}, j = {}, accu = {}) : origines[i, j] = {} ...".format(y, i, j, accu, origines[i, j]))  # DEBUG
    if i == 0 or j == 0:
        return accu
    if origines[i, j] == '↖':    # Vraie correspondance, on ajoute une lettre !
        return utiliseTableOrigines_y(x, origines, i-1, j-1, y[j-1] + accu)
    elif origines[i, j] == '↑':  # Fausse correspondance, on continue a gauche...
        return utiliseTableOrigines_y(x, origines, i-1, j, accu)
    elif origines[i, j] == '←':  # Fausse correspondance, on continue en haut...
        return utiliseTableOrigines_y(x, origines, i, j-1, accu)
    else:
        raise ValueError("Erreur dans la table 'origines', invalide pour le mot y = {} ...".format(y))


# TODO meilleures explications

# In[24]:


def sousMotSeqGlouton(x, y, verb=False, verifie=True):
    """ Calcule la plus longue sous-mot séquence a x et y, par programmation dynamique.
    
        - affiche un peu ce qu'il se passe si verb=True,
        - vérifie que la sous-séquence commun est bien une bonne sous-séquence commune si verifie=True,
        - renvoie laSousSeq, longueurs, origines, indices_x, indices_y si verifie=False,
        - renvoie laSousSeq, longueurs, origines, indices_x, indices_y si verifie=True.
    """
    def message(*args):
        if verb:
            print(*args) 
    # 1. et 2. Initialisation et construction Matrice longueurs
    n = len(x)
    m = len(y)
    message("\n1. Initialisation des look-up matrices longueurs et origines de taille (n+1, m+1) : n = {} m = {} ...".format(n, m))
    longueurs = np.zeros((n+1, m+1), dtype=int)     # Matrice c du dev en PDF
    origines = np.array([[' '] * (m+1)] * (n+1), dtype=str)  # Matrice b du dev en PDF
    # Note : on pourrait utiliser un codage a base d'entier, 0 1 2 3 pour ' ' '←' '↑' '↖' mais c'est moins joli...
    message("2. Construction bottom-up des loop-up matrices longueurs et origines ...")
    for i in range(1, n+1):
        for j in range(1, m+1):
            if x[i-1] == y[j-1]:
                longueurs[i, j] = 1 + longueurs[i-1, j-1]
                origines[i, j] = '↖'
                message("      Vraie correspondance en cours, u[{}] = {} et v[{}] = {}, de longueur courante {} ...".format(i-1, x[i-1], j-1, y[j-1], longueurs[i, j]))
            elif longueurs[i-1, j] >= longueurs[i, j-1]:
                longueurs[i, j] = longueurs[i-1, j]
                origines[i, j] = '↑'
                message("      Correspondance gauche (u) en cours, u[{}] = {} et v[{}] = {}, de pseudo-longueur courante {} ...".format(i-1, x[i-1], j-1, y[j-1], longueurs[i, j]))
            else:
                longueurs[i, j] = longueurs[i, j-1]
                origines[i, j] = '←'
                message("      Correspondance haute (v) en cours, u[{}] = {} et v[{}] = {}, de pseudo-longueur courante {} ...".format(i-1, x[i-1], j-1, y[j-1], longueurs[i, j]))

    # 3. Utilisation de la matrice longueurs
    laSousSeq = utiliseTableOrigines_x(x, origines, n, m, accu='')

    # 4. Vérification
    if verifie:
        res_x, indices_x = estSousSeq(laSousSeq, x, indices=True)
        if not res_x:
            raise ValueError("Erreur: La séquence {} de x (aux indices {}) n'est pas une bonne sous-séquence de x = {}.".format(laSousSeq, indices_x, x))
        
        laSousSeq_y = utiliseTableOrigines_y(y, origines, n, m, accu='')
        if laSousSeq != laSousSeq_y:
            raise ValueError("Erreur: La sous-séquence {} de x est différente de celle de y : {} ...".format(laSousSeq, laSousSeq_y))

        res_y, indices_y = estSousSeq(laSousSeq, y, indices=True)
        if not res_y:
            raise ValueError("Erreur: La séquence {} de y (aux indices {}) n'est pas une bonne sous-séquence de y = {}.".format(laSousSeq, indices_y, y))
        
        # Fini !
        return laSousSeq, longueurs, origines, indices_x, indices_y
    else:
        return laSousSeq, longueurs, origines


# ---

# ### 5.2.1 Exemple, venant du développement

# Blabla

# In[25]:


x = "ABCBDAB"
y = "BDCABA"
laSousSeq, longueurs, origines, indices_x, indices_y = sousMotSeqGlouton(x, y, verifie=True)
print("Sous-seq de taille", len(laSousSeq), "valant", laSousSeq, "...")
print("   - aux indices", indices_x, "pour x =", x, "...")
print("   - aux indices", indices_y, "pour y =", y, "...")
print("Et la table longueurs vaut :\n", longueurs, "...")
print("Et la table origines vaut :\n", origines, "...")


# ### 5.2.2 Autres exemples

# TODO

# ----
# 
# > *C'est tout pour aujourd'hui les amis !*
# > [Allez voir d'autres notebooks](https://github.com/Naereen/notebooks/tree/master/agreg) si vous voulez.
