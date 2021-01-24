#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Titre-de-l'oral-:-«-Comment-dessiner-des-droites-sur-un-écran-d'ordinateur-?-»" data-toc-modified-id="Titre-de-l'oral-:-«-Comment-dessiner-des-droites-sur-un-écran-d'ordinateur-?-»-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Titre de l'oral : « <em>Comment dessiner des droites sur un écran d'ordinateur ?</em> »</a></span><ul class="toc-item"><li><span><a href="#Texte-d'oral-de-modélisation,-agrég-maths-option-D-&quot;Droite-Discrète&quot;-(public-2012-D5)" data-toc-modified-id="Texte-d'oral-de-modélisation,-agrég-maths-option-D-&quot;Droite-Discrète&quot;-(public-2012-D5)-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Texte d'oral de modélisation, agrég maths option D "Droite Discrète" (public 2012 D5)</a></span></li><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Introduction</a></span></li></ul></li><li><span><a href="#Tracé-de-droites,-formalisation" data-toc-modified-id="Tracé-de-droites,-formalisation-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Tracé de droites, formalisation</a></span><ul class="toc-item"><li><span><a href="#Formalisation,-et-hypothèses" data-toc-modified-id="Formalisation,-et-hypothèses-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Formalisation, et hypothèses</a></span></li><li><span><a href="#Présentation-du-problème" data-toc-modified-id="Présentation-du-problème-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Présentation du problème</a></span></li><li><span><a href="#Généralisation-au-delà-de-ces-hypothèses-?" data-toc-modified-id="Généralisation-au-delà-de-ces-hypothèses-?-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Généralisation au delà de ces hypothèses ?</a></span></li></ul></li><li><span><a href="#Trois-méthodes-différentes-:-algorithmes,-implémentations,-exemples" data-toc-modified-id="Trois-méthodes-différentes-:-algorithmes,-implémentations,-exemples-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Trois méthodes différentes : algorithmes, implémentations, exemples</a></span><ul class="toc-item"><li><span><a href="#Implémentation-de-l'exercice-de-programmation" data-toc-modified-id="Implémentation-de-l'exercice-de-programmation-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Implémentation de l'exercice de programmation</a></span><ul class="toc-item"><li><span><a href="#Un-bidouillage-avec-Python-:-un-&quot;wrapper&quot;-qui-gère-les-symétries,-pour-ne-pas-avoir-à-les-coder-plusieurs-fois" data-toc-modified-id="Un-bidouillage-avec-Python-:-un-&quot;wrapper&quot;-qui-gère-les-symétries,-pour-ne-pas-avoir-à-les-coder-plusieurs-fois-3.1.1"><span class="toc-item-num">3.1.1&nbsp;&nbsp;</span>Un bidouillage avec Python : un "wrapper" qui gère les symétries, pour ne pas avoir à les coder plusieurs fois</a></span></li><li><span><a href="#Exemples-:-deux-premiers-quadrants,-deux-premières-demi-droites" data-toc-modified-id="Exemples-:-deux-premiers-quadrants,-deux-premières-demi-droites-3.1.2"><span class="toc-item-num">3.1.2&nbsp;&nbsp;</span>Exemples : deux premiers quadrants, deux premières demi-droites</a></span></li><li><span><a href="#Autres-exemples-:-six-autre-premiers-quadrants,-deux-autres-demi-droites" data-toc-modified-id="Autres-exemples-:-six-autre-premiers-quadrants,-deux-autres-demi-droites-3.1.3"><span class="toc-item-num">3.1.3&nbsp;&nbsp;</span>Autres exemples : six autre premiers quadrants, deux autres demi-droites</a></span></li></ul></li><li><span><a href="#Deux-autres-méthodes" data-toc-modified-id="Deux-autres-méthodes-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Deux autres méthodes</a></span><ul class="toc-item"><li><span><a href="#Longer-au-plus-près-inférieurement" data-toc-modified-id="Longer-au-plus-près-inférieurement-3.2.1"><span class="toc-item-num">3.2.1&nbsp;&nbsp;</span>Longer au plus près inférieurement</a></span></li><li><span><a href="#Longer-au-plus-près-supérieurement" data-toc-modified-id="Longer-au-plus-près-supérieurement-3.2.2"><span class="toc-item-num">3.2.2&nbsp;&nbsp;</span>Longer au plus près supérieurement</a></span></li><li><span><a href="#Une-dernière-méthode-?" data-toc-modified-id="Une-dernière-méthode-?-3.2.3"><span class="toc-item-num">3.2.3&nbsp;&nbsp;</span>Une dernière méthode ?</a></span></li><li><span><a href="#Exemples-:-deux-premiers-quadrants,-deux-premières-demi-droites" data-toc-modified-id="Exemples-:-deux-premiers-quadrants,-deux-premières-demi-droites-3.2.4"><span class="toc-item-num">3.2.4&nbsp;&nbsp;</span>Exemples : deux premiers quadrants, deux premières demi-droites</a></span></li><li><span><a href="#Autres-exemples-:-six-autre-premiers-quadrants,-deux-autres-demi-droites" data-toc-modified-id="Autres-exemples-:-six-autre-premiers-quadrants,-deux-autres-demi-droites-3.2.5"><span class="toc-item-num">3.2.5&nbsp;&nbsp;</span>Autres exemples : six autre premiers quadrants, deux autres demi-droites</a></span></li></ul></li><li><span><a href="#Visualisation-?-[si-le-temps]" data-toc-modified-id="Visualisation-?-[si-le-temps]-3.3"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>Visualisation ? <em>[si le temps]</em></a></span><ul class="toc-item"><li><span><a href="#Exemples-manuels-:" data-toc-modified-id="Exemples-manuels-:-3.3.1"><span class="toc-item-num">3.3.1&nbsp;&nbsp;</span>Exemples manuels :</a></span></li><li><span><a href="#Comparaison-graphique-des-trois-méthodes-:" data-toc-modified-id="Comparaison-graphique-des-trois-méthodes-:-3.3.2"><span class="toc-item-num">3.3.2&nbsp;&nbsp;</span>Comparaison graphique des trois méthodes :</a></span></li><li><span><a href="#Meilleur-visualisation-avec-quatre-sous-figures-?" data-toc-modified-id="Meilleur-visualisation-avec-quatre-sous-figures-?-3.3.3"><span class="toc-item-num">3.3.3&nbsp;&nbsp;</span>Meilleur visualisation avec quatre sous-figures ?</a></span></li></ul></li></ul></li><li><span><a href="#Conclusion-de-l'oral" data-toc-modified-id="Conclusion-de-l'oral-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Conclusion de l'oral</a></span><ul class="toc-item"><li><span><a href="#Autres-pistes-:" data-toc-modified-id="Autres-pistes-:-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Autres pistes :</a></span></li></ul></li></ul></div>

# # Titre de l'oral : « *Comment dessiner des droites sur un écran d'ordinateur ?* »
# ## Texte d'oral de modélisation, agrég maths option D "Droite Discrète" (public 2012 D5)
# 
# > Voir : [cette page](https://agreg.org/index.php?id=option-d) et [ce texte (public2012-D5.pdf)](https://agreg.org/Textes/public2012-D5.pdf) :
# > **2012-D5** À partir du problème de la représentation des droites sur un écran d’ordinateur, on étudie la notion de droite discrète, et le mot binaire périodique associé. On met en évidence la relation biunivoque entre droites discrètes et certains mots binaires, puis entre ces mots et les nombres rationnels de [0, 1]. Mots clefs : algorithmes, géométrie discrète, mots binaires, topologie.
# 
# - Auteur : [Lilian Besson](https://github.com/Naereen/)
# - Écrit en Python 3
# - License : [MIT Licensed](https://lbesson.mit-license.org/)
# - Date : 25/01/2021 (j'avais écrit [une solution en OCaml en 2014](https://github.com/Naereen/notebooks/tree/master/agreg/public2012_D5_OCaml.ipynb))

# ## Introduction
# 
# Donner un petit discours d'introduction :
# 
# > On cherche à dessiner des courbes mathématiques sur un écran d'ordinateur. Pour simplifier l'exposé, on ne va considérer que des écrans quadrillés, où chaque case est un "pixel", et aussi on se restreint à des graphismes en noir et blanc. Ainsi, un écran est un tableau 2D, une matrice, de pixels, et chaque pixel est soit éteint, soit allumé.
# > Si on cherche à tracer une courbe mathématique, par exemple une droite, un cercle ou d'autres courbes plus compliquée, sur un tel écran d'ordinateur, on va devoir décider quels pixels allumer ou garder éteint, le long du tracé de la courbe.
# > [faire un dessin au tableau]
# 
# > Pour commencer, on va uniquement s'intéresser au cas d'une droite, qui va du pixel O=(0,0) tout en bas à droite de l'écran, jusqu'à un autre point B=(b1,b2) de l'écran (à coordonnées entières, donc), situé à droite et en haut de l'origine O.
# > On pose $\alpha=b2/b1 \in \mathbb{R} \cup \{\pm\infty\}$ la pente de cette droite.
# 
# > Comme on le voit, si la courbe est un cas particulier très facile, il n'y a pas de difficultés particulières.
# > Les cas faciles sont les courbes horizontales, de pente $1$ ou verticales, soit $\alpha \in \{0,1,\infty\}$.
# > Dans les autres cas, la pente est toujours rationnelle, mais en général elle ne sera pas entière.
# > Nous allons d'abord étudier le cas particulier d'une pente $\alpha < 1$, mais il est très facile de généraliser aux sept autres quadrants [faire un dessin], avec des rotations, et en échangeant le point de départ A et l'arrivée B.
# 
# > Nous formalisons le problème, en faisant le lien entre les coordonnées réelles des points $M_i = (x_i,y_i)$ sur la droite [AB], qui sont $x_i = i$ et $y_i \in \mathbb{R}$ peut être réel et même irrationnels, et les points $(x_i, \tilde{y_i})$ qui sont les coordonnées
# > (par convention, le point de référence des pixels est le point en bas à gauche)
# 
# > Nous présenterons et implémenterons trois différentes méthodes, qui ont toute la même complexité algorithmique, mais qui donnent des tracés différents dans le cas d'une droite quelconque.
# 
# > 
# 
# **Plan** : voir table des matières pour le détail. [écrire au tableau]
# 
# - I)   *Introduction*
# - II)  Tracé de droites, formalisation
# - III) Trois méthodes différentes : algorithmes, implémentations, exemples *[visualisation si le temps ?]*
# - IV)  Mathématiques des droites discrètes
# - V)   Mots binaires
# - VI)  Liens entre les (pentes) rationnels et les mots binaires *[si le temps ?]*
# - VII) *Conclusion et ouvertures*

# #  Tracé de droites, formalisation
# AU TABLEAU

# ## Formalisation, et hypothèses

# ## Présentation du problème
# 
# TODO
# 
# TL;DR : on cherche des algorithmes qui évitent de calculer des erreurs sur des nombres réels, parce qu'on sait que les flottants propagent des erreurs de calculs.

# ## Généralisation au delà de ces hypothèses ?

# # Trois méthodes différentes : algorithmes, implémentations, exemples 

# ## Implémentation de l'exercice de programmation
# 
# <span style="color:red;">ATTENTION</span> depuis 2019, l'*exercice de programmation obligatoire* qui était indiqué dans les anciens textes d'option D est devenu, comme pour les autres options A/B/C, une simple *suggestion*.
# - Avant 2019, il fallait absolument implémenter l'exercice demandé, et éventuellement faire plus ;
# - Maintenant, on fait ce qu'on veut. Le jury n'a pas encore diffusé de texte suivant la nouvelle consigne, donc je vous conseille l'approche suivante : pour les vieux textes, il faut juste remplacer *exercice de programmation obligatoire* par *suggestion de programmation*.

# > Écrire  un  programme  permettant  de  représenter  le  segment [AB],  où A= (a1,a2) et B=(b1,b2), en suivant l’algorithme de Bresenham. On supposera que a1<b1, a2≤b2 et que la pente $\alpha$ de la droite est inférieure à 1.
# > La sortie du programme sera la liste des couples (xi,yi) des points représentant le segment.

# ### Un bidouillage avec Python : un "wrapper" qui gère les symétries, pour ne pas avoir à les coder plusieurs fois
# 
# On peut écrire un décorateur Python qui se charge de gérer toutes les symétries, afin de ne pas à avoir à copier-coller ça pour les méthodes suivantes.

# In[198]:


def gerersymetrie(nom=""):
    def decorator(f):
        def g(A, B):
            a1, a2 = int(A[0]), int(A[1])
            b1, b2 = int(B[0]), int(B[1])
            # on commence à traiter les symétries

            if a1 == b1:
                # il faut renvoyer une droite verticale, facile à faire
                if b2 < a2:
                    print(f"{nom} (avant symétries) avec une pente = -oo")
                    return g(B, A)
                # OK maintenant b2 >= a2
                print(f"{nom} (avant symétries) avec une pente = +oo")
                points = [
                    (a1, a2 + i) for i in range(b2 - a2 + 1)
                    # droite verticale, même x, y change
                ]
                return points

            pente = float(b2-a2) / float(b1-a1)

            if a1 > b1:  # cas facile !
                print(f"{nom} (avant symétries) avec une pente = {pente}")
                return g(B, A)

            # OK maintenant a1 < b1
            # vérification des hypothèses 1/2
            assert a1 < b1, f"Erreur : {nom} demande a1 = {a1} < a2 = {b1}."

            if pente > 1:  # cas plus difficile, il faudra calculer une symétrie
                # --> i) symétrie % axe horizontal
                Bx = [B[1], B[0]]
                print(f"{nom} (avant symétries) avec une pente = {pente}")
                points = g(A, Bx)
                # <-- i) symétrie % droite {(x,x)}
                points = [ (y, x) for (x,y) in points ]
                return points

            if a2 > b2:  # cas plus difficile, il faudra calculer une symétrie
                Ax = [0,0]
                # --> i) translation =>
                Bx = [b1 - a1, b2 - a2]
                # --> --> ii) symétrie % axe horizontal
                Bxx = [Bx[0], -Bx[1]]
                print(f"{nom} (avant symétries) avec une pente = {pente}")
                points = g(Ax, Bxx)
                # <-- <-- ii) symétrie % axe horizontal
                points = [ (x, -y) for (x,y) in points ]
                # <-- i) translation <=
                points = [ (x + a1, y + a2) for (x,y) in points ]
                return points
            
            # cas de base, on propage
            return f(A, B)

        if f.__doc__:
            g.__doc__ = f.__doc__
        g.__nom__ = nom
        # maintenant on a un wrapper g(A,B) qui gère les symétries
        return g
    # et voilà on a un decorateur
    return decorator


# Maintenant on peut écrire la méthode de Bresenham, en gérant uniquement le cas qui nous arrange :

# In[199]:


# cette ligne fait que la fonction finale va gérer les symétries !
@gerersymetrie(nom="Méthode de Bresenham")
def methode_bresenham(A, B):
    """ Méthode de Bresenham.
    
    - Si N = |A B| longueur du segment, cette fonction tourne en temps O(N) et en mémoire O(N)
      N = max(n, m) avec m = |b2 - a2| et n = |b1 - a1| nb de déplacement sur l'axe horizontal/vertical

    - Fonctionne dans tous les cas, supporte les huit quadrants, les quatre demi-droites,
      et le cas spécial A==B, en exploitant les symétries et se ramener au cas de base :
      a1 < b1, b2 <= a2 (pente = (b2-a2)/(b1-a1) = alpha, 0 <= alpha <= 1)
    """
    a1, a2 = int(A[0]), int(A[1])
    b1, b2 = int(B[0]), int(B[1])

    pente = float(b2-a2) / float(b1-a1)

    # vérification des hypothèses 2/2
    assert 0 <= pente <= 1, f"Erreur : la méthode de Bresenham demande 0 <= pente = {pente} <= 1."
    print(f"Méthode de Bresenham (après symétries éventuelles) avec une pente 0 <= pente = {pente} <= 1")

    points = []
    points.append(A)    # premier point A

    nombre_point = b1 - a1  # c'est le n du texte
    pente_normalise = b2 - a2  # le m du texte = b2-a2, c'est la pente normalisée alpha*n
    xi = int(a1)
    yi = int(a2)
    ei = 0
    
    for i in range(1, nombre_point):
        xi += 1

        # cette partie spécifique à Bresenham, et change selon les trois méthodes
        if 2 * ( ei + pente_normalise ) <= nombre_point:
            ei += pente_normalise
            yi += 0  # inutile, juste pour le montrer
        else:
            ei += pente_normalise - nombre_point
            yi += 1

        points.append((xi, yi))
    
    # et dernier point B
    points.append(B)
    return points


# ### Exemples : deux premiers quadrants, deux premières demi-droites

# - Avec une pente $\alpha=1$, tous les `yi += O/1` seront `yi += 1` :

# In[200]:


A = (0, 0)
B = (4, 4)  # pente 1
print(methode_bresenham(A, B))


# - Avec une pente $\alpha=0$, tous les `yi += O/1` seront `yi += 0` :

# In[201]:


A = (0, 0)
B = (4, 0)  # pente 0
print(methode_bresenham(A, B))


# - Avec une pente $0 < \alpha < 1$, tous les `yi += O/1` suivent la méthode de Bresenham :

# In[202]:


A = (0, 0)
B = (4, 3)  # pente 3/4
print(methode_bresenham(A, B))


# - Avec une pente $1 < \alpha < +\infty$, ce sont maintenant les `yi += 1` mais les `xi += O/1` qui suivent la méthode de Bresenham :

# In[203]:


A = (0, 0)
B = (3, 4)  # pente 4/3
print(methode_bresenham(A, B))


# - Avec une pente $\alpha = -\infty$, ce sont maintenant les `yi += 1` et tous les `xi += O/1` sont des `+= 1` :

# In[204]:


A = (0, 0)
B = (0, 4)  # pente +infini
print(methode_bresenham(A, B))


# ### Autres exemples : six autre premiers quadrants, deux autres demi-droites
# 
# On fera ces autres exemples quand on aura les deux autres méthodes.

# ## Deux autres méthodes

# Une fois que l'on aura écrit la méthode de Bresenham, on peut rapidement implémenter deux autres approches qui consistent en longer au plus près inférieurement, supérieurement.

# In[206]:


from math import floor, ceil


# ### Longer au plus près inférieurement

# In[207]:


@gerersymetrie(nom="Méthode de longer au plus près inférieurement")
def methode_longer_inferieurement(A, B):
    """ Méthode de longer au plus près inférieurement.
    
    - Si N = |A B| longueur du segment, cette fonction tourne en temps O(N) et en mémoire O(N)
      N = max(n, m) avec m = |b2 - a2| et n = |b1 - a1| nb de déplacement sur l'axe horizontal/vertical

    - Fonctionne dans tous les cas, supporte les huit quadrants, les quatre demi-droites,
      et le cas spécial A==B, en exploitant les symétries et se ramener au cas de base :
      a1 < b1, b2 <= a2 (pente = (b2-a2)/(b1-a1) = alpha, 0 <= alpha <= 1)
    """
    a1, a2 = int(A[0]), int(A[1])
    b1, b2 = int(B[0]), int(B[1])

    pente = float(b2-a2) / float(b1-a1)

    # vérification des hypothèses 2/2
    assert 0 <= pente <= 1, f"Erreur : la méthode de longer au plus près inférieurement demande 0 <= pente = {pente} <= 1."
    print(f"Méthode de longer au plus près inférieurement (après symétries éventuelles) avec une pente 0 <= pente = {pente} <= 1")

    points = []
    points.append(A)    # premier point A

    nombre_point = b1 - a1  # c'est le n du texte
    pente_normalise = b2 - a2  # le m du texte = b2-a2, c'est la pente normalisée alpha*n
    xi = int(a1)
    yi = int(a2)
    ei = 0
    
    for i in range(1, nombre_point):
        xi += 1
        # cette partie est spécifique à cette méthode
        yi = floor(a2 + pente*i)

        points.append((xi, yi))
    
    # et dernier point B
    points.append(B)
    return points


# ### Longer au plus près supérieurement

# In[208]:


@gerersymetrie(nom="Méthode de longer au plus près supérieurement")
def methode_longer_superieurement(A, B):
    """ Méthode de longer au plus près supérieurement.
    
    - Si N = |A B| longueur du segment, cette fonction tourne en temps O(N) et en mémoire O(N)
      N = max(n, m) avec m = |b2 - a2| et n = |b1 - a1| nb de déplacement sur l'axe horizontal/vertical

    - Fonctionne dans tous les cas, supporte les huit quadrants, les quatre demi-droites,
      et le cas spécial A==B, en exploitant les symétries et se ramener au cas de base :
      a1 < b1, b2 <= a2 (pente = (b2-a2)/(b1-a1) = alpha, 0 <= alpha <= 1)
    """
    a1, a2 = int(A[0]), int(A[1])
    b1, b2 = int(B[0]), int(B[1])

    pente = float(b2-a2) / float(b1-a1)

    # vérification des hypothèses 2/2
    assert 0 <= pente <= 1, f"Erreur : la méthode de longer au plus près supérieurement demande 0 <= pente = {pente} <= 1."
    print(f"Méthode de longer au plus près supérieurement (après symétries éventuelles) avec une pente 0 <= pente = {pente} <= 1")

    points = []
    points.append(A)    # premier point A

    nombre_point = b1 - a1  # c'est le n du texte
    pente_normalise = b2 - a2  # le m du texte = b2-a2, c'est la pente normalisée alpha*n
    xi = int(a1)
    yi = int(a2)
    ei = 0
    
    for i in range(1, nombre_point):
        xi += 1
        # cette partie est spécifique à cette méthode
        yi = ceil(a2 + pente*i)

        points.append((xi, yi))
    
    # et dernier point B
    points.append(B)
    return points


# ### Une dernière méthode ?
# 
# On peut aussi longer la droite aléatoirement, en prenant inférieurement ou supérieurement uniformément au hasard.
# Cela n'a pas d'intérêt particulier, mais c'est rapide à écrire alors autant le faire :

# In[209]:


import random


# In[210]:


[ random.randint(0, 1) for _ in range(20) ]


# On peut facilement remplacer le calcul de $\tilde{y_i}$ par simplement un choix aléatoire uniforme entre le choix floor et le choix ceil :

# In[347]:


@gerersymetrie(nom="Méthode de longer aléatoirement")
def methode_longer_aleatoirement(A, B):
    """ Méthode de longer aléatoirement.
    
    - Si N = |A B| longueur du segment, cette fonction tourne en temps O(N) et en mémoire O(N)
      N = max(n, m) avec m = |b2 - a2| et n = |b1 - a1| nb de déplacement sur l'axe horizontal/vertical

    - Fonctionne dans tous les cas, supporte les huit quadrants, les quatre demi-droites,
      et le cas spécial A==B, en exploitant les symétries et se ramener au cas de base :
      a1 < b1, b2 <= a2 (pente = (b2-a2)/(b1-a1) = alpha, 0 <= alpha <= 1)
    """
    a1, a2 = int(A[0]), int(A[1])
    b1, b2 = int(B[0]), int(B[1])

    pente = float(b2-a2) / float(b1-a1)

    # vérification des hypothèses 2/2
    assert 0 <= pente <= 1, f"Erreur : la méthode de longer aléatoirement demande 0 <= pente = {pente} <= 1."
    print(f"Méthode de longer aléatoirement (après symétries éventuelles) avec une pente 0 <= pente = {pente} <= 1")

    points = []
    points.append(A)    # premier point A

    nombre_point = b1 - a1  # c'est le n du texte
    pente_normalise = b2 - a2  # le m du texte = b2-a2, c'est la pente normalisée alpha*n
    xi = int(a1)
    yi = int(a2)
    ei = 0
    
    for i in range(1, nombre_point):
        xi += 1
        # cette partie est spécifique à cette méthode
        if random.randint(0, 1) == 0:
            yi = floor(a2 + pente*i)
        else:
            yi = ceil(a2 + pente*i)
        # écrire cela est aussi possible
        # yi += random.randint(0, 1)  # TODO

        points.append((xi, yi))
    
    # et dernier point B
    points.append(B)
    return points


# ### Exemples : deux premiers quadrants, deux premières demi-droites

# - Avec une pente $\alpha=1$, tous les `yi += O/1` seront `yi += 1` :

# In[212]:


A = (0, 0)
B = (4, 4)  # pente 1
print(methode_longer_inferieurement(A, B))
print(methode_longer_superieurement(A, B))
print(methode_longer_aleatoirement(A, B))


# - Avec une pente $\alpha=0$, tous les `yi += O/1` seront `yi += 0` :

# In[213]:


A = (0, 0)
B = (4, 0)  # pente 0
print(methode_longer_inferieurement(A, B))
print(methode_longer_superieurement(A, B))
print(methode_longer_aleatoirement(A, B))


# - Avec une pente $0 < \alpha < 1$, tous les `yi += O/1` suivent la méthode choisie :

# In[214]:


A = (0, 0)
B = (4, 3)  # pente 3/4
print(methode_longer_inferieurement(A, B))
print(methode_longer_superieurement(A, B))
print(methode_longer_aleatoirement(A, B))


# - Avec une pente $1 < \alpha < +\infty$, ce sont maintenant les `yi += 1` mais les `xi += O/1` qui suivent la méthode choisie :

# In[215]:


A = (0, 0)
B = (3, 4)  # pente 4/3
print(methode_longer_inferieurement(A, B))
print(methode_longer_superieurement(A, B))
print(methode_longer_aleatoirement(A, B))


# - Avec une pente $\alpha = -\infty$, ce sont maintenant les `yi += 1` et tous les `xi += O/1` sont des `+= 1` :

# In[216]:


A = (0, 0)
B = (0, 4)  # pente +infini
print(methode_longer_inferieurement(A, B))
print(methode_longer_superieurement(A, B))
print(methode_longer_aleatoirement(A, B))


# ### Autres exemples : six autre premiers quadrants, deux autres demi-droites
# 
# On fera ces autres exemples quand on aura les deux autres méthodes.

# - Quadrant #3, b1 < a1 mais b2 > a2 et b2 >= b1 :

# In[217]:


A = (0, 0)
B = (-3, 4)  # pente -4/3
print(methode_bresenham(A, B))
print(methode_longer_inferieurement(A, B))
print(methode_longer_superieurement(A, B))
print(methode_longer_aleatoirement(A, B))


# - Quadrant #4, b1 < a1 mais b2 > a2 et b2 < b1 :

# In[218]:


A = (0, 0)
B = (-4, 3)  # pente -3/4
print(methode_bresenham(A, B))
print(methode_longer_inferieurement(A, B))
print(methode_longer_superieurement(A, B))
print(methode_longer_aleatoirement(A, B))


# - Quadrant #5 :

# In[219]:


A = (0, 0)
B = (-4, -3)  # pente -3/-4
print(methode_bresenham(A, B))
print(methode_longer_inferieurement(A, B))
print(methode_longer_superieurement(A, B))
print(methode_longer_aleatoirement(A, B))


# - Quadrant #6 :

# In[ ]:


A = (0, 0)
B = (-3, -4)  # pente -4/-3
print(methode_bresenham(A, B))
print(methode_longer_inferieurement(A, B))
print(methode_longer_superieurement(A, B))
print(methode_longer_aleatoirement(A, B))


# **TODO fix this bug?**

# - Quadrant #7 :

# In[348]:


A = (0, 0)
B = (3, -4)  # pente 3/-4
print(methode_bresenham(A, B))
print(methode_longer_inferieurement(A, B))
print(methode_longer_superieurement(A, B))
print(methode_longer_aleatoirement(A, B))


# - Quadrant #8 :

# In[349]:


A = (0, 0)
B = (4, -3)  # pente 4/-3
print(methode_bresenham(A, B))
print(methode_longer_inferieurement(A, B))
print(methode_longer_superieurement(A, B))
print(methode_longer_aleatoirement(A, B))


# ---
# ## Visualisation ? *[si le temps]*
# 
# Ca ne devrait pas être trop compliqué :
# 
# - il faut pouvoir donner la pente, comme un rationnel ou un flottant,
# - et les points [M0,...,MN] donné avec leurs coordonnées (en général, M0=A=O=(0,0) et MN=B=(b1,b2)),
# - et afficher la courbe et les pixels allumés, comme des gros rectangles.

# In[ ]:


import matplotlib.pyplot as plt

# https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.patches.Rectangle.html?highlight=rectangle#matplotlib.patches.Rectangle
from matplotlib.patches import Rectangle


# In[288]:


def plot_discrete_line(points=None,  # liste des coordonnées [M0,...,MN]
                       A=None, B=None,
                       methodes=[],  # liste de fonctions à utiliser pour calculer les points, si absents
                       title="Dessin d'une droite discrète",
                       width=50, height=None,
                       figsize=(10,7),
                       linewidth=2,
                       fill=True,
                       edgecolors=['r'],
                       facecolors=None,
                       alpha=0.4,
                       linecolor='k',
                       equal=True,
                       pente=None,
                      ):
    fig = plt.figure(figsize=figsize)

    if equal: plt.axis('equal')
    if not facecolors: facecolors = edgecolors
    if not height: height = width
        
    use_fake_methode = False
    if not methodes:
        use_fake_methode = True
        def fake_methode(A, B): return points
        fake_methode.__nom__ = "Fake method XXX"
        methodes = [fake_methode]

    for i, methode in enumerate(methodes):
        points = methode(A, B)
    
        # points in P should be ordored, but not restricted to Mi = (xi, yi) with xi=i
        min_x = min(p[0] for p in points)
        max_x = max(p[0] for p in points)
        plt.xlim((min_x - 0.2)*width, (max_x + 1 + 0.2)*width)
        min_y = min(p[1] for p in points)
        max_y = max(p[1] for p in points)
        plt.ylim((min_y - 0.2)*height, (max_y + 1 + 0.2)*height)

        # plot the points as big rectangles
        for p in points:
            x, y = p
            rect = Rectangle(
                (x*width, y*height),
                width, height,
                linewidth=linewidth,
                edgecolor=edgecolors[i], facecolor=facecolors[i],
                alpha=alpha, fill=fill,
            )
            plt.gca().add_patch(rect)
        
        _xs = np.linspace(min_x, max_x, 2000)
        _ys = np.linspace(min_y, max_y, 2000)

        # Trick to add a legend?
        plt.plot(
            _xs[:2]*width, _ys[:2]*width,
            color=edgecolors[i], label=methode.__nom__
        )
        
        # plot the line
        plt.plot(_xs*width, _ys*width, color=linecolor, linewidth=1+linewidth)
        

    if not use_fake_methode:
        plt.legend()
    if title:
        if pente and "pente" not in title:
            if not isinstance(pente, str):
                pente = "{:.3g}".format(pente)
            title += " de pente = ${}$".format(pente)
        plt.title(title)

    fig.tight_layout()
    plt.show()
    # return fig


# ### Exemples manuels :

# In[279]:


points = [ (0,0), (1,1), (2,2), (3,3), (4,4) ]

plot_discrete_line(points, pente=1.0)


# In[280]:


points = [ (0,0), (1,0), (2,1), (3,1), (4,2), (5,2) ]

plot_discrete_line(points, pente=0.5)


# On peut évidemment dessiner des droites avec une pente qui ne vérifie pas $0 < \alpha < 1$ :

# In[281]:


points = [ (0,0), (0,1), (1,2), (1,3), (2,4), (2,5) ]

plot_discrete_line(points, pente=2)


# ### Comparaison graphique des trois méthodes :
# 
# On va prendre les exemples précédents, et les afficher dans la même figure :

# In[291]:


methodes = [
    methode_bresenham,
    methode_longer_inferieurement,
    methode_longer_superieurement,
    methode_longer_aleatoirement
]


# - Avec une pente $\alpha=1$, tous les `yi += O/1` seront `yi += 1` :

# In[292]:


A = (0, 0)
B = (20, 20)  # pente 1
pente = (B[1] - A[1]) / (B[0] - A[0])
plot_discrete_line(A=A, B=B, pente=pente,
                   methodes=methodes,
                   edgecolors=['red', 'blue', 'orange', 'purple']
)


# - Avec une pente $\alpha=0$, tous les `yi += O/1` seront `yi += 0` :

# In[293]:


A = (0, 0)
B = (20, 0)  # pente 0
pente = (B[1] - A[1]) / (B[0] - A[0])
plot_discrete_line(A=A, B=B, pente=pente,
                   methodes=methodes,
                   edgecolors=['red', 'blue', 'orange', 'purple']
)


# - Avec une pente $0 < \alpha < 1$, tous les `yi += O/1` suivent la méthode de Bresenham :

# In[294]:


A = (0, 0)
B = (20, 7)  # pente 7/20
pente = (B[1] - A[1]) / (B[0] - A[0])
plot_discrete_line(A=A, B=B, pente=pente,
                   methodes=methodes,
                   edgecolors=['red', 'blue', 'orange', 'purple']
)


# In[295]:


A = (0, 0)
B = (7, 20)  # pente 20/7
pente = (B[1] - A[1]) / (B[0] - A[0])
plot_discrete_line(A=A, B=B, pente=pente,
                   methodes=methodes,
                   edgecolors=['red', 'blue', 'orange', 'purple']
)


# - Avec une pente $\alpha = +\infty$, ce sont maintenant les `yi += 1` et tous les `xi += O/1` sont des `+= 1` :

# In[296]:


A = (0, 0)
B = (0, 7)  # pente +infini
print(methode_bresenham(A, B))
pente = '+oo'
plot_discrete_line(A=A, B=B, pente=pente,
                   methodes=methodes,
                   edgecolors=['red', 'blue', 'orange', 'purple']
)


# ### Meilleur visualisation avec quatre sous-figures ?
# 
# Pas le temps, mais il serait plus approprié de montrer les quatres méthodes m1/m2/m3/m4 comme ça :
# [ m1 | m2 ]
# [ m3 | m4 ]
# 
# Avec plt.subplots(2,2) ce ne serait pas trop difficile

# In[327]:


nos_4_methodes = [
    methode_bresenham,
    methode_longer_aleatoirement,
    methode_longer_inferieurement,
    methode_longer_superieurement,
]


# In[343]:


def plot_4_differents_methods(A=None, B=None,
                       title="Dessin d'une droite discrète",
                       width=50, height=None,
                       figsize=(20,14),
                       linewidth=2,
                       fill=True,
                       methodes=nos_4_methodes,
                       edgecolors=['red', 'blue', 'orange', 'purple'],
                       facecolors=None,
                       alpha=0.4,
                       linecolor='k',
                       equal=True,
                       pente=None,
                      ):
    fig, axs = plt.subplots(2, 2, figsize=figsize)

    if not facecolors: facecolors = edgecolors
    if not height: height = width
        
    use_fake_methode = False
    if not methodes:
        use_fake_methode = True
        def fake_methode(A, B): return points
        fake_methode.__nom__ = "Fake method XXX"
        methodes = [fake_methode]

    i_x_axis = 0
    j_y_axis = 0
    for i, methode in enumerate(methodes):
        points = methode(A, B)
        ax = axs[i_x_axis, j_y_axis]
        if equal: ax.set_aspect('equal')
    
        # points in P should be ordored, but not restricted to Mi = (xi, yi) with xi=i
        min_x = min(p[0] for p in points)
        max_x = max(p[0] for p in points)
        # plt.xlim((min_x - 0.2)*width, (max_x + 1 + 0.2)*width)
        min_y = min(p[1] for p in points)
        max_y = max(p[1] for p in points)
        # plt.ylim((min_y - 0.2)*height, (max_y + 1 + 0.2)*height)
        
        _xs = np.linspace(min_x, max_x, 2000)
        _ys = np.linspace(min_y, max_y, 2000)

        # Trick to add a legend?
        ax.plot(
            _xs[:2]*width, _ys[:2]*width,
            color=edgecolors[i], label=methode.__nom__
        )
        
        # plot the line
        ax.plot(_xs*width, _ys*width, color=linecolor, linewidth=1+linewidth)

        # plot the points as big rectangles
        for p in points:
            x, y = p
            rect = Rectangle(
                (x*width, y*height),
                width, height,
                linewidth=linewidth,
                edgecolor=edgecolors[i], facecolor=facecolors[i],
                alpha=alpha, fill=fill,
            )
            ax.add_patch(rect)
        
        i_x_axis = (i_x_axis + 1) % 2
        if i_x_axis == 1:
            j_y_axis = (j_y_axis + 1) % 2

        if not use_fake_methode:
            ax.legend()
        if not title:
            title = methode.nom
        if title:
            if pente and "pente" not in title:
                if not isinstance(pente, str):
                    pente = "{:.5g}".format(pente)
                title += " de pente = ${}$".format(pente)
            ax.set_title(title)

    plt.show()
    # return fig


# Un exemple :

# In[344]:


A = (0, 0)
B = (20, 7)  # pente 7/20
pente = (B[1] - A[1]) / (B[0] - A[0])
plot_4_differents_methods(A=A, B=B, pente=pente)


# In[345]:


A = (0, 0)
B = (7, 20)  # pente 20/7
pente = (B[1] - A[1]) / (B[0] - A[0])
plot_4_differents_methods(A=A, B=B, pente=pente)


# In[346]:


A = (0, 0)
B = (-7, 20)  # pente 20/-7
pente = (B[1] - A[1]) / (B[0] - A[0])
plot_4_differents_methods(A=A, B=B, pente=pente)


# **Bon c'était clairement trop long, inutile et impossible le jour même.**

# TODO si le temps:
# - corriger dessin de la courbe noire en cas de symétries

# ---
# # Conclusion de l'oral
# 
# Donner une conclusion, scientifique et aussi personnelle, en 2-4 minutes.
# 
# Blabla TODO
# 
# > Cela peut aussi s'appliquer en dehors des écrans, par exemple les mosaïques ou la broderie subissent les mêmes contraintes de dessins sur un support quadrillé et "pixelisé", et donc les méthodes mises au point sur le premier problème pourraient être aussi utilisées dans ces pratiques artistiques.
# > On peut même imaginer qu'un artist mosaïste durant l'Antiquité Romaine suivant ce genre de méthodes de "longer au plus près inférieurement", sans même y réfléchir formellement.
# 
# *[si le temps]*
# > Une question en ouverture : et si on passe en 3D, est-ce beaucoup plus compliqué ?
# > Mon intuition dit que oui ! Et il s'ajoute aussi la difficulté de savoir quel *support* est utilisé pour représenter un objet en 3D.
# > L'analogie la plus simple sera de jouer avec des briques de Légo, qui pourraient se fixer dans les six directions (aux sommets du cube actuel).
# > Même si ce serait intéressant de généraliser notre modélisation et les méthodes développées pour le tracé de courbes, du 2D à la 3D, je peine à voir ce qu'on pourrait généraliser pour la partie plus mathématiques liées au mots binaires.

# ## Autres pistes :
# 
# - DONE généraliser à tous les cas d'une droite : verticale, horizontale, et les sept autre quadrants (ici, seulement $0 < \alpha < 1$ et $a_2 \leq b_2$) ;
# 
# - DONE écrire une fonction permettant de visualiser cette méthode de Bresenham, et les autres méthodes, par exemple avec ipythonblocks (pratique mais pas possible le jour J des oraux), ou avec matplotlib (ce sera un peu plus long, mais disponible le jour J) ;
# 
# - TODO généraliser l'algorithme à un cercle, par exemple, ou d'autres figures dont on connaît des équations et qu'on peut chercher à vouloir longer au plus près inférieurement, supérieurement, ou de façon hybride à la Bresenham ;
# 
# - TODO pour s'éloigner davantage du problème de tracés de droite, on peut implémenter des choses concernant les mots binaires (ultimement) périodiques (abbrégés en *mbup*) :
# 
#   + représentation d'un *mbup*, affichage ;
#   + vérification qu'un mot binaire est bien équilibré : est-ce seulement possible, sachant que Déf.5 porte sur un mot infini ?
#   + transformation d'un *mbup* en une droite discrète (§6) $\sigma \mapsto (M_0,\dots,M_n)$ ;
#   + mot binaire *up* associé à un rationnel, et inversement : est-ce facile d'écrire deux fonctions qui effectuent ces transformations, par exemple $\frac{2}{3} \leftrightarrow (011)^\omega$ ?
