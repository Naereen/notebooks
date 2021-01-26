#!/usr/bin/env python
# coding: utf-8

# # Mini tutoriel pour la résolution de programmes linéaires avec Python - ENS Rennes 2021

# ## Références si vous êtes curieux-ses
# 
# Un très bon tutoriel :
# 
# - https://realpython.com/linear-programming-python/
# 
# Documentation de `scipy.optimize` :
# 
# - https://docs.scipy.org/doc/scipy/reference/optimize.html
# 
# D'autres tutoriels :
# - https://scipy-lectures.org/advanced/mathematical_optimization/index.html
# - https://medium.com/better-programming/how-to-solving-linear-programming-problems-with-examples-and-implementation-in-python-a7b7061bafc9
# - http://stackoverflow.com/questions/10697995/ddg#10705799

# - Auteur : [Lilian Besson](https://perso.crans.org/besson/)
# - License : [MIT](https://lbesson.mit-license.org/)
# - Date : 27/01/2021
# - Cours : [ALGO2](http://people.irisa.fr/Francois.Schwarzentruber/algo2/) @ [ENS Rennes](http://www.dit.ens-rennes.fr/)

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Mini-tutoriel-pour-la-résolution-de-programmes-linéaires-avec-Python---ENS-Rennes-2021" data-toc-modified-id="Mini-tutoriel-pour-la-résolution-de-programmes-linéaires-avec-Python---ENS-Rennes-2021-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Mini tutoriel pour la résolution de programmes linéaires avec Python - ENS Rennes 2021</a></span><ul class="toc-item"><li><span><a href="#Références-si-vous-êtes-curieux-ses" data-toc-modified-id="Références-si-vous-êtes-curieux-ses-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Références si vous êtes curieux-ses</a></span></li><li><span><a href="#Pré-requis-pour-exécuter-ce-notebook" data-toc-modified-id="Pré-requis-pour-exécuter-ce-notebook-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Pré-requis pour exécuter ce notebook</a></span></li></ul></li><li><span><a href="#Quelques-petits-problèmes-linéaires" data-toc-modified-id="Quelques-petits-problèmes-linéaires-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Quelques petits problèmes linéaires</a></span><ul class="toc-item"><li><span><a href="#Premier-problème-linéaire" data-toc-modified-id="Premier-problème-linéaire-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Premier problème linéaire</a></span></li><li><span><a href="#Problème-exemple-du-cours-sur-le-simplexe" data-toc-modified-id="Problème-exemple-du-cours-sur-le-simplexe-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Problème exemple du cours sur le simplexe</a></span><ul class="toc-item"><li><span><a href="#Exercice-1-:-sur-ce-problème,-cherchez-quelles-contraintes-(inégalités)-sont-saturées-(devenues-des-égalités)" data-toc-modified-id="Exercice-1-:-sur-ce-problème,-cherchez-quelles-contraintes-(inégalités)-sont-saturées-(devenues-des-égalités)-2.2.1"><span class="toc-item-num">2.2.1&nbsp;&nbsp;</span><strong>Exercice 1</strong> : sur ce problème, cherchez quelles contraintes (inégalités) sont saturées (devenues des égalités)</a></span></li><li><span><a href="#Exercice-2-:-résoudre-un-autre-problème-vu-en-cours" data-toc-modified-id="Exercice-2-:-résoudre-un-autre-problème-vu-en-cours-2.2.2"><span class="toc-item-num">2.2.2&nbsp;&nbsp;</span><strong>Exercice 2</strong> : résoudre un autre problème vu en cours</a></span></li><li><span><a href="#Bonus-:-réfléchir-à-une-situation-de-votre-vie-personnelle-qui-pourrait-être-mis-en-forme-comme-un-problème-linéaire" data-toc-modified-id="Bonus-:-réfléchir-à-une-situation-de-votre-vie-personnelle-qui-pourrait-être-mis-en-forme-comme-un-problème-linéaire-2.2.3"><span class="toc-item-num">2.2.3&nbsp;&nbsp;</span>Bonus : réfléchir à une situation de votre vie personnelle qui pourrait être mis en forme comme un problème linéaire</a></span></li></ul></li><li><span><a href="#Comparer-différentes-méthodes-:" data-toc-modified-id="Comparer-différentes-méthodes-:-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Comparer différentes méthodes :</a></span><ul class="toc-item"><li><span><a href="#Exercice-3-:-sur-un-problème-de-votre-choix,-testez-au-moins-deux-méthodes." data-toc-modified-id="Exercice-3-:-sur-un-problème-de-votre-choix,-testez-au-moins-deux-méthodes.-2.3.1"><span class="toc-item-num">2.3.1&nbsp;&nbsp;</span><strong>Exercice 3</strong> : sur un problème de votre choix, testez au moins deux méthodes.</a></span></li><li><span><a href="#Exercice-4-:-Chercher-un-problème-qui-donne-une-réponse-différente-sur-deux-méthodes-différentes." data-toc-modified-id="Exercice-4-:-Chercher-un-problème-qui-donne-une-réponse-différente-sur-deux-méthodes-différentes.-2.3.2"><span class="toc-item-num">2.3.2&nbsp;&nbsp;</span><strong>Exercice 4</strong> : Chercher un problème qui donne une réponse différente sur deux méthodes différentes.</a></span></li></ul></li><li><span><a href="#Conclusion" data-toc-modified-id="Conclusion-2.4"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>Conclusion</a></span></li></ul></li></ul></div>

# ## Pré-requis pour exécuter ce notebook
# 
# - Soit vous le téléchargez et vous l'utilisez localement, dans ce cas il faut que vous ayez installé le module `scipy`.
#   + Utilisez votre gestionnaire de paquet système (`apt-get` par exemple) si Python installé par ce gestionnaire ;
#   + Utilisez `pip install scipy` ou pip3, ou avec `sudo pip` (Linux/Mac) ou pip.exe (Windows) si modules Python gérés avec [pip](https://pypi.org/) (recommandé) ;
#   + Utilisez `conda install scipy` si modules Python gérés avec conda (si installé avec [Anaconda](https://www.anaconda.com/products/individual).
# 
# - Soit vous utilisez le lien fourni dans Discord pour exécuter ce notebook dans un environnement en ligne, avec [MyBinder](https://mybinder.org/) (gratuit libre et sans connexion).

# In[21]:


try:
    import scipy.optimize
except ImportError:
    print("Vous avez lu le paragraphe précédent...?")
    print("Je t'envoie sur https://scipy.org/install.html et tu auras plus d'informations...")
    import webbrowser
    webbrowser.open_new_tab("https://scipy.org/install.html")


# ----
# # Quelques petits problèmes linéaires

# ## Premier problème linéaire
# 
# Il vient du tutoriel [susmentionné](https://medium.com/better-programming/how-to-solving-linear-programming-problems-with-examples-and-implementation-in-python-a7b7061bafc9) :

# In[44]:


# Objective Function: 50x_1 + 80x_2
# Constraint 1: 5x_1 + 2x_2 <= 20
# Constraint 2: -10x_1 + -12x_2 <= -90

result = scipy.optimize.linprog(
    [50, 80],  # Cost function: 50x_1 + 80x_2
    A_ub=[[5, 2], [-10, -12]],  # Coefficients for inequalities
    b_ub=[20, -90],  # Constraints for inequalities: 20 and -90
    bounds=(0, None), # Bounds on x, 0 <= x_i <= +oo by default
)


# On utilise les fonctionnalités de scipy pour les problèmes linéaires ([doc](https://docs.scipy.org/doc/scipy/reference/optimize.html#linear-programming)), et pour commencer [la seule fonction `scipy.optimize.linprog`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html#scipy.optimize.linprog) :

# In[45]:


if result.success:
    print(f"X1: {round(result.x[0], 2)} hours")
    print(f"X2: {round(result.x[1], 2)} hours")
else:
    print("No solution")


# Et voilà, pas plus compliqué !
# 
# Vous pourrez observer que le résultat de l'appel à cette fonction (si tout marche bien) est un objet qui encapsule plusieurs choses :
# 
# - la valeur de la solution, `result.x` ;
# - le nombre d'itérations, `result.nit` ;
# - l'état des slacks variables (cf cours sur le simplexe), `result.slack` ;
# - évaluation de l'état de l'optimisation, `result.success`, et `result.message` ;
# - et même la valeur de la fonction objectif à ce point solution (c'est utile pour gagner du temps, si cette fonction objectif est très couteuse, par exemple quand on apprend un gros réseau de neurone, avec d'autres solveurs).

# In[26]:


print(result)


# ## Problème exemple du cours sur le simplexe
# 
# Attention, généralement les solveurs cherchent à **minimiser** la fonction de coût, pas à la maximiser !
# 
# <span style="color:red;">C'est un piège classique, on rentre le problème, le solveur répond [0,0,..,0] comme solution, et on ne sait pas ce qui n'a pas marché...</span>

# In[54]:


# Objective Function: x_1 + 6*x_2 + 13*x_3
# Constraint 1: x_1 <= 200
# Constraint 2: x_2 <= 300
# Constraint 3: x_1 + x_2 + x_3 <= 400
# Constraint 4: x_2 + 3*x_3 <= 600
# les variables sont supposées positives par défaut
# x_1 >= 0
# x_2 >= 0
# x_3 >= 0

result = scipy.optimize.linprog(
    [-1, -6, -13],  # Cost function: -x_1 + -6*x_2 + -13*x_3 to MINIMIZE
    A_ub=[  # Coefficients for inequalities
        [1, 0, 0],  # for C1: 1*x_1 + 0*x_2 + 0*x_3 <= 200
        [0, 1, 0],  # for C2: 0*x_1 + 1*x_2 + 0*x_3 <= 300
        [1, 1, 1],  # for C3: 1*x_1 + 1*x_2 + 1*x_3 <= 400
        [0, 1, 3],  # for C4: 0*x_1 + 1*x_2 + 3*x_3 <= 600
    ],
    b_ub=[200, 300, 400, 600],  # Constraints for inequalities: 200, 300, 400, 600
    bounds=(0, None), # Bounds on x, 0 <= x_i <= +oo by default
    method="simplex",
)


# In[55]:


print(result)


# In[56]:


if result.success:
    print(f"X1: {round(result.x[0], 2)} chocolats simples")
    print(f"X2: {round(result.x[1], 2)} pyramides")
    print(f"X2: {round(result.x[2], 2)} pyramides de luxe")
else:
    print("No solution")


# On trouve donc la solution commerciale optimale pour Charlie le chocolatier : 300 pyramides, et 100 pyramides de luxe.

# ### **Exercice 1** : sur ce problème, cherchez quelles contraintes (inégalités) sont saturées (devenues des égalités)
# 
# Indice : lire le tableau `result.slack` et l'interpréter.

# In[ ]:


# TODO
print(result)

print("Variables slack:")
print(result.slack)


# ### **Exercice 2** : résoudre un autre problème vu en cours

# ### Bonus : réfléchir à une situation de votre vie personnelle qui pourrait être mis en forme comme un problème linéaire
# 
# Un exemple que j'ai beaucoup est le suivant, qui généralise l'idée de « régime diététique optimal » : https://jeremykun.com/2014/06/02/linear-programming-and-the-most-affordable-healthy-diet-part-1/ (très bon blogue à suivre si ça vous plaît).

# ## Comparer différentes méthodes :

# Comme le dit la documentation :
# 
# > The linprog function supports the following methods:
# 
#     linprog(method=’simplex’)
#     linprog(method=’interior-point’)
#     linprog(method=’revised simplex’)
#     linprog(method=’highs-ipm’)
#     linprog(method=’highs-ds’)
#     linprog(method=’highs’)

# > Certaines méthodes peuvent ne pas être disponible sur votre installation, mais normalement `"simplex"` et `"interior-point"` sont disponibles partout.

# ### **Exercice 3** : sur un problème de votre choix, testez au moins deux méthodes.
# 
# Ce petit morceau de code peut vous aider :

# In[33]:


methods = [
    "simplex",
    "interior-point",
    #"revised-simplex",
    #"highs-ipm",
    #"highs-ds",
    #"highs",
]


# In[34]:


def solve_problem_1(method):
    return scipy.optimize.linprog(
        [50, 80],  # Cost function: 50x_1 + 80x_2
        A_ub=[[5, 2], [-10, -12]],  # Coefficients for inequalities
        b_ub=[20, -90],  # Constraints for inequalities: 20 and -90
        method=method
    )


# In[35]:


for i, method in enumerate(methods):
    # solve problem with this method
    print(f"\n- Pour la méthode #{i}, {method}...")
    solution = solve_problem_1(method)
    print(f"La solution trouvée est {solution}")


# ### **Exercice 4** : Chercher un problème qui donne une réponse différente sur deux méthodes différentes.

# Avec le code ci-dessous, cherchez un problème plus compliqué qui donne une solution différente.
# Même si la différence est faible, commentez là :
# 
# - en terme de nombre d'étape ?
# - valeurs de x* ?
# - valeur de f(x*) ?

# ---
# ## Conclusion
# 
# Si vous êtes très curieux, regardez un peu les références données en haut de ce document.
# 
# N'hésitez pas à nous contacter si vous avez des questions !
