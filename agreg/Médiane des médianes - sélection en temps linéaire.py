#!/usr/bin/env python
# coding: utf-8

# # Problème de sélection du k-ième plus petit élément d'un tableau
# 
# Étant donné un tableau T=[T[0],...,T[n-1]] de $n$ éléments quelconques (par exemple des entiers), et $k\in\{1,\dots,n\}$, on cherche le k-ième plus petit élément du tableau.
# 
# Exemple : pour `T = [5, 4, 1, 2, 3]`, pour `k=1` on a 1, `k=2` on a 2, etc.
# 
# En cas d'éléments distincts, par exemple `T = [1, 1, 2, 3]`, le 2-ième plus petit peut être définit comme 2, ou comme 1. Il vaut mieux le définir comme 1, ainsi l'élément cherché a toujours un sens.
# 
# 
# Ce petit [notebook Python](https://www.Jupyter.org/) implémente :
# 
# - un algorithme naïf, qui s'exécute en temps $\mathcal{O}(k n)$ (pire cas $\mathcal{O}(n^2)$),
# - une solution naïve qui trie le tableau et lit la k-ième valeur et s'exécute donc en temps $\mathcal{O}(n \log(n))$, indépemment de $k$,
# - et un algorithme **optimal** qui s'exécute en temps $\mathcal{O}(n)$ (on ne peut pas faire mieux car il faut forcément lire le tableau au moins une fois s'il n'est pas trié).
# 
# Je fais aussi des expériences numériques pour illustrer empiriquement leurs complexités.
# 
# 
# - Auteur : [Lilian Besson](https://github.com/Naereen/notebooks/)
# - Date : 29 septembre 2020
# - [License : MIT](https://lbesson.mit-license.org)

# In[1]:


from sys import version
print(version)


# J'ai pris l'habitude d'écrire des signatures de fonctions en python qui soient typées :

# In[4]:


from typing import List, Any, TypeVar

T = TypeVar("T")


# Je ferai les premiers exemples avec ces deux tableaux :

# In[183]:


tableau1 = [5, 4, 1, 2, 3]
tableau2 = [1, 1, 2, 3]    # avec un doublon


# ----
# ## Solution naïve en temps quadratique
# 
# On peut rapidement imaginer un algorithme "divisé pour régner" naïf :
# 
# - Si `k=1`, on calcule en temps linéaire le minimum du tableau,
# - Sinon, on calcule le minimum, on construit un tableau de taille `n-1` qui est le tableau initial privé d'UNE occurrence de son minimum (en temps $\mathcal{O}(n)$), puis on appelle la sélection avec `k-1` sur ce tableau. Si on note $T(n, k)$ le nombre d'opérations élémentaires dans le pire cas pour un tableau quelconque de taille $n$, alors elle est croissante et vérifie la relation de récurrence suivante :
#   $$ \forall n > 1, 1 \leq k \leq n \; T(n, k) = O(n) + T(n-1, k-1) $$
#   et $T(1) = O(1)$, ce qui donne $T(n,k) = O(n k)$ (pas par une application directe du théorème maître, mais c'est la même idée de preuve).

# In[16]:


def selection_naive(tableau: List[T], k: int) -> T:
    """ Sélection du k-ième plus petit élément du tableau, récursivement et naïvement.
    
    - Complexité mémoire : O(n)
    - Complexité temps : O(k n)
    """
    assert 1 <= k <= len(tableau), f"Erreur : k = {k} doit être entre 1 et n = {len(tableau)} = len(tableau)"
    min_tableau = min(tableau)
    if k == 1:  # cas simple
        return min_tableau
    else:
        # on construit un nouveau tableau, de taille n-1, en enlevant UNE occurrence de min
        nouveau_tableau = []
        min_deja_vu = False
        for valeur in tableau:
            if valeur == min_tableau:
                if min_deja_vu:  # on a déjà vu UNE occurrence de min, on l'ajoute encore
                    nouveau_tableau.append(valeur)
                else:            # première occurrence de min
                    min_deja_vu = True
            else:
                nouveau_tableau.append(valeur)
        return selection_naive(nouveau_tableau, k-1)


# Deux exemples :

# In[14]:


print(f"Pour le tableau {tableau1} :")
for k in range(1, 1 + len(tableau1)):
    print(f"    Le {k}-ième élément du tableau est {selection_naive(tableau1, k)}")


# In[13]:


print(f"Pour le tableau {tableau2} :")
for k in range(1, 1 + len(tableau2)):
    print(f"    Le {k}-ième élément du tableau est {selection_naive(tableau2, k)}")


# ----
# ## Solution naïve en temps sur logarithmique (O(n log n))
# 
# C'est un algorithme très simple :
# 
# - On trie le tableau (avec n'importe quel algorithme de tri général, en $\Theta(n \log(n))$, par exemple le tri fusion, le tri rapide, le tri par tas, etc) ;
# - Puis on a juste à lire la k-ième valeur du tableau trié.

# In[17]:


def selection_par_tri(tableau: List[T], k: int) -> T:
    """ Sélection du k-ième plus petit élément du tableau, par un tri.
    
    - Complexité mémoire : O(n)
    - Complexité temps : O(n \log n)
    """
    copie_tableau = list(tableau)  # ou tableau.copy()
    copie_tableau.sort()
    return copie_tableau[k - 1]


# Deux exemples :

# In[46]:


print(f"Pour le tableau {tableau1} :")
for k in range(1, 1 + len(tableau1)):
    print(f"    Le {k}-ième élément du tableau est {selection_par_tri(tableau1, k)}")


# In[47]:


print(f"Pour le tableau {tableau2} :")
for k in range(1, 1 + len(tableau2)):
    print(f"    Le {k}-ième élément du tableau est {selection_par_tri(tableau2, k)}")


# ## Méthode optimale : médiane des médianes
# 
# L'algorithme se déroule en 3 étapes :
# 
# - L'algorithme divise la liste en groupes de cinq éléments. Ensuite, pour chaque groupe de cinq, la médiane est calculée (une opération qui peut s'effectuer en temps constant, par exemple en utilisant un algorithme de tri),
# - L'algorithme est alors appelé récursivement sur cette sous-liste de n / 5 éléments pour trouver la vraie médiane de ces éléments. On peut alors garantir que l'élément obtenu se place entre le 30e et le 70e centile,
# - Enfin, la médiane des médianes est choisie pour être le pivot. Selon la position de l'élément recherché, l'algorithme recommence avec les éléments au-dessus du pivot ou en dessous, qui représentent au plus 70 % de la taille initiale de l'espace de recherche.
# 
# > Référence : https://fr.wikipedia.org/wiki/Médiane_des_médianes, aussi dans [Algorithmique, Cormen et al]

# ### Calcul en temps constant de la médiane de 5 valeurs

# In[35]:


def mediane_cinq_valeurs(tableau: List[T]) -> T:
    assert 1 <= len(tableau) <= 5, f"Erreur : tableau a longueur = {len(tableau)} mais devrait etre 1 <= .. <= 5"
    valeurs = sorted(tableau)
    return valeurs[len(tableau) // 2]


# In[36]:


assert 3 == mediane_cinq_valeurs([1, 2, 3, 4, 5])
assert 3 == mediane_cinq_valeurs([5, 1, 4, 2, 3])


# Que se passe-t-il si la liste n'est pas de taille impaire ?
# On peut prendre la valeur à gauche ou à droite du milieu. Ici, c'est la valeur à droite qui a été choisie :

# In[37]:


mediane_cinq_valeurs([1, 2, 3, 4])


# In[38]:


mediane_cinq_valeurs([1, 2, 4])


# ### Découper le tableau en sous-tableaux :
# 
# Par exemple :

# In[39]:


tableau3 = [1,2,3,4,5, 6,7,8,9,10, 11,12,13]
# On va le découper comme ça :
[
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13],
]


# Cela est très rapide avec des listes par compréhension :

# In[40]:


[
    tableau3[i:i+5]
    for i in range(0, len(tableau3), 5)
]


# Et donc si on calcule les médianes :

# In[41]:


[
    mediane_cinq_valeurs(tableau3[i:i+5])
    for i in range(0, len(tableau3), 5)
]


# ### Médiane des médianes par une approche récursive

# In[42]:


def mediane_des_medianes(tableau: List[T]) -> T:
    """ Méthode de la médiane des médianes.
    
    - Complexité mémoire : O(n).
    - Complexité temps : O(n) car T(n) = O(n) + T(n/5) pour tout n=5^k (cas (i) du Master Theorem).
    """
    assert 1 <= len(tableau), f"Erreur : k = {k} doit être entre 1 et n = {len(tableau)} = len(tableau)"
    n = len(tableau)
    if n <= 5:  # O(1)
        return mediane_cinq_valeurs(tableau)
    else:
        medianes = [
            # au plus 1 + (n/5) sous-tableaux de taille <= 5
            mediane_cinq_valeur(tableau[i : i+5])
            for i in range(0, n, 5)
        ]
        # un appel récursive en T(n/5)  (si on fait la preuve juste pour des n = 5^k)
        return mediane_des_medianes(medianes)


# Par exemple, la médiane des médianes du tableau d'exemple est 8 car son tableau des médianes des sous-tableaux de taille <= 5 est [3, 8, 12] :

# In[43]:


mediane_des_medianes(tableau3)


# ### Sélection par médianes
# 
# On met ensemble tous les éléments :

# In[66]:


def selection_par_medianes(tableau: List[T], k: int) -> T:
    """ Sélection du k-ième plus petit élément du tableau, par la méthode de la médiane des médianes.
    
    - Complexité mémoire : O(n)
    - Complexité temps : O(n)
    """
    assert 1 <= k <= len(tableau), f"Erreur : k = {k} doit être entre 1 et n = {len(tableau)} = len(tableau)"
    n = len(tableau)
    print(f"DEBUG : n = {n}, tableau = {tableau}, k = {k}")
    if n <= 1:
        return tableau[0]
    if n <= 5:
        print(f"WARNING n = {n} <= k = {k}")
    mediane = mediane_des_medianes(tableau)
    index_mediane = tableau.index(mediane)
    if (k-1) == index_mediane:
        return mediane
    else:
        if (k-1) < index_mediane:
            sous_tableau = [ x for x in tableau if x <= mediane ]
        else:  # (k-1) > index_mediane
            sous_tableau = [ x for x in tableau if x >= mediane ]
        return selection_par_medianes(sous_tableau, k)      


# Deux exemples :

# In[67]:


print(f"Pour le tableau {tableau1} :")
for k in range(1, 1 + len(tableau1)):
    print(f"    Le {k}-ième élément du tableau est {selection_par_medianes(tableau1, k)}")


# In[54]:


print(f"Pour le tableau {tableau2} :")
for k in range(1, 1 + len(tableau2)):
    print(f"    Le {k}-ième élément du tableau est {selection_par_medianes(tableau2, k)}")


# ### Autre approche
# 
# En regardant le code donné sur https://en.wikipedia.org/wiki/Median_of_medians

# On va faire plein d'échanges de valeurs dans un tableau :

# In[112]:


def swap(tableau: List[T], i: int, j: int) -> None:
    """ Échange tableau[i] et tableau[j] en temps constant."""
    tableau[i], tableau[j] = tableau[j], tableau[i]


# Avec un petit tri par insertion sur cinq éléments (max cinq), on peut trouver la médiane d'un petit tableau en temps constant :

# In[113]:


def partition5(tableau: List[T], left: int, right: int) -> int:
    """ Sélecte la médiane d'un tableau d'au plus 5 éléments, par un tri par insertion sur ces cinq éléments."""
    print(f"DEBUG: partition5({tableau}, {left}, {right})")
    i = left + 1
    while i <= right:
        j = i
        while j > left and tableau[j-1] > tableau[j]:
            swap(tableau, j-1, j)
            j = j - 1
        i = i + 1
    return (left + right) // 2


# Par exemple :

# In[114]:


t = [5, 3, 2, 1, 4]
print(partition5(t, 0, len(t) - 1))
print(t)


# Le calcul du pivot fera un appel à `selection`, qui lui-même appelle `pivot` (par récursion mutuelle) :

# In[115]:


def pivot(tableau: List[T], left: int, right: int) -> int:
    """ Pivot en temps O(n)."""
    print(f"DEBUG: pivot({tableau}, {left}, {right})")
    if right - left + 1 <= 5:  # <= 5 éléments
        return partition5(tableau, left, right)
    # sinon, on déplace les médianes des sous tableaux de cinq éléments vers les n/5 premières positions
    for i in range(left, right + 1, 5):
        # calcule la position de la médiane du i-ieme sous-groupe :
        sub_right = i + 4
        if sub_right > right:
            sub_right = right
        median5 = partition5(tableau, i, sub_right)
        new_pos = left + (i - left)//5
        swap(tableau, median5, new_pos)

    # médiane des n/5 médianes des sous-groupes
    mid = (right - left) // 10 + left + 1
    return selection(tableau, mid, left=left, right=left + (right - left) // 5)


# La sélection utilisera la fonction `pivot` et la `partition` :

# In[116]:


from typing import Optional


# In[117]:


def selection(tableau: List[T], k: int, left: Optional[int] = None, right: Optional[int] = None) -> int:
    """ Sélection en temps linéaire du k-ième plus petit élément dans [tab[left],...,tab[right]]."""
    if left is None: left = 0
    if right is None: right = len(tableau) - 1
    print(f"DEBUG: selection({tableau}, {k}, {left}, {right})")
    while True:
        if left == right:
            return left
        pivot_index = pivot(tableau, left, right)
        pivot_index = partition(tableau, left, right, pivot_index, k)
        if k == pivot_index:
            return k  # déjà à la bonne position
        elif k < pivot_index:
            right = pivot_index - 1
        else:
            left  = pivot_index + 1


# Et enfin la fonction de partition :

# In[118]:


def partition(tableau: List[T], left: int, right: int, pivot_index: int, k: int) -> int:
    print(f"DEBUG: partition({tableau}, {left}, {right}, {pivot_index}, {k})")
    pivot_value = tableau[pivot_index]
    swap(tableau, pivot_index, right)  # on déplace le pivot à la fin
    store_index = left
    # on déplace les éléments plus petits que le pivot à sa gauche
    for i in range(left, right):
        if tableau[i] < pivot_value:
            swap(tableau, store_index, i)
            store_index = store_index + 1
    # on déplace tous les éléments égaux au pivot just après les plus petits éléments
    store_index_eq = store_index
    for i in range(store_index, right):
        if tableau[i] == pivot_value:
            swap(tableau, store_index_eq, i)
            store_index_eq = store_index_eq + 1
    # on déplace le pivot à sa position finale au milieu
    swap(tableau, right, store_index_eq)
    # on renvoie la localisation du pivot, compte tenu de la position recherchée k
    if k < store_index:
        return store_index     # k est dans le groupe des petits éléments
    elif k == store_index_eq:
        return k               # k est dans le groupe égal au pivot
    else:
        return store_index_eq  # k est dans le groupe des petits éléments


# Deux exemples :

# In[127]:


print(f"Pour le tableau {tableau1} :")
for k in range(1, 1 + len(tableau1)):
    print(f"    Le {k}-ième élément du tableau est {selection(tableau1[:], k)}")


# In[184]:


for tab in (
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4],
        # [1, 2, 3] * 10,
    ):
    print(f"Pour le tableau {tab} :")
    for k in range(1, 1 + len(tab)):
        print(f"    Le {k}-ième élément du tableau est {selection(tab[:], k)}")


# In[129]:


for tab in (
        tableau2,
        tableau2[::-1],
    ):
        print(f"Pour le tableau {tab} :")
        for k in range(1, 1 + len(tab)):
            print(f"    Le {k}-ième élément du tableau est {selection(tab[:], k)}")


# ### Autre implémentation
# 
# Celle-ci sera la bonne :
# 
# > Inspirée de https://stackoverflow.com/a/34911527/

# In[185]:


def find_i_th_smallest(tableau: List[T], k: Optional[int] = None, items_per_column: int = 5) -> T:
    if k is None:
        k = (len(tableau) - 1) // 2
    n = len(tableau)
    if n <= items_per_column:
        # si tableau est assez petit, on fait juste un tri et on trouve le k-ième élément
        return sorted(tableau)[k]
    else:
        # 1. partition A into columns of items_per_column items each. items_per_column is odd, say 15.
        # 2. find the median of every column
        # 3. put all medians in a new list, say, called medians
        medians = [
            find_i_th_smallest(tableau[j : (j + items_per_column)])
            for j in range(0, n, items_per_column)
        ]

        # 4. find M, the median of the medians
        median_of_medians = find_i_th_smallest(medians)  # with k=None, computes middle value = median

        # 5. split A into 3 parts by M, { < M }, { == M }, and { > M }
        # 6. find which above set has tableau's k-th smallest, recursively.
        lefts = [ x for x in tableau if x < median_of_medians ]
        if k < len(lefts):
            return find_i_th_smallest(lefts, k)
        rights = [ x for x in tableau if x > median_of_medians ]
        len_rights = len(rights)
        if k < (n - len_rights):
            return median_of_medians
        return find_i_th_smallest(rights, k - (n - len_rights))


# On peut faire quelques tests :

# In[175]:


try:
    from tqdm.notebook import tqdm
except ImportError:
    def tqdm(iterator, **kwargs): return iterator


# In[186]:


number_of_tests = 1

# How many numbers should be randomly generated for testing?
for number_of_numbers in tqdm([100, 1000, 10000]):
    print(f"Pour des listes de taille {number_of_numbers} :")
    for test in tqdm(range(number_of_tests)):
        print(f"Test {test + 1} / {number_of_tests} avec une liste de taille {number_of_numbers} :")
        # create a list of random positive integers
        tableau = [ random.randint(0, number_of_numbers) for i in range(0, number_of_numbers) ]
        for L in [ tableau, tableau*2 ]:

            sorted_L = sorted(L)
            for k in range(len(L)):
                assert sorted_L[k] == find_i_th_smallest(L, k)

            get_ipython().run_line_magic('timeit', '-n1 sorted(L)[random.randint(0, len(L) - 1)]')
            get_ipython().run_line_magic('timeit', '-n1 find_i_th_smallest(L, random.randint(0, len(L) - 1))')


# In[182]:


number_of_tests = 1

# How many numbers should be randomly generated for testing?
for number_of_numbers in tqdm([500, 5000, 50000, 100000]):
    print(f"Pour des listes de taille {number_of_numbers} :")
    for test in tqdm(range(number_of_tests)):
        print(f"Test {test + 1} / {number_of_tests} avec une liste de taille {number_of_numbers} :")
        # create a list of random positive integers
        tableau = [ random.randint(0, number_of_numbers) for i in range(0, number_of_numbers) ]
        for L in [ tableau, tableau*2 ]:

            sorted_L = sorted(L)
            for k in range(len(L)):
                assert sorted_L[k] == find_i_th_smallest(L, k)

            get_ipython().run_line_magic('timeit', '-n1 sorted(L)[random.randint(0, len(L) - 1)]')
            get_ipython().run_line_magic('timeit', '-n1 find_i_th_smallest(L, random.randint(0, len(L) - 1))')


# Empiriquement, pour des listes pas trop grandes, la méthode naïve qui trie la liste est plus rapide.
# C'est assez logique, le tri `sorted()` de Python est implémenté en C et est très efficace.
# 
# Pour des listes plus grandes, on voit que la tendance s'inverse.

# ----
# ## Conclusion
# C'est tout pour ce notebook ! Merci de l'avoir lu.
# 
# > Pour plus de notebooks, cf https://GitHub.com/Naereen/notebooks
