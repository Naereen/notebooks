#!/usr/bin/env python
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#Oraux-CentraleSupélec-PSI---Juin-2019" data-toc-modified-id="Oraux-CentraleSupélec-PSI---Juin-2019-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Oraux CentraleSupélec PSI - Juin 2019</a></div><div class="lev2 toc-item"><a href="#Remarques-préliminaires" data-toc-modified-id="Remarques-préliminaires-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Remarques préliminaires</a></div><div class="lev3 toc-item"><a href="#Importez-les-modules-:" data-toc-modified-id="Importez-les-modules-:-111"><span class="toc-item-num">1.1.1&nbsp;&nbsp;</span>Importez les modules :</a></div><div class="lev2 toc-item"><a href="#Planche-160" data-toc-modified-id="Planche-160-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Planche 160</a></div><div class="lev2 toc-item"><a href="#Planche-162" data-toc-modified-id="Planche-162-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Planche 162</a></div><div class="lev2 toc-item"><a href="#Planche-166" data-toc-modified-id="Planche-166-14"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Planche 166</a></div><div class="lev2 toc-item"><a href="#Planche-168" data-toc-modified-id="Planche-168-15"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Planche 168</a></div><div class="lev2 toc-item"><a href="#Planche-170" data-toc-modified-id="Planche-170-16"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Planche 170</a></div><div class="lev2 toc-item"><a href="#Planche-172" data-toc-modified-id="Planche-172-17"><span class="toc-item-num">1.7&nbsp;&nbsp;</span>Planche 172</a></div><div class="lev2 toc-item"><a href="#Planche-177" data-toc-modified-id="Planche-177-18"><span class="toc-item-num">1.8&nbsp;&nbsp;</span>Planche 177</a></div><div class="lev1 toc-item"><a href="#À-voir-aussi" data-toc-modified-id="À-voir-aussi-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>À voir aussi</a></div><div class="lev2 toc-item"><a href="#Les-oraux---(exercices-de-maths-avec-Python)" data-toc-modified-id="Les-oraux---(exercices-de-maths-avec-Python)-21"><span class="toc-item-num">2.1&nbsp;&nbsp;</span><a href="http://perso.crans.org/besson/infoMP/oraux/solutions/" target="_blank">Les oraux</a>   <em>(exercices de maths avec Python)</em></a></div><div class="lev2 toc-item"><a href="#Fiches-de-révisions-pour-les-oraux" data-toc-modified-id="Fiches-de-révisions-pour-les-oraux-22"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Fiches de révisions <em>pour les oraux</em></a></div><div class="lev2 toc-item"><a href="#D'autres-notebooks-?" data-toc-modified-id="D'autres-notebooks-?-23"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>D'autres notebooks ?</a></div>

# # Oraux CentraleSupélec PSI - Juin 2019
# 
# - Ce [notebook Jupyter](https://www.jupyter.org) est une proposition de correction, en [Python 3](https://www.python.org/), d'exercices d'annales de l'épreuve "maths-info" du [concours CentraleSupélec](http://www.concours-centrale-supelec.fr/), filière PSI.
# - Les exercices viennent de l'[Officiel de la Taupe](http://odlt.fr/), [2017](http://www.odlt.fr/Oraux_2017.pdf) (planches 162 à 177, pages 10 et 11).
# - Ce document a été écrit par [Lilian Besson](http://perso.crans.org/besson/), et est disponible en ligne [sur mon site](https://perso.crans.org/besson/publis/notebooks/Oraux_CentraleSupelec_PSI__Juin_2019.html).

# ## Remarques préliminaires
# - Les exercices sans Python ne sont pas traités.
# - Les exercices avec Python utilisent Python 3, [numpy](http://numpy.org), [matplotlib](http://matplotlib.org), [scipy](http://scipy.org) et [sympy](http://sympy.org), et essaient d'être résolus le plus simplement et le plus rapidement possible. L'efficacité (algorithmique, en terme de mémoire et de temps de calcul), n'est *pas* une priorité. La concision et simplicité de la solution proposée est prioritaire.

# In[1]:


import numpy as np
import matplotlib as mpl
mpl.rcParams['figure.figsize'] = (10, 7)
import matplotlib.pyplot as plt
from scipy import integrate
import numpy.random as rd


# In[16]:


import seaborn as sns
sns.set(context="notebook", style="whitegrid", palette="hls", font="sans-serif", font_scale=1.1)


# ### Importez les modules :

# In[ ]:


import numpy as np


# In[ ]:


import matplotlib.pyplot as plt


# In[ ]:


from scipy import integrate


# In[ ]:


import numpy.random as rd


# ----
# ## Planche 160

# - $I_n := \int_0^1 \frac{1}{(1+t)^n \sqrt{1-t}} \mathrm{d}t$ et $I_n := \int_0^1 \frac{1/2}{(1+t)^n \sqrt{1-t}} \mathrm{d}t$ sont définies pour tout $n$ car leur intégrande est continue et bien définie sur $]0,1[$ et intégrable en $1$ parce qu'on sait (par intégrale de Riemann) que $\frac{1}{\sqrt{u}}$ est intégrable en $0^+$ (et changement de variable $u = 1-t$).
# - On les calcule très simplement :

# In[2]:


def I(n):
    def f(t):
        return 1 / ((1+t)**n * np.sqrt(1-t))
    i, err = integrate.quad(f, 0, 1)
    return i


# In[3]:


def J(n):
    def f(t):
        return 1 / ((1+t)**n * np.sqrt(1-t))
    i, err = integrate.quad(f, 0, 0.5)
    return i


# In[4]:


valeurs_n = np.arange(1, 50)
valeurs_In = np.array([I(n) for n in valeurs_n])

plt.figure()
plt.plot(valeurs_n, valeurs_In, 'ro')
plt.title("Valeurs de $I_n$")
plt.show()


# - On conjecture que $I_n$ est décroissante. C'est évident puisque si on note $f_n(t)$ son intégrande, on observe que $f_{n+1}(t) \leq f_n(t)$ pour tout $t$, et donc par monotonie de l'intégrale, $I_{n+1} \leq I_n$.
# - On conjecture que $I_n \to 0$. Cela se montre très facilement avec le théorème de convergence dominée.

# In[5]:


plt.figure()
plt.plot(np.log(valeurs_n), np.log(valeurs_In), 'go')
plt.title(r"Valeurs de $\ln(I_n)$ en fonction de $\ln(n)$")
plt.show()


# - Ce qu'on observe permet de conjecturer que $\alpha=1$ est l'unique entier tel que $n^{\alpha} I_n$ converge vers une limite non nulle.

# In[16]:


valeurs_n = np.arange(1, 500)
valeurs_In = np.array([I(n) for n in valeurs_n])
valeurs_Jn = np.array([J(n) for n in valeurs_n])
alpha = 0.9

plt.figure()
plt.plot(valeurs_n, valeurs_n**alpha * valeurs_In, 'r+', label=r'$n^{\alpha} I_n$')
plt.plot(valeurs_n, valeurs_n**alpha * valeurs_Jn, 'b+', label=r'$n^{\alpha} J_n$')
plt.legend()
plt.title(r"Valeurs de $n^{\alpha} I_n$ et $n^{\alpha} J_n$")
plt.show()


# - On en déduit qu'il en est de même pour $J_n$, on a $n^{\alpha} J_n \to l$ la même limite que $n^{\alpha} I_n$.

# - Pour finir, on montre mathématiquement que $n^{\alpha} (I_n - J_n)$ tend vers $0$.

# In[22]:


plt.figure()
plt.plot(valeurs_n, valeurs_n**alpha * (valeurs_In - valeurs_Jn), 'g+', label=r'$n^{\alpha} (I_n - J_n)$')
plt.legend()
plt.title(r"Valeurs de $n^{\alpha} (I_n - J_n)$")
plt.show()


# - Puis rapidement, on montre que $\forall x \geq 0, \ln(1 + x) \geq \frac{x}{1+x}$. Ca peut se prouver de plein de façons différentes, mais par exemple on écrit $f(x) = (x+1) \log(x+1) - x$ qui est de classe $\mathcal{C}^1$, et on la dérive. $f'(x) = \log(x+1) + 1 - 1 > 0$ donc $f$ est croissante, et $f(0) = 0$ donc $f(x) \geq f(0) = 0$ pour tout $x \geq 0$.

# In[26]:


X = np.linspace(0, 100, 1000)
plt.plot(X, np.log(1 + X), 'ro-', label=r'$\log(1+x)$', markevery=50)
plt.plot(X, X / (1 + X), 'b+-', label=r'$\frac{x}{1+x}$', markevery=50)
plt.legend()
plt.title("Comparaison entre deux fonctions")
plt.show()


# ---
# ## Planche 162

# On commence par définir la fonction, en utilisant `numpy.cos` et pas `math.cos` (les fonctions de `numpy` peuvent travailler sur des tableaux, c'est plus pratique).

# In[27]:


def f(x):
    return x * (1 - x) * (1 + np.cos(5 * np.pi * x))

Xs = np.linspace(0, 1, 2000)
Ys = f(Xs)


# Pas besoin de lire le maximum sur un graphique :

# In[29]:


M = max_de_f = max(Ys)
print("Sur [0, 1], avec 2000 points, le maximum de f(x) est M =", M)


# In[32]:


i_maximisant_f = np.argmax(Ys)
x_maximisant_f = Xs[i_maximisant_f]
print("Sur ces 2000 points, le maximum est atteint en x =", x_maximisant_f)


# On affiche la fonction, comme demandé, avec un titre :

# In[39]:


plt.figure()
plt.plot(Xs, Ys)
plt.vlines(x_maximisant_f, min(Ys), max(Ys), color="b", linestyles="dotted")
plt.hlines(max(Ys), min(Xs), max(Xs), color="b", linestyles="dotted")
plt.title("Fonction $f(x)$ sur $[0,1]$")
plt.show()


# Pour calculer l'intégrale, on utilise `scipy.integrate.quad` :

# In[40]:


def In(x, n):
    def fn(x):
        return f(x) ** n
    return integrate.quad(fn, 0, 1)[0]

def Sn(x):
    return np.sum([In(Xs, n) * x**n for n in range(0, n+1)], axis=0)


# On vérifie avant de se lancer dans l'affichage :

# In[41]:


for n in range(10):
    print("In(x,", n, ") =", In(Xs, n))


# In[45]:


a = 1/M + 0.1
X2s = np.linspace(-a, a, 2000)

plt.figure()
for n in [10, 20, 30, 40, 50]:
    plt.plot(X2s, Sn(X2s), "-+", label="n =" + str(n), markevery=20)
plt.legend()
plt.show()


# $S_n(x)$ semble diverger pour $x\to2^-$ quand $n\to\infty$.
# Le rayon de convergence de la série $\sum In x^n$ **semble** être $2$.

# In[46]:


def un(n):
    return In(Xs, n + 1) / In(Xs, n)


# In[47]:


for n in range(10):
    print("un =", un(n), "pour n =", n)


# Ici, `un` ne peut pas être utilisé comme une fonction "numpy" qui travaille sur un tableau, on stocke donc les valeurs "plus manuellement" :

# In[50]:


def affiche_termes_un(N):
    valeurs_un = [0] * N
    for n in range(N):
        valeurs_un[n] = un(n)

    plt.figure()
    plt.plot(valeurs_un, 'o-')
    plt.title("Suite $u_n$")
    plt.grid(True)
    plt.show()


# In[51]:


affiche_termes_un(30)


# La suite $u_n$ semble être croissante (on peut le prouver), toujours plus petite que $1$ (se prouve facilement aussi, $I_{n+1} < I_n$), et semble converger.
# Peut-être vers $1/2$, il faut aller regarder plus loin ?

# In[52]:


affiche_termes_un(100)


# Pour conclure, on peut prouver que la suite est monotone et bornée, donc elle converge.
# Il est plus dur de calculer sa limite, et cela sort de l'exercice.

# ---
# ## Planche 166

# In[53]:


case_max = 12
univers = list(range(case_max))


# In[54]:


def prochaine_case(case):
    return (case + rd.randint(1, 6+1)) % case_max


# In[55]:


def Yn(duree, depart=0):
    case = depart
    for coup in range(duree):
        case = prochaine_case(case)
    return case


# Avant de s'en servir pour simuler plein de trajectoirs, on peut vérifier :
# 
# - en un coup, on avance pas plus de 6 cases :

# In[56]:


[Yn(1) for _ in range(10)]


# - En 100 coups, on commence à ne plus voir de tendance :

# In[62]:


[Yn(100) for _ in range(10)]


# Pour l'histogramme, on triche un peu en utilisant `numpy.bincount`. Mais on peut le faire à la main très simplement !

# In[64]:


observations = [Yn(100) for _ in range(10)]
print(observations)
np.bincount(observations, minlength=case_max)


# In[65]:


def histogramme(duree, repetitions=5000):
    cases = [Yn(duree) for _ in range(repetitions)]
    frequences = np.bincount(cases, minlength=case_max)
    # aussi a la main si besoin
    frequences = [0] * case_max
    for case in cases:
        frequences[case] += 1
    return frequences / np.sum(frequences)


# In[66]:


histogramme(50)


# On va afficher des histogrammes :

# In[67]:


def voir_histogramme(valeurs_n):
    for n in valeurs_n:
        plt.figure()
        plt.bar(np.arange(case_max), histogramme(n))
        plt.title("Histogramme de cases visitées en " + str(n) + " coups")
        plt.show()


# In[68]:


voir_histogramme([1, 2, 3, 50, 100, 200])


# On s'approche d'une distribution uniforme !

# On a tout simplement l'expression suivante :
# $$\forall n \geq 0, \mathbb{P}(Y_{n+1} = k) = \frac{1}{6} \sum_{\delta = 1}^{6} \mathbb{P}(Y_n = k - \delta \mod 12).$$
# Avec $k - 1 \mod 12 = 11$ si $k = 0$ par exemple. 

# On a donc la matrice suivante pour exprimer $U_n = (\mathbb{P}(Y_n = k))_{0\leq k \leq 11}$ en fonction de $U_{n-1}$ :
# 
# $$ P = \frac{1}{6} \begin{bmatrix}
# 0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 & 1 & 1 & 1 & 1 \\
# 1 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 & 1 & 1 & 1\\
# 1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 & 1 & 1\\
# 1 & 1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 1 & 1\\
# 1 & 1 & 1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 1\\
# 1 & 1 & 1 & 1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 & 1\\
# 1 & 1 & 1 & 1 & 1 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
# 0 & 1 & 1 & 1 & 1 & 1 & 1 & 0 & 0 & 0 & 0 & 0 \\
# 0 & 0 & 1 & 1 & 1 & 1 & 1 & 1 & 0 & 0 & 0 & 0 \\
# 0 & 0 & 0 & 1 & 1 & 1 & 1 & 1 & 1 & 0 & 0 & 0 \\
# 0 & 0 & 0 & 0 & 1 & 1 & 1 & 1 & 1 & 1 & 0 & 0 \\
# 0 & 0 & 0 & 0 & 0 & 1 & 1 & 1 & 1 & 1 & 1 & 0 \\
# \end{bmatrix}$$

# On va la définir rapidement en Python, et calculer ses valeurs propres notamment.

# In[18]:


case_max = 12


# In[19]:


P = np.zeros((case_max, case_max))


# In[26]:


for k in range(case_max):
    for i in range(k - 6, k):
        P[k, i] = 1/6


# In[27]:


P


# In[28]:


import numpy.linalg as LA


# In[29]:


spectre, vecteur_propres = LA.eig(P)


# On a besoin d'éliminer les erreurs d'arrondis, mais on voit que $1$ est valeur propre, associée au vecteur $[1,\dots,1,\dots,1]$ avec un $1$ seulement à la 8ème composante.

# In[34]:


np.round(spectre,10)


# In[31]:


np.round(vecteur_propres[0])


# $P$ n'est pas diagonalisable, **à prouver** au tableau si l'examinateur le demande.

# ----
# ## Planche 168

# - Soit $f(x) = \frac{1}{2 - \exp(x)}$, et $a(n) = \frac{f^{(n)}(0)}{n!}$.
# 

# In[76]:


def f(x):
    return 1 / (2 - np.exp(x))


# - Soit $g(x) = 2 - \exp(x)$, telle que $g(x) f(x) = 1$. En dérivant $n > 0$ fois cette identité et en utilisant la formule de Leibniz, on trouve :
# $$ (g(x)f(x))^{(n)} = 0 = \sum_{k=0}^n {n \choose k} g^{(k)}(x) f^{(n-k)}(x).$$
# Donc en $x=0$, on utilise que $g^{(k)}(x) = - \exp(x)$, qui donne que $g^{(k)}(0) = 1$ si $k=0$ ou $-1$ sinon, pour trouver que $\sum_{k=0}^n {n \choose k} f^{(k)}(0) = f^{(n)}(0)$. En écrivant ${n \choose k} = \frac{k! (n-k)!}{n!}$ et avec la formule définissant $a(n)$, cela donne directement la somme recherchée : $$ a(n) = \sum_{k=1}^n \frac{a(n-k)}{k!}.$$

# - Pour calculer $a(n)$ avec Python, on utilise cette formule comme une formule récursive, et on triche un peu en utilisant `math.factorial` pour calculer $k!$.Il nous faut aussi $a(0) = f(0) = 1$ :

# In[77]:


from math import factorial

def a_0an(nMax):
    valeurs_a = np.zeros(nMax+1)
    valeurs_a[0] = 1.0
    for n in range(1, nMax+1):
        valeurs_a[n] = sum(valeurs_a[n-k] / factorial(k) for k in range(1, n+1))
    return valeurs_a


# In[78]:


nMax = 10
valeurs_n = np.arange(0, nMax + 1)
valeurs_a = a_0an(nMax)

for n in valeurs_n:
    print("Pour n =", n, "on a a(n) =", valeurs_a[n])


# In[83]:


plt.figure()
plt.plot(valeurs_n, valeurs_a, 'ro-', label=r'$a(n)$', markersize=12)
plt.plot(valeurs_n, 1 / np.log(2)**valeurs_n, 'g+-', label=r'$1/\log(2)^n$')
plt.plot(valeurs_n, 1 / (2 * np.log(2)**valeurs_n), 'bd-', label=r'$1/(2\log(2)^n)$')
plt.title("$a(n)$ et deux autres suites")
plt.legend()
plt.show()


# - On observe que $a(n)$ est comprise entre $\frac{1}{2(\log(2))^n}$ et $\frac{1}{\log(2)^n}$, donc le rayon de convergence de $S(x) = \sum a(n) x^n$ est $\log(2)$.
# - On va calculer les sommes partielles $S_n(x)$ de la série $S(x)$ :

# In[84]:


def Sn(x, n):
    valeurs_a = a_0an(n)
    return sum(valeurs_a[k] * x**k for k in range(0, n + 1))


# On peut vérifie que notre fonction marche :

# In[85]:


x = 0.5
for n in range(0, 6 + 1):
    print("Pour n =", n, "S_n(x) =", Sn(x, n))


# In[86]:


valeurs_x = np.linspace(0, 0.5, 1000)
valeurs_f = f(valeurs_x)


# <span style="color:red;">Je pense que l'énoncé comporte une typo sur l'intervale ! Vu le rayon de convergence, on ne voit rien si on affiche sur $[0,10]$ !</span>

# In[89]:


plt.figure()
for n in range(0, 6 + 1):
    valeurs_Sn = []
    for x in valeurs_x:
        valeurs_Sn.append(Sn(x, n))
    plt.plot(valeurs_x, valeurs_Sn, 'o:', label='$S_' + str(n) + '(x)$', markevery=50)
plt.plot(valeurs_x, valeurs_f, '+-', label='$f(x)$', markevery=50)
plt.title("$f(x)$ et $S_n(x)$ pour $n = 0$ à $n = 6$")
plt.legend()
plt.show()


# ## Planche 170

# In[90]:


def u(n):
    return np.arctan(n+1) - np.arctan(n)


# In[92]:


valeurs_n = np.arange(50)
valeurs_u = u(valeurs_n)

plt.figure()
plt.plot(valeurs_n, valeurs_u, "o-")
plt.xlabel("Entier $n$")
plt.ylabel("Valeur $u_n$")
plt.title("Premières valeurs de $u_n$")


# On peut vérifier le prognostic quand à la somme de la série $\sum u_n$ :

# In[93]:


pi/2


# In[94]:


sum(valeurs_u)


# In[95]:


somme_serie = pi/2
somme_partielle = sum(valeurs_u)
erreur_relative = abs(somme_partielle - somme_serie) / somme_serie
erreur_relative


# Avec seulement $50$ termes, on a moins de $1.5\%$ d'erreur relative, c'est déjà pas mal !

# $(u_n)_n$ semble être décroisante, et tendre vers $0$. On peut prouver ça mathématiquement.

# On sait aussi que $\forall x\neq0, \arctan(x) + \arctan(1/x) = \frac{\pi}{2}$, et que $\arctan(x) \sim x$, donc on obtient que $u_n \sim \frac{1}{n} - \frac{1}{n+1} = \frac{1}{n(n+1)}$.
# On peut le vérifier :

# In[97]:


valeurs_n = np.arange(10, 1000)
valeurs_u = u(valeurs_n)
valeurs_equivalents = 1 / (valeurs_n * (valeurs_n + 1))

plt.figure()
plt.plot(valeurs_n, valeurs_u / valeurs_equivalents, "-")
plt.xlabel("Entier $n$")
plt.title(r"Valeurs de $u_n / \frac{1}{n(n+1)}$")


# - Pour $e = (e_n)_{n\in\mathbb{N}}$ une suite de nombres égaux à $0$ ou $1$ (*i.e.*, $\forall n, e_n \in \{0,1\}$, $S_n(e) = \sum{i=0}^n e_i u_i$ est bornée entre $0$ et $\sum_{i=0}^n u_i$. Et $u_n \sim \frac{1}{n(n+1)}$ qui est le terme général d'une série convergente (par critère de Cauchy, par exemple, avec $\alpha=2$). Donc la série $\sum u_n$ converge et donc par encadrement, $S_n(e)$ converge pour $n\to\infty$, *i.e.*, $S(e)$ converge. Ces justifications donnent aussi que $$0 \leq S(e) \leq \sum_{n\geq0} u_n = \lim_{n\to\infty} \arctan(n) - \arctan(0) = \frac{\pi}{2}.$$

# - Pour $e = (0, 1, 0, 1, \ldots)$, $S(e)$ peut être calculée avec Python. Pour trouver une valeur approchée à $\delta = 10^{-5}$ près, il faut borner le **reste** de la série, $R_n(e) = \sum_{i \geq n + 1} e_i u_i$. Ici, $R_{2n+1}(e) \leq u_{2n+2}$ or $u_i \leq \frac{1}{i(i+1)}$, donc $R_{2n+1}(e) \leq \frac{1}{(2n+1)(2n+2)}$. $\frac{1}{(2n+1)(2n+2)} \leq \delta$ dès que $2n+1 \geq \sqrt{\delta}$, *i.e.*, $n \geq \frac{\sqrt{\delta}+1}{2}$. Calculons ça :

# In[98]:


from math import ceil, sqrt, pi


# In[99]:


def Se(e, delta=1e-5, borne_sur_n_0=10000):
    borne_sur_n_1 = int(ceil(1 + sqrt(delta)/2.0))
    borne_sur_n = max(borne_sur_n_0, borne_sur_n_1)
    somme_partielle = 0
    for n in range(0, borne_sur_n + 1):
        somme_partielle += e(n) * u(n)
    return somme_partielle


# In[100]:


def e010101(n):
    return 1 if n % 2 == 0 else 0


# In[101]:


delta = 1e-5
Se010101 = Se(e010101, delta)
print("Pour delta =", delta, "on a Se010101(delta) ~=", round(Se010101, 5))


# - Pour inverser la fonction, et trouver la suite $e$ telle que $S(e) = x$ pour un $x$ donné, il faut réfléchir un peu plus.

# In[102]:


def inverse_Se(x, n):
    assert 0 < x < pi/2.0, "Erreur : x doit être entre 0 et pi/2 strictement."
    print("Je vous laisse chercher.")
    raise NotImplementedError


# Ca suffit pour la partie Python.

# ----
# ## Planche 172

# In[103]:


from random import random

def pile(proba):
    """ True si pile, False si face (false, face, facile à retenir)."""
    return random() < proba


# - D'abord, on écrit une fonction pour **simuler** l'événement aléatoire :

# In[104]:


def En(n, p):
    lance = pile(p)
    for i in range(n - 1):
        nouveau_lance = pile(p)
        if lance and nouveau_lance:
            return False
        nouveau_lance = lance
    return True


# In[105]:


import numpy as np


# In[106]:


lances = [ En(2, 0.5) for _ in range(100) ]
np.bincount(lances)


# In[107]:


def pn(n, p, nbSimulations=100000):
    return np.mean([ En(n, p) for _ in range(nbSimulations) ])


# - Par exemple, pour seulement $2$ lancés, on a $1 - p_n = p^2$ car $\overline{E_n}$ est l'événement d'obtenir $2$ piles qui est de probabilité $p^2$.

# In[108]:


pn(2, 0.5)


# - Avec $4$ lancés, on a $p_n$ bien plus petit.

# In[109]:


pn(4, 0.5)


# - On vérifie que $p_n(n, p)$ est décroissante en $p$, à $n$ fixé :

# In[110]:


pn(4, 0.1)


# In[111]:


pn(4, 0.9)


# - On vérifie que $p_n(n, p)$ est décroissante en $n$, à $p$ fixé :

# In[112]:


pn(6, 0.2)


# In[113]:


pn(20, 0.2)


# In[114]:


pn(100, 0.2)


# - Notons que la suite semble converger ? Ou alors elle décroit de moins en moins rapidement.

# - Par récurrence et en considérant les possibles valeurs des deux derniers lancés numérotés $n+2$ et $n+1$, on peut montrer que
#   $$\forall n, p_{n+2} = (1-p) p_{n+1} + p(1-p) p_n$$

# - Si $p_n$ converge, on trouve sa limite $l$ comme point fixe de l'équation précédente. $l = (1-p) l + p(1-p) l$ ssi $1 = 1-p + p(1-p)$ ou $l=0$, donc si $p\neq0$, $l=0$. Ainsi l'événement "on obtient deux piles d'affilé sur un nombre infini de lancers$ est bien presque sûr.

# - Je vous laisse terminer pour calculer $T$ et les dernières questions.

# ----
# ## Planche 177
# 
# - Le domaine de définition de $f(x) = \sum_{n \geq 1} \frac{x^n}{n^2}$ est $[-1, 1]$ car $\sum \frac{x^n}{n^k}$ converge si $\sum x^n$ converge (par $k$ dérivations successives), qui converge ssi $|x| < 1$. Et en $-1$ et $1$, on utilise $\sum \frac{1}{n^2} = \frac{\pi^2}{6}$.
# 
# - Pour calculer $f(x)$ à $10^{-5}$ près, il faut calculer sa somme partielle $S_n(x) := \sum_{i=1}^n \frac{x^i}{i^2}$ en bornant son reste $S_n(x) := \sum_{i \geq n+1} \frac{x^i}{i^2}$ par (au moins) $10^{-5}$. Une inégalité montre rapidement que $R_n(x) \leq |x|^{n+1}\sum_{i\geq n+1} \frac{1}{i^2} $, et donc $R_n(x) \leq \delta$ dès que $|x|^{n+1} \leq \frac{\pi^2}{6} \delta$, puisque $\sum_{i\geq n+1} \frac{1}{i^2} \leq \sum_{i=0}^{+\infty} \frac{1}{i^2} = \frac{\pi^2}{6}$. En inversant pour trouver $n$, cela donne que le reste est contrôlé par $\delta$ dès que $n \leq \log_{|x|}\left( \frac{6}{\pi^2} \delta \right) - 1$ (si $x\neq 0$, et par $n \geq 0$ sinon).

# In[115]:


from math import floor, log, pi


# In[116]:


delta = 1e-5

def f(x):
    if x == 0: return 0
    borne_sur_n = int(floor(log((6/pi**2 * delta), abs(x)) - 1))
    somme_partielle = 0
    for n in range(1, borne_sur_n + 1):
        somme_partielle += x**n / n**2
    return somme_partielle


# In[117]:


for x in [-0.75, -0.5, 0.25, 0, 0.25, 0.5, 0.75]:
    print("Pour x =", x, "\tf(x) =", round(f(x), 5))


# - L'intégrale $g(t) = \int_0^x \frac{\ln(1 - t)}{t} \mathrm{d}t$ est bien défine sur $D = [-1, 1]$ puisque son intégrande existe, est continue et bien intégrable sur tout interval de la forme $]a, 0[$ ou $]0, b[$ pour $-1 < a < 0$ ou $0 < b < 1$. Le seul point qui peut déranger l'intégrabilité est en $0$, mais $\ln(1-t) \sim t$ quand $t\to0$ donc l'intégrande est $\sim 1$ en $0^-$ et $0^+$ et donc est bien intégrable. De plus, comme "intégrale de la borne supérieure" d'une fonction continue, $g$ est dérivable sur l'intérieur de son domaine, *i.e.*, sur $]-1, 1[$.
# 
# - Pour la calculer numériquement, on utilise **évidemment** le module `scipy.integrate` et sa fonction `integrale, erreur = quad(f, a, b)`, qui donne une approximation de la valeur d'une intégrale en dimension 1 et une *borne* sur son erreur :

# In[118]:


from scipy import integrate


# In[119]:


def g(x):
    def h(t):
        return log(1 - t) / t
    integrale, erreur = integrate.quad(h, 0, x)
    return integrale


# - On visualise les deux fonctions $f$ et $g$ sur le domaine $D$ :

# In[120]:


import numpy as np
import matplotlib.pyplot as plt


# In[122]:


domaine = np.linspace(-0.99, 0.99, 1000)

valeurs_f = [f(x) for x in domaine]
valeurs_g = [g(x) for x in domaine]

plt.figure()
plt.plot(domaine, valeurs_f, "+-", label="$f(x)$", markevery=50)
plt.plot(domaine, valeurs_g, "+-", label="$g(x)$", markevery=50)
plt.legend()
plt.grid()
plt.title("Représentation de $f(x)$ et $g(x)$")
plt.show()


# - On conjecture que $g(x) = - f(x)$.
# 
# La suite des questions est à faire au brouillon et sans Python :
# 
# - On trouve que $f'(x) = \sum_{n\geq 1} \frac{n x^{n-1}}{n^2} = \frac{1}{x} \sum_{n\geq 1} \frac{x^n}{n}$ si $x\neq0$. Or on sait que $\log(1 + x) = \sum_{n\geq 1} \frac{x^n}{n}$ et donc cela montre bien que $g(x) = \int_0^x - f'(t) \mathrm{d}t = f(0) - f(x) = f(x)$ comme observé.
# 
# - On trouve que $g(1) = - f(1) = - \frac{\pi^2}{6}$.
# 
# - Par ailleurs, un changement de variable $u=1-x$ donne $g(1-x) = \int_x^1 \frac{\ln(u)}{1-u} \mathrm{d} u$, et une intégration par partie avec $a(u) = \ln(u)$ et $b'(u) = \frac{1}{1-u}$ donne $g(1-x) = [\ln(u)\ln(1-u)]_x^1 + \int_x^1 \frac{\ln(1-u)}{u} \mathrm{d}u$ et donc on reconnaît que $$g(1-x) = \ln(x)\ln(1-x) + g(1) - g(x).$$
# 
# - Je vous laisse la fin comme exercice !

# ----
# # À voir aussi
# 
# ## [Les oraux](http://perso.crans.org/besson/infoMP/oraux/solutions/)   *(exercices de maths avec Python)*
# 
# Se préparer aux oraux de ["maths avec Python" (maths 2)](http://www.concours-centrale-supelec.fr/CentraleSupelec/MultiY/C2015/#oMat2) du concours Centrale Supélec peut être utile.
# 
# Après les écrits et la fin de l'année, pour ceux qui seront admissibles à Centrale-Supélec, ils vous restera <b>les oraux</b> (le concours Centrale-Supélec a un <a title="Quelques exemples d'exercices sur le site du concours Centrale-Supélec" href="http://www.concours-centrale-supelec.fr/CentraleSupelec/MultiY/C2015/#oMat2">oral d'informatique</a>, et un peu d'algorithmique et de Python peuvent en théorie être demandés à chaque oral de maths et de SI).
# 
# Je vous invite à lire [cette page avec attention](http://www.concours-centrale-supelec.fr/CentraleSupelec/MultiY/C2015/#oMat2), et à jeter un œil aux documents mis à disposition :
# 
# ## Fiches de révisions *pour les oraux*
# 
# 1. [Calcul matriciel](http://www.concours-centrale-supelec.fr/CentraleSupelec/MultiY/C2015/Python-matrices.pdf), avec [numpy](https://docs.scipy.org/doc/numpy/) et [numpy.linalg](http://docs.scipy.org/doc/numpy/reference/routines.linalg.html),
# 2. [Réalisation de tracés](http://www.concours-centrale-supelec.fr/CentraleSupelec/MultiY/C2015/Python-plot.pdf), avec [matplotlib](http://matplotlib.org/users/beginner.html),
# 3. [Analyse numérique](http://www.concours-centrale-supelec.fr/CentraleSupelec/MultiY/C2015/Python-AN.pdf), avec [numpy](https://docs.scipy.org/doc/numpy/) et [scipy](http://docs.scipy.org/doc/scipy/reference/tutorial/index.html). Voir par exemple [scipy.integrate](http://docs.scipy.org/doc/scipy/reference/tutorial/integrate.html) avec les fonctions [scipy.integrate.quad](http://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.quad.html) (intégrale numérique) et [scipy.integrate.odeint](http://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.odeint.html) (résolution numérique d'une équation différentielle),
# 4. [Polynômes](http://www.concours-centrale-supelec.fr/CentraleSupelec/MultiY/C2015/Python-polynomes.pdf) : avec [numpy.polynomials](https://docs.scipy.org/doc/numpy/reference/routines.polynomials.package.html), [ce tutoriel peut aider](https://docs.scipy.org/doc/numpy/reference/routines.polynomials.classes.html),
# 5. [Probabilités](http://www.concours-centrale-supelec.fr/CentraleSupelec/MultiY/C2015/Python-random.pdf), avec [numpy](https://docs.scipy.org/doc/numpy/) et [random](https://docs.python.org/3/library/random.html).
# 
# Pour réviser : voir [ce tutoriel Matplotlib (en anglais)](http://www.labri.fr/perso/nrougier/teaching/matplotlib/), [ce tutoriel Numpy (en anglais)](http://www.labri.fr/perso/nrougier/teaching/numpy/numpy.html).
# Ainsi que tous les [TP](http://perso.crans.org/besson/infoMP/TPs/solutions/), [TD](http://perso.crans.org/besson/infoMP/TDs/solutions/) et [DS](http://perso.crans.org/besson/infoMP/DSs/solutions/) en Python que j'ai donné et corrigé au Lycée Lakanal (Sceaux, 92) en 2015-2016 !

# ----
# ## D'autres notebooks ?
# 
# > Ce document est distribué [sous licence libre (MIT)](https://lbesson.mit-license.org/), comme [les autres notebooks](https://GitHub.com/Naereen/notebooks/) que j'ai écrit depuis 2015.
