
# coding: utf-8

# # Table des matières
# * [1. Agrégation externe de mathématiques, texte d’exercice diffusé en 2012](#1.-Agrégation-externe-de-mathématiques,-texte-d’exercice-diffusé-en-2012)
# 	* [1.1 Épreuve de modélisation, option informatique](#1.1-Épreuve-de-modélisation,-option-informatique)
# 	* [1.2 *Proposition* d'implémentation, en [Python 3](https://docs.python.org/3/)](#1.2-*Proposition*-d'implémentation,-en-[Python-3]%28https://docs.python.org/3/%29)
# 		* [1.2.1 Pour [l'option informatique (D)](http://www.dit.ens-rennes.fr/agregation-option-d/programme-de-l-option-informatique-de-l-agregation-de-mathematiques-48358.kjsp) de l'[agrégation de mathématiques](http://agreg.org/) (en France).](#1.2.1-Pour-[l'option-informatique-%28D%29]%28http://www.dit.ens-rennes.fr/agregation-option-d/programme-de-l-option-informatique-de-l-agregation-de-mathematiques-48358.kjsp%29-de-l'[agrégation-de-mathématiques]%28http://agreg.org/%29-%28en-France%29.)
# 	* [1.3 Dépendances et importation de modules](#1.3-Dépendances-et-importation-de-modules)
# 	* [1.4 Jeux de Nim](#1.4-Jeux-de-Nim)
# 		* [1.4.1 Représentation des configurations](#1.4.1-Représentation-des-configurations)
# 		* [1.4.2 Fonction de Sprague-Grundy pour le jeu de Nim](#1.4.2-Fonction-de-Sprague-Grundy-pour-le-jeu-de-Nim)
# 		* [1.4.3 Déterminer un coup à jouer selon une stratégie gagnante (s'il y en a une)](#1.4.3-Déterminer-un-coup-à-jouer-selon-une-stratégie-gagnante-%28s'il-y-en-a-une%29)
# 			* [1.4.3.1 Stratégie optimale](#1.4.3.1-Stratégie-optimale)
# 		* [1.4.4 Stratégie stupide](#1.4.4-Stratégie-stupide)
# 		* [1.4.5 Un bonus : *simulation du jeu*](#1.4.5-Un-bonus-:-*simulation-du-jeu*)
# 		* [1.4.6 Configuration aléatoire](#1.4.6-Configuration-aléatoire)
# 	* [1.5 Conclusion](#1.5-Conclusion)
# 	* [1.6 Attention :](#1.6-Attention-:)
# 

# # 1. Agrégation externe de mathématiques, texte d’exercice diffusé en 2012

# ## 1.1 Épreuve de modélisation, option informatique

# > - Ce [notebook Jupyter](http://jupyter.org/) est une correction [non officielle](https://github.com/Naereen/notebooks/tree/master/agreg) d'un texte de modélisation pour l'option informatique de l'agrégation externe de mathématiques.
# > - Il s'agit du texte [public2012-D3](http://agreg.org/Textes/public2012-D3.pdf).
# > - Cette tentative de correction partielle a été rédigée par [Lilian Besson](http://perso.crans.org/besson/) ([sur GitHub ?](https://github.com/Naereen/), [sur Bitbucket ?](https://bitbucket.org/lbesson)), et [est open-source](https://github.com/Naereen/notebooks/blob/master/agreg/public2012_D3.ipynb).
# 
# > #### Feedbacks?
# > - Vous avez trouvé un bug ? → [Signalez-le moi svp !](https://github.com/Naereen/notebooks/issues/new), merci d'avance.
# > - Vous avez une question ? → [Posez la svp !](https://github.com/Naereen/ama.fr) [![Demandez moi n'importe quoi !](https://img.shields.io/badge/Demandez%20moi-n'%20importe%20quoi-1abc9c.svg)](https://GitHub.com/Naereen/ama.fr)
# 
# ----

# ## 1.2 *Proposition* d'implémentation, en [Python 3](https://docs.python.org/3/)

# ### 1.2.1 Pour [l'option informatique (D)](http://www.dit.ens-rennes.fr/agregation-option-d/programme-de-l-option-informatique-de-l-agregation-de-mathematiques-48358.kjsp) de l'[agrégation de mathématiques](http://agreg.org/) (en France).

# **Attention** : ce document ne prétend pas être LA correction du texte, mais **un exemple de solution**.
# 
# ----

# ## 1.3 Dépendances et importation de modules

# In[73]:


import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt


# ## 1.4 Jeux de Nim

# ### 1.4.1 Représentation des configurations
# On représente une configuration `Nim(x1,..,xk)` simplement par un tableau qui contient `[x1,..,xk]` :

# In[2]:


a = [1, 3, 5]


# On va d'abord écrire une fonction toute simple qui affiche une configuration, en mode texte.
# Aucune raison de perdre son temps à en faire une plus jolie (par exemple, avec [matplotlib](http://www.matplotlib.org) qui utiliserait une fenêtre graphique).

# In[7]:


def print_nim(configuration):
    """ Affiche une configuration, donnée sous forme d'une liste d'entiers. """
    for i, nb in enumerate(configuration):
        print(i, ':', '! ' * nb)


# On peut définir et afficher deux exemples de configuration d'un jeu de Nim, venant de la figure 1.

# In[8]:


print_nim(a)


# In[9]:


b = [1, 3, 2]
print_nim(b)


# ### 1.4.2 Fonction de Sprague-Grundy pour le jeu de Nim

# Elle est donnée par le corollaire 1. en page 6/7 du texte.
# On a besoin du **xor** (*"ou exclusif"*, cf [cette page](https://fr.wikipedia.org/wiki/Fonction_OU_exclusif)), **bit à bit** (tel que $\oplus$ est défini dans le texte).
# 
# Cet opérateur est obtenu en Python avec l'opérateur ``^`` :
# 
# $$ \gamma(\mathrm{Nim}(x_1, \dots, x_k)) := \bigoplus_{i=1}^{k} x_i = x_1 \oplus \dots \oplus x_k. $$

# Petit rappel sur cette fonction **xor** :

# In[10]:


from itertools import product

for b1, b2 in product([False, True], repeat=2):
    print("{!s:>5} XOR {!s:>5} = {!s:>5} ^ {!s:>5} = {!s:>5}".format(b1, b2, b1, b2, b1 ^ b2))
# Ce morceau de code est un peu fancy mais concis et joli, cf. https://pyformat.info/#string_pad_align


# | Entrée      | |  Entrée  | Sortie  |
# | ----- |:--------:| ----- | ------: |
# | False | $\oplus$ | False | = False |
# | False | $\oplus$ | True  | = True  |
# | True  | $\oplus$ | False | = True  |
# | True  | $\oplus$ | True  | = False |

# - Ensuite, d'autres valeurs, juste pour tester :

# In[12]:


3  ^ 5  # 3  xor 5  =  0b011  xor 0b101  = 0b111  = 6


# In[13]:


5  ^ 9  # 5  xor 9  =  0b0101 xor 0b1001 = 0b1100 = 12


# In[14]:


12 ^ 1  # 12 xor 1  =  0b1100 xor 0b0001 = 0b1101 = 13


# In[15]:


12 ^ 2  # 12 xor 2  =  0b1100 xor 0b0010 = 0b1110 = 14


# ----
# D'apres le corollaire 1., il suffit d'appliquer un **xor** à chaque valeur du tableau pour calculer $\gamma$.
# 
# On peut faire ça simplement avec une boucle :

# In[24]:


def gamma(configuration):
    """ Fonction gamma de Sprague-Grundy pour le jeu de Nim. """
    resultat = 0
    for nb in configuration:
        resultat = (resultat ^ nb)
    return resultat


# In[25]:


print("Gamma(a) =", gamma(a))
print("Gamma(b) =", gamma(b))


# On peut aussi obtenir pareil avec la fonction `functools.reduce`, qui fait comme `Array.fold_left` en OCaml.

# In[28]:


from functools import reduce  # Comme Array.fold_left ou List.fold_left en OCaml
from operator  import xor     # Version préfixe de l'opérateur ^ infixe

def gamma(configuration):
    """ Fonction gamma de Sprague-Grundy pour le jeu de Nim. """
    return reduce(xor, configuration)


# In[27]:


print("Gamma(a) =", gamma(a))
print("Gamma(b) =", gamma(b))


# ### 1.4.3 Déterminer un coup à jouer selon une stratégie gagnante (s'il y en a une)

# On suit l'algorithme proposé par le texte, qui utilise la fonction $\gamma$ sur la configuration pour savoir s'il y a une stratégie ou non (d'après la proposition 5.), et ensuite si elle existe on doit trouver un coup qui ammene $\gamma$ à 0.
# 
# On a d'abord besoin d'une exception pour signaler s'il n'y a pas de stratégie gagnante, et du calcul du nombre minimal d'allumette à enlever.

# In[33]:


class PasDeStratGagnante(Exception):
    """ Exception renvoyée s'il n'y a pas de stratégie gagnante. """
    pass


# #### 1.4.3.1 Stratégie optimale
# L'algorithme va être assez naïf, depuis une configuration actuelle $c$ :
# - si $\gamma(c)$ est $0$, on échoue (`PasDeStratGagnante`),
# - sinon, on explore toutes les configurations $c'$ atteignables en un coup depuis $c$, et on choisis la première qui amène à $\gamma(c') = 0$.

# In[34]:


def optimal(configuration, joueur=0):
    """ Essaie de trouver un coup à jouer pour le joueur 0 ou 1, et renvoit la configuration modifiée."""
    g = gamma(configuration)
    if g == 0:
        print("Il n'y a pas de stratégie gagnante !")
        raise PasDeStratGagnante  # On quitte
    print("Il y a une stratégie gagnante... Trouvons la !")
    # On chercher le coup à jouer : il suffit d'explorer tous les coups possibles
    colonne = 0
    nb = 1
    nouvelle_configuration = configuration[:]
    for j in range(len(configuration)):
        for i in range(1, configuration[j]):
            nouvelle_configuration[j] -= i  # On tente de jouer ce coup
            if gamma(nouvelle_configuration) == 0:
                colonne, nb = j, i  # On stocke j, i
            nouvelle_configuration = configuration[:]  # On l'annule
    # On devrait avoir trouver un coup qui amène gamma(nouvelle_configuration) = 0
    # On applique ce coup
    print("Le joueur courant", joueur, "a choisi de retirer", nb, "allumettes à la rangée numéro", colonne)
    nouvelle_configuration = configuration[:]
    nouvelle_configuration[colonne] -= nb
    if gamma(nouvelle_configuration) != 0:
        print("  Attention, apparemment on a été contraint de choisir un coup qui n'est pas gagnant (n'amène pas à gamma(c') = 0).")
    return nouvelle_configuration


# On peut tester cette fonction sur nos deux configuration a et b :

# In[35]:


print_nim(a)
print_nim(optimal(a, joueur=0))  # Ça joue


# In[36]:


print_nim(b)
print_nim(optimal(b, joueur=0))  # Pas de stratégie gagnante ici !


# ### 1.4.4 Stratégie stupide

# Dans le but de comparer cette fonction qui implémente une stratégie optimale, on implémente aussi une stratégie complétement aléatoire ("Dummy player").
# 
# La stratégie aléatoire fonctionne en trois étapes :
# 1. trouve les rangées qui ont encore des allumettes (en calculant leurs indices, via une construction de tableau par compréhension, dans le tableau `lignes_non_vides`),
# 2. choisi une rangée aléatoirement `i` (uniformément) avec `random.choice()`,
# 3. enlève un nombre aléatoire (uniforme) d'allumette entre `1` et `xi`, pour `xi` le nombre d'allumette dans la rangée `i` (i.e., `xi = config.(i)`).

# In[37]:


def stupide(configuration, joueur=0):
    """ Choisit un coup aléatoire (uniforme) pour le joueur 0 ou 1, et renvoit la configuration modifiée."""
    # On choisit le coup à jouer : ligne random, nb d'allumette(s) random...
    lignes_non_vides = [i for i, c in enumerate(configuration) if c > 0]
    position_random = random.choice(lignes_non_vides)
    print("Le joueur", joueur, "aléatoire uniforme a choisi de regarder la ligne", position_random)
    total = configuration[position_random]
    a_enlever = random.randint(1, 1 + total)
    print("Le joueur", joueur, "aléatoire uniforme a choisi de retirer", a_enlever, "allumettes parmi les", total, "disponibles")
    # On applique ce coup
    nouvelle_configuration = configuration[:]
    nouvelle_configuration[position_random] -= a_enlever
    return nouvelle_configuration


# On peut ainsi faire un exemple de début de partie entre deux joueurs "stupides" :

# In[39]:


random.seed(0)  # Assure la reproductibilité des résultats.
a0 = a  # Debut du jeu
print_nim(a0)
a1 = stupide(a0, joueur=0)
print_nim(a1)
a2 = stupide(a1, joueur=1)
print_nim(a2)
a3 = stupide(a2, joueur=0)
print_nim(a3)
# ... etc


# On peut aussi faire le même exemple de début de partie entre un joueur "optimal" et un joueur "stupide" :

# In[40]:


random.seed(0)  # Assure la reproductibilité des résultats.
a0 = a  # Debut du jeu
print_nim(a0)
a1 = optimal(a0, joueur=0)
print_nim(a1)
a2 = stupide(a1, joueur=1)
print_nim(a2)
# ... etc


# ### 1.4.5 Un bonus : *simulation du jeu*

# Maintenant qu'on dispose d'un joueur stupide et d'un joueur optimal, on peut rapidement coder une petite fonction qui les fera s'affronter (même si c'est un peu cruel envers le pauvre joueur "stupide" purement aléatoire !).

# In[41]:


class Perdu(Exception):
    """ Représente le joueur numero i qui a perdu."""
    def __init__(self, numero):
        self.numero = numero

    def __str__(self):
        return "Le joueur {} a perdu !".format(self.numero)


# La fonction ``simule`` va jouer la partie, en partant de la configuration donnée, en commençant par le joueur ``numero`` et pour un certain nombre de coups joués (``nb_coups``).
# Si on ne donne pas ce nombre de coups, le nombre total d'allumette est utilisé (sachant qu'une partie se termine souvent par une exception ``PasDeStratGagnante`` lorsque le joueur optimal ne peut plus gagner).

# In[49]:


def simule(configuration, numero=0, nb_coups=None):
    """ Simule le jeu de Nim, alternant un joeur malin et un joueur stupide. """
    config = configuration[:]  # On ne change pas la liste donnee en argument !
    # Si on n'a pas donne le nb de coups max, on calcule une borne :
    if nb_coups is None:
        nb_coups = sum(configuration)
    print("Début de la simulation pour maximum", nb_coups, "coups.")
    # On lance la simulation
    for coup in range(1, 1 + nb_coups):
        print("\n# Tour numéro", coup)
        print_nim(config)
        # On perd si on ne peut plus enlever d'allumettes
        if not config or sum(config) == 0:
            raise Perdu(numero)
        else:
            if numero == 0:  # Joueur malin
                config = optimal(config, joueur=numero)
            else:  # Joueur stupide
                config = stupide(config, joueur=numero)
        # Joueur suivant
        numero = 1 - numero  # 0 -> 1, 1 -> 0
    # A la fin, la configuration finale est renvoyée.
    return config


# On peut finalement implementer une jolie fonction qui simule en partant du joueur ``0`` (comme le vrai jeu de Nim) et interprète l'exception renvoyée pour afficher l'issue du jeu :

# In[60]:


def nim(configuration):
    try:
        simule(configuration)
    except PasDeStratGagnante:
        print("==> Blocage car le joueur 0 n'a pas pu trouver de coup gagnant, il déclare forfait (le pleutre !).")
    except Perdu as e:
        print("==> Le joueur", e.numero, "a perdu.")


# In[62]:


nim(a)


# In[64]:


nim(b)


# ### 1.4.6 Configuration aléatoire

# On peut écrire une fonction qui génére une configuration aléatoire, et ensuite lancer notre simulation ``nim()`` dessus, pour voir ce que ça donne sur une configuration plus grande.
# 
# La fonction `config_aleatoire(k, p)` va générer une configuration aléatoire :
# 
# - avec un nombre de lignes uniforme dans `{1, ..., k}`,
# - et un nombre d'allumettes uniforme dans `{1, ..., p}` pour chaque ligne.

# In[74]:


def config_aleatoire(nb_ligne, nb_max_allumette):
    """ Configuration aléatoire, chaque ligne est uniformément tirée dans [1, nb_max_allumette] (bornes incluses)."""
    return list(random.randint(1, 1 + nb_max_allumette, nb_ligne))


# In[81]:


c = config_aleatoire(4, 4)
print("Configuration random c :")
print_nim(c)
nim(c)


# ----

# ## 1.5 Conclusion

# C'est tout ce que j'avais eu le temps d'implémenter durant les 4h de préparation (c'est un des textes que j'avais préparé en juin 2014, dans les "vraies" conditions en oraux blanc, à l'ENS Cachan, et le code initial était en OCaml mais je n'ai rien changé à part la conversion en Python3).
# 
# Quelques remarques :
# 
# - durant l'épreuve de modélisation, vous êtes libres de faire ce que vous voulez, la seule partie requise est dans le paragraphe **Exercice de programmation** (ici, il s'agissait d'implémenter une fonction similaire à ``optimal()`` (cf. plus haut).
# - les quelques développements supplémentaires traites ci-dessus (stratégie stupide, configuration aléatoire, simulation de jeu), ne sont qu'une suggestion de ce qui pouvait être fait sur ce texte,
# - d'autres suggestions sont possibles, si vous avez des idées, [envoyez-moi vos notebooks !](https://github.com/Naereen/notebooks/pulls).
# 
# > *Edit :* j'avais une erreur dans mon calcul de `next`, corrigée le 11/01/17.

# ## 1.6 Attention :

# Les 40 minutes de passage au tableau ne doivent PAS être uniquement consacrée à la présentation de vos expériences sur l'ordinateur !
# 
# Il faut aussi :
# 
# - faire une introduction générale (citer des mots clés),
# - présenter le plan de votre présentation,
# - introduire les notations, les objectifs et les résultats donnés par le texte,
# - prouver ou exposer des développements **theoriques** personnels (à choisir parmi la liste proposée, mais pas seulement),
# - etc.

# ----
# 
# > *C'est tout pour aujourd'hui les amis !*
# > [Allez voir d'autres notebooks](https://github.com/Naereen/notebooks/tree/master/agreg) si vous voulez.
