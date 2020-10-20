#!/usr/bin/env python
# coding: utf-8

# # Tri tricolore - un petit exerice d'algorithmique
# 
# On aligne $n$ boules, réparties en un nombre quelconque de boules de couleur bleue, blanche ou rouge.
# Ces boules sont disposees dans un ordre quelconque. La ligne de boules est representée par un tableau `B` de taille $n$, dont chaque  ́element `B[i]` appartient à l’ensemble `{bleu, blanc, rouge}`
# 
# **Question :** ́Ecrire un algorithme qui trie le tableau de telle facon que toutes les boules bleues apparaissent au debut, suivies des boules blanches puis des boules rouges.
# La contrainte est que le tri du tableau doit être realise en seul parcours (on ne peut tester qu’une seule fois la couleur de chaque boule) et en place (sans utiliser de deuxieme tableau).
# 
# **Indication :** Les elements d’un tableau peuvent être réécrits.

# ## Solution en Python : exemples et affichage

# D'abord, quelques exemples de tableaux.

# In[1]:


BLEU, BLANC, ROUGE = "bleu", "blanc", "rouge"


# In[2]:


boules1 = [BLEU, BLANC, ROUGE, ROUGE, BLANC, BLEU, BLANC, ROUGE, BLANC, BLEU, ROUGE]


# In[36]:


boules2 = [BLEU, BLANC, ROUGE, ROUGE, BLANC, BLEU, BLANC, ROUGE, BLANC, BLEU, ROUGE][::-1]


# In[37]:


boules3 = boules2 *2 + boules1 * 2


# Et des cas spéciaux, sans forcément avoir des boules de chaque couleurs :

# In[79]:


boules4 = [BLEU, BLANC, BLEU, BLANC, BLEU, BLANC, BLEU, BLANC, BLEU, BLANC, BLEU, BLANC]  # pas de rouges
boules5 = [BLANC, ROUGE, BLANC, ROUGE, BLANC, ROUGE, BLANC, ROUGE, BLANC, ROUGE, BLANC, ROUGE]  # pas de bleues
boules6 = [ROUGE, BLEU, ROUGE, BLEU, ROUGE, BLEU, ROUGE, BLEU, ROUGE, BLEU, ROUGE, BLEU, ROUGE, BLEU]  # pas de blanches


# In[88]:


boules7 = [BLEU] * 20  # que des bleues
boules8 = [BLANC] * 20  # que des blanches
boules9 = [ROUGE] * 20  # que des rouges


# Juste pour faire joli, je vais écrire des fonctions qui soient "typées" en Python, c'est-à-dire avec des indications de types. Python reste un langage dynamiquement typé, ces indications seront JUSTE là pour faire joli.

# In[5]:


from typing import List, Union

Boule = Union["bleu", "blanc", "rouge"]
Boules = List[Boule]


# Visualisation : je vais utiliser le petit module [`ipythonblocks`](http://www.ipythonblocks.org/about) :

# In[22]:


from ipythonblocks import BlockGrid

c_bleu, c_blanc, c_rouge = (0, 0, 255), (215, 215, 215), (255, 0, 0)


# In[32]:


def boules_vers_grid(boules: Boules) -> BlockGrid:
    n = len(boules)
    grid = BlockGrid(n, 1, fill=(c_blanc))
    for i, boule in enumerate(boules):
        if boule == BLEU:
            grid[0,i].set_colors(*c_bleu)
        elif boule == BLANC:
            grid[0,i].set_colors(*c_blanc)
        elif boule == ROUGE:
            grid[0,i].set_colors(*c_rouge)
    return grid

def print_boules(boules: Boules) -> None:
    boules_vers_grid(boules).show()


# In[81]:


print_boules(boules1)
print_boules(boules2)
print_boules(boules3)


# In[89]:


print_boules(boules4)
print_boules(boules5)
print_boules(boules6)


# In[90]:


print_boules(boules7)
print_boules(boules8)
print_boules(boules9)


# ## Algorithmes de tri tricolore

# ### Tri naïf : avec `sorted` ou un tri écrit à la main

# In[40]:


def echange(tab: List, i: int, j: int) -> None:
    tab[i], tab[j] = tab[j], tab[i]


# In[41]:


def comparaison_couleur(boule1: Boule, boule2: Boule) -> int:
    """ Renvoie +1 si boule1 > boule2, 0 si =, -1 si <."""
    b1, b2 = boule1, boule2
    if b1 == b2:
        return 0
    elif b1 == BLEU:
        return -1
    elif b1 == BLANC:
        if b2 == BLEU:
            return +1
        elif b2 == ROUGE:
            return -1
    elif b1 == ROUGE:
        return +1


# In[42]:


import itertools


# In[46]:


for boule1, boule2 in itertools.product([BLEU, BLANC, ROUGE], repeat=2):
    print(f"Comparaison {boule1:>5} et {boule2:>5} = {comparaison_couleur(boule1, boule2)}")


# In[52]:


def tri_a_bulle(boules: Boules) -> Boules:
    b = boules[:]
    n = len(b)
    for i in range(n - 1, -1, -1):
        for j in range(0, i):
            if comparaison_couleur(b[j+1], b[j]) < 0:
                echange(b, j+1, j)
                print_boules(b)
    return b


# In[53]:


tri_a_bulle(boules1)


# In[54]:


tri_a_bulle(boules2)


# In[55]:


tri_a_bulle(boules3)


# ### Tri comptage (sans échange de valeurs)
# 
# Ici, on connaît le domaine des valeurs, qui est de taille 3 (trois couleurs).
# Le tri comptage va faire une seule passe sur le tableau d'entrée, et compter combien de boules de chaque couleurs sont présentes, puis réécrire le tableau de sortie en écrivant le bon nombre de boules bleues, puis blanches, puis rouges.

# In[106]:


def tri_comptage(boules: Boules) -> Boules:
    n = len(boules)
    comptages = {BLEU: 0, BLANC: 0, ROUGE: 0}
    for boule in boules:
        comptages[boule] += 1
    # exactement un seul parcours du tableau
    b = [None] * n
    nb_bleu, nb_blanc, nb_rouge = comptages[BLEU], comptages[BLANC], comptages[ROUGE]
    print(f"En une seule passe du tableau, on a compté {nb_bleu} boule(s) bleue(s), {nb_blanc} boule(s) blanche(s), {nb_rouge} boule(s) rouge(s).")
    boule_actuelle = BLEU
    if nb_bleu == 0:
        boule_actuelle = BLANC
        if nb_blanc == 0:
            boule_actuelle = ROUGE
    # et exactement un seul parcours du tableau de destination
    for i in range(0, n):
        b[i] = boule_actuelle
        print_boules(b[:i + 1])
        if i + 1 >= nb_bleu + nb_blanc:
            boule_actuelle = ROUGE
        elif i + 1 >= nb_bleu:
            boule_actuelle = BLANC
    # note en Python on aurait pu faire
    b2 = ([BLEU] * nb_bleu) + ([BLANC] * nb_blanc) + ([ROUGE] * nb_rouge)
    assert b == b2
    return b


# In[107]:


print_boules(boules1)
tri_comptage(boules1)


# In[76]:


print_boules(boules2)
tri_comptage(boules2)


# In[77]:


print_boules(boules3)
tri_comptage(boules3)


# Autres exemples :

# In[97]:


print_boules(boules4)
tri_comptage(boules4)


# In[98]:


print_boules(boules5)
tri_comptage(boules5)


# In[104]:


print_boules(boules6)
tri_comptage(boules6)


# Encore des exemples :

# In[105]:


print_boules(boules7)
tri_comptage(boules7)


# In[108]:


print_boules(boules8)
tri_comptage(boules8)


# In[109]:


print_boules(boules9)
tri_comptage(boules9)


# ## Explications
# 
# Voilà.
