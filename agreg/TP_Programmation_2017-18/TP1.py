
# coding: utf-8

# In[ ]:





# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#TP-1---Programmation-pour-la-préparation-à-l'agrégation-maths-option-info" data-toc-modified-id="TP-1---Programmation-pour-la-préparation-à-l'agrégation-maths-option-info-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>TP 1 - Programmation pour la préparation à l'agrégation maths option info</a></div><div class="lev1 toc-item"><a href="#Fonctions" data-toc-modified-id="Fonctions-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Fonctions</a></div><div class="lev2 toc-item"><a href="#Exercice-4" data-toc-modified-id="Exercice-4-21"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Exercice 4</a></div><div class="lev2 toc-item"><a href="#Exercice-5" data-toc-modified-id="Exercice-5-22"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Exercice 5</a></div><div class="lev2 toc-item"><a href="#Exercice-6" data-toc-modified-id="Exercice-6-23"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Exercice 6</a></div><div class="lev1 toc-item"><a href="#Récursivité" data-toc-modified-id="Récursivité-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Récursivité</a></div><div class="lev2 toc-item"><a href="#Exercice-7" data-toc-modified-id="Exercice-7-31"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Exercice 7</a></div><div class="lev2 toc-item"><a href="#Exercice-8" data-toc-modified-id="Exercice-8-32"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Exercice 8</a></div><div class="lev2 toc-item"><a href="#Exercice-9" data-toc-modified-id="Exercice-9-33"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>Exercice 9</a></div><div class="lev2 toc-item"><a href="#Exercice-10" data-toc-modified-id="Exercice-10-34"><span class="toc-item-num">3.4&nbsp;&nbsp;</span>Exercice 10</a></div><div class="lev2 toc-item"><a href="#Exercice-11" data-toc-modified-id="Exercice-11-35"><span class="toc-item-num">3.5&nbsp;&nbsp;</span>Exercice 11</a></div><div class="lev1 toc-item"><a href="#Listes" data-toc-modified-id="Listes-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Listes</a></div><div class="lev2 toc-item"><a href="#Exercice-12" data-toc-modified-id="Exercice-12-41"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Exercice 12</a></div><div class="lev2 toc-item"><a href="#Exercice-13" data-toc-modified-id="Exercice-13-42"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>Exercice 13</a></div><div class="lev2 toc-item"><a href="#Exercice-14" data-toc-modified-id="Exercice-14-43"><span class="toc-item-num">4.3&nbsp;&nbsp;</span>Exercice 14</a></div><div class="lev2 toc-item"><a href="#Exercice-15" data-toc-modified-id="Exercice-15-44"><span class="toc-item-num">4.4&nbsp;&nbsp;</span>Exercice 15</a></div><div class="lev2 toc-item"><a href="#Exercice-16" data-toc-modified-id="Exercice-16-45"><span class="toc-item-num">4.5&nbsp;&nbsp;</span>Exercice 16</a></div><div class="lev2 toc-item"><a href="#Exercice-17" data-toc-modified-id="Exercice-17-46"><span class="toc-item-num">4.6&nbsp;&nbsp;</span>Exercice 17</a></div><div class="lev1 toc-item"><a href="#Exponentiation-rapide" data-toc-modified-id="Exponentiation-rapide-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Exponentiation rapide</a></div><div class="lev2 toc-item"><a href="#Exercice-18" data-toc-modified-id="Exercice-18-51"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>Exercice 18</a></div><div class="lev2 toc-item"><a href="#Exercice-19" data-toc-modified-id="Exercice-19-52"><span class="toc-item-num">5.2&nbsp;&nbsp;</span>Exercice 19</a></div><div class="lev2 toc-item"><a href="#Exercice-20" data-toc-modified-id="Exercice-20-53"><span class="toc-item-num">5.3&nbsp;&nbsp;</span>Exercice 20</a></div><div class="lev2 toc-item"><a href="#Exercice-21" data-toc-modified-id="Exercice-21-54"><span class="toc-item-num">5.4&nbsp;&nbsp;</span>Exercice 21</a></div><div class="lev2 toc-item"><a href="#Exercice-22" data-toc-modified-id="Exercice-22-55"><span class="toc-item-num">5.5&nbsp;&nbsp;</span>Exercice 22</a></div><div class="lev2 toc-item"><a href="#Exercice-23" data-toc-modified-id="Exercice-23-56"><span class="toc-item-num">5.6&nbsp;&nbsp;</span>Exercice 23</a></div><div class="lev1 toc-item"><a href="#Formule-du-calcul-propositionnel" data-toc-modified-id="Formule-du-calcul-propositionnel-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Formule du calcul propositionnel</a></div><div class="lev2 toc-item"><a href="#Exercice-24" data-toc-modified-id="Exercice-24-61"><span class="toc-item-num">6.1&nbsp;&nbsp;</span>Exercice 24</a></div><div class="lev2 toc-item"><a href="#Exercice-25" data-toc-modified-id="Exercice-25-62"><span class="toc-item-num">6.2&nbsp;&nbsp;</span>Exercice 25</a></div><div class="lev2 toc-item"><a href="#Exercice-26" data-toc-modified-id="Exercice-26-63"><span class="toc-item-num">6.3&nbsp;&nbsp;</span>Exercice 26</a></div><div class="lev2 toc-item"><a href="#Exercice-27" data-toc-modified-id="Exercice-27-64"><span class="toc-item-num">6.4&nbsp;&nbsp;</span>Exercice 27</a></div><div class="lev2 toc-item"><a href="#Exercice-28" data-toc-modified-id="Exercice-28-65"><span class="toc-item-num">6.5&nbsp;&nbsp;</span>Exercice 28</a></div><div class="lev1 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Conclusion</a></div>

# # TP 1 - Programmation pour la préparation à l'agrégation maths option info
# - En Python 3, avec des annotations de types.
# - Notez que ce ne sont que des annotations.
# - Pour plus, il faudrait utiliser [quelque chose comme `beartype`](https://stackoverflow.com/a/37961120/2809027).

# # Fonctions

# ## Exercice 4

# In[17]:


def successeur(i : int) -> int:
    assert isinstance(i, int)
    assert i >= 0
    return i + 1


# In[4]:


successeur(3)
successeur(2 * 2)
successeur(2.5)


# ## Exercice 5

# In[9]:


def produit3(x, y, z):
    return x * y * z

produit3_2 = lambda x, y, z: x * y * z

produit3_3 = lambda x: lambda y: lambda z: x * y * z


# In[12]:


produit3(1, 2, 3)
produit3_2(1, 2, 3)
produit3_3(1)(2)  # lambda z : 1 * 2 * z
produit3_3(1)(2)(3)


# ## Exercice 6

# In[18]:


def exercice6(n : int) -> None:
    for i in range(1, n + 1):
        print(i)
    for i in range(n, 0, -1):
        print(i)


# In[19]:


exercice6(4)


# # Récursivité

# ## Exercice 7

# In[20]:


def factorielle(n : int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * factorielle(n - 1)


# In[25]:


for i in range(8):
    print("{}! = {:>5}".format(i, factorielle(i)))


# ## Exercice 8

# In[66]:


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


# In[67]:


pgcd(10, 5)


# In[71]:


from sympy import gcd
from random import randint
for _ in range(10):
    x = randint(1, 100)
    y = randint(1, 100)
    d = pgcd(x, y)
    print("{:>2} ^ {:>2} = {:>2}".format(x, y, d))
    assert d == gcd(x, y)


# ## Exercice 9

# In[72]:


def fibonacci(n : int) -> int:
    assert n >= 0
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# In[76]:


get_ipython().magic('timeit fibonacci(35)')


# In[77]:


def fibonacci_lin(n : int) -> int:
    un, uns = 1, 1
    for _ in range(n):
        un, uns = uns, un + uns
    return un


# In[79]:


for i in range(10):
    assert fibonacci(i) == fibonacci_lin(i)


# In[80]:


get_ipython().magic('timeit fibonacci_lin(35)')


# Voilà la différence.

# ## Exercice 10
# 
# Aucune hypothèse n'est faite sur les arguments de la fonction, on supposera seulement qu'elle est itérable sur sa sortie.

# In[44]:


from types import FunctionType

# première version, f : type x -> type x (simple)
def itere(f : FunctionType, n : int) -> FunctionType:
    def fn(x):
        for _ in range(n):
            x = f(x)
        return x
    return fn


# In[45]:


itere(lambda x: x + 1, 10)(1)


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
# Elles ne fonctionnent **pas** comme des listes simplement chaînées comme en Caml.

# In[152]:


def concatene(liste1 : list, liste2 : list) -> list:
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

# In[163]:


from types import FunctionType

def applique(f : FunctionType, liste : list) -> list:
    res = [f(x) for x in liste]  # solution facile
    res = map(f, liste)  # encore plus facile
    # en itérant la liste :
    res = []
    for x in liste:
        res.append(f(x))
    # en itérant ses valeurs :
    res = []
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

# In[3]:


def exp(x : int, n : int) -> int:
    res = 1
    for _ in range(n):
        res *= x
    return res


# In[4]:


x = 3
for n in range(8):
    print("  {} ** {} = {:>5}".format(x, n, exp(x, n)))


# ## Exercice 19

# In[201]:


def exp2(x : int, n : int) -> int:
    assert n >= 0
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n % 2 == 0:
        return exp2(x ** 2, n // 2)
    elif n % 2 == 1:
        return exp2(x ** 2, (n - 1) // 2) * x


# In[205]:


x = 3
for n in range(8):
    print("  {} ** {} = {:>5}".format(x, n, exp2(x, n)))


# ## Exercice 20
# On ne dispose pas de typage pour faire ça aussi joliment qu'en Caml...

# In[6]:


def mult_float(x : float, y : float) -> float:
    return x * y

monoide_flottants = {
    'mult': mult_float,   # (*.) en Caml
    'neutre': 1.
}


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

# In[33]:


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

# In[48]:


from operator import mul

def exp_rapide_2(x, n : int):
    def mul_par_x(y):
        return x * y
    return itere(mul_par_x, n)(x)


# In[49]:


exp_rapide_2(2.0, 8)


# ----
# # Formule du calcul propositionnel
# 
# *Spoiler alert* : en Python, c'est chaud.
# 
# On va faire des choses non typées, avec des dictionnaires, pour bidouiller.
# 
# ## Exercice 24

# ``(not p ^ ((q ^ not p) v (r v q)))`` s'écrit en Caml `` (Conj(Not(V("p")),Disj(Conj(V("q"),Not(V("p"))),Disj(V("r"),V("q")))))``.
# 
# On va imbriquer des dictionnaires, les types, `V`, `Not`, `Conj` et `Disj` seront des clés, et les valeurs seront des formules ou couples de formules.
# Mais on va cacher ça et l'utilisateur verra exactement la même chose qu'en Caml !

# In[63]:


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


# In[59]:


(Conj(Not(V("p")),Disj(Conj(V("q"),Not(V("p"))),Disj(V("r"),V("q")))))


# ## Exercice 25

# Ensuite on fait une filtration "à la main" sur les clés du dictionnaire (de niveau 1, on ne récurse pas quand on teste `'V' in formule`).

# In[79]:


def taille(formule : dict) -> str:
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


# In[69]:


taille(f)


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


# Et voilà. Pas tellement plus dire hein !

# ## Exercice 27
# Les valeurs des variables seront données comme un dictionnaire associant nom de variable à valeurs booléennes.
# Et comme on veut frimer, on prend un [`defaultdict`](https://docs.python.org/3/library/collections.html#collections.defaultdict).

# In[115]:


from collections import defaultdict

d = defaultdict(lambda: False, {'p': True, 'q': False})
d['p']  # -> True car présent et True
d['q']  # -> False car présent et False
d['x']  # -> False car absent


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
# > On peut vérifier, par exemple sur [Wolfram|Alpha](https%3A%2F%2Fwww.wolframalpha.com%2Finput%2F%3Fi%3D%28%7Ep%2B%2526%2B%28%28q%2B%2526%2B%7Ep%29%2B%257C%2B%28r%2B%257C%2Bq%29%29%29) que l'on obtient bien le bon résultat...

# ----
# 
# # Conclusion
# 
# Comme vous le voyez, on arrive à répondre aux mêmes questions dans les deux langages, et il n'y a pas de grosses différences en pratique dans la mise en oeuvre.
# 
# Là où Caml excelle pour les types définis, le filtrage et la récursion, Python gagne en simplicité sur l'affichage, sa librairie standard et les dictionnaires et ensembles...
