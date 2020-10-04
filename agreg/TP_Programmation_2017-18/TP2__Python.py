#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#TP-2---Programmation-pour-la-préparation-à-l'agrégation-maths-option-info" data-toc-modified-id="TP-2---Programmation-pour-la-préparation-à-l'agrégation-maths-option-info-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>TP 2 - Programmation pour la préparation à l'agrégation maths option info</a></span></li><li><span><a href="#Listes" data-toc-modified-id="Listes-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Listes</a></span><ul class="toc-item"><li><span><a href="#Exercice-1-:-taille" data-toc-modified-id="Exercice-1-:-taille-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Exercice 1 : <code>taille</code></a></span></li><li><span><a href="#Exercice-2-:-concat" data-toc-modified-id="Exercice-2-:-concat-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Exercice 2 : <code>concat</code></a></span></li><li><span><a href="#Exercice-3-:-appartient" data-toc-modified-id="Exercice-3-:-appartient-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Exercice 3 : <code>appartient</code></a></span></li><li><span><a href="#Exercice-4-:-miroir" data-toc-modified-id="Exercice-4-:-miroir-2.4"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>Exercice 4 : <code>miroir</code></a></span></li><li><span><a href="#Exercice-5-:-alterne" data-toc-modified-id="Exercice-5-:-alterne-2.5"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>Exercice 5 : <code>alterne</code></a></span></li><li><span><a href="#Exercice-6-:-nb_occurrences" data-toc-modified-id="Exercice-6-:-nb_occurrences-2.6"><span class="toc-item-num">2.6&nbsp;&nbsp;</span>Exercice 6 : <code>nb_occurrences</code></a></span></li><li><span><a href="#Exercice-7-:-pairs" data-toc-modified-id="Exercice-7-:-pairs-2.7"><span class="toc-item-num">2.7&nbsp;&nbsp;</span>Exercice 7 : <code>pairs</code></a></span></li><li><span><a href="#Exercice-8-:-range" data-toc-modified-id="Exercice-8-:-range-2.8"><span class="toc-item-num">2.8&nbsp;&nbsp;</span>Exercice 8 : <code>range</code></a></span></li><li><span><a href="#Exercice-9-:-premiers" data-toc-modified-id="Exercice-9-:-premiers-2.9"><span class="toc-item-num">2.9&nbsp;&nbsp;</span>Exercice 9 : <code>premiers</code></a></span></li></ul></li><li><span><a href="#Listes-simplement-chaînée-(manuellement-définies)" data-toc-modified-id="Listes-simplement-chaînée-(manuellement-définies)-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Listes simplement chaînée (manuellement définies)</a></span><ul class="toc-item"><li><span><a href="#La-classe-ListeChainee" data-toc-modified-id="La-classe-ListeChainee-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>La classe <code>ListeChainee</code></a></span></li><li><span><a href="#Exercice-1-:-taille" data-toc-modified-id="Exercice-1-:-taille-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Exercice 1 : <code>taille</code></a></span></li><li><span><a href="#Exercice-2-:-concat" data-toc-modified-id="Exercice-2-:-concat-3.3"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>Exercice 2 : <code>concat</code></a></span></li><li><span><a href="#Exercice-3-:-appartient" data-toc-modified-id="Exercice-3-:-appartient-3.4"><span class="toc-item-num">3.4&nbsp;&nbsp;</span>Exercice 3 : <code>appartient</code></a></span></li><li><span><a href="#Exercice-4-:-miroir" data-toc-modified-id="Exercice-4-:-miroir-3.5"><span class="toc-item-num">3.5&nbsp;&nbsp;</span>Exercice 4 : <code>miroir</code></a></span></li><li><span><a href="#Exercice-5-:-alterne" data-toc-modified-id="Exercice-5-:-alterne-3.6"><span class="toc-item-num">3.6&nbsp;&nbsp;</span>Exercice 5 : <code>alterne</code></a></span></li><li><span><a href="#Exercice-6-:-nb_occurrences" data-toc-modified-id="Exercice-6-:-nb_occurrences-3.7"><span class="toc-item-num">3.7&nbsp;&nbsp;</span>Exercice 6 : <code>nb_occurrences</code></a></span></li><li><span><a href="#Exercice-7-:-pairs" data-toc-modified-id="Exercice-7-:-pairs-3.8"><span class="toc-item-num">3.8&nbsp;&nbsp;</span>Exercice 7 : <code>pairs</code></a></span></li><li><span><a href="#Exercice-8-:-range" data-toc-modified-id="Exercice-8-:-range-3.9"><span class="toc-item-num">3.9&nbsp;&nbsp;</span>Exercice 8 : <code>range</code></a></span></li><li><span><a href="#Exercice-9-:-premiers" data-toc-modified-id="Exercice-9-:-premiers-3.10"><span class="toc-item-num">3.10&nbsp;&nbsp;</span>Exercice 9 : <code>premiers</code></a></span></li></ul></li><li><span><a href="#Quelques-tris-par-comparaison" data-toc-modified-id="Quelques-tris-par-comparaison-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Quelques tris par comparaison</a></span><ul class="toc-item"><li><span><a href="#Exercice-10-:-Tri-insertion" data-toc-modified-id="Exercice-10-:-Tri-insertion-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Exercice 10 : Tri insertion</a></span></li><li><span><a href="#Exercice-11-:-Tri-insertion-générique" data-toc-modified-id="Exercice-11-:-Tri-insertion-générique-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>Exercice 11 : Tri insertion générique</a></span></li><li><span><a href="#Exercice-12-:-Tri-selection" data-toc-modified-id="Exercice-12-:-Tri-selection-4.3"><span class="toc-item-num">4.3&nbsp;&nbsp;</span>Exercice 12 : Tri selection</a></span></li><li><span><a href="#Exercices-13,-14,-15-:-Tri-fusion" data-toc-modified-id="Exercices-13,-14,-15-:-Tri-fusion-4.4"><span class="toc-item-num">4.4&nbsp;&nbsp;</span>Exercices 13, 14, 15 : Tri fusion</a></span></li><li><span><a href="#Comparaisons" data-toc-modified-id="Comparaisons-4.5"><span class="toc-item-num">4.5&nbsp;&nbsp;</span>Comparaisons</a></span></li></ul></li><li><span><a href="#Listes-:-l'ordre-supérieur" data-toc-modified-id="Listes-:-l'ordre-supérieur-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Listes : l'ordre supérieur</a></span><ul class="toc-item"><li><span><a href="#Exercice-16-:-applique" data-toc-modified-id="Exercice-16-:-applique-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>Exercice 16 : <code>applique</code></a></span></li><li><span><a href="#Exercice-17" data-toc-modified-id="Exercice-17-5.2"><span class="toc-item-num">5.2&nbsp;&nbsp;</span>Exercice 17</a></span></li><li><span><a href="#Exercice-18-:-itere" data-toc-modified-id="Exercice-18-:-itere-5.3"><span class="toc-item-num">5.3&nbsp;&nbsp;</span>Exercice 18 : <code>itere</code></a></span></li><li><span><a href="#Exercice-19" data-toc-modified-id="Exercice-19-5.4"><span class="toc-item-num">5.4&nbsp;&nbsp;</span>Exercice 19</a></span></li><li><span><a href="#Exercice-20-:-qqsoit-et-ilexiste" data-toc-modified-id="Exercice-20-:-qqsoit-et-ilexiste-5.5"><span class="toc-item-num">5.5&nbsp;&nbsp;</span>Exercice 20 : <code>qqsoit</code> et <code>ilexiste</code></a></span></li><li><span><a href="#Exercice-21-:-appartient-version-2" data-toc-modified-id="Exercice-21-:-appartient-version-2-5.6"><span class="toc-item-num">5.6&nbsp;&nbsp;</span>Exercice 21 : <code>appartient</code> version 2</a></span></li><li><span><a href="#Exercice-22-:-filtre" data-toc-modified-id="Exercice-22-:-filtre-5.7"><span class="toc-item-num">5.7&nbsp;&nbsp;</span>Exercice 22 : <code>filtre</code></a></span></li><li><span><a href="#Exercice-23" data-toc-modified-id="Exercice-23-5.8"><span class="toc-item-num">5.8&nbsp;&nbsp;</span>Exercice 23</a></span></li><li><span><a href="#Exercice-24-:-reduit" data-toc-modified-id="Exercice-24-:-reduit-5.9"><span class="toc-item-num">5.9&nbsp;&nbsp;</span>Exercice 24 : <code>reduit</code></a></span></li><li><span><a href="#Exercice-25-:-somme,-produit" data-toc-modified-id="Exercice-25-:-somme,-produit-5.10"><span class="toc-item-num">5.10&nbsp;&nbsp;</span>Exercice 25 : <code>somme</code>, <code>produit</code></a></span></li><li><span><a href="#Exercice-26-:-miroir-version-2" data-toc-modified-id="Exercice-26-:-miroir-version-2-5.11"><span class="toc-item-num">5.11&nbsp;&nbsp;</span>Exercice 26 : <code>miroir</code> version 2</a></span></li></ul></li><li><span><a href="#Arbres" data-toc-modified-id="Arbres-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Arbres</a></span><ul class="toc-item"><li><span><a href="#Exercice-27" data-toc-modified-id="Exercice-27-6.1"><span class="toc-item-num">6.1&nbsp;&nbsp;</span>Exercice 27</a></span></li><li><span><a href="#Exercice-28" data-toc-modified-id="Exercice-28-6.2"><span class="toc-item-num">6.2&nbsp;&nbsp;</span>Exercice 28</a></span></li><li><span><a href="#Exercice-29" data-toc-modified-id="Exercice-29-6.3"><span class="toc-item-num">6.3&nbsp;&nbsp;</span>Exercice 29</a></span></li><li><span><a href="#Exercice-30" data-toc-modified-id="Exercice-30-6.4"><span class="toc-item-num">6.4&nbsp;&nbsp;</span>Exercice 30</a></span></li></ul></li><li><span><a href="#Parcours-d'arbres-binaires" data-toc-modified-id="Parcours-d'arbres-binaires-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Parcours d'arbres binaires</a></span><ul class="toc-item"><li><span><a href="#Exercice-31" data-toc-modified-id="Exercice-31-7.1"><span class="toc-item-num">7.1&nbsp;&nbsp;</span>Exercice 31</a></span></li><li><span><a href="#Exercice-32-:-Parcours-naifs-(complexité-quadratique)" data-toc-modified-id="Exercice-32-:-Parcours-naifs-(complexité-quadratique)-7.2"><span class="toc-item-num">7.2&nbsp;&nbsp;</span>Exercice 32 : Parcours naifs (complexité quadratique)</a></span></li><li><span><a href="#Exercice-33-:-Parcours-linéaires" data-toc-modified-id="Exercice-33-:-Parcours-linéaires-7.3"><span class="toc-item-num">7.3&nbsp;&nbsp;</span>Exercice 33 : Parcours linéaires</a></span></li><li><span><a href="#Exercice-34-:-parcours-en-largeur-et-en-profondeur" data-toc-modified-id="Exercice-34-:-parcours-en-largeur-et-en-profondeur-7.4"><span class="toc-item-num">7.4&nbsp;&nbsp;</span>Exercice 34 : parcours en largeur et en profondeur</a></span></li><li><span><a href="#Exercice-35-et-fin" data-toc-modified-id="Exercice-35-et-fin-7.5"><span class="toc-item-num">7.5&nbsp;&nbsp;</span>Exercice 35 et fin</a></span><ul class="toc-item"><li><span><a href="#Reconstruction-depuis-le-parcours-prefixe" data-toc-modified-id="Reconstruction-depuis-le-parcours-prefixe-7.5.1"><span class="toc-item-num">7.5.1&nbsp;&nbsp;</span>Reconstruction depuis le parcours prefixe</a></span></li><li><span><a href="#Reconstruction-depuis-le-parcours-en-largeur" data-toc-modified-id="Reconstruction-depuis-le-parcours-en-largeur-7.5.2"><span class="toc-item-num">7.5.2&nbsp;&nbsp;</span>Reconstruction depuis le parcours en largeur</a></span></li></ul></li></ul></li><li><span><a href="#Conclusion" data-toc-modified-id="Conclusion-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>Conclusion</a></span></li></ul></div>

# # TP 2 - Programmation pour la préparation à l'agrégation maths option info
# - En Python, version 3.

# In[4]:


from sys import version
print(version)


# ----
# # Listes
# Ces exercices sont un peu foireux : les "*listes*" en Python **ne sont pas des listes simplement chaînées** !

# ## Exercice 1 : `taille`

# In[12]:


from typing import TypeVar, List
_a = TypeVar('alpha')

def taille(liste : List[_a]) -> int:
    longueur = 0
    for _ in liste:
        longueur += 1
    return longueur

taille([])
taille([1, 2, 3])


# In[7]:


len([])
len([1, 2, 3])


# ## Exercice 2 : `concat`

# In[16]:


from typing import TypeVar, List
_a = TypeVar('alpha')

def concatene(liste1 : List[_a], liste2 : List[_a]) -> List[_a]:
    # return liste1 + liste2  # easy solution
    liste = []
    for i in liste1:
        liste.append(i)
    for i in liste2:
        liste.append(i)
    return liste


# In[19]:


concatene([1, 2], [3, 4])
[1, 2] + [3, 4]


# Mais attention le typage est toujours optionnel en Python :

# In[20]:


concatene([1, 2], ["pas", "entier", "?"])


# ## Exercice 3 : `appartient`

# In[21]:


from typing import TypeVar, List
_a = TypeVar('alpha')

def appartient(x : _a, liste : List[_a]) -> bool:
    for y in liste:
        if x == y:
            return True  # on stoppe avant la fin
    return False

appartient(1, [])
appartient(1, [1])
appartient(1, [1, 2, 3])
appartient(4, [1, 2, 3])


# In[22]:


1 in []
1 in [1]
1 in [1, 2, 3]
4 in [1, 2, 3]


# Notre implémentation est évidemment plus lente que le test `x in liste` de la librarie standard...
# Mais pas tant :

# In[23]:


get_ipython().run_line_magic('timeit', 'appartient(1000, list(range(10000)))')
get_ipython().run_line_magic('timeit', '1000 in list(range(10000))')


# ## Exercice 4 : `miroir`

# In[26]:


from typing import TypeVar, List
_a = TypeVar('alpha')

def miroir(liste : List[_a]) -> List[_a]:
    # return liste[::-1]  # version facile
    liste2 = []
    for x in liste:
        liste2.insert(0, x)
    return liste2


# In[28]:


miroir([2, 3, 5, 7, 11])
[2, 3, 5, 7, 11][::-1]


# In[29]:


get_ipython().run_line_magic('timeit', 'miroir([2, 3, 5, 7, 11])')
get_ipython().run_line_magic('timeit', '[2, 3, 5, 7, 11][::-1]')


# ## Exercice 5 : `alterne`

# La sémantique n'était pas très claire, mais on peut imaginer quelque chose comme ça :

# In[30]:


from typing import TypeVar, List
_a = TypeVar('alpha')

def alterne(liste1 : List[_a], liste2 : List[_a]) -> List[_a]:
    liste3 = []
    i, j = 0, 0
    n, m = len(liste1), len(liste2)
    while i < n and j < m:  # encore deux
        liste3.append(liste1[i])
        i += 1
        liste3.append(liste2[j])
        j += 1
    while i < n:  # si n > m
        liste3.append(liste1[i])
        i += 1
    while j < m:  # ou si n < m
        liste3.append(liste2[j])
        j += 1
    return liste3


# In[31]:


alterne([3, 5], [2, 4, 6])
alterne([1, 3, 5], [2, 4, 6])
alterne([1, 3, 5], [4, 6])


# La complexité est linéaire en $\mathcal{O}(\max(|\text{liste 1}|, |\text{liste 2}|)$.

# ## Exercice 6 : `nb_occurrences`

# In[32]:


from typing import TypeVar, List
_a = TypeVar('alpha')

def nb_occurrences(x : _a, liste : List[_a]) -> int:
    nb = 0
    for y in liste:
        if x == y:
            nb += 1
    return nb

nb_occurrences(0, [1, 2, 3, 4])
nb_occurrences(2, [1, 2, 3, 4])
nb_occurrences(2, [1, 2, 2, 3, 2, 4])
nb_occurrences(5, [1, 2, 3, 4])


# ## Exercice 7 : `pairs`
# 
# C'est un filtrage :

# In[33]:


get_ipython().run_line_magic('pinfo', 'filter')


# In[36]:


from typing import List

def pairs(liste : List[int]) -> List[int]:
    # return list(filter(lambda x : x % 2 == 0, liste))
    return [x for x in liste if x % 2 == 0]


# In[37]:


pairs([1, 2, 3, 4, 5, 6])
pairs([1, 2, 3, 4, 5, 6, 7, 100000])
pairs([1, 2, 3, 4, 5, 6, 7, 100000000000])
pairs([1, 2, 3, 4, 5, 6, 7, 1000000000000000000])


# ## Exercice 8 : `range`

# In[84]:


from typing import List

def myrange(n : int) -> List[int]:
    liste = []
    i = 1
    while i <= n:
        liste.append(i)
        i += 1
    return liste


# In[85]:


myrange(4)


# In[47]:


from typing import List

def intervale(a : int, b : int=None) -> List[int]:
    if b == None:
        a, b = 1, a
    liste = []
    i = a
    while i <= b:
        liste.append(i)
        i += 1
    return liste


# In[48]:


intervale(10)
intervale(1, 4)


# ## Exercice 9 : `premiers`
# Plusieurs possibilités. Un filtre d'Erathosthène marche bien, ou une filtration.
# Je ne vais pas utiliser de tableaux donc on est un peu réduit d'utiliser une filtration (filtrage ? *pattern matching*)

# In[77]:


def racine(n : int) -> int:
    i = 1
    for i in range(n + 1):
        if i*i > n:
            return i - 1
    return i

racine(1)
racine(5)
racine(102)
racine(120031)


# In[78]:


from typing import List

def intervale2(a : int, b : int, pas : int=1) -> List[int]:
    assert pas > 0
    liste = []
    i = a
    while i <= b:
        liste.append(i)
        i += pas
    return liste


# In[79]:


intervale2(2, 12, 1)
intervale2(2, 12, 3)


# Une version purement fonctionnelle est moins facile qu'une version impérative avec une référence booléenne.

# In[80]:


def estDivisible(n : int, k : int) -> bool:
    return (n % k) == 0


# In[81]:


estDivisible(10, 2)
estDivisible(10, 3)
estDivisible(10, 4)
estDivisible(10, 5)


# In[107]:


def estPremier(n : int) -> bool:
    return (n == 2) or (n == 3) or not any(map(lambda k: estDivisible(n, k), intervale2(2, racine(n), 1)))


# In[108]:


for n in range(2, 20):
    print(n, list(map(lambda k: estDivisible(n, k), intervale2(2, racine(n), 1))))


# In[109]:


from typing import List

def premiers(n : int) -> List[int]:
    return [p for p in intervale2(2, n, 1) if estPremier(p)]


# In[110]:


premiers(10)


# In[111]:


premiers(100)


# ----
# # Listes simplement chaînée (manuellement définies)
# 
# Comme ces exercices étaient un peu foireux à écrire avec les "*listes*" de Python, qui **ne sont pas des listes simplement chaînées**, je propose une autre solution où l'on va définir une petite classe qui représentera une liste simplement chaînée, et on va écrire les fonctions demandées avec cette classe.

# ## La classe `ListeChainee`
# 
# On va supposer que les listes que l'on représentera ne contiendront pas la valeur `None`, qui est utilisée pour représenter l'absence de tête et/ou de queue de la liste.

# In[173]:


class ListeChainee():
    def __init__(self, hd=None, tl=None):
        self.hd = hd
        self.tl = tl
    
    def __repr__(self) -> str:
        if self.tl is None:
            if self.hd is None:
                return "[]"
            else:
                return f"{self.hd} :: []"
        else:
            return f"{self.hd} :: {self.tl}"
    
    def jolie(self) -> str:
        if self.tl is None:
            if self.hd is None:
                return "[]"
            else:
                return f"[{self.hd}]"
        else:
            j = self.tl.jolie()
            j = j.replace("[", "").replace("]", "")
            if j == "":
                return f"[{self.hd}]"
            else:
                return f"[{self.hd}, {j}]"


# In[174]:


# équivalent à :: en OCaml
def insert(hd, tl: ListeChainee) -> ListeChainee:
    """ Insère hd en début de la liste chainée tl."""
    return ListeChainee(hd=hd, tl=tl)


# In[175]:


# liste vide, puis des listes plus grandes
vide = ListeChainee()   # []
l_1   = insert(1, vide)  # 1 :: [] ~= [1]
l_12  = insert(2, l_1)   # 2 :: 1 :: [] ~= [2, 1]
l_123 = insert(3, l_12)  # 3 :: 2 :: 1 :: []


# In[176]:


print(vide)     # []
print(l_1)      # 1 :: []
print(l_12)     # 2 :: 1 :: []
print(l_123)    # 3 :: 2 :: 1 :: []


# In[177]:


print(vide.jolie())     # []
print(l_1.jolie())      # [1]
print(l_12.jolie())     # [2, 1]
print(l_123.jolie())    # [3, 2, 1]


# ## Exercice 1 : `taille`
# 
# Par exemple la longueur sera bien en O(n) si n=taille(liste) avec cette approche récursive :

# In[149]:


from typing import Optional


# In[150]:


def taille(liste: Optional[ListeChainee]) -> int:
    if liste is None:
        return 0
    elif liste.tl is None:
        return 0 if liste.hd is None else 1
    return 1 + taille(liste.tl)


# In[151]:


print(taille(vide))   # 0
print(taille(l_1))    # 1
print(taille(l_12))   # 2
print(taille(l_123))  # 3


# ## Exercice 2 : `concat`
# 
# Je vais déjà commencer par écrire une fonction `copy` qui permet de copier récursivement une liste simplement chaînée, pour être sûr que l'on ne modifie pas en place une des listes données en argument.

# In[152]:


def copy(liste: ListeChainee) -> ListeChainee:
    if liste.tl is None:
        return ListeChainee(hd=liste.hd, tl=None)
    else:
        return ListeChainee(hd=liste.hd, tl=copy(liste.tl))


# On peut vérifier que cela marche en regardant, par exemple, l'`id` de deux objets si le deuxième est une copie du premier : les `id` seront bien différents.

# In[153]:


print(id(vide))
print(id(copy(vide)))


# Et donc pour concaténer deux chaînes, c'est facile :

# In[154]:


def concat(liste1: ListeChainee, liste2: ListeChainee) -> ListeChainee:
    if taille(liste1) == 0:
        return liste2
    elif taille(liste2) == 0:
        return liste1
    # nouvelle liste : comme ça changer queue.tl ne modifie PAS liste1
    resultat = copy(liste1)
    queue = resultat
    while taille(queue.tl) > 0:
        queue = queue.tl
    assert taille(queue.tl) == 0
    queue.tl = ListeChainee(hd=liste2.hd, tl=liste2.tl)
    return resultat


# In[156]:


print(concat(vide, l_1))
print(vide)  # pas modifiée : []
print(l_1)   # pas modifiée : 1 :: []


# In[135]:


concat(l_1, l_12)  # 1 :: 2 :: 1 :: []


# In[136]:


concat(l_1, l_123)  # 1 :: 3 :: 2 :: 1 :: []


# In[137]:


concat(l_1, vide)   # 1 :: []


# In[138]:


concat(l_12, vide)   # 2 :: 1 :: []


# In[139]:


concat(l_12, l_1)   # 2 :: 1 :: 1 :: []


# In[140]:


concat(l_123, l_123)   # 3 :: 2 :: 1 :: 3 :: 2 :: 1 :: []


# ## Exercice 3 : `appartient`
# 
# C'est en complexité linéaire dans le pire des cas.

# In[141]:


def appartient(x, liste: ListeChainee) -> bool:
    if liste.hd is None:
        return False
    else:
        if liste.hd == x:
            return True
        else:
            return appartient(x, liste.tl)


# In[144]:


assert appartient(0, vide)  == False
assert appartient(0, l_1)   == False
assert appartient(0, l_12)  == False
assert appartient(0, l_123) == False
assert appartient(1, l_1)   == True
assert appartient(1, l_12)  == True
assert appartient(1, l_123) == True
assert appartient(2, l_1)   == False
assert appartient(2, l_12)  == True
assert appartient(2, l_123) == True
assert appartient(3, l_1)   == False
assert appartient(3, l_12)  == False
assert appartient(3, l_123) == True


# ## Exercice 4 : `miroir`
# 
# Ce sera en temps quadratique, à cause de toutes les recopies :

# In[178]:


def miroir(liste: ListeChainee) -> ListeChainee:
    if taille(liste) <= 1:
        return copy(liste)
    else:
        hd, tl = liste.hd, copy(liste.tl)  # O(n)
        juste_hd = ListeChainee(hd=hd, tl=None)  # O(1)
        return concat(miroir(tl), juste_hd)  # O(n^2) + O(n) à cause de concat


# In[255]:


print(miroir(vide))   # [] => []
print(miroir(l_1))    # [1] => [1]
print(miroir(l_12))   # [2, 1] => [1, 2]
print(miroir(l_123))  # [3, 2, 1] => [1, 2, 3]


# ## Exercice 5 : `alterne`

# La sémantique n'était pas très claire, mais on peut imaginer quelque chose comme ça :
# 
# - si une des deux listes est vide, on prend l'autre,
# - si les deux ne sont pas vide, on prend le début de l1, de l2, puis alterne(queue l1, queue l2)

# In[256]:


def alterne(liste1: ListeChainee, liste2: ListeChainee) -> ListeChainee:
    if taille(liste1) == 0:
        return copy(liste2)  # on recopie pour ne rien modifier
    if taille(liste2) == 0:
        return copy(liste1)  # on recopie pour ne rien modifier
    h1, t1 = liste1.hd, liste1.tl  
    h2, t2 = liste2.hd, liste2.tl
    return insert(h1, insert(h2, alterne(t1, t2)))


# In[257]:


print(alterne(l_1, l_12))     # [1, 2, 1]
print(alterne(l_12, l_1))     # [2, 1, 1]
print(alterne(l_123, l_1))    # [3, 1, 2, 1]
print(alterne(l_123, l_12))   # [3, 2, 2, 1, 1]
print(alterne(l_123, l_123))  # [3, 3, 2, 2, 1, 1]
print(alterne(l_12, l_123))   # [2, 3, 1, 2, 1]
print(alterne(l_1, l_123))    # [1, 3, 2, 1]


# La complexité est quadratique en $\mathcal{O}((\max(|\text{liste 1}|, |\text{liste 2}|)^2)$ à cause des recopies.

# ## Exercice 6 : `nb_occurrences`
# 
# Ce sera en temps linéaire, dans tous les cas.
# 

# In[264]:


def nb_occurrences(x, liste: ListeChainee) -> int:
    if liste is None or liste.hd is None:
        return 0
    else:
        count = 1 if x == liste.hd else 0
    if liste.tl is None:
        return count
    else:
        return count + nb_occurrences(x, liste.tl)


# In[265]:


assert nb_occurrences(1, vide) == 0
assert nb_occurrences(1, l_1) == 1
assert nb_occurrences(1, l_12) == 1
assert nb_occurrences(2, l_12) == 1
assert nb_occurrences(1, l_123) == 1
assert nb_occurrences(2, l_123) == 1
assert nb_occurrences(3, l_123) == 1
assert nb_occurrences(1, concat(l_1, l_1)) == 2
assert nb_occurrences(2, concat(l_1, l_12)) == 1
assert nb_occurrences(3, concat(l_12, l_1)) == 0
assert nb_occurrences(1, concat(l_12, l_12)) == 2
assert nb_occurrences(2, concat(l_12, l_12)) == 2
assert nb_occurrences(1, concat(l_123, concat(l_1, l_1))) == 3
assert nb_occurrences(2, concat(l_123, concat(l_1, l_12))) == 2
assert nb_occurrences(3, concat(l_123, concat(l_12, l_1))) == 1
assert nb_occurrences(3, concat(l_123, concat(l_12, l_12))) == 1


# On peut facilement écrire une variante qui sera récursive terminale ("tail recursive") :

# In[266]:


def nb_occurrences(x, liste: ListeChainee, count=0) -> int:
    if liste is None or liste.hd is None:
        return count
    else:
        count += 1 if x == liste.hd else 0
        if liste.tl is None:
            return count
        else:
            return nb_occurrences(x, liste.tl, count=count)


# ## Exercice 7 : `pairs`
# 
# C'est un filtrage par le prédicat `x % 2 == 0`.
# Autant écrire la fonction de filtrage générique :

# In[268]:


def filtrer(liste: ListeChainee, predicate) -> ListeChainee:
    if liste is None or liste.hd is None:  # liste de taille 0
        return ListeChainee(hd=None, tl=None)
    elif liste.tl is None:  # liste de taille 1
        if predicate(liste.hd):  # on renvoie [hd]
            return ListeChainee(hd=liste.hd, tl=None)
        else:  # on renvoie []
            return ListeChainee(hd=None, tl=None)
    else:  # liste de taille >= 2
        if predicate(liste.hd):
            return insert(liste.hd, filtrer(liste.tl, predicate))
        else:
            return filtrer(liste.tl, predicate)


# Et donc c'est rapide :

# In[269]:


def pairs(liste: ListeChainee) -> ListeChainee:
    def predicate(x):
        return (x % 2) == 0
    # aussi : predicate = lambda x: (x % 2) == 0
    return filtrer(liste, predicate)


# In[270]:


def impairs(liste: ListeChainee) -> ListeChainee:
    def predicate(x):
        return (x % 2) == 1
    return filtrer(liste, predicate)


# In[206]:


print(pairs(vide))   # []
print(pairs(l_1))    # []
print(pairs(l_12))   # [2]
print(pairs(l_123))  # [2]
print(pairs(insert(4, insert(6, insert(8, l_123)))))  # [4, 6, 8, 2]
print(pairs(insert(5, insert(6, insert(8, l_123)))))  # [6, 8, 2]


# In[272]:


print(impairs(vide))   # []
print(impairs(l_1))    # [1]
print(impairs(l_12))   # [1]
print(impairs(l_123))  # [3, 1]
print(impairs(insert(4, insert(6, insert(8, l_123)))))  # [3, 1]
print(impairs(insert(5, insert(6, insert(8, l_123)))))  # [5, 3, 1]


# ## Exercice 8 : `range`
# 
# Ce sera de complexité temporelle linéaire :

# In[288]:


def myrange(n: int) -> ListeChainee:
    if n <= 0:
        return ListeChainee(hd=None, tl=None)
    elif n == 1:
        return ListeChainee(hd=1, tl=None)
        # return insert(1, vide)
    else:
        return ListeChainee(hd=n, tl=myrange(n-1))


# In[289]:


print(myrange(1))  # [1]
print(myrange(2))  # [1, 2]
print(myrange(3))  # [1, 2, 3]
print(myrange(4))  # [1, 2, 3, 4]


# Si on veut les avoir dans l'ordre croissant, il faudrait utiliser `miroir` qui est quadratique.
# Autant écrire directement une fonction `intervale(a, b)` qui renvoie la liste simplement chaînée contenant `a :: (a+1) :: ... :: b` :

# In[216]:


def intervale(a: int, b: Optional[int]=None) -> ListeChainee:
    if b is None:
        a, b = 1, a
    n = b - a
    if n < 0:     # [a..b] = []
        return ListeChainee(hd=None, tl=None)
    elif n == 0:  # [a..b] = [a]
        return ListeChainee(hd=a, tl=None)
    else:         # [a..b] = a :: [a+1..b]
        return ListeChainee(hd=a, tl=intervale(a+1, b))


# In[217]:


print(intervale(10))      # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(intervale(1, 4))    # [1, 2, 3, 4]
print(intervale(13, 13))  # [13]
print(intervale(13, 10))  # []


# Une autre approche est d'écrire la fonction `mymap` et de dire que
# ```python
# intervale_bis(a, b) = miroir(mymap(lambda x: x + (a - 1), myrange(b - a + 1)))
# ```

# In[277]:


from typing import Callable

def mymap(fonction: Callable, liste: ListeChainee) -> ListeChainee:
    if liste is None or liste.hd is None:  # liste de taille 0
        return ListeChainee(hd=None, tl=None)
    elif liste.tl is None:  # liste de taille 1
        return ListeChainee(hd=fonction(liste.hd), tl=None)
    else:  # liste de taille >= 2
        return ListeChainee(hd=fonction(liste.hd), tl=mymap(fonction, liste.tl))


# In[281]:


print(myrange(10))
print(mymap(lambda x: x, myrange(10)))


# In[290]:


def intervale_bis(a: int, b: int) -> ListeChainee:
    return miroir(mymap(lambda x: x + (a - 1), myrange(b - a + 1)))


# In[291]:


print(intervale_bis(1, 10))   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(intervale_bis(1, 4))    # [1, 2, 3, 4]
print(intervale_bis(13, 13))  # [13]
print(intervale_bis(13, 10))  # []


# ## Exercice 9 : `premiers`
# Plusieurs possibilités. Un filtre d'Erathosthène marche bien, ou une filtrage.
# Je ne vais pas utiliser de tableaux donc on est un peu réduit d'utiliser une filtrage.
# 
# On a besoin des fonctions suivantes :
# 
# - calculer la racine entière de $n$, très facile par une boucle,
# - calculer les nombres impairs entre 5 et $\lfloor \sqrt{n} \rfloor$,
# - filtrer cette liste de nombres impairs pour garder ceux qui divisent $n$,
# - et dire que $n$ est premier s'il a un diviseur non trivial.

# In[293]:


def racine(n: int) -> int:
    i = 1
    for i in range(n + 1):
        if i*i > n:
            return i - 1
    return i

print(racine(1))  # 1
print(racine(5))  # 2
print(racine(102))  # 10
print(racine(120031))  # 346


# In[294]:


def intervale2(a: int, b: Optional[int]=None, pas: int=1) -> ListeChainee:
    if b is None:
        a, b = 1, a
    n = b - a
    if n < 0:     # [a..b::p] = []
        return ListeChainee(hd=None, tl=None)
    elif n == 0:  # [a..b::p] = [a]
        return ListeChainee(hd=a, tl=None)
    else:         # [a..b::p] = a :: [a+p..b::p]
        return ListeChainee(hd=a, tl=intervale2(a + pas, b=b, pas=pas))


# In[295]:


print(intervale2(1, 10, 2))      # [1, 3, 5, 7, 9]
print(intervale2(1, 4, 2))    # [1, 3]
print(intervale2(13, 13, 2))  # [13]
print(intervale2(13, 10, 2))  # []


# Une version purement fonctionnelle est moins facile qu'une version impérative avec une référence booléenne.

# In[296]:


def estDivisible(n: int, k: int) -> bool:
    return (n % k) == 0


# In[236]:


estDivisible(10, 2)
estDivisible(10, 3)
estDivisible(10, 4)
estDivisible(10, 5)


# On est prêt à écrire `estPremier` :

# In[247]:


def estPremier(n : int) -> bool:
    return taille(filtrer(intervale2(2, racine(n), 1), lambda k: estDivisible(n, k))) == 0


# En effet il suffit de construire d'abord la liste des entiers impairs de 2 à $\lfloor \sqrt{n} \rfloor$, de les filtrer par ceux qui divisent $n$, et de vérifier si on a aucun diviseur (`taille(..) == 0`) auquel cas $n$ est premier, ou si $n$ a au moins un diviseur auquel cas $n$ n'est pas premier.

# In[254]:


for n in range(2, 20):
    print("Petits diviseurs de", n, " -> ", filtrer(intervale2(2, racine(n), 1), lambda k: estDivisible(n, k)))


# On voit dans l'exemple ci dessus les nombres premiers comme ceux n'ayant aucun diviseurs, et les nombres non premiers comme ceux ayant au moins un diviseur.

# In[249]:


def premiers(n : int) -> ListeChainee:
    return filtrer(intervale2(2, n, 1), estPremier)


# In[250]:


premiers(10)  # [2, 3, 5, 7]


# In[251]:


premiers(100)  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


# ----
# # Quelques tris par comparaison

# On fera les tris en ordre croissant.

# In[112]:


test = [3, 1, 8, 4, 5, 6, 1, 2]


# ## Exercice 10 : Tri insertion

# In[113]:


from typing import TypeVar, List
_a = TypeVar('alpha')

def insere(x : _a, liste : List[_a]) -> List[_a]:
    if len(liste) == 0:
        return [x]
    else:
        t, q = liste[0], liste[1:]
        if x <= t:
            return [x] + liste
        else:
            return [t] + insere(x, q)


# In[114]:


def tri_insertion(liste : List[_a]) -> List[_a]:
    if len(liste) == 0:
        return []
    else:
        t, q = liste[0], liste[1:]
        return insere(t, tri_insertion(q))


# In[115]:


tri_insertion(test)


# Complexité en temps $\mathcal{O}(n^2)$.

# ## Exercice 11 : Tri insertion générique

# In[121]:


from typing import TypeVar, List, Callable
_a = TypeVar('alpha')

def insere2(ordre : Callable[[_a, _a], bool], x : _a, liste : List[_a]) -> List[_a]:
    if len(liste) == 0:
        return [x]
    else:
        t, q = liste[0], liste[1:]
        if ordre(x, t):
            return [x] + liste
        else:
            return [t] + insere2(ordre, x, q)


# In[122]:


def tri_insertion2(ordre : Callable[[_a, _a], bool], liste : List[_a]) -> List[_a]:
    if len(liste) == 0:
        return []
    else:
        t, q = liste[0], liste[1:]
        return insere2(ordre, t, tri_insertion2(ordre, q))


# In[123]:


ordre_croissant = lambda x, y: x <= y


# In[124]:


tri_insertion2(ordre_croissant, test)


# In[125]:


ordre_decroissant = lambda x, y: x >= y


# In[126]:


tri_insertion2(ordre_decroissant, test)


# ## Exercice 12 : Tri selection

# In[127]:


from typing import TypeVar, List, Tuple
_a = TypeVar('alpha')

def selectionne_min(liste : List[_a]) -> Tuple[_a, List[_a]]:
    if len(liste) == 0:
        raise ValueError("Selectionne_min sur liste vide")
    else:
        def cherche_min(mini : _a, autres : List[_a], reste : List[_a]) -> Tuple[_a, List[_a]]:
            if len(reste) == 0:
                return (mini, autres)
            else:
                t, q = reste[0], reste[1:]
                if t < mini:
                    return cherche_min(t, [mini] + autres, q)
                else:
                    return cherche_min(mini, [t] + autres, q)
        t, q = liste[0], liste[1:]
        return cherche_min(t, [], q)


# In[129]:


test
selectionne_min(test)


# (On voit que la liste `autre` a été inversée)

# In[130]:


def tri_selection(liste : List[_a]) -> List[_a]:
    if len(liste) == 0:
        return []
    else:
        mini, autres = selectionne_min(liste)
        return [mini] + tri_selection(autres)


# In[131]:


tri_selection(test)


# Complexité en temps : $\mathcal{O}(n^2)$.

# ## Exercices 13, 14, 15 : Tri fusion

# In[132]:


from typing import TypeVar, List, Tuple
_a = TypeVar('alpha')

def separe(liste : List[_a]) -> Tuple[List[_a], List[_a]]:
    if len(liste) == 0:
        return ([], [])
    elif len(liste) == 1:
        return ([liste[0]], [])
    else:
        x, y, q = liste[0], liste[1], liste[2:]
        a, b = separe(q)
        return ([x] + a, [y] + b)


# In[133]:


test
separe(test)


# In[134]:


def fusion(liste1 : List[_a], liste2 : List[_a]) -> List[_a]:
    if (len(liste1), len(liste2)) == (0, 0):
        return []
    elif len(liste1) == 0:
        return liste2
    elif len(liste2) == 0:
        return liste1
    else:  # les deux sont non vides
        x, a = liste1[0], liste1[1:]
        y, b = liste2[0], liste2[1:]
        if x <= y:
            return [x] + fusion(a, [y] + b)
        else:
            return [y] + fusion([x] + a, b)

        
fusion([1, 3, 7], [2, 3, 8])


# In[136]:


def tri_fusion(liste : List[_a]) -> List[_a]:
    if len(liste) <= 1:
        return liste
    else:
        a, b = separe(liste)
        return fusion(tri_fusion(a), tri_fusion(b))


# In[137]:


tri_fusion(test)


# Complexité en temps $\mathcal{O}(n \log n)$.

# ## Comparaisons

# In[138]:


get_ipython().run_line_magic('timeit', 'tri_insertion(test)')
get_ipython().run_line_magic('timeit', 'tri_selection(test)')
get_ipython().run_line_magic('timeit', 'tri_fusion(test)')


# In[152]:


from sys import setrecursionlimit
setrecursionlimit(100000)
# nécessaire pour tester les différentes fonctions récursives sur de grosses listes


# In[153]:


import random

def test_random(n : int) -> List[int]:
    return [random.randint(-1000, 1000) for _ in range(n)]

for n in [10, 100, 1000]:
    print("\nFor n =", n)
    for tri in [tri_insertion, tri_selection, tri_fusion]:
        print("    and tri = {}".format(tri.__name__))
        get_ipython().run_line_magic('timeit', 'tri(test_random(n))')


# - C'est assez pour vérifier que le tri fusion est **bien plus efficace** que les autres.
# - On voit aussi que les tris par insertion et sélection sont pire que linéaires,
# - Mais que le tri par fusion est presque linéaire (pour $n$ petits, $n \log n$ est presque linéaire).

# ----
# # Listes : l'ordre supérieur
# 
# Je ne corrige pas les questions qui étaient traitées dans le TP1.

# ## Exercice 16 : `applique`

# In[155]:


from typing import TypeVar, List, Callable
_a, _b = TypeVar('_a'), TypeVar('_b')

def applique(f : Callable[[_a], _b], liste : List[_a]) -> List[_b]:
    # Triche :
    return list(map(f, liste))
    # 1ère approche :
    return [f(x) for x in liste]
    # 2ème approche :
    fliste = []
    for x in liste:
        fliste.append(f(x))
    return fliste
    # 3ème approche
    n = len(liste)
    if n == 0: return []
    fliste = [liste[0] for _ in range(n)]
    for i in range(n):
        fliste[i] = f(liste[i])
    return fliste


# ## Exercice 17

# In[156]:


def premiers_carres_parfaits(n : int) -> List[int]:
    return applique(lambda x : x * x, list(range(1, n + 1)))


# In[157]:


premiers_carres_parfaits(12)


# ## Exercice 18 : `itere`

# In[158]:


from typing import TypeVar, List, Callable
_a = TypeVar('_a')

def itere(f : Callable[[_a], None], liste : List[_a]) -> None:
    for x in liste:
        f(x)


# ## Exercice 19

# In[161]:


print_int = lambda i: print("{}".format(i))


# In[163]:


def affiche_liste_entiers(liste : List[int]) -> None:
    print("Debut")
    itere(print_int, liste)
    print("Fin")

affiche_liste_entiers([1, 2, 4, 5, 12011993])


# ## Exercice 20 : `qqsoit` et `ilexiste`

# In[164]:


from typing import TypeVar, List, Callable
_a = TypeVar('_a')

# Comme all(map(f, liste))
def qqsoit(f : Callable[[_a], bool], liste : List[_a]) -> bool:
    for x in liste:
        if not f(x): return False   # arret preliminaire
    return True


# In[176]:


# Comme any(map(f, liste))
def ilexiste(f : Callable[[_a], bool], liste : List[_a]) -> bool:
    for x in liste:
        if f(x): return True   # arret preliminaire
    return False


# In[177]:


qqsoit(lambda x: (x % 2) == 0, [1, 2, 3, 4, 5])
ilexiste(lambda x: (x % 2) == 0, [1, 2, 3, 4, 5])


# In[167]:


get_ipython().run_line_magic('timeit', 'qqsoit(lambda x: (x % 2) == 0, [1, 2, 3, 4, 5])')
get_ipython().run_line_magic('timeit', 'all(map(lambda x: (x % 2) == 0, [1, 2, 3, 4, 5]))')


# In[168]:


get_ipython().run_line_magic('timeit', 'ilexiste(lambda x: (x % 2) == 0, [1, 2, 3, 4, 5])')
get_ipython().run_line_magic('timeit', 'any(map(lambda x: (x % 2) == 0, [1, 2, 3, 4, 5]))')


# ## Exercice 21 : `appartient` version 2

# In[178]:


def appartient_curry(x : _a) -> Callable[[List[_a]], bool]:
    return lambda liste: ilexiste(lambda y: x == y, liste)

def appartient(x : _a, liste : List[_a]) -> bool:
    return ilexiste(lambda y: x == y, liste)


# In[179]:


def toutes_egales(x : _a, liste : List[_a]) -> bool:
    return qqsoit(lambda y: x == y, liste)


# In[181]:


appartient_curry(1)([1, 2, 3])

appartient(1, [1, 2, 3])
appartient(5, [1, 2, 3])

toutes_egales(1, [1, 2, 3])
toutes_egales(5, [1, 2, 3])


# Est-ce que notre implémentation peut être plus rapide que le test `x in liste` ?
# Non, mais elle est aussi rapide. C'est déjà pas mal !

# In[183]:


get_ipython().run_line_magic('timeit', 'appartient(random.randint(-10, 10), [random.randint(-1000, 1000) for _ in range(1000)])')
get_ipython().run_line_magic('timeit', 'random.randint(-10, 10) in [random.randint(-1000, 1000) for _ in range(1000)]')


# ## Exercice 22 : `filtre`

# In[186]:


from typing import TypeVar, List, Callable
_a = TypeVar('_a')

# Comme list(filter(f, liste))
def filtre(f : Callable[[_a], bool], liste : List[_a]) -> List[_a]:
    # return [x for x in liste if f(x)]
    liste2 = []
    for x in liste:
        if f(x):
            liste2.append(x)
    return liste2


# In[185]:


filtre(lambda x: (x % 2) == 0, [1, 2, 3, 4, 5])
filtre(lambda x: (x % 2) != 0, [1, 2, 3, 4, 5])


# ## Exercice 23
# Je vous laisse trouver pour `premiers`.

# In[189]:


pairs   = lambda liste: filtre(lambda x: (x % 2) == 0, liste)
impairs = lambda liste: filtre(lambda x: (x % 2) != 0, liste)


# In[188]:


pairs(list(range(10)))
impairs(list(range(10)))


# ## Exercice 24 : `reduit`

# In[211]:


from typing import TypeVar, List, Callable
_a = TypeVar('_a')

# Comme list(filter(f, liste))
def reduit_rec(f : Callable[[_a, _b], _a], acc : _a, liste : List[_b]) -> _a:
    if len(liste) == 0:
        return acc
    else:
        h, q = liste[0], liste[1:]
        return reduit(f, f(acc, h), q)

# Version non récursive, bien plus efficace
def reduit(f : Callable[[_a, _b], _a], acc : _a, liste : List[_b]) -> _a:
    acc_value = acc
    for x in liste:
        acc_value = f(acc_value, x)
    return acc_value


# Très pratique pour calculer des sommes, notamment.

# ## Exercice 25 : `somme`, `produit`

# In[212]:


from operator import add
somme_rec = lambda liste: reduit_rec(add, 0, liste)
somme = lambda liste: reduit(add, 0, liste)

somme_rec(list(range(10)))
somme(list(range(10)))
sum(list(range(10)))


# In[213]:


get_ipython().run_line_magic('timeit', 'somme_rec(list(range(10)))')
get_ipython().run_line_magic('timeit', 'somme(list(range(10)))')
get_ipython().run_line_magic('timeit', 'sum(list(range(10)))')


# Pour de petites listes, la version récursive est aussi efficace que la version impérative. Chouette !

# In[214]:


get_ipython().run_line_magic('timeit', 'somme_rec(list(range(1000)))')
get_ipython().run_line_magic('timeit', 'somme(list(range(1000)))')
get_ipython().run_line_magic('timeit', 'sum(list(range(1000)))')


# In[205]:


from operator import mul
produit = lambda liste: reduit(mul, 1, liste)

produit(list(range(1, 6)))  # 5! = 120


# Bonus :

# In[208]:


def factorielle(n : int) -> int:
    return produit(range(1, n + 1))

for n in range(1, 15):
    print("{:>7}! = {:>13}".format(n, factorielle(n)))


# ## Exercice 26 : `miroir` version 2

# In[220]:


miroir = lambda liste: reduit(lambda l, x : [x] + l, [], liste)


# In[221]:


miroir([2, 3, 5, 7, 11])


# **Attention** en Python, les listes ne sont PAS simplement chainées, donc `lambda l, x : [x] + l` est en temps **linéaire** en $|l| = n$, pas en $\mathcal{O}(1)$ comme en Caml/OCaml pour `fun l x -> x :: l`.

# ----
# # Arbres

# /!\ Les deux dernières parties sont **bien plus difficiles** en Python qu'en Caml.

# ## Exercice 27

# In[1]:


from typing import Dict, Optional, Tuple

# Impossible de définir un type récursivement, pas comme en Caml
arbre_bin = Dict[str, Optional[Tuple[Dict, Dict]]]


# In[37]:


from pprint import pprint


# In[38]:


arbre_test = {'Noeud': (
        {'Noeud': (
            {'Noeud': (
                {'Feuille': None},
                {'Feuille': None}
            )},
            {'Feuille': None}
        )},
        {'Feuille': None}
    )}


# In[39]:


pprint(arbre_test)


# Avec une syntaxe améliorée, on se rapproche de très près de la syntaxe de Caml/OCaml :

# In[40]:


Feuille = {'Feuille': None}
Noeud = lambda x, y : {'Noeud': (x, y)}


# In[34]:


arbre_test = Noeud(Noeud(Noeud(Feuille, Feuille), Feuille), Feuille)


# In[36]:


pprint(arbre_test)


# ## Exercice 28

# Compte le nombre de feuilles et de sommets.

# In[5]:


def taille(a : arbre_bin) -> int:
    # Pattern matching ~= if, elif,.. sur les clés de la profondeur 1
    # du dictionnaire (une seule clé)
    if 'Feuille' in a:
        return 1
    elif 'Noeud' in a:
        x, y = a['Noeud']
        return 1 + taille(x) + taille(y)


# In[6]:


taille(arbre_test)  # 7


# ## Exercice 29

# In[7]:


def hauteur(a : arbre_bin) -> int:
    if 'Feuille' in a:
        return 0
    elif 'Noeud' in a:
        x, y = a['Noeud']
        return 1 + max(hauteur(x), hauteur(y))


# In[8]:


hauteur(arbre_test)  # 3


# ## Exercice 30

# Bonus. (Écrivez une fonction testant si un arbre étiqueté par des entiers est tournoi.)

# ----
# # Parcours d'arbres binaires

# Après quelques exercices manipulant cette structure de dictionnaire, écrire la suite n'est pas trop difficile.

# ## Exercice 31

# In[9]:


from typing import TypeVar, Union, List

F = TypeVar('F')
N = TypeVar('N')

element_parcours = Union[F, N]
parcours = List[element_parcours]


# ## Exercice 32 : Parcours naifs (complexité quadratique)

# In[10]:


def parcours_prefixe(a : arbre_bin) -> parcours:
    if 'Feuille' in a:
        return [F]
    elif 'Noeud' in a:
        g, d = a['Noeud']
        return [N] + parcours_prefixe(g) + parcours_prefixe(d)

parcours_prefixe(arbre_test)


# In[11]:


def parcours_postfixe(a : arbre_bin) -> parcours:
    if 'Feuille' in a:
        return [F]
    elif 'Noeud' in a:
        g, d = a['Noeud']
        return parcours_postfixe(g) + parcours_postfixe(d) + [N]

parcours_postfixe(arbre_test)


# In[12]:


def parcours_infixe(a : arbre_bin) -> parcours:
    if 'Feuille' in a:
        return [F]
    elif 'Noeud' in a:
        g, d = a['Noeud']
        return parcours_infixe(g) + [N] + parcours_infixe(d)

parcours_infixe(arbre_test)


# Pourquoi ont-ils une complexité quadratique ? La concaténation (`@` en OCaml, `+` en Python) ne se fait pas en temps constant mais linéaire dans la taille de la plus longue liste.

# ## Exercice 33 : Parcours linéaires
# 
# On ajoute une fonction auxiliaire et un argument `vus` qui est une liste qui stocke les élements observés dans l'ordre du parcours

# In[13]:


def parcours_prefixe2(a : arbre_bin) -> parcours:
    def parcours(vus, b):
        if 'Feuille' in b:
            vus.insert(0, F)
            return vus
        elif 'Noeud' in b:
            vus.insert(0, N)
            g, d = b['Noeud']
            return parcours(parcours(vus, g), d)
    p = parcours([], a)
    return p[::-1]

parcours_prefixe2(arbre_test)


# In[14]:


def parcours_postfixe2(a : arbre_bin) -> parcours:
    def parcours(vus, b):
        if 'Feuille' in b:
            vus.insert(0, F)
            return vus
        elif 'Noeud' in b:
            g, d = b['Noeud']
            p = parcours(parcours(vus, g), d)
            p.insert(0, N)
            return p
    p = parcours([], a)
    return p[::-1]

parcours_postfixe2(arbre_test)


# In[15]:


def parcours_infixe2(a : arbre_bin) -> parcours:
    def parcours(vus, b):
        if 'Feuille' in b:
            vus.insert(0, F)
            return vus
        elif 'Noeud' in b:
            g, d = b['Noeud']
            p = parcours(vus, g)
            p.insert(0, N)
            return parcours(p, d)
    p = parcours([], a)
    return p[::-1]

parcours_infixe2(arbre_test)


# ## Exercice 34 : parcours en largeur et en profondeur

# Pour utiliser une file de priorité (*priority queue*), on utilise le module [collections.deque](https://docs.python.org/3/library/collections.html#collections.deque).

# In[16]:


from collections import deque

def parcours_largeur(a : arbre_bin) -> parcours:
    file = deque()
    # fonction avec effet de bord sur la file
    def vasy() -> parcours:
        if len(file) == 0:
            return []
        else:
            b = file.pop()
            if 'Feuille' in b:
                # return [F] + vasy()
                v = vasy()
                v.insert(0, F)
                return v
            elif 'Noeud' in b:
                g, d = b['Noeud']
                file.insert(0, g)
                file.insert(0, d)
                # return [N] + vasy()
                v = vasy()
                v.insert(0, N)
                return v
    file.insert(0, a)
    return vasy()

parcours_largeur(arbre_test)


# En remplaçant la file par une pile (une simple `list`), on obtient le parcours en profondeur, avec la même complexité.

# In[17]:


def parcours_profondeur(a : arbre_bin) -> parcours:
    pile = []
    # fonction avec effet de bord sur la file
    def vasy() -> parcours:
        if len(pile) == 0:
            return []
        else:
            b = pile.pop()
            if 'Feuille' in b:
                # return [F] + vasy()
                v = vasy()
                v.append(F)
                return v
            elif 'Noeud' in b:
                g, d = b['Noeud']
                pile.append(g)
                pile.append(d)
                # return [N] + vasy()
                v = vasy()
                v.insert(0, N)
                return v
    pile.append(a)
    return vasy()

parcours_profondeur(arbre_test)


# ## Exercice 35 et fin

# ### Reconstruction depuis le parcours prefixe

# In[18]:


test_prefixe = parcours_prefixe2(arbre_test)
test_prefixe


# L'idée de cette solution est la suivante :
# j'aimerais une fonction récursive qui fasse le travail;
# le problème c'est que si on prend un parcours prefixe, soit il commence
# par F et l'arbre doit être une feuille; soit il est de la forme N::q
# où q n'est plus un parcours prefixe mais la concaténation de DEUX parcours
# prefixe, on ne peut donc plus appeler la fonction sur q.
# On va donc écrire une fonction qui prend une liste qui contient plusieurs
# parcours concaténé et qui renvoie l'arbre correspondant au premier parcours
# et ce qui n'a pas été utilisé :

# In[22]:


from typing import Tuple

def reconstruit_prefixe(par : parcours) -> arbre_bin:
    def reconstruit(p : parcours) -> Tuple[arbre_bin, parcours]:
        if len(p) == 0:
            raise ValueError("parcours invalide pour reconstruit_prefixe")
        elif p[0] == F:
            return (Feuille, p[1:])
        elif p[0] == N:
            g, q = reconstruit(p[1:])
            d, r = reconstruit(q)
            return (Noeud(g, d), r)
    # call it
    a, p = reconstruit(par)
    if len(p) == 0:
        return a
    else:
        raise ValueError("parcours invalide pour reconstruit_prefixe")


# In[23]:


reconstruit_prefixe([F])


# In[24]:


reconstruit_prefixe(test_prefixe)


# Et cet exemple va échouer :

# In[25]:


reconstruit_prefixe([N, F, F] + test_prefixe)  # échoue


# ### Reconstruction depuis le parcours en largeur

# Ce n'est pas évident quand on ne connait pas. L'idée est de se servir d'une file
# pour stocker les arbres qu'on reconstruit peu à peu depuis les feuilles. La file
# permet de récupérer les bons sous-arbres quand on rencontre un noeud

# In[27]:


largeur_test = parcours_largeur(arbre_test)
largeur_test


# In[41]:


from collections import deque

def reconstruit_largeur(par : parcours) -> arbre_bin:
    file = deque()
    # Fonction avec effets de bord
    def lire_element(e : element_parcours) -> None:
        if e == F:
            file.append(Feuille)
        elif e == N:
            d = file.popleft()
            g = file.popleft()  # attention à l'ordre !
            file.append(Noeud(g, d))
    # Applique cette fonction à chaque élement du parcours
    for e in reversed(par):
        lire_element(e)
    if len(file) == 1:
        return file.popleft()
    else:
        raise ValueError("parcours invalide pour reconstruit_largeur")


# In[43]:


largeur_test
reconstruit_largeur(largeur_test)
arbre_test


# Le même algorithme (enfin presque, modulo interversion de g et d)
# avec une pile donne une autre version de la reconstruction du parcours prefixe.

# In[44]:


from collections import deque

def reconstruit_prefixe2(par : parcours) -> arbre_bin:
    pile = deque()
    # Fonction avec effets de bord
    def lire_element(e : element_parcours) -> None:
        if e == F:
            pile.append(Feuille)
        elif e == N:
            g = pile.pop()
            d = pile.pop()  # attention à l'ordre !
            pile.append(Noeud(g, d))
    # Applique cette fonction à chaque élement du parcours
    for e in reversed(par):
        lire_element(e)
    if len(pile) == 1:
        return pile.pop()
    else:
        raise ValueError("parcours invalide pour reconstruit_prefixe2")


# In[45]:


prefixe_test = parcours_prefixe2(arbre_test)
prefixe_test


# In[46]:


reconstruit_prefixe2(prefixe_test)
arbre_test


# ----
# # Conclusion
# 
# Fin. À la séance prochaine.
