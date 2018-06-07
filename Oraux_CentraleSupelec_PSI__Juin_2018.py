
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#Oraux-CentraleSupélec-PSI---Juin-2017" data-toc-modified-id="Oraux-CentraleSupélec-PSI---Juin-2017-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Oraux CentraleSupélec PSI - Juin 2017</a></div><div class="lev2 toc-item"><a href="#Remarques-préliminaires" data-toc-modified-id="Remarques-préliminaires-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Remarques préliminaires</a></div><div class="lev2 toc-item"><a href="#Planche-162" data-toc-modified-id="Planche-162-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Planche 162</a></div><div class="lev2 toc-item"><a href="#Planche-166" data-toc-modified-id="Planche-166-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Planche 166</a></div><div class="lev2 toc-item"><a href="#Planche-170" data-toc-modified-id="Planche-170-14"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Planche 170</a></div><div class="lev2 toc-item"><a href="#Planche-177" data-toc-modified-id="Planche-177-15"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Planche 177</a></div><div class="lev1 toc-item"><a href="#À-voir-aussi" data-toc-modified-id="À-voir-aussi-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>À voir aussi</a></div><div class="lev2 toc-item"><a href="#Les-oraux---(exercices-de-maths-avec-Python)" data-toc-modified-id="Les-oraux---(exercices-de-maths-avec-Python)-21"><span class="toc-item-num">2.1&nbsp;&nbsp;</span><a href="http://perso.crans.org/besson/infoMP/oraux/solutions/" target="_blank">Les oraux</a>   <em>(exercices de maths avec Python)</em></a></div><div class="lev2 toc-item"><a href="#Fiches-de-révisions-pour-les-oraux" data-toc-modified-id="Fiches-de-révisions-pour-les-oraux-22"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Fiches de révisions <em>pour les oraux</em></a></div><div class="lev2 toc-item"><a href="#Quelques-exemples-de-sujets-d'oraux-corrigés" data-toc-modified-id="Quelques-exemples-de-sujets-d'oraux-corrigés-23"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Quelques exemples de sujets <em>d'oraux</em> corrigés</a></div><div class="lev2 toc-item"><a href="#D'autres-notebooks-?" data-toc-modified-id="D'autres-notebooks-?-24"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>D'autres notebooks ?</a></div>

# # Oraux CentraleSupélec PSI - Juin 2017
# 
# - Ce [notebook Jupyter](https://www.jupyter.org) est une proposition de correction, en [Python 3](https://www.python.org/), d'exercices d'annales de l'épreuve "maths-info" du [concours CentraleSupélec](http://www.concours-centrale-supelec.fr/), filière PSI.
# - Les exercices viennent de l'[Officiel de la Taupe](http://odlt.fr/), [2016](http://www.odlt.fr/Oraux_2017.pdf) (planches 162 à 177, page 23).
# - Ce document a été écrit par [Lilian Besson](http://perso.crans.org/besson/), et est disponible en ligne [sur mon site](https://perso.crans.org/besson/publis/notebooks/Oraux_CentraleSupélec_PSI__Juin_2018.html).

# ## Remarques préliminaires
# - Les exercices sans Python ne sont pas traités.
# - Les exercices avec Python utilisent Python 3, [numpy](http://numpy.org), [matplotlib](http://matplotlib.org), [scipy](http://scipy.org) et [sympy](http://sympy.org), et essaient d'être résolus le plus simplement et le plus rapidement possible. L'efficacité (algorithmique, en terme de mémoire et de temps de calcul), n'est *pas* une priorité. La concision et simplicité de la solution proposée est prioritaire.

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import numpy.random as rd


# ---
# ## Planche 162

# On commence par définir la fonction, en utilisant `numpy.cos` et pas `math.cos` (les fonctions de `numpy` peuvent travailler sur des tableaux, c'est plus pratique).

# In[ ]:


def f(x):
    return x * (1 - x) * (1 + np.cos(5 * np.pi * x))

Xs = np.linspace(0, 1, 2000)
Ys = f(Xs)


# Pas besoin de lire le maximum sur un graphique :

# In[3]:


M = max_de_f = max(Ys)
print("Sur [0, 1], avec 2000 points, M =", M)


# On affiche la fonction, comme demandé, avec un titre :

# In[4]:


plt.figure()
plt.plot(Xs, Ys)
plt.title("Fonction $f(x)$ sur $[0,1]$")
plt.show()


# Pour calculer l'intégrale, on utilise `scipy.integrate.quad` :

# In[11]:


def In(x, n):
    def fn(x):
        return f(x) ** n
    return integrate.quad(fn, 0, 1)[0]

def Sn(x):
    return np.sum([In(Xs, n) * x**n for n in range(0, n+1)], axis=0)


# On vérifie avant de se lancer dans l'affichage :

# In[12]:


for n in range(10):
    print("In(x,", n, ") =", In(Xs, n))


# In[13]:


a = 1/M + 0.1
X2s = np.linspace(-a, a, 2000)

plt.figure()
for n in [10, 20, 30, 40, 50]:
    plt.plot(X2s, Sn(X2s), label="n =" + str(n))
plt.legend()
plt.show()


# $S_n(x)$ semble diverger pour $x\to2^-$ quand $n\to\infty$.
# Le rayon de convergence de la série $\sum In x^n$ **semble** être $2$.

# In[14]:


def un(n):
    return In(Xs, n + 1) / In(Xs, n)


# In[15]:


for n in range(10):
    print("un =", un(n), "pour n =", n)


# Ici, `un` ne peut pas être utilisé comme une fonction "numpy" qui travaille sur un tableau, on stocke donc les valeurs "plus manuellement" :

# In[26]:


def affiche_termes_un(N):
    valeurs_un = [0] * N
    for n in range(N):
        valeurs_un[n] = un(n)

    plt.figure()
    plt.plot(valeurs_un, 'o-')
    plt.title("Suite $u_n$")
    plt.grid()
    plt.show()


# In[27]:


affiche_termes_un(30)


# La suite $u_n$ semble être croissante (on peut le prouver), toujours plus petite que $1$ (se prouve facilement aussi, $I_{n+1} < I_n$), et semble converger.
# Peut-être vers $1/2$, il faut aller regarder plus loin ?

# In[28]:


affiche_termes_un(100)


# Pour conclure, on peut prouver que la suite est monotone et bornée, donc elle converge.
# Il est plus dur de calculer sa limite, et cela sort de l'exercice.

# ---
# ## Planche 166

# In[29]:


case_max = 12
univers = list(range(case_max))


# In[30]:


def prochaine_case(case):
    return (case + rd.randint(1, 6+1)) % case_max


# In[48]:


def Yn(duree, depart=0):
    case = depart
    for coup in range(duree):
        case = prochaine_case(case)
    return case


# Avant de s'en servir pour simuler plein de trajectoirs, on peut vérifier :
# 
# - en un coup, on avance pas plus de 6 cases :

# In[32]:


[Yn(1) for _ in range(10)]


# - En 100 coups, on commence à ne plus voir de tendance :

# In[39]:


[Yn(100) for _ in range(10)]


# Pour l'histogramme, on triche un peu en utilisant `numpy.bincount`. Mais on peut le faire à la main très simplement !

# In[40]:


np.bincount(_, minlength=case_max)


# In[44]:


def histogramme(duree, repetitions=5000):
    cases = [Yn(duree) for _ in range(repetitions)]
    frequences = np.bincount(cases, minlength=case_max)
    # aussi a la main si besoin
    frequences = [0] * case_max
    for case in cases:
        frequences[case] += 1
    return frequences / np.sum(frequences)


# In[45]:


histogramme(50)


# In[55]:


def voir_histogramme(valeurs_n):
    for n in valeurs_n:
        plt.figure()
        plt.bar(np.arange(case_max), histogramme(n))
        plt.title("Histogramme de cases visitées en " + str(n) + " coups")
        plt.show()


# In[58]:


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

# In[70]:


P = np.zeros((case_max, case_max))


# In[71]:


for k in range(case_max):
    for i in range(k - 6, k):
        P[k, i] = 1


# In[72]:


P


# In[73]:


import numpy.linalg as LA


# In[75]:


spectre, vecteur_propres = LA.eig(P)


# On a besoin d'éliminer les erreurs d'arrondis, mais on voit que $6$ est valeur propre, associée au vecteur $[0,\dots,1,\dots,0]$ avec un $1$ seulement à la 8ème composante.

# In[84]:


np.round(spectre)


# In[83]:


np.round(vecteur_propres[0])


# $P$ n'est pas diagonalisable, **à prouver** au tableau si l'examinateur le demande.

# ## Planche 170

# In[ ]:


def u(n):
    return np.arctan(n+1) - np.arctan(n)


# In[85]:


valeurs_n = np.arange(50)
valeurs_u = u(valeurs_n)

plt.figure()
plt.plot(valeurs_n, valeurs_u, "o-")
plt.title("Premières valeurs de $u_n$")


# $(u_n)_n$ semble être décroisante, et tendre vers $0$. On peut prouver ça mathématiquement.

# On sait aussi que $\forall x\neq0, \arctan(x) + \arctan(1/x) = \frac{\pi}{2}$, et que $\arctan(x) \sim x$, donc on obtient que $u_n \sim \frac{1}{n} - \frac{1}{n+1} = \frac{1}{n(n+1)}$.
# On peut le vérifier :

# In[91]:


valeurs_n = np.arange(10, 1000)
valeurs_u = u(valeurs_n)
valeurs_equivalents = 1 / (valeurs_n * (valeurs_n + 1))

plt.figure()
plt.plot(valeurs_n, valeurs_u / valeurs_equivalents, "-")
plt.title(r"Valeurs de $u_n / \frac{1}{n(n+1)}$")


# Ca suffit pour la partie Python.

# ----
# ## Planche 177
# 
# - Le domaine de définition de $f(x) = \sum_{n \geq 1} \frac{x^n}{n^2}$ est $[-1, 1]$ car $\sum \frac{x^n}{n^k}$ converge si $\sum x^n$ converge (par $k$ dérivations successives), qui converge ssi $|x| < 1$. Et en $-1$ et $1$, on utilise $\sum \frac{1}{n^2} = \frac{\pi^2}{6}$.
# 
# - Pour calculer $f(x)$ à $10^{-5}$ près, il faut calculer sa somme partielle $S_n(x) := \sum_{i=1}^n \frac{x^i}{i^2}$ en bornant son reste $S_n(x) := \sum_{i \geq n+1} \frac{x^i}{i^2}$ par (au moins) $10^{-5}$. Une inégalité montre rapidement que $R_n(x) \leq |x|^{n+1}\sum_{i\geq n+1} \frac{1}{i^2} $, et donc $R_n(x) \leq \delta$ dès que $|x|^{n+1} \leq \frac{\pi^2}{6} \delta$, puisque $\sum_{i\geq n+1} \frac{1}{i^2} \leq \sum_{i=0}^{+\infty} \frac{1}{i^2} = \frac{\pi^2}{6}$. En inversant pour trouver $n$, cela donne que le reste est contrôlé par $\delta$ dès que $n \leq \log_{|x|}\left( \frac{6}{\pi^2} \delta \right) - 1$ (si $x\neq 0$, et par $n \geq 0$ sinon).

# In[9]:


from math import floor, log, pi


# In[10]:


delta = 1e-5

def f(x):
    if x == 0: return 0
    borne_sur_n = int(floor(log((6/pi**2 * delta), abs(x)) - 1))
    somme_partielle = 0
    for n in range(1, borne_sur_n + 1):
        somme_partielle += x**n / n**2
    return somme_partielle


# In[13]:


for x in [-0.75, -0.5, 0.25, 0, 0.25, 0.5, 0.75]:
    print("Pour x =", x, "f(x) =", f(x))


# - L'intégrale $g(t) = \int_0^x \frac{\ln(1 - t)}{t} \mathrm{d}t$ est bien défine sur $D = [-1, 1]$ puisque son intégrande existe, est continue et bien intégrable sur tout interval de la forme $]a, 0[$ ou $]0, b[$ pour $-1 < a < 0$ ou $0 < b < 1$. Le seul point qui peut déranger l'intégrabilité est en $0$, mais $\ln(1-t) \sim t$ quand $t\to0$ donc l'intégrande est $\sim 1$ en $0^-$ et $0^+$ et donc est bien intégrable. De plus, comme "intégrale de la borne supérieure" d'une fonction continue, $g$ est dérivable sur l'intérieur de son domaine, *i.e.*, sur $]-1, 1[$.
# 
# - Pour la calculer numériquement, on utilise **évidemment** le module `scipy.integrate` et sa fonction `integrale, erreur = quad(f, a, b)`, qui donne une approximation de la valeur d'une intégrale en dimension 1 et une *borne* sur son erreur :

# In[17]:


from scipy import integrate


# In[18]:


def g(x):
    def h(t):
        return log(1 - t) / t
    integrale, erreur = integrate.quad(h, 0, x)
    return integrale


# - On visualise les deux fonctions $f$ et $g$ sur le domaine $D$ :

# In[22]:


import numpy as np
import matplotlib.pyplot as plt


# In[25]:


domaine = np.linspace(-0.99, 0.99, 1000)

valeurs_f = [f(x) for x in domaine]
valeurs_g = [g(x) for x in domaine]

plt.figure()
plt.plot(domaine, valeurs_f, label="$f(x)$")
plt.plot(domaine, valeurs_g, label="$g(x)$")
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
# 
# ## Quelques exemples de sujets *d'oraux* corrigés
# > Ces 5 sujets sont corrigés, et nous les avons tous traité en classe durant les deux TP de révisions pour les oraux (10 et 11 juin).
# 
# - PC : [sujet #1](http://www.concours-centrale-supelec.fr/CentraleSupelec/MultiY/C2015/PC-Mat2-2015-27.pdf) ([correction PC #1](http://perso.crans.org/besson/infoMP/oraux/solutions/PC_Mat2_2015_27.html)), [sujet #2](http://www.concours-centrale-supelec.fr/CentraleSupelec/MultiY/C2015/PC-Mat2-2015-28.pdf) ([correction PC #2](http://perso.crans.org/besson/infoMP/oraux/solutions/PC_Mat2_2015_28.html)).
# - PSI : [sujet #1](http://www.concours-centrale-supelec.fr/CentraleSupelec/MultiY/C2015/PSI-Mat2-2015-24.pdf) ([correction PSI #1](http://perso.crans.org/besson/infoMP/oraux/solutions/PSI_Mat2_2015_24.html)), [sujet #2](http://www.concours-centrale-supelec.fr/CentraleSupelec/MultiY/C2015/PSI-Mat2-2015-25.pdf) ([correction PSI #2](http://perso.crans.org/besson/infoMP/oraux/solutions/PSI_Mat2_2015_25.html)), [sujet #3](http://www.concours-centrale-supelec.fr/CentraleSupelec/MultiY/C2015/PSI-Mat2-2015-26.pdf) ([correction PSI #3](http://perso.crans.org/besson/infoMP/oraux/solutions/PSI_Mat2_2015_26.html)).
# - MP : pas de sujet mis à disposition, mais le programme est le même que pour les PC et PSI (pour cette épreuve).

# ----
# ## D'autres notebooks ?
# 
# > Ce document est distribué [sous licence libre (MIT)](https://lbesson.mit-license.org/), comme [les autres notebooks](https://GitHub.com/Naereen/notebooks/) que j'ai écrit depuis 2015.
