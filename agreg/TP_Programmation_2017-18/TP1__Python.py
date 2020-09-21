#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#TP-1---Programmation-pour-la-préparation-à-l'agrégation-maths-option-info" data-toc-modified-id="TP-1---Programmation-pour-la-préparation-à-l'agrégation-maths-option-info-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>TP 1 - Programmation pour la préparation à l'agrégation maths option info</a></span><ul class="toc-item"><li><span><a href="#Remarques-sur-le-style" data-toc-modified-id="Remarques-sur-le-style-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Remarques sur le style</a></span></li></ul></li><li><span><a href="#Fonctions" data-toc-modified-id="Fonctions-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Fonctions</a></span><ul class="toc-item"><li><span><a href="#Exercice-4" data-toc-modified-id="Exercice-4-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Exercice 4</a></span></li><li><span><a href="#Exercice-5" data-toc-modified-id="Exercice-5-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Exercice 5</a></span></li><li><span><a href="#Exercice-6" data-toc-modified-id="Exercice-6-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Exercice 6</a></span></li></ul></li><li><span><a href="#Récursivité" data-toc-modified-id="Récursivité-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Récursivité</a></span><ul class="toc-item"><li><span><a href="#Exercice-7" data-toc-modified-id="Exercice-7-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Exercice 7</a></span></li><li><span><a href="#Exercice-8" data-toc-modified-id="Exercice-8-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Exercice 8</a></span></li><li><span><a href="#Exercice-9" data-toc-modified-id="Exercice-9-3.3"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>Exercice 9</a></span></li><li><span><a href="#Exercice-10" data-toc-modified-id="Exercice-10-3.4"><span class="toc-item-num">3.4&nbsp;&nbsp;</span>Exercice 10</a></span></li><li><span><a href="#Exercice-11" data-toc-modified-id="Exercice-11-3.5"><span class="toc-item-num">3.5&nbsp;&nbsp;</span>Exercice 11</a></span></li></ul></li><li><span><a href="#Listes" data-toc-modified-id="Listes-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Listes</a></span><ul class="toc-item"><li><span><a href="#Exercice-12" data-toc-modified-id="Exercice-12-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Exercice 12</a></span></li><li><span><a href="#Exercice-13" data-toc-modified-id="Exercice-13-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>Exercice 13</a></span></li><li><span><a href="#Exercice-14" data-toc-modified-id="Exercice-14-4.3"><span class="toc-item-num">4.3&nbsp;&nbsp;</span>Exercice 14</a></span></li><li><span><a href="#Exercice-15" data-toc-modified-id="Exercice-15-4.4"><span class="toc-item-num">4.4&nbsp;&nbsp;</span>Exercice 15</a></span></li><li><span><a href="#Exercice-16" data-toc-modified-id="Exercice-16-4.5"><span class="toc-item-num">4.5&nbsp;&nbsp;</span>Exercice 16</a></span></li><li><span><a href="#Exercice-17" data-toc-modified-id="Exercice-17-4.6"><span class="toc-item-num">4.6&nbsp;&nbsp;</span>Exercice 17</a></span></li></ul></li><li><span><a href="#Exponentiation-rapide" data-toc-modified-id="Exponentiation-rapide-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Exponentiation rapide</a></span><ul class="toc-item"><li><span><a href="#Exercice-18" data-toc-modified-id="Exercice-18-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>Exercice 18</a></span></li><li><span><a href="#Exercice-19" data-toc-modified-id="Exercice-19-5.2"><span class="toc-item-num">5.2&nbsp;&nbsp;</span>Exercice 19</a></span></li><li><span><a href="#Exercice-20" data-toc-modified-id="Exercice-20-5.3"><span class="toc-item-num">5.3&nbsp;&nbsp;</span>Exercice 20</a></span></li><li><span><a href="#Exercice-21" data-toc-modified-id="Exercice-21-5.4"><span class="toc-item-num">5.4&nbsp;&nbsp;</span>Exercice 21</a></span></li><li><span><a href="#Exercice-22" data-toc-modified-id="Exercice-22-5.5"><span class="toc-item-num">5.5&nbsp;&nbsp;</span>Exercice 22</a></span></li><li><span><a href="#Exercice-23" data-toc-modified-id="Exercice-23-5.6"><span class="toc-item-num">5.6&nbsp;&nbsp;</span>Exercice 23</a></span></li></ul></li><li><span><a href="#Formule-du-calcul-propositionnel" data-toc-modified-id="Formule-du-calcul-propositionnel-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Formule du calcul propositionnel</a></span><ul class="toc-item"><li><span><a href="#Exercice-24" data-toc-modified-id="Exercice-24-6.1"><span class="toc-item-num">6.1&nbsp;&nbsp;</span>Exercice 24</a></span></li><li><span><a href="#Exercice-25" data-toc-modified-id="Exercice-25-6.2"><span class="toc-item-num">6.2&nbsp;&nbsp;</span>Exercice 25</a></span></li><li><span><a href="#Exercice-26" data-toc-modified-id="Exercice-26-6.3"><span class="toc-item-num">6.3&nbsp;&nbsp;</span>Exercice 26</a></span></li><li><span><a href="#Exercice-27" data-toc-modified-id="Exercice-27-6.4"><span class="toc-item-num">6.4&nbsp;&nbsp;</span>Exercice 27</a></span></li><li><span><a href="#Exercice-28" data-toc-modified-id="Exercice-28-6.5"><span class="toc-item-num">6.5&nbsp;&nbsp;</span>Exercice 28</a></span></li></ul></li><li><span><a href="#Conclusion" data-toc-modified-id="Conclusion-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Conclusion</a></span></li></ul></div>

# # TP 1 - Programmation pour la préparation à l'agrégation maths option info
# 
# ## Remarques sur le style
# Ici, pour vous montrer, j'ai utilisé :
# - En Python 3, avec des annotations de types.
# - Notez que ce ne sont que des annotations.
# - Pour plus, il faudrait utiliser [quelque chose comme `beartype`](https://stackoverflow.com/a/37961120/2809027).
# 
# Notez que ce n'est absolument *pas nécessaire*, c'était juste pour montrer que ce genre d'annotations peut aider à passer de Caml à Python.

# # Fonctions

# ## Exercice 4

# In[65]:


def successeur(i : int) -> int:
    assert isinstance(i, int), "Erreur : i = {} doit etre entier.".format(i)
    assert i >= 0, "Erreur : i = {} doit etre >= 0.".format(i)
    return i + 1


# In[66]:


successeur(3)
successeur(2 * 2)
successeur(2.5)


# ## Exercice 5

# In[4]:


def produit3(x, y, z):
    return x * y * z

produit3_2 = lambda x, y, z: x * y * z

produit3_3 = lambda x: lambda y: lambda z: x * y * z


# In[5]:


produit3(1, 2, 3)
produit3_2(1, 2, 3)
produit3_3(1)(2)  # lambda z : 1 * 2 * z
f = produit3_3(1)(2)  # lambda z : 1 * 2 * z
f(3)
produit3_3(1)(2)(3)


# ## Exercice 6

# In[6]:


def exercice6(n : int) -> None:
    for i in range(1, n + 1):
        print(i)
    for i in range(n, 0, -1):
        print(i)


# In[7]:


exercice6(4)


# # Récursivité
# 
# C'est simple. Pas besoin d'un mot clé `rec` quand on définit une fonction récursive en Python.

# ## Exercice 7

# In[8]:


def factorielle(n : int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * factorielle(n - 1)


# In[10]:


for i in range(8):
    print("{}! = {:>5}".format(i, factorielle(i)))
    # Note : ce {:>5} signifie que l'affichage utilise au moins
    # 5 caractères, pour avoir un joli alignement :


# ## Exercice 8
# 
# Pour ce genre de fonction, j'aime bien afficher les appels récursifs. On peut rendre ça optionnel, avec comme ici un argument nommé `log`, à valeur par défaut `log=False`.

# In[73]:


def pgcd(x : int, y : int, log: bool=False) -> int:
    if log: print("x = {:>7}, y = {:>7}".format(x, y))
    assert x >= 0 and y >= 0
    if y == 1:
        return 1
    elif y == x or y == 0:
        return x
    if x < y:
        return pgcd(x, y % x, log=log)
    else:
        return pgcd(y, x % y, log=log)


# In[74]:


pgcd(2021, 4, log=True)


# In[75]:


pgcd(10, 5)


# On peut faire des essais pour afficher notre calcul de PGCD, sur des entiers aléatoires entre $1$ et $100$.
# 
# Pour se rassurer, on peut chercher dans la bibliothèque standard, à partir de Python 3.6 il y a la fonction `math.gcd` pour calculer le PGCD, sinon `fractions.gcd` ou encore dans le module (non standard) SymPy `sympy.gcd`.

# In[15]:


try:
    from math import gcd
except ImportError:
    try:
        from fractions import gcd
    except ImportError:
        from sympy import gcd


from random import randint
for _ in range(10):
    x = randint(1, 100)
    y = randint(1, 100)
    d = pgcd(x, y)
    print("{:>3} ^ {:>3} = {:>3}".format(x, y, d))
    assert d == gcd(x, y), "Erreur : mauvais calcul de pgcd(x={}, y={}) = {}, alors qu'il devrait etre = {}.".format(x, y, pgcd(x, y), gcd(x, y))


# ## Exercice 9
# 
# Rien de particulier à faire, la récursivité fonctionne sans réfléchir :

# In[3]:


def fibonacci(n : int) -> int:
    assert n >= 0
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Dans IPython (ou Jupyter) on peut facilement mesurer le temps (moyen) d'exécution d'une fonction sur une entrée donnée, avec la *macro* `%timeit`.

# In[18]:


get_ipython().run_line_magic('timeit', 'fibonacci(35)')


# Dans Python, on peut faire pareil avec `timeit()` du module `timeit`.
# 
# - avantage : on peut plus facilement récupérer le temps de calcul, et ensuite en faire des graphiques par exemple (e.g., afficher $T(f(n))$ en fonction de $n$ pour $n=10,100,...$),
# - inconvénients :
#     + il faut bien penser de passer l'argument optionnel `globals=globals()` (`globals()` donne un dictionnaire qui stocke la valeur de toutes les variables définies, donc ici notamment de `fibonacci()`)
#     + il faut penser à changer l'argument `number` qui par défaut vaut `1000000` : c'est très grand, et donc valable seulement pour estimer le temps de calculs très rapides, par exemple :

# In[9]:


get_ipython().run_line_magic('timeit', '2**35')
from timeit import timeit
timeit("2**35") / 1000000


# In[5]:


from timeit import timeit
number = 5
temps_calcul_fibo35 = timeit("fibonacci(35)", globals=globals(), number=number) / number
print("Pour calculer fibonacci(35), la fonction récursive naïve a pris {} secondes (moyenne sur {} essais)".format(temps_calcul_fibo35, number))


# ##### Fibonacci linéaire impérative
# Pour la version qui est en complexité (temporelle) linéaire dans l'entrée $n$, il suffit de déplier la récursion en calculant $F_{n+1}$ progressivement en partant de $F_0, F_1$.

# In[16]:


def fibonacci_lin(n : int) -> int:
    fim1, fi = 1, 1
    for _ in range(n):
        fim1, fi = fi, fim1 + fi
    return fim1


# On peut vérifier que cette deuxième implémentation fonctionne comme la première, et ensuite vérifier qu'elle est (bien) plus rapide.

# In[17]:


for i in range(10):
    assert fibonacci(i) == fibonacci_lin(i)


# In[18]:


get_ipython().run_line_magic('timeit', 'fibonacci_lin(35)')


# ##### Fibonacci linéaire récursive
# Pour la version qui est en complexité (temporelle) linéaire dans l'entrée $n$, il suffit de déplier la récursion en calculant $F_{n+1}$ progressivement en partant de $F_0, F_1$.

# In[12]:


def fibonacci_lin_rec(n: int) -> int:
    # invariant :
    #   m >= 1
    #   u = fibo(n-m+1)
    #   v = fibo(n-m)
    #   aux m u v = fibo(n)
    def aux(m: int, u: int, v: int) -> int:
        assert m >= 0
        if m <= 1:
            return u
        else:
            return aux(m-1, u+v, u)
    return aux(n, 1, 1)


# On peut vérifier que cette troisième implémentation fonctionne comme la première, et ensuite vérifier qu'elle est (bien) plus rapide.

# In[13]:


for i in range(10):
    assert fibonacci(i) == fibonacci_lin_rec(i)


# In[15]:


get_ipython().run_line_magic('timeit', 'fibonacci_lin_rec(35)')


# Voilà les différences :
# 
# - Les deux implémentations linéaires sont bien plus rapides que l'implémentation naïve (exponentielle), comme prévu !
# - L'implémentation linéaire impérative est plus rapide que l'implémentation linéaire fonctionnelle récursive, car elle n'a pas besoin de faire des appels de fonctions et de dépiler ensuite les appels de fonctions.

# ##### Un petit graphique : juste pour montrer ce que l'on peut faire rapidement

# In[19]:


import numpy as np
import matplotlib.pyplot as plt


# In[30]:


# optionnel : vous ne l'aurez pas le jour de l'oral, mais c'est joli
from tqdm.notebook import tqdm


# In[31]:


valeurs_n = np.array(range(1, 32))
number = 5


# In[32]:


get_ipython().run_cell_magic('time', '', 'temps_calcul_fibo_rec = [\n    timeit("fibonacci({})".format(n), globals=globals(), number=number) / number\n    for n in tqdm(valeurs_n)\n    # enrober un itérateur de la fonction tqdm(...)\n    # permet d\'avoir une joli barre de progression\n]')


# In[33]:


number = 100
temps_calcul_fibo_lin = [
    timeit("fibonacci_lin({})".format(n), globals=globals(), number=number) / number
    for n in tqdm(valeurs_n)
]
temps_calcul_fibo_lin_rec = [
    timeit("fibonacci_lin_rec({})".format(n), globals=globals(), number=number) / number
    for n in tqdm(valeurs_n)
]


# In[36]:


plt.figure(figsize=(14, 10))
plt.plot(valeurs_n, temps_calcul_fibo_rec, "ro-", label="Récursive naïve")
plt.plot(valeurs_n, temps_calcul_fibo_lin, "bd:", label="Linéaire impérative")
plt.plot(valeurs_n, temps_calcul_fibo_lin_rec, "ys:", label="Linéaire récursive")

plt.legend()
plt.title("Comparaison de trois implémentations de la fonction de Fibonacci")
plt.xlabel("Valeurs de n")
plt.ylabel("Temps moyen de calcul en secondes")
plt.show()


# In[39]:


get_ipython().run_cell_magic('time', '', 'valeurs_n = np.array(range(10, 1000, 10))\nnumber = 1000\ntemps_calcul_fibo_lin = [\n    timeit("fibonacci_lin({})".format(n), globals=globals(), number=number) / number\n    for n in tqdm(valeurs_n)\n]\ntemps_calcul_fibo_lin_rec = [\n    timeit("fibonacci_lin_rec({})".format(n), globals=globals(), number=number) / number\n    for n in tqdm(valeurs_n)\n]')


# In[40]:


plt.figure(figsize=(14, 10))
plt.plot(valeurs_n, temps_calcul_fibo_lin, "bd:", label="Linéaire impérative")
plt.plot(valeurs_n, temps_calcul_fibo_lin_rec, "ys:", label="Linéaire récursive")

plt.legend()
plt.title("Comparaison de deux implémentations de la fonction de Fibonacci")
plt.xlabel("Valeurs de n")
plt.ylabel("Temps moyen de calcul en secondes")
plt.show()


# ## Exercice 10
# 
# Aucune hypothèse n'est faite sur les arguments de la fonction, on supposera seulement qu'elle est itérable sur sa sortie.

# In[43]:


from types import FunctionType  # inutile, juste pour faire joli

# première version, f : type x -> type x (simple)
def itere(f : FunctionType, n : int) -> FunctionType:
    def fn(x):
        for _ in range(n):
            x = f(x)
        return x
    return fn


# In[44]:


itere(lambda x: x + 1, 10)(1)


# On peut aussi écrire une version récursive :

# In[45]:


def compose(f, g):
    return lambda x: f(g(x))
    """
    def f_rond_g(x):
        return f(g(x))
    return f_rond_g
    """


# In[48]:


def itere_rec(f : FunctionType, n : int) -> FunctionType:
    assert n >= 0
    if n == 0:
        return lambda x: x
    elif n == 1:
        return f
    else:
        return compose(f, itere_rec(f, n-1))
        return compose(itere_rec(f, n-1), f)


# In[49]:


itere_rec(lambda x: x + 1, 10)(1)


# In[50]:


get_ipython().run_line_magic('timeit', 'itere(lambda x: x + 1, 1000)(1)')
get_ipython().run_line_magic('timeit', 'itere_rec(lambda x: x + 1, 1000)(1)')


# In[119]:


# deuxième version, f : tuple -> tuple (simple)
def itere2(f : FunctionType, n : int) -> FunctionType:
    def fn(*args):
        for _ in range(n):
            if isinstance(args, tuple):
                args = f(*args)
            else:
                args = f(args)
        if isinstance(args, tuple) and len(args) == 1:
            return args[0]
        else:
            return args
    return fn


# In[132]:


def plusun(x):
    return x + 1

itere2(plusun, 10)(1)

def foisdeux(x, y):
    return x * 2, y * 2

itere2(foisdeux, 10)(1, 2)


# ## Exercice 11
# 
# C'est assez naturel, on affiche la suite de mouvement à faire, comme une suite de `"T1 -> T2"` par exemple.
# La fonction suivante affiche les déplacements qu'il faut faire pour déplacer une tour de hauteur `n` initialement posée en `x`, à destination de `z` et avec `y` comme position intermédiaire.
# 
# - le cas de base est pour une tour de hauteur 1 : un seul déplacement de `x` vers `z` suffit,
# - le cas récursif est très simple : pour une tour de hauteur `n`, il faut déplacer de `x` vers `y` le haut de la tour (de hauteur `n-1` : 1er appel récursif), puis déplacer le plus gros disque (en un mouvement) de `x` vers `z`, puis de nouveau déplacer le haut de la tour (toujours de hauteur `n-1` : 2nd appel récursif) de `y` vers `z`.

# In[144]:


def hanoi(x : str, y : str, z : str, n : int) -> None:
    def hanoiaux(orig : str, dest : str, inter : str, n : int):
        if n == 0:
            return 0
        c1 = hanoiaux(orig, inter, dest, n - 1)
        print("{} -> {}".format(orig, dest))
        c2 = hanoiaux(inter, dest, orig, n - 1)
        return c1 + 1 + c2
    return hanoiaux(x, z, y, n)


# In[145]:


hanoi("T1", "T2", "T3", 1)


# In[146]:


hanoi("T1", "T2", "T3", 2)


# In[148]:


hanoi("T1", "T2", "T3", 5)  # 31 = 2^5 - 1


# ----
# # Listes
# ## Exercice 12
# Les listes en Python sont des `list`.
# 
# Elles ne fonctionnent **pas** comme des listes simplement chaînées comme en Caml : ce sont des tableaux, donc l'accès à `T[i]` pour n'importe quel `i` est en $\mathcal{O}(1)$ pour n'importe quel `i` et `n`.
# 
# <span style="color: red;">MUST READ</span>
# Allez lire la page https://wiki.python.org/moin/TimeComplexity#list en détail !

# In[51]:


def concatene(liste1 : list, liste2 : list) -> list:
    """ O(len(liste1) + len(liste2))"""
    # return liste1 + liste2  # solution facile
    n1, n2 = len(liste1), len(liste2)
    res = []
    for i in range(n1 + n2):
        if i < n1:
            res.append(liste1[i])
        else:
            res.append(liste2[i - n1])
    return res


# In[153]:


concatene([1, 2, 3], [4, 5])


# ## Exercice 13

# In[56]:


from types import FunctionType

def applique(f : FunctionType, liste : list) -> list:
    res = [f(x) for x in liste]  # solution facile
    res = map(f, liste)  # encore plus facile
    # en itérant la liste :
    res = [ ]  # tableau vide
    for x in liste:
        res.append(f(x))
    # en itérant ses valeurs :
    res = [ ]  # tableau
    for i in range(len(liste)):
        res.append(f(liste[i]))
    return res


# In[164]:


applique(lambda x : x + 1, [1, 2, 3])


# ## Exercice 14

# In[165]:


def liste_carree(liste : list) -> list:
    return applique(lambda x: x**2, liste)


# In[167]:


liste_carree([1, 2, 3])


# ## Exercice 15

# In[180]:


def miroir_quad(liste : list) -> list:
    # aucune idée pour le faire innefficacement en Python,
    # ce ne sont pas des listes chaînées
    return liste[::-1]

def miroir_lin(liste : list) -> list:
    return [liste[-i] for i in range(1, len(liste) + 1)]


# In[181]:


miroir_lin([1, 2, 3])


# ## Exercice 16

# In[186]:


def insertion_dans_liste_triee(entiers : list, x : int) -> list:
    i = 0
    while i < len(entiers) and entiers[i] < x:
        i += 1
    return entiers[:i] + [x] + entiers[i:]


# In[187]:


insertion_dans_liste_triee([1, 2, 5, 6], 4)


# In[190]:


def tri_insertion(entiers : list) -> list:
    assert all([isinstance(i, int) for _ in entiers])
    def trix(e : list, acc : list) -> list:
        if len(e) == 0: return acc
        else: return trix(e[1:], insertion_dans_liste_triee(acc, e[0]))
    return trix(entiers, [])


# In[191]:


tri_insertion([5, 2, 6, 1, 4])


# ## Exercice 17

# In[193]:


def ordre_decroissant(x, y):
    return x > y


# In[195]:


from types import FunctionType

def insertion_dans_liste_triee2(entiers : list, x : int, ordre : FunctionType) -> list:
    i = 0
    while i < len(entiers) and ordre(entiers[i], x):
        i += 1
    return entiers[:i] + [x] + entiers[i:]


# In[196]:


insertion_dans_liste_triee2([6, 5, 2, 1], 4, ordre_decroissant)


# In[197]:


def tri_insertion2(entiers : list, ordre : FunctionType) -> list:
    assert all([isinstance(i, int) for _ in entiers])
    def trix(e : list, acc : list) -> list:
        if len(e) == 0: return acc
        else: return trix(e[1:], insertion_dans_liste_triee2(acc, e[0], ordre))
    return trix(entiers, [])


# In[200]:


tri_insertion([5, 2, 6, 1, 4])
tri_insertion2([5, 2, 6, 1, 4], ordre_decroissant)


# ----
# # Exponentiation rapide
# ## Exercice 18
# 
# Une approche naïve, de complexité temporelle linéaire en $n$ ($\mathcal{O}(n)$).

# In[76]:


def exp(x : int, n : int) -> int:
    res = 1
    for _ in range(n):
        res *= x
    return res


# In[80]:


x = 3
for n in range(8):
    print(x, "**", n, "=", exp(x, n), "et =", x**n)


# In[4]:


x = 3
for n in range(8):
    print("  {} ** {} = {:>5}".format(x, n, exp(x, n)))


# ## Exercice 19
# 
# Une approche maline (optimale, en fait).
# 
# Si n = 0 $x^0 = 1$
# 
# Si n est pair :
# $$ x^n = (x^{(n/2)})^2$$
# $$ x^n = (x*x)^{(n/2)}$$
# 
# Si n est impair :
# $$ x^n = x * (x^{((n-1)/2)})^2$$
# $$ x^n = x * (x*x)^{((n-1)/2)}$$
# 

# In[82]:


def exp2(x : int, n : int) -> int:
    assert n >= 0
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n % 2 == 0:
        # NE PAS FAIRE CA
         # return exp2(x, n // 2) * exp2(x, n // 2)
        return exp2(x * x, n // 2)
        return exp2(x, n // 2) ** 2
    elif n % 2 == 1:
        return exp2(x * x, (n - 1) // 2) * x


# In[83]:


x = 3
for n in range(8):
    print("  {} ** {} = {:>5}".format(x, n, exp2(x, n)))


# In[86]:


x = 3.1415
for n in range(8):
    print("  {} ** {} = {:>5} et x**n = {}".format(x, n, exp2(x, n), x**n))


# ## Exercice 20
# On ne dispose pas de typage pour faire ça aussi joliment qu'en Caml...

# In[6]:


def mult_float(x : float, y : float) -> float:
    return x * y

monoide_flottants = {
    'mult': mult_float,   # (*.) en Caml
    'neutre': 1.
}


# In[6]:


class Monoide_flottant():
    def __init__(self, x):
        self.x
        self.neutre = 1.0
    
    def mult(self, other_float):
        return self.x * other_float.x


# In[15]:


import numpy as np

def mult_ndarray(A : np.array, B : np.array) -> np.array:
    return np.dot(A, B)

# Pas possible d'avoir un neutre pour une taille quelconque !
monoide_nparray = lambda n, m: {
    'mult': mult_ndarray,
    'neutre': np.eye(n, m)
}


# In[16]:


mult_ndarray([[1, 1], [1, 1]], [[1, 2], [3, 4]])


# Manuellement ce n'est pas trop dur :

# In[31]:


def mult_mat(A : list, B : list) -> list:
    n, m = len(A), len(A[0])  # A est (n, m)
    m2, p = len(B), len(B[0]) # B est (m2, p)
    assert m == m2
    C = [[0 for _ in range(p)] for _ in range(n)]  # C est (n, p)
    for i in range(n):
        for j in range(p):
            for k in range(m):
                C[i][j] += A[i][k] * B[k][j]
    return C

# Pas possible d'avoir un neutre pour une taille quelconque !
monoide_mat = lambda n, m: {
    'mult': mult_mat,
    'neutre': [[int(i==j) for j in range(m)] for i in range(n)]  # I est (n, m)
}


# In[32]:


mult_mat([[1, 1], [1, 1]], [[1, 2], [3, 4]])


# ## Exercice 21

# In[87]:


def exp_rapide(monoide : dict, x, n : int):
    mult = monoide['mult']
    assert n >= 0
    if n == 0:
        return monoide['neutre']
    elif n == 1:
        return x
    elif n % 2 == 0:
        return exp_rapide(monoide, mult(x, x), n // 2)
    elif n % 2 == 1:
        return mult(exp_rapide(monoide, mult(x, x), (n - 1) // 2), x)


# ## Exercice 22

# In[34]:


def exp_rapide_float(x : float, n : int) -> float:
    return exp_rapide(monoide_flottants, x, n)


# In[35]:


exp_rapide_float(2.0, 8)


# In[36]:


exp_rapide_float(0.2, 8)


# Et pour les matrices, un petit piège à cause des tailles :

# In[37]:


def exp_rapide_mat(A : list, k : int) -> float:
    n, m = len(A), len(A[0])
    mono = monoide_mat(n, m)
    return exp_rapide(mono, A, k)


# In[38]:


for k in range(5):
    exp_rapide_mat([[1, 1], [1, 1]], k)


# In[42]:


for k in range(5):  # nilpotente
    exp_rapide_mat([[0, 1, 2], [0, 0, 1], [0, 0, 0]], k)


# ## Exercice 23
# 
# - On peut commencer par réécrire l'exponentiation rapide avec un `itere` :

# In[48]:


def exp_rapide_2(x, n : int):
    def mul_par_x(y):
        return x * y
    return itere(mul_par_x, n)(x)


# In[49]:


exp_rapide_2(2.0, 8)


# - Mais on demandait ici d'écrire `itere` avec l'exponentiation rapide :

# In[94]:


def mult_fonction(f : FunctionType, g : FunctionType) -> FunctionType:
    return lambda x: f(g(x))

monoide_fonction = {
    'mult': mult_fonction,
    'neutre': lambda x: x  # identité !
}


# In[95]:


def itere_depuis_monoide(f, n):
    return exp_rapide(monoide_fonction, f, n)


# In[99]:


print(itere_depuis_monoide(lambda x: x+1, 0)(1))  # 1
print(itere_depuis_monoide(lambda x: x+1, 10)(1)) # 11
print(itere_depuis_monoide(lambda x: x+1, 1000000)(1))  # pas de stack overflow car complexité O(log(n))


# A comparer avec l'implémentation naïve qui était en $\mathcal{O}(n)$ :

# In[101]:


print(itere(lambda x: x+1, 0)(1))  # 1
print(itere(lambda x: x+1, 10)(1)) # 11
print(itere(lambda x: x+1, 1000000)(1))  # stack overflow car complexité O(n)


# ----
# # Formule du calcul propositionnel
# 
# **Spoiler alert** : en Python, c'est chaud.
# 
# **ATTENTION** Il faut un peu d'habitude et d'idées pour réussir à faire tout ça aussi efficacement (enfin presque) qu'en OCaml.
# 
# On va faire des choses non typées, avec des dictionnaires, pour bidouiller.
# 
# ## Exercice 24

# ``(not p ^ ((q ^ not p) v (r v q)))`` s'écrit en Caml `` (Conj(Not(V("p")),Disj(Conj(V("q"),Not(V("p"))),Disj(V("r"),V("q")))))``.
# 
# On va imbriquer des dictionnaires, les types, `V`, `Not`, `Conj` et `Disj` seront des clés, et les valeurs seront des formules ou couples de formules.
# Mais on va cacher ça et l'utilisateur verra exactement la même chose qu'en Caml !

# In[57]:


V = lambda x: {'V': x}
Not = lambda x: {'Not': x}
Disj = lambda x, y: {'Disj': (x, y)}
Conj = lambda x, y: {'Conj': (x, y)}

p = V('p')
r = V('r')
q = V('q')
not_p = Not(p)

f = Conj(Not(p), Disj(Conj(q, not_p), Disj(r, q)))
f


# In[60]:


f2 = (Conj(Not(V("p")),Disj(Conj(V("q"),Not(V("p"))),Disj(V("r"),V("q")))))
f2


# Si on veut afficher plus joliment ce genre de structures récursives, la fonction `pprint.pprint(...)` est là pour ça (elle affiche avec de l'indentation) :

# In[59]:


from pprint import pprint


# In[61]:


pprint(f2)


# ## Exercice 25

# Ensuite on fait une filtration "à la main" sur les clés du dictionnaire (de niveau 1, on ne récurse pas quand on teste `'V' in formule`).

# In[62]:


def taille(formule : dict) -> int:
    if 'V' in formule:
        return 0
    elif 'Not' in formule:
        return 1 + taille(formule['Not'])
    elif 'Conj' in formule:
        x, y = formule['Conj']
        return 1 + taille(x) + taille(y)
    elif 'Disj' in formule:
        x, y = formule['Disj']
        return 1 + taille(x) + taille(y)


# In[63]:


taille(f)


# In[64]:


taille(f2)


# ## Exercice 26

# In[109]:


def formule_to_string(formule : dict) -> str:
    if 'V' in formule:
        return formule['V']
    elif 'Not' in formule:
        return "~" + formule_to_string(formule['Not'])
    elif 'Conj' in formule:
        x, y = formule['Conj']
        return "(" + formule_to_string(x) + " ^ " + formule_to_string(y) + ")"
    elif 'Disj' in formule:
        x, y = formule['Disj']
        return "(" + formule_to_string(x) + " V " + formule_to_string(y) + ")"


# In[110]:


def affiche(formule):
    print(formule_to_string(formule))


# In[111]:


affiche(f)


# Et voilà. Pas tellement plus dur hein !

# ## Exercice 27
# Les valeurs des variables seront données comme un dictionnaire associant nom de variable à valeurs booléennes.
# Et comme on veut frimer, on prend un [`defaultdict`](https://docs.python.org/3/library/collections.html#collections.defaultdict), qui est comme un `dict` mais qui stocke aussi une fonction qui donne la valeur des clés absentes du dictionnaire :

# In[104]:


from collections import defaultdict

d = defaultdict(lambda: False, {'p': True, 'q': False})
print(d['p'])  # -> True car présent et True
print(d['q'])  # -> False car présent et False
print(d['x'])  # -> False car absent
print(d['xokazeok'])  # -> False car absent


# In[113]:


valeurs_1 = defaultdict(lambda: False, {'p': True})


# In[114]:


valeurs_2 = defaultdict(lambda: False, {'r': True})


# In[89]:


def eval(valeurs : dict, formule : dict) -> bool:
    if 'V' in formule:
        return valeurs[formule['V']]
    elif 'Not' in formule:
        return not eval(valeurs, formule['Not'])
    elif 'Conj' in formule:
        x, y = formule['Conj']
        return eval(valeurs, x) and eval(valeurs, y)
    elif 'Disj' in formule:
        x, y = formule['Disj']
        return eval(valeurs, x) or eval(valeurs, y)


# In[90]:


eval(valeurs_1, f)


# In[91]:


eval(valeurs_2, f)


# ## Exercice 28

# In[93]:


def extrait_variables_x(formule : dict) -> list:
    if 'V' in formule:
        return [formule['V']]
    elif 'Not' in formule:
        return extrait_variables_x(formule['Not'])
    elif 'Conj' in formule:
        x, y = formule['Conj']
        return extrait_variables_x(x) + extrait_variables_x(y)
    elif 'Disj' in formule:
        x, y = formule['Disj']
        return extrait_variables_x(x) + extrait_variables_x(y)

# on enlève les doublons
def extrait_variables(formule : dict) -> list:
    return list(set(extrait_variables_x(formule)))


# In[94]:


extrait_variables(f)


# On trouve facilement les $n$ variables d'une formule.
# 
# Ensuite, un [`itertools.product`](https://docs.python.org/3/library/itertools.html#itertools.product) permet de générer les $2^n$ valuations.

# In[98]:


from itertools import product

def toutes_valeurs(variables):
    for valeurs in product([False, True], repeat=len(variables)):
        yield defaultdict(lambda: False, {k:v for k,v in zip(variables, valeurs)})


# In[103]:


list(toutes_valeurs(extrait_variables(f)))


# In[106]:


def str_of_bool(x : bool) -> str:
    # return str(int(x))
    return '1' if x else '0'


# In[116]:


def table_verite(formule : dict) -> None:
    variables = extrait_variables(formule)
    # D'abord la formule
    for k in variables:
        print(k, end=' ')
    print('| ', end='')
    affiche(f)
    # Puis toutes ces valeurs possibles
    for valeurs in toutes_valeurs(variables):
        for k in variables:
            print(str_of_bool(valeurs[k]), end=' ')
        print('| ', end='')
        print(str_of_bool(eval(valeurs, formule)))


# In[117]:


table_verite(f)


# Note : ce code est encore plus concis que celui donné dans la solution en Caml.
# 
# > On peut vérifier, par exemple sur [Wolfram|Alpha](https://www.wolframalpha.com/input/?i=%28%28not+p%29+and+%28%28q+and+%28not+p%29%29+or+%28r+or+q%29%29%29) que l'on obtient bien le bon résultat...

# ----
# 
# # Conclusion
# 
# Comme vous le voyez, on arrive à répondre aux mêmes questions dans les deux langages, et il n'y a pas de grosses différences en pratique dans la mise en oeuvre.
# 
# Là où OCaml excelle pour les types définis, le filtrage et la récursion, Python gagne en simplicité sur l'affichage, sa librairie standard et les dictionnaires et ensembles...
