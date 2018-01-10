
# coding: utf-8

# # Des dates qui font des nombres premiers (suite) ?
# 
# Ce petit [notebook Jupyter](https://www.jupyter.org/), écrit en [Python](https://www.python.org/), a pour but de résoudre la question suivante :
# 
# > *"Pour un jour fixé, en utilisant le jour le mois et les deux chiffres de l'année comme briques de base, et les opérations arithmétiques $+,\times,-,\mod,\%$, quel est le plus grand nombre premier que l'on peut obtenir ?"*
# 
# Par exemple, en 2017, le 31 mai donne `31`, `5`, et `17`.
# 
# - $31 \times 5 \times 17$ n'est évidemment pas premier,
# - $17 \times (31 \mod 5) = 17$ est premier.
# 
# > Pour d'autres questions sur les dates et les nombres premiers, [ce premier notebook est aussi intéressant !](https://nbviewer.jupyter.org/github/Naereen/notebooks/blob/master/simus/Des_dates_qui_font_des_nombres_premiers.ipynb).

# ----
# ## Une première solution, naïve
# - On va d'abord écrire (ou importer) une fonction pour tester si un entier est premier,
# - Puis on va écrire une fonction qui transforme une date en ses trois nombres,
# - Et une fonction qui essaie toutes les opérations possibles sur les trois nombres,
# - Et enfin une boucle sur les 365 (ou 366) jours de l'année suffira à afficher, pour chaque jour, le plus grand nombre premier obtenu.

# ### Tester la primalité, version tricheur
# [`sympy`](http://www.sympy.org/) propose une fonction [`sympy.isprime`](http://docs.sympy.org/latest/modules/ntheory.html#sympy.ntheory.primetest.isprime).

# In[3]:


from sympy import isprime


# Elle marche très bien, et est très rapide !

# In[4]:


[isprime(i) for i in [2, 3, 5, 7, 10, 11, 13, 17, 2017]]


# Pour des nombres de 8 chiffres (c'est tout petit), elle est vraiment rapide :

# In[5]:


from numpy.random import randint
get_ipython().run_line_magic('timeit', 'sum([isprime(i) for i in randint(1e8, 1e9-1, 10**4)])')


# $\implies$ $65 ~\text{ms}$ pour 10000 nombres à tester, ça me semble assez rapide pour ce qu'on veut en faire !

# ----
# ### Transformer une date en nombre
# On va utiliser le module [`datetime`](https://docs.python.org/3/library/datetime.html) de la bibliothèque standard :

# In[6]:


from datetime import datetime


# In[7]:


today = datetime.today()
YEAR = today.year
print("On va travailler avec l'année", YEAR, "!")


# C'est ensuite facile de transformer une date en nombre, selon les deux formats.
# On utilise [le formatage avec `.format()`](https://pyformat.info/#datetime) (en Python 3) :

# In[46]:


def date_vers_nombre(date):
    day = int("{:%d}".format(date))
    month = int("{:%m}".format(date))
    year = int("{:%Y}".format(date)[-2:])
    return day, month, year


# In[63]:


date = datetime(YEAR, 1, 12)
print(date_vers_nombre(date))


# ### Tester toutes les opérations possibles
# - On utilise la fonction [`itertools.permutations`](https://docs.python.org/3/library/itertools.html#itertools.permutation) pour obtenir les permutations des trois nombres $x,y,z$,
# - On applique les opérations dans l'ordre $f_1(f_2(x, y), z)$ et $f_1(x, f_2(y, z))$, ce qui suffit à couvrir tous les cas.
# - On utilise le module [`operator`](https://docs.python.org/3/library/operator.html) pour avoir des fonctions pour les opérations autorisées.

# In[68]:


from itertools import permutations
from operator import mod, mul, add, pow, sub, floordiv

operations = [mod, mul, add, sub, floordiv]


# In[69]:


def tous_les_resultats(nombres, ops=operations):
    assert len(nombres) == 3
    tous = []
    for (x, y, z) in permutations(nombres):
        # on a un ordre pour x, y, z
        for f1 in ops:
            for f2 in ops:
                tous.append(f1(f2(x, y), z))
                tous.append(f1(x, f2(y, z)))
    # on enlève les doublons ici
    return list(set(tous))


# On peut la vérifier sur de petites entrées :

# In[70]:


tous_les_resultats([1, 2, 3], [add])
tous_les_resultats([1, 2, 3], [add, mul])


# On voit que stocker juste l'entier résultat ne suffit pas, on aimerait garder trace de chaque façon de l'obtenir !

# In[71]:


noms_operations = {
    mod: '%',
    mul: '*',
    add: '+',
    sub: '-',
    floordiv: '/',
}


# In[72]:


def tous_les_resultats_2(nombres, ops=operations):
    assert len(nombres) == 3
    tous = {}
    for (x, y, z) in permutations(nombres):
        # on a un ordre pour x, y, z
        for f1 in ops:
            for f2 in ops:
                n1 = f1(f2(x, y), z)
                s1 = "{}({}({}, {}), {})".format(noms_operations[f1], noms_operations[f2], x, y, z)
                tous[s1] = n1
                n2 = f1(x, f2(y, z))
                s2 = "{}({}, {}({}, {}))".format(noms_operations[f1], x, noms_operations[f2], y, z)
                tous[s2] = n2
    return tous


# In[73]:


tous_les_resultats_2([1, 2, 3], [add])
tous_les_resultats_2([1, 2, 3], [add, mul])


# Si on stocke avec comme clés les expressions, on va en avoir BEAUCOUP.
# Faisons l'inverse, avec le résultat de l'expression comme clés.

# In[74]:


def tous_les_resultats_3(nombres, ops=operations):
    assert len(nombres) == 3
    tous = {}
    for (x, y, z) in permutations(nombres):
        # on a un ordre pour x, y, z
        for f1 in ops:
            for f2 in ops:
                n1 = f1(f2(x, y), z)
                s1 = "{}({}({}, {}), {})".format(noms_operations[f1], noms_operations[f2], x, y, z)
                tous[n1] = s1
                n2 = f1(x, f2(y, z))
                s2 = "{}({}, {}({}, {}))".format(noms_operations[f1], x, noms_operations[f2], y, z)
                tous[n2] = s2
    return tous


# In[75]:


tous_les_resultats_3([1, 2, 3], [add])
tous_les_resultats_3([1, 2, 3], [add, mul])


# Beaucoup plus raisonnable ! Ici, pour le 2ème exemple, le plus grand nombre premier obtenu est $7 = (3 \times 2) + 1$.

# In[76]:


def plus_grand_premier(nombres, ops=operations):
    tous = tous_les_resultats_3(nombres, ops=ops)
    premiers = [ p for p in tous.keys() if isprime(p) ]
    plus_grand_premier = max(premiers)
    expression = tous[plus_grand_premier]
    return plus_grand_premier, expression


# In[77]:


plus_grand_premier([1, 2, 3], [add, mul])


# In[78]:


plus_grand_premier([1, 2, 3])


# Il faut ignorer les erreurs de calculs et ne pas ajouter le nombre dans ce cas:

# In[84]:


def tous_les_resultats_4(nombres, ops=operations):
    assert len(nombres) == 3
    tous = {}
    for (x, y, z) in permutations(nombres):
        # on a un ordre pour x, y, z
        for f1 in ops:
            for f2 in ops:
                try:
                    n1 = f1(f2(x, y), z)
                    s1 = "{}({}({}, {}), {})".format(noms_operations[f1], noms_operations[f2], x, y, z)
                    tous[n1] = s1
                except:
                    pass
                try:
                    n2 = f1(x, f2(y, z))
                    s2 = "{}({}, {}({}, {}))".format(noms_operations[f1], x, noms_operations[f2], y, z)
                    tous[n2] = s2
                except:
                    pass
    return tous


# In[85]:


def plus_grand_premier_2(nombres, ops=operations):
    tous = tous_les_resultats_4(nombres, ops=ops)
    premiers = [ p for p in tous.keys() if isprime(p) ]
    plus_grand_premier = max(premiers)
    expression = tous[plus_grand_premier]
    return plus_grand_premier, expression


# In[86]:


plus_grand_premier_2([1, 2, 3], [add, mul])


# In[88]:


plus_grand_premier_2([1, 2, 3])


# In[89]:


plus_grand_premier_2([12, 1, 93])


# ### Tester sur un jour

# In[90]:


date
x, y, z = date_vers_nombre(date)
plus_grand_premier_2([x, y, z])


# ### Tester tous les jours de l'année

# On peut partir du 1er janvier de cette année, et ajouter des jours un par un.
# On utilise un itérateur (avec le mot clé `yield`), pour pouvoir facilement boucler sur tous les jours de l'année en cours :

# In[91]:


from datetime import timedelta

def tous_les_jours(year=YEAR):
    date = datetime(year, 1, 1)
    un_jour = timedelta(days=1)
    for i in range(0, 366):
        yield date
        date += un_jour
        if date.year > year:  # On est allé trop loin
            raise StopIteration


# In[92]:


tous = []
for date in tous_les_jours():
    x, y, z = date_vers_nombre(date)
    p, expr = plus_grand_premier_2([x, y, z])
    tous.append(([x, y, z], p, expr))
    print("Pour la date {:%d-%m-%Y}, le plus grand nombre premier obtenu est {}, avec l'expression {}.".format(date, p, expr))


# In[94]:


max(tous, key=lambda t: t[1])


# Le plus grand nombre premier est donc pour le 30 novembre 2017, 521 obtenu avec $(17 \times 30) + 11$.

# ----
# ## Conclusions
# - C'était bien inutile.
# - Mais marrant.

# > C'est tout pour aujourd'hui les amis, [allez voir d'autres notebooks si vous êtes curieux !](https://github.com/Naereen/notebooks/).
# 
# > [See this repository for other Python notebook doing numerical simulations](https://github.com/Naereen/notebooks/tree/master/simus/).
