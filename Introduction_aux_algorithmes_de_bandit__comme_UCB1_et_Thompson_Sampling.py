
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#Introduction-aux-algorithmes-de-bandit-(UCB1,-Thompson-Sampling)" data-toc-modified-id="Introduction-aux-algorithmes-de-bandit-(UCB1,-Thompson-Sampling)-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction aux <em>algorithmes de bandit</em> (UCB1, Thompson Sampling)</a></div><div class="lev2 toc-item"><a href="#Problèmes-de-bandit" data-toc-modified-id="Problèmes-de-bandit-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Problèmes de bandit</a></div><div class="lev3 toc-item"><a href="#Problèmes-stochastiques" data-toc-modified-id="Problèmes-stochastiques-111"><span class="toc-item-num">1.1.1&nbsp;&nbsp;</span>Problèmes stochastiques</a></div><div class="lev3 toc-item"><a href="#Radio-intelligente-?" data-toc-modified-id="Radio-intelligente-?-112"><span class="toc-item-num">1.1.2&nbsp;&nbsp;</span>Radio intelligente ?</a></div><div class="lev2 toc-item"><a href="#Simulation-de-problèmes-de-bandit" data-toc-modified-id="Simulation-de-problèmes-de-bandit-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Simulation de problèmes de bandit</a></div><div class="lev2 toc-item"><a href="#Bras-stochastiques,-de-Bernoulli" data-toc-modified-id="Bras-stochastiques,-de-Bernoulli-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Bras stochastiques, de Bernoulli</a></div><div class="lev2 toc-item"><a href="#Présentation-des-algorithmes-de-bandit" data-toc-modified-id="Présentation-des-algorithmes-de-bandit-14"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Présentation des algorithmes de bandit</a></div><div class="lev2 toc-item"><a href="#Deux-algorithmes-naïfs" data-toc-modified-id="Deux-algorithmes-naïfs-15"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Deux algorithmes naïfs</a></div><div class="lev3 toc-item"><a href="#ChoixUniforme" data-toc-modified-id="ChoixUniforme-151"><span class="toc-item-num">1.5.1&nbsp;&nbsp;</span><code>ChoixUniforme</code></a></div><div class="lev3 toc-item"><a href="#MoyenneEmpirique" data-toc-modified-id="MoyenneEmpirique-152"><span class="toc-item-num">1.5.2&nbsp;&nbsp;</span><code>MoyenneEmpirique</code></a></div><div class="lev2 toc-item"><a href="#Approche-fréquentiste,-UCB1,-&quot;Upper-Confidence-Bound&quot;" data-toc-modified-id="Approche-fréquentiste,-UCB1,-&quot;Upper-Confidence-Bound&quot;-16"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Approche fréquentiste, UCB1, "Upper Confidence Bound"</a></div><div class="lev2 toc-item"><a href="#Variantes-d'UCB-:-UCB-V-et-UCB-H" data-toc-modified-id="Variantes-d'UCB-:-UCB-V-et-UCB-H-17"><span class="toc-item-num">1.7&nbsp;&nbsp;</span>Variantes d'UCB : UCB-V et UCB-H</a></div><div class="lev2 toc-item"><a href="#Approche-fréquentiste-optimale,-KL-UCB,-&quot;Kullback-Leibler-UCB&quot;" data-toc-modified-id="Approche-fréquentiste-optimale,-KL-UCB,-&quot;Kullback-Leibler-UCB&quot;-18"><span class="toc-item-num">1.8&nbsp;&nbsp;</span>Approche fréquentiste optimale, KL-UCB, "Kullback-Leibler UCB"</a></div><div class="lev3 toc-item"><a href="#KL-binaire" data-toc-modified-id="KL-binaire-181"><span class="toc-item-num">1.8.1&nbsp;&nbsp;</span>KL binaire</a></div><div class="lev3 toc-item"><a href="#KLUCB" data-toc-modified-id="KLUCB-182"><span class="toc-item-num">1.8.2&nbsp;&nbsp;</span>KLUCB</a></div><div class="lev2 toc-item"><a href="#Approche-bayésienne,-Thompson-Sampling" data-toc-modified-id="Approche-bayésienne,-Thompson-Sampling-19"><span class="toc-item-num">1.9&nbsp;&nbsp;</span>Approche bayésienne, Thompson Sampling</a></div><div class="lev2 toc-item"><a href="#Exemples-de-simulations" data-toc-modified-id="Exemples-de-simulations-110"><span class="toc-item-num">1.10&nbsp;&nbsp;</span>Exemples de simulations</a></div><div class="lev3 toc-item"><a href="#Fonctions-pour-l'affichage" data-toc-modified-id="Fonctions-pour-l'affichage-1101"><span class="toc-item-num">1.10.1&nbsp;&nbsp;</span>Fonctions pour l'affichage</a></div><div class="lev3 toc-item"><a href="#Premier-problème,-à-3-bras" data-toc-modified-id="Premier-problème,-à-3-bras-1102"><span class="toc-item-num">1.10.2&nbsp;&nbsp;</span>Premier problème, à 3 bras</a></div><div class="lev3 toc-item"><a href="#Second-problème,-à-9-bras" data-toc-modified-id="Second-problème,-à-9-bras-1103"><span class="toc-item-num">1.10.3&nbsp;&nbsp;</span>Second problème, à 9 bras</a></div><div class="lev3 toc-item"><a href="#Troisième-problème,-simulé-100-fois" data-toc-modified-id="Troisième-problème,-simulé-100-fois-1104"><span class="toc-item-num">1.10.4&nbsp;&nbsp;</span>Troisième problème, simulé 100 fois</a></div><div class="lev3 toc-item"><a href="#Dernier-problème" data-toc-modified-id="Dernier-problème-1105"><span class="toc-item-num">1.10.5&nbsp;&nbsp;</span>Dernier problème</a></div><div class="lev2 toc-item"><a href="#Une-autre-politique-d'indice-:-ApproximatedFHGittins" data-toc-modified-id="Une-autre-politique-d'indice-:-ApproximatedFHGittins-111"><span class="toc-item-num">1.11&nbsp;&nbsp;</span>Une autre politique d'indice : ApproximatedFHGittins</a></div><div class="lev3 toc-item"><a href="#Comparaison-de-ApproximatedFHGittins-avec-les-autres-algorithmes" data-toc-modified-id="Comparaison-de-ApproximatedFHGittins-avec-les-autres-algorithmes-1111"><span class="toc-item-num">1.11.1&nbsp;&nbsp;</span>Comparaison de <code>ApproximatedFHGittins</code> avec les autres algorithmes</a></div><div class="lev2 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-112"><span class="toc-item-num">1.12&nbsp;&nbsp;</span>Conclusion</a></div>

# # Introduction aux *algorithmes de bandit* (UCB1, Thompson Sampling)
# Ce petit document est un [notebook Jupyter](https://www.jupyter.org), ayant pour but de présenter le concept de problèmes de bandit, comment les simuler et les résoudre, et deux algorithmes conçus dans ce but.
# 
# Je ne vais pas donner beaucoup d'explications mathématiques, je conseille plutôt [ce petit article, datant de 2017, en français, écrit par Émilie Kaufmann](http://chercheurs.lille.inria.fr/ekaufman/Matapli_Kaufmann.pdf).
# 
# Je préfère me focaliser sur une implémentation simple, claire et concise de chaque morceau nécessaire à la simulation de problèmes et d'algorithmes de bandit.
# J'utilise le [langage de programmation Python](https://www.python.org/).
# 
# Dans ce but, j'utilise une approche *objet* : chaque morceau sera une classe, et des *instances* (des *objets*) seront utilisées pour toutes les composantes.

# In[1]:


# Dépendances
import numpy as np
import random as rd


# In[2]:


import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(context="notebook", style="whitegrid", palette="hls", font="sans-serif", font_scale=1.4)
from tqdm import tqdm_notebook as tqdm


# In[3]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -m -a "Lilian Besson (Naereen)" -p scipy,numpy,matplotlib,sympy,seaborn -g')


# ----
# ## Problèmes de bandit
# 
# Je ne rentrerai pas trop dans les détails ici. Pour plus d'explications, [cette page Wikipédia (en français)](https://fr.wikipedia.org/wiki/Bandit_manchot_(math%C3%A9matiques)) est très bien faite.
# 
# > "Dans le problème dit du bandit manchot, un utilisateur fait face à $K \geq 2$ machines à sou. Chacune donnant une récompense moyenne que l'utilisateur ne connait pas à priori. A chacune de ces actions, il va donc sélectionner une machine permettant de maximiser son gain."
# 
# ### Problèmes stochastiques
# On se focalise ici sur des problèmes dits stochastiques : pour chaque bras, $k\in\{1,\dots,K\}$, une [distribution de probabilité](https://fr.wikipedia.org/wiki/Distribution_de_probabilit%C3%A9s) $\nu_k$ est supposée générer les récompense à chaque sélection.
# Les récompenses $r_k(t)$ venant du $k$ième bras sont donc "i.i.d." : indépendentes (les unes des autres) et identiquement distribuées, selon $\nu_k$ :
# $$ \forall t \geq 1, \;\; r_k(t) \sim \nu_k. $$
# 
# Un des exemples les plus simples sera de considérer des [lois de Bernoulli](https://fr.wikipedia.org/wiki/Loi_de_Bernoulli), avec des *récompenses binaires*, par exemple pour un traitement médical $r_k(t) = 0$ signifie que le traitement a échoué, et $r_k(t) = 1$ que le traitement a réussi à guérir telle maladie :
# $$ \forall t \geq 1, r_k(t) \in \{0,1\}, \;\text{et}\; r_k(t) \sim \mathrm{B}(\mu_k). $$
# 
# ### Radio intelligente ?
# Dans le contexte de la [radio intelligente](http://orbi.ulg.be/bitstream/2268/16757/1/SCS09_Jouini_Wassim.pdf), le vocabulaire change un peu :
# 
# - les bras sont des *canaux radio*,
# - les joueurs sont des *objets communiquants*,
# - et des *récompenses binaires* sont obtenues soit avant la communication (avec une écoute du spectre, "sensing", pour l'Accès Opportuniste au Spectre, "OSA"), soit après la communication (avec un "acknowledgement" reçu depuis une station de base),
# - ou bien des *récompenses réelles*, reflétant par exemple le SNR de la communication, le débit, la puissance reçue etc.

# ----
# ## Simulation de problèmes de bandit
# 
# Une simple *fonction* suffira ici, pour initialiser un algorithme, le simuler durant $T$ étapes, et stocker les récompenses et les bras tirés.
# 
# Il est important de tout stocker pour ensuite pouvoir afficher différentes statistiques sur l'expérience, permettant d'évaluer l'efficacité des différentes algorithmes.
# 
# Je préfère donner directement cette fonction afin de fixer les *signatures* des différentes classes qu'on va écrire ensuite :
# 
# - Les *bras* ont besoin d'une seule méthode, `tire()` qui donne $r_k(t) \sim \nu_k$ à l'instant $t$ pour la distribution $\nu_k$ du $k^{\text{ième}}$ bras, noté `r_k_t`.
# - Les *algorithmes* ont besoin de trois méthodes :
#     + `commence()` pour initialiser l'algorithme, une fois,
#     + `A_t = choix()` pour choisir un bras, à chaque instant $t$, noté $A(t) \in \{1,\dots,K\}$,
#     + `recompense(A_t, r_k_t)` pour donner la récompense `r_k_t` tirée du bras `A_t`.

# In[4]:


def simulation(bras, algorithme, horizon):
    """ Simule l'algorithme donné sur ces bras, durant horizon étapes."""
    choix, recompenses = np.zeros(horizon), np.zeros(horizon)
    # 1. Initialise l'algorithme
    algorithme.commence()
    # 2. Boucle en temps, pour t = 0 à horizon - 1
    for t in range(horizon):
        # 2.a. L'algorithme choisi son bras à essayer
        A_t = algorithme.choix()
        # 2.b. Le bras k donne une récompense
        r_k_t = bras[A_t].tire()
        # 2.c. La récompense est donnée à l'algorithme
        algorithme.recompense(A_t, r_k_t)
        # 2.d. On stocke les deux
        choix[t] = A_t
        recompenses[t] = r_k_t
    # 3. On termine en renvoyant ces deux vecteurs
    return recompenses, choix


# ----
# ## Bras stochastiques, de Bernoulli
# 
# Les récompenses de tels bras, notées $r_k(t)$ pour le bras $k$ à l'instant $t$, sont tirées de façons identiquement distribuées et indépendantes, selon une loi de Bernoulli :
# $$ \forall t\in\mathbb{N}, \forall k\in\{1,\dots,K\}, r_k(t) \in \{0,1\}, \;\text{et}\; r_k(t) \sim \mathrm{B}(\mu_k). $$

# In[5]:


class Bernoulli():
    """ Bras distribués selon une loi de Bernoulli."""

    def __init__(self, probabilite):
        assert 0 <= probabilite <= 1, "Erreur, probabilite doit être entre 0 et 1 pour un bras de Bernoulli."
        self.probabilite = probabilite

    def tire(self):
        """ Tire une récompense aléatoire."""
        return float(rd.random() <= self.probabilite)


# Par exemple, on peut considérer le problème à trois bras ($K = 3$), caractérisé par ces paramètres $\boldsymbol{\mu} = [\mu_1,\dots,\mu_K] = [0.1, 0.5, 0.9]$ :

# In[6]:


mus = [ 0.1, 0.5, 0.9 ]
bras = [ Bernoulli(mu) for mu in mus ]


# On peut prendre 10 échantillons de chaque bras, et vérifier leurs moyennes :

# In[7]:


rd.seed(10000)  # pour être reproductible.
T = 10
exemples_echantillons = [ [ bras_k.tire() for _ in range(T) ] for bras_k in bras ]
exemples_echantillons


# In[8]:


np.mean(exemples_echantillons, axis=1)


# > C'est assez proche de $\boldsymbol{\mu} = [\mu_1,\dots,\mu_K] = [0.1, 0.5, 0.9]$...

# ----
# ## Présentation des algorithmes de bandit
# Comme on l'a dit plus haut, les *algorithmes* ont besoin de trois méthodes :
# 
# - `commence()` pour initialiser l'algorithme, une fois. Généralement, il s'agit de remettre à zero les vecteurs de mémoires internes de l'algorithme, et de mettre $t = 0$.
# - `A_t = choix()` pour choisir un bras, à chaque instant $t$, noté $A(t) \in \{1,\dots,K\}$. C'est la partie "intelligente" qui doit être conçue avec soin.
# - `recompense(A_t, r_k_t)` pour donner la récompense `r_k_t` tirée du bras `A_t`. Souvent, il suffit de mettre à jour les deux ou trois vecteurs internes.
# 
# En fait, il faut aussi une méthode pour *créer* l'instance de la classe, i.e., une méthode `__init__(K)`, qui demande de simplement connaître $K$, le nombre de bras.
# 
# > Bien-sûr, les algorithmes ne doivent pas connaître $\boldsymbol{\mu} = [\mu_1,\dots,\mu_K]$ les paramètres du problème... Sinon l'apprentissage n'a aucun intérêt : il suffit de viser $k^* = \arg\max_k \mu_k$...
# 
# - Lisez [ce paragraphe sur la page Wikipédia précédemment citée](https://fr.wikipedia.org/wiki/Bandit_manchot_(math%C3%A9matiques)#R.C3.A9solution_du_probl.C3.A8me), il est assez instructif.

# ----
# ## Deux algorithmes naïfs
# On va commencer par donner deux exemples naïfs :
# 
# 1. Un algorithme "stupide" qui choisi un bras de façon complètement uniforme, $A^{1}(t) \sim U(1,\dots,K), \forall t$, à chaque instant $t \in \mathbb{N}$, via la classe `ChoixUniforme`.
# 
# 2. Un algorithme moins stupide, mais assez naïf, qui utilise un *estimateur empirique* $\widehat{\mu_k}(t) = \frac{X_k(t)}{N_k(t)}$ de la *moyenne* de chaque bras, et tire $A^{2}(t) \in \arg\max_k \widehat{\mu_k}(t)$ à chaque instant $t \in \mathbb{N}$. Ici, $X_k(t) = \sum_{\tau=0}^{t} \mathbb{1}(A(\tau) = k) r_k(\tau)$ compte les récompenses *accumulées* en tirant le bras $k$, sur les instants $t = 0,\dots,\tau$. Et $N_k(t) = \sum_{\tau=0}^{t} \mathbb{1}(A(\tau) = k)$ compte le nombre de sélections de ce bras $k$. Via la classe `MoyenneEmpirique`.

# ### `ChoixUniforme`
# 
# C'est l'algorithme le plus naïf : à chaque instant, le bras choisi est tiré uniformément dans $\{0,\dots,K-1\}$ (notation Python, on indice à partir de $0$).

# In[9]:


class ChoixUniforme(object):
    """Algorithme stupide, choix uniforme."""
    
    def __init__(self, K):
        """Crée l'instance de l'algorithme."""
        self.K = K
    
    def commence(self):
        """Initialise l'algorithme : rien à faire ici."""
        pass
    
    def choix(self):
        """Choix uniforme d'un indice A(t) ~ U(1...K)."""
        return rd.randint(0, self.K - 1)
        
    def recompense(self, k, r):
        """Donne une récompense r tirée sur le bras k à l'algorithme : rien à faire ici."""
        pass


# ### `MoyenneEmpirique`
# Voilà qui donne une bonne idée de la structure que vont devoir suivre les différentes algorithmes.
# 
# L'algorithme suivant est un peu plus complexe. Il est aussi appelé "Follow the Leader" (FTL).

# In[10]:


class MoyenneEmpirique(object):
    """Algorithme naïf, qui utilise la moyenne empirique."""
    
    def __init__(self, K):
        """Crée l'instance de l'algorithme."""
        self.K = K
        # Il nous faut de la mémoire interne
        self.recompenses = np.zeros(K)  # X_k(t) pour chaque k
        self.tirages = np.zeros(K)      # N_k(t) pour chaque k
        self.t = 0                      # Temps t interne
    
    def commence(self):
        """Initialise l'algorithme : remet à zeros chaque X_k et N_k, et t = 0."""
        self.recompenses.fill(0)
        self.tirages.fill(0)
        self.t = 0
    
    def choix(self):
        """Si on a vu tous les bras, on prend celui de moyenne empirique la plus grande."""
        # 1er cas : il y a encore des bras qu'on a jamais vu
        if np.min(self.tirages) == 0:
            k = np.min(np.where(self.tirages == 0)[0])
        # 2nd cas : tous les bras ont été essayé
        else:
            # Notez qu'on aurait pu ne stocker que ce vecteur moyennes_empiriques
            moyennes_empiriques = self.recompenses / self.tirages
            k = np.argmax(moyennes_empiriques)
        self.t += 1      # Inutile ici
        return k
        
    def recompense(self, k, r):
        """Donne une récompense r tirée sur le bras k à l'algorithme : met à jour les deux vecteurs internes."""
        self.recompenses[k] += r
        self.tirages[k] += 1


# ----
# ## Approche fréquentiste, UCB1, "Upper Confidence Bound"
# 
# Il s'agit d'une amélioration de l'algorithme précédent, où on utilise un autre *indice*.
# 
# Au lieu d'utiliser la moyenne empirique $g_k(t) = \widehat{\mu_k}(t) = \frac{X_k(t)}{N_k(t)}$ et $A(t) = \arg\max_k  g_k(t)$, on utilise une borne supérieure d'un intervalle de confiance autour de cette moyenne :
# $$g'_k(t) = \widehat{\mu_k}(t) + \sqrt{\alpha \frac{\log t}{N_k(t)}}.$$
# Et cet *indice* est toujours utilisé pour décider le bras à essayer à chaque instant :
# $$A^{\mathrm{UCB}1}(t) = \arg\max_k g'_k(t).$$
# 
# Il faut une constante $\alpha \geq 0$, qu'on choisira $\alpha \geq \frac12$ pour avoir des performances raisonnables. $\alpha$ contrôle le compromis entre *exploitation* et *exploration*, et ne doit pas être trop grand. $\alpha = 1$ est un bon choix par défaut.
# 
# > On va gagner du temps en *héritant* de la classe `MoyenneEmpirique` précédente. Ça permet de ne pas réécrire les méthodes qui sont déjà bien écrites.

# In[11]:


class UCB1(MoyenneEmpirique):
    """Algorithme UCB1."""
    
    def __init__(self, K, alpha=1):
        """Crée l'instance de l'algorithme. Par défaut, alpha=1."""
        super(UCB1, self).__init__(K)  # On laisse la classe mère faire le travaille
        assert alpha >= 0, "Erreur : alpha doit etre >= 0."
        self.alpha = alpha
    
    def choix(self):
        """Si on a vu tous les bras, on prend celui d'indice moyenne empirique + UCB le plus grand."""
        self.t += 1      # Nécessaire ici
        # 1er cas : il y a encore des bras qu'on a jamais vu
        if np.min(self.tirages) == 0:
            k = np.min(np.where(self.tirages == 0)[0])
        # 2nd cas : tous les bras ont été essayé
        else:
            moyennes_empiriques = self.recompenses / self.tirages
            ucb = np.sqrt(self.alpha * np.log(self.t) / self.tirages)
            indices = moyennes_empiriques + ucb
            k = np.argmax(indices)
        return k


# ----
# ## Variantes d'UCB : UCB-V et UCB-H
# On peut rapidement implémenter deux variantes d'UCB, UCB-V qui utilise les carrés des récompenses pour estimer la variance de chaque bras et calculer un meilleur intervalle de confiance, et UCB-H qui utilise la connaissance de l'horizon $T$ de l'expérience pour utiliser $\sqrt{\log(T) / N_k(t)}$ à la place de $\sqrt{\log(t) / N_k(t)}$ et obtenir de meilleures performances.

# In[33]:


class UCBV(MoyenneEmpirique):
    """Algorithme UCBV."""
    
    def __init__(self, K, alpha=1):
        """Crée l'instance de l'algorithme. Par défaut, alpha=1."""
        super(UCBV, self).__init__(K)  # On laisse la classe mère faire le travaille
        assert alpha >= 0, "Erreur : alpha doit etre >= 0."
        self.alpha = alpha
        self.recompensesCarrees = np.zeros(K)  # somme des r_k(t)^2 pour chaque k
        
    def recompense(self, k, r):
        """Donne une récompense r tirée sur le bras k à l'algorithme : met à jour les deux vecteurs internes."""
        self.recompenses[k] += r
        self.recompensesCarrees[k] += r ** 2
        self.tirages[k] += 1

    def choix(self):
        """Si on a vu tous les bras, on prend celui d'indice moyenne empirique + UCB le plus grand."""
        self.t += 1      # Nécessaire ici
        # 1er cas : il y a encore des bras qu'on a jamais vu
        if np.min(self.tirages) == 0:
            k = np.min(np.where(self.tirages == 0)[0])
        # 2nd cas : tous les bras ont été essayé
        else:
            moyennes_empiriques = self.recompenses / self.tirages
            variance = (self.recompensesCarrees / self.tirages) - moyennes_empiriques ** 2  # Estimee de la variance

            ucb = np.sqrt(self.alpha * np.log(self.t) * variance / self.tirages) + 3.0 * np.log(self.t) / self.tirages
            
            indices = moyennes_empiriques + ucb
            k = np.argmax(indices)
        return k


# Et pour UCBH :

# In[13]:


class UCBH(MoyenneEmpirique):
    """Algorithme UCBH."""
    
    def __init__(self, K, horizon, alpha=1):
        """Crée l'instance de l'algorithme. Par défaut, alpha=1."""
        super(UCBH, self).__init__(K)  # On laisse la classe mère faire le travaille
        self.horizon = int(horizon)
        assert alpha >= 0, "Erreur : alpha doit etre >= 0."
        self.alpha = alpha
    
    def choix(self):
        """Si on a vu tous les bras, on prend celui d'indice moyenne empirique + UCB le plus grand."""
        self.t += 1      # Nécessaire ici
        # 1er cas : il y a encore des bras qu'on a jamais vu
        if np.min(self.tirages) == 0:
            k = np.min(np.where(self.tirages == 0)[0])
        # 2nd cas : tous les bras ont été essayé
        else:
            moyennes_empiriques = self.recompenses / self.tirages
            ucb = np.sqrt(self.alpha * np.log(self.horizon) / self.tirages)
            indices = moyennes_empiriques + ucb
            k = np.argmax(indices)
        return k


# ----
# ## Approche fréquentiste optimale, KL-UCB, "Kullback-Leibler UCB"

# ### KL binaire
# Pour $x,y\in\{0,1\}$, $x,y\neq 0,1$, $\mathrm{kl}(x,y)$, on définit [la divergence de Kullback-Leibler binaire](https://en.wikipedia.org/wiki/Bernoulli_distribution#Kullback.E2.80.93Leibler_divergence) de $x$ et $y$ comme la KL de deux lois de Bernoulli de moyennes $x$ et $y$, ce qui est défini comme :
# $$\mathrm{kl}(x,y) := x \log\left(\frac{x}{y}\right) + (1-x)\log\left(\frac{1-x}{1-y}\right).$$
# 
# Pour vous facilier la tâche, la fonction $\mathrm{kl}$ est déjà implémentée, ainsi qu'une fonction pour résoudre (de façon approchée) le probl_me d'optimisation contrainte qui définit l'indice $g_k''(t)$.

# In[14]:


# Just forcing the ?? in Jupyter to be in the main document (to be saved) and not a floating window.
# Thanks to https://nbviewer.jupyter.org/gist/minrk/7715212
from __future__ import print_function
from IPython.core import page
def myprint(s):
    try:
        print(s['text/plain'])
    except (KeyError, TypeError):
        print(s)
page.page = myprint


# In[15]:


from kullback import klBern
get_ipython().run_line_magic('pinfo', 'klBern')


# ### KLUCB
# > ([Garivier & Cappé - COLT, 2011](https://arxiv.org/pdf/1102.2490.pdf))
# 
# Il s'agit d'une autre amélioration de l'algorithme précédent, où on utilise un autre *indice*.
# 
# Au lieu d'utiliser une borne supérieure d'un intervalle de confiance autour de cette moyenne, on utilise la [pseudo-distance de Kullback-Leibler](https://fr.wikipedia.org/wiki/Divergence_de_Kullback-Leibler) afin d'obtenir l'intervale de confiance optimal :
# $$g''_k(t) = \sup\limits_{q \in [0,1]} \left\{ q : \mathrm{kl}(\hat{\mu}_k(t), q) \leq \frac{f(t)}{N_k(t)} \right\}.$$
# Et cet *indice* est toujours utilisé pour décider le bras à essayer à chaque instant :
# $$A^{\mathrm{KLUCB}}(t) = \arg\max_k g''_k(t).$$
# 
# On utilise $$f(t) := \log(t) + c\log\log(t).$$
# Il faut une constante $c \geq 0$, qu'on doit choisir $c > 0$ pour simplifier les preuves théoriques. En pratique, $c = 0$ est un bon choix par défaut.

# In[16]:


from kullback import klucb
get_ipython().run_line_magic('pinfo', 'klucb')
# do klucb?? to see the code


# In[17]:


from kullback import klucbBern
get_ipython().run_line_magic('pinfo', 'klucbBern')
# do klucbBern?? to see the code


# C'est assez facile avec tout ça :

# In[19]:


def f(t, c=0):
    return np.log(t) + c * np.log(np.maximum(0, np.log(t)))

class KLUCB(MoyenneEmpirique):
    """Algorithme KLUCB."""
    
    def __init__(self, K, c=0, tolerance=1e-4):
        """Crée l'instance de l'algorithme. Par défaut, c=0."""
        super(KLUCB, self).__init__(K)  # On laisse la classe mère faire le travaille
        assert c >= 0, "Erreur : c doit etre >= 0."
        self.c = c
        self.tolerance = tolerance
        # Version vectorisée
        self.klucb = np.vectorize(klucbBern)
    
    def choix(self):
        """Si on a vu tous les bras, on prend celui d'indice KLUCB le plus grand."""
        self.t += 1      # Nécessaire ici
        # 1er cas : il y a encore des bras qu'on a jamais vu
        if np.min(self.tirages) == 0:
            k = np.min(np.where(self.tirages == 0)[0])
        # 2nd cas : tous les bras ont été essayé
        else:
            indices = self.klucb(self.recompenses / self.tirages, f(self.t, self.c) / self.tirages, self.tolerance)
            k = np.argmax(indices)
        return k


# ----
# ## Approche bayésienne, Thompson Sampling
# 
# [Ce petit article](http://chercheurs.lille.inria.fr/ekaufman/Matapli_Kaufmann.pdf) explique très bien l'approche bayésienne.
# 
# On a besoin de savoir manipuler des posteriors, qui seront les posteriors conjugués des distributions des bras.
# 
# Pour des bras de Bernoulli, le posterior conjugué associé est une loi Beta, notée $\mathrm{Beta}(\alpha,\beta)$ pour deux paramètres $\alpha,\beta > 0$.
# 
# - Les posteriors sont initialisés à $\mathrm{Beta}(1, 1) = U([0,1])$, c'est-à-dire qu'on met un a priori uniforme sur les $\mu_k$, comme on ne connaît que $\mu_k \in [0,1]$.
# - Comme les *observations* sont binaires, $r_k(t) \in \{0,1\}$, les paramètres $\alpha$,$\beta$ restent entiers.

# In[20]:


from numpy.random import beta

class Beta():
    """Posteriors d'expériences de Bernoulli."""

    def __init__(self):
        self.N = [1, 1]

    def reinitialise(self):
        self.N = [1, 1]

    def echantillon(self):
        """Un échantillon aléatoire de ce posterior Beta."""
        return beta(self.N[1], self.N[0])

    def observe(self, obs):
        """Ajoute une nouvelle observation. Si 'obs'=1, augmente alpha, sinon si 'obs'=0, augmente beta."""
        self.N[int(obs)] += 1


# Dès qu'on sait manipuler ces postériors Beta, on peut implémenter rapidement le dernier algorithme, Thompson Sampling.
# 
# Les paramètres du posterior sur $\mu_k$, i.e., $\alpha_k(t)$,$\beta_k(t)$ seront mis à jour à chaque étape pour compter le nombre d'observations réussies et échouées :
# $$ \alpha_k(t) = 1 + X_k(t) \\ \beta_k(t) = 1 + N_k(t) - X_k(t).$$
# 
# La moyenne empirique estimant $\mu_k$ sera, à l'instant $t$,
# $$ \widetilde{\mu_k}(t) = \frac{\alpha_k(t)}{\alpha_k(t) + \beta_k(t)} = \frac{1 + X_k(t)}{2 + N_k(t)} \simeq \frac{X_k(t)}{N_k(t)}.$$
# 
# La différence avec UCB1 est que la prise de décision de Thompson Sampling se fait sur un indice, tiré aléatoirement selon les posteriors.
# C'est une *politique d'indice randomisée*.
# 
# D'un point de vue bayésien, un *modèle* est tiré selon les posteriors, puis on joue selon le meilleur modèle :
# $$ g'''_k(t) \sim \mathrm{Beta}(\alpha_k(t), \beta_k(t)) \\ A^{\mathrm{TS}}(t) = \arg\max_k g'''_k(t). $$

# In[21]:


class ThompsonSampling(MoyenneEmpirique):
    """Algorithme Thompson Sampling."""
    
    def __init__(self, K, posterior=Beta):
        """Crée l'instance de l'algorithme. Par défaut, alpha=1."""
        self.K = K
        # On créé K posteriors
        self.posteriors = [posterior() for k in range(K)]
    
    def commence(self):
        """Réinitialise les K posteriors."""
        for posterior in self.posteriors:
            posterior.reinitialise()
    
    def choix(self):
        """On tire K modèles depuis les posteriors, et on joue dans le meilleur."""
        moyennes_estimees = [posterior.echantillon() for posterior in self.posteriors]
        k = np.argmax(moyennes_estimees)
        return k

    def recompense(self, k, r):
        """Observe cette récompense r sur le bras k en mettant à jour le kième posterior."""
        self.posteriors[k].observe(r)


# ----
# ## Exemples de simulations
# 
# On va comparer, sur deux problèmes, les 4 algorithmes définis plus haut.
# 
# Les problèmes sont caractérisés par les moyennes des bras de Bernoulli, $\boldsymbol{\mu} = [\mu_1,\dots,\mu_K]$, et on les suppose ordonnées par ordre décroissant : $\mu_1 > \mu_2 \ge \dots \ge \mu_K$.
# 
# On affichera plusieurs choses, dans des graphiques au cours du temps $t = 0, \dots, T$ pour un horizon $T = 1000$ ou $T = 5000$ étapes :
# 
# 1. leurs *taux de sélection* du meilleur bras $k^*$, (qui sera toujours $\mu_1$ le premier bras), i.e., $N_k(t) / t$ en $\%$, pour chaque algorithme,
# 2. leurs *récompenses accumulées*, i.e., $R(t) = \sum_{\tau=0}^{t} \sum_{k=1}^{K} X_k(\tau) \mathbb{1}(A(t) = k)$, pour chaque algorithme,
# 3. les *récompenses moyennes*, i.e., $R(t) / t$, qui devrait converger vers $\mu^* = \mu_{k^*} = \mu_1$,
# 4. et enfin leurs *regret*. Cette notion est moins triviale, mais pour notre problème simple il se définit comme la perte, en récompenses accumulées, entre la meilleure stratégie (toujours sélectionner le meilleur bras $k^* = 1$) et la performance de l'algorithme :
#    $$ \mathcal{R}(t) = \mu^* t - R(t) $$
#    On souhaite maximiser $R(t)$, donc minimiser $\mathcal{R}(t)$.
#    Les algorithmes "efficaces" ont typiquement un regret *logarithmique*, i.e., $\mathcal{R}(T) = \mathcal{O}(\log T)$ *asymptotiquement*, ce qu'on souhaiterait vérifier.

# ### Fonctions pour l'affichage
# 
# On définit 4 fonctions d'affichage pour ces quantités.

# In[22]:


mpl.rcParams['figure.figsize'] = (15, 8)


# In[23]:


def affiche_selections(choix, noms, kstar=0):
    plt.figure()
    for i, c in enumerate(choix):
        selection_kstar = 1.0 * (c == kstar)
        selection_moyenne = np.cumsum(selection_kstar) / np.cumsum(np.ones_like(c))
        plt.plot(selection_moyenne, label=noms[i])
    plt.legend()
    plt.xlabel("Temps discret, $t = 1, ..., T = {}$".format(len(choix[0])))
    plt.ylabel("Taux de sélection")
    plt.title("Sélection du meilleur bras #{} pour différents algorithmes".format(1 + kstar))
    plt.show()


# In[24]:


def affiche_recompenses(recompenses, noms):
    plt.figure()
    for i, r in enumerate(recompenses):
        recompense_accumulee = np.cumsum(r)
        plt.plot(recompense_accumulee, label=noms[i])
    plt.legend()
    plt.xlabel("Temps discret, $t = 1, ..., T = {}$".format(len(recompenses[0])))
    plt.ylabel("Récompenses accumulées")
    plt.title("Récompenses accumulées pour différents algorithmes")
    plt.show()


# In[25]:


def affiche_recompenses_moyennes(recompenses, noms):
    plt.figure()
    for i, r in enumerate(recompenses):
        recompense_moyenne = np.cumsum(r) / np.cumsum(np.ones_like(r))
        plt.plot(recompense_moyenne, label=noms[i])
    plt.legend()
    plt.xlabel("Temps discret, $t = 1, ..., T = {}$".format(len(recompenses[0])))
    plt.ylabel(r"Récompenses moyennes $\in [0, 1]$")
    plt.title("Récompenses moyennes pour différents algorithmes")
    plt.show()


# In[26]:


def affiche_regret(recompenses, noms, mustar=1):
    plt.figure()
    for i, r in enumerate(recompenses):
        recompense_accumulee = np.cumsum(r)
        regret = mustar * np.cumsum(np.ones_like(r)) - recompense_accumulee
        plt.plot(regret, label=noms[i])
    plt.legend()
    plt.xlabel("Temps discret, $t = 1, ..., T = {}$".format(len(recompenses[0])))
    plt.ylabel("Regret")
    plt.title("Regret accumulé pour différents algorithmes")
    plt.show()


# Pour afficher un histogramme, c'est moins évident, mais voici :

# In[93]:


def nrows_ncols(N):
    """(nrows, ncols) pour créer un subplots de N figures avec les bonnes dimensions."""
    nrows = int(np.ceil(np.sqrt(N)))
    ncols = N // nrows
    while N > nrows * ncols:
        ncols += 1
    nrows, ncols = max(nrows, ncols), min(nrows, ncols)
    return nrows, ncols


# In[94]:


def affiche_hist_regret(recompenses, noms, horizon, mustar=1):
    nrows, ncols = nrows_ncols(len(noms))
    fig, axes = plt.subplots(nrows, ncols, sharex=False, sharey=False)
    fig.suptitle("Histogramme du regret à $t = T = {}$ pour différents algorithmes".format(len(choix[0])))

    # XXX See https://stackoverflow.com/a/36542971/
    ax0 = fig.add_subplot(111, frame_on=False)  # add a big axes, hide frame
    ax0.grid(False)  # hide grid
    ax0.tick_params(labelcolor='none', top='off', bottom='off', left='off', right='off')  # hide tick and tick label of the big axes
    # Add only once the ylabel, xlabel, in the middle
    ax0.set_ylabel("Distribution")
    ax0.set_xlabel("Regret")

    for i, r in enumerate(recompenses):
        x, y = i % nrows, i // nrows
        ax = axes[x, y] if ncols > 1 else axes[x]
        regret = mustar * horizon - r
        ax.hist(regret, normed=True, bins=25)
        ax.set_title(noms[i])
    plt.show()


# ### Premier problème, à 3 bras
# On reprend le problème donné plus haut :

# In[28]:


horizon = 1000
mus = [0.9, 0.5, 0.1]
bras = [ Bernoulli(mu) for mu in mus ]
K = len(mus)
kstar = np.argmax(mus)  # = 0


# In[29]:


horizon, mus, bras, K, kstar


# In[34]:


algorithmes = [ChoixUniforme(K), MoyenneEmpirique(K),
               UCB1(K, alpha=1), UCBV(K, alpha=1), UCBH(K, horizon, alpha=1),
               KLUCB(K), ThompsonSampling(K)]
algorithmes


# Pour les légendes, on a besoin des noms des algorithmes :

# In[35]:


noms = ["ChoixUniforme", "MoyenneEmpirique",
        "UCB1(alpha=1)", "UCBV(alpha=1)", "UCBH(alpha=1)",
        "KLUCB", "ThompsonSampling"]


# On peut commencer la simulation, pour chaque algorithme.

# In[36]:


get_ipython().run_cell_magic('time', '', 'N = len(algorithmes)\nrecompenses, choix = np.zeros((N, horizon)), np.zeros((N, horizon))\n\nfor i, alg in tqdm(enumerate(algorithmes), desc="Algorithmes"):\n    rec, ch = simulation(bras, alg, horizon)\n    recompenses[i] = rec\n    choix[i] = ch')


# In[37]:


recompenses, choix


# On affiche et vérifie les résultats attendus :

# In[38]:


affiche_selections(choix, noms, kstar)


# In[39]:


affiche_recompenses(recompenses, noms)


# In[40]:


affiche_recompenses_moyennes(recompenses, noms)


# In[41]:


affiche_regret(recompenses, noms, mustar=mus[kstar])


# $\implies$ L'algorithme uniforme est, bien évidemment, très inefficace !
# Il empêche de visualiser le regret des trois autres algorithmes.
# 
# Et sur ce problème simple à trois bras, avec *une seule simulation* (donc une variance immense), difficile de savoir lequel des trois algorithmes est le plus efficace...

# ### Second problème, à 9 bras

# In[42]:


horizon = 5000
mus = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
bras = [ Bernoulli(mu) for mu in mus ]
K = len(mus)
kstar = np.argmax(mus)  # = 0


# In[43]:


horizon, mus, bras, K, kstar


# On va comparer différents choix de $\alpha$ pour l'algorithme UCB : $\alpha = 4, 1, 0.5, 0.1$.

# In[44]:


algorithmes = [MoyenneEmpirique(K),
               UCB1(K, alpha=4), UCB1(K, alpha=1), UCB1(K, alpha=0.5), UCB1(K, alpha=0.1),
               UCBV(K, alpha=1), UCBH(K, horizon, alpha=1),
               KLUCB(K), ThompsonSampling(K)]
algorithmes


# Pour les légendes, on a besoin des noms des algorithmes :

# In[45]:


noms = ["MoyenneEmpirique",
        "UCB1(alpha=4)", "UCB1(alpha=1)", "UCB1(alpha=0.5)", "UCB1(alpha=0.1)",
        "UCBV(alpha=1)", "UCBH(alpha=1)",
        "KLUCB", "ThompsonSampling"]


# On peut commencer la simulation, pour chaque algorithme.

# In[46]:


get_ipython().run_cell_magic('time', '', 'N = len(algorithmes)\nrecompenses, choix = np.zeros((N, horizon)), np.zeros((N, horizon))\n\nfor i, alg in tqdm(enumerate(algorithmes), desc="Algorithmes"):\n    rec, ch = simulation(bras, alg, horizon)\n    recompenses[i] = rec\n    choix[i] = ch')


# In[47]:


recompenses, choix


# On affiche et vérifie les résultats attendus :

# In[48]:


affiche_selections(choix, noms, kstar)


# On commence à voir une différence de vitesse de convergence, pour l'identification du meilleur bras.

# In[49]:


affiche_recompenses(recompenses, noms)


# Difficile de différence quel algorithme est le plus efficace, même si clairement les plus grandes valeurs de $\alpha = 4, 1$ pour UCB semblent avoir moins bien fonctionné.

# In[50]:


affiche_recompenses_moyennes(recompenses, noms)


# En terme de récompenses moyennes au cours du temps, les 4 algorithmes les plus efficaces convergent vers $\mu^* = \mu_1 = 0.9$.

# In[51]:


affiche_regret(recompenses, noms, mustar=mus[kstar])


# Encore une fois, une seule simulation ne permet pas vraiment de conclure...
# 
# Mais on voit quand même :
# 
# - KLUCB, UCBH et Thompson Sampling sont tous les trois très efficaces,
# - UCBV ne semble pas meilleur que UCB,
# - Et FTL (MoyenneEmpirique) est pas si mauvais !

# ### Troisième problème, simulé 100 fois
# On s'intéresse au même problème, mais simulé 100 fois et sur un horizon plus long ($T = 10000$).
# 
# On s'intéressera ensuite aux statistiques *moyennes* (du regret cumulé) sur ces 100 répétitions pour les graphiques.
# On doit aussi considérer la distribution du regret (par exemple à $t=T$ fixé), afin de vérifier que *chaque* répétition de l'expérience a donné des résultats similaires (la moyenne efface les valeurs extrêmes si elles sont peu présentes).

# In[52]:


horizon = 10000
repetitions = 100
mus = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1]
bras = [ Bernoulli(mu) for mu in mus ]
K = len(mus)
kstar = np.argmax(mus)  # = 0


# In[53]:


horizon, repetitions, mus, bras, K, kstar


# On va comparer différents choix de $\alpha$ pour l'algorithme UCB : $\alpha = 4, 1, 0.5, 0.1$.

# In[54]:


algorithmes = [MoyenneEmpirique(K),
               UCB1(K, alpha=4), UCB1(K, alpha=1), UCB1(K, alpha=0.5), UCB1(K, alpha=0.1),
               UCBV(K, alpha=1), UCBH(K, horizon, alpha=1),
               KLUCB(K), ThompsonSampling(K)]
algorithmes


# Pour les légendes, on a besoin des noms des algorithmes :

# In[55]:


noms = ["MoyenneEmpirique",
        "UCB1(alpha=4)", "UCB1(alpha=1)", "UCB1(alpha=0.5)", "UCB1(alpha=0.1)",
        "UCBV(alpha=1)", "UCBH(alpha=1)",
        "KLUCB", "ThompsonSampling"]


# On peut commencer la simulation, pour chaque algorithme.

# In[56]:


get_ipython().run_cell_magic('time', '', 'N = len(algorithmes)\nrecompenses, choix = np.zeros((N, repetitions, horizon)), np.zeros((N, repetitions, horizon))\n\n# Pour chaque répétitions\nfor rep in tqdm(range(repetitions), desc="Répétitions"):\n    for i, alg in enumerate(algorithmes):\n        rec, ch = simulation(bras, alg, horizon)\n        recompenses[i, rep] = rec\n        choix[i, rep] = ch')


# In[71]:


# On moyenne
recompenses_moy = np.mean(recompenses, axis=1)
choix_moy = np.mean(choix, axis=1)
print("Dimension de 'recompenses_moy' =", np.shape(recompenses_moy))  # juste pour vérifier

# On garde la distribution à t=T
recompenses_fin = np.sum(recompenses, axis=2)
choix_fin = np.sum(choix, axis=2)
print("Dimension de 'recompenses_fin' =", np.shape(recompenses_fin))  # juste pour vérifier


# Cette fois, les statistiques accumulées ne sont plus entières.

# In[72]:


recompenses_moy, choix_moy


# In[73]:


recompenses_fin


# On affiche et vérifie les résultats attendus :

# In[74]:


choix_moy = np.floor(choix_moy)


# In[75]:


affiche_selections(choix_moy, noms, kstar)


# On commence à voir une différence de vitesse de convergence, pour l'identification du meilleur bras.

# In[76]:


affiche_recompenses(recompenses_moy, noms)


# Difficile de différence quel algorithme est le plus efficace, même si clairement les plus grandes valeurs de $\alpha = 4, 1$ pour UCB semblent avoir moins bien fonctionner.

# In[77]:


affiche_recompenses_moyennes(recompenses_moy, noms)


# En terme de récompenses moyennes au cours du temps, les 4 algorithmes les plus efficaces convergent vers $\mu^* = \mu_1 = 0.9$.

# In[89]:


affiche_regret(recompenses_moy, noms, mustar=mus[kstar])


# In[95]:


affiche_hist_regret(recompenses_fin, noms, horizon, mustar=mus[kstar])


# > Attention, l'axe $x$ est différent pour chaque histogramme !

# Cette fois, ces 100 simulations permet de conclure quelques points :
# 
# - `MoyenneEmpirique` converge rapidement au début, mais son regret $\mathcal{R}(t)$ ne semble pas avoir un profil logarithmique (il faudrait essayer de plus grands horizons pour le confirmer),
# - Les différents `UCB` semblent tous avoir un regret logarithmique, i.e., $\mathcal{R}(t) = \mathcal{O}(\log t)$, et plus le $\alpha$ est petit, plus le regret est bas,
# - `ThompsonSampling` et `KLUCB` fonctionnent très bien, sans avoir à choisir de constante $\alpha$.

# ### Dernier problème
# On s'intéresse enfin à un problème bien plus difficile.

# In[96]:


horizon = 10000
repetitions = 10
mus = [0.3, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.02, 0.02, 0.02, 0.01, 0.01, 0.005, 0.005, 0.001, 0.001]
bras = [ Bernoulli(mu) for mu in mus ]
K = len(mus)
kstar = np.argmax(mus)


# In[97]:


horizon, repetitions, mus, bras, K, kstar


# On va comparer différents choix de $\alpha$ pour l'algorithme UCB : $\alpha = 4, 1, 0.5, 0.1, 0.01, 0.001$.

# In[98]:


algorithmes = [MoyenneEmpirique(K),
               UCB1(K, alpha=4), UCB1(K, alpha=1), UCB1(K, alpha=0.5),
               UCB1(K, alpha=0.1), UCB1(K, alpha=0.01), UCB1(K, alpha=0.001),
               UCBV(K, alpha=1), UCBH(K, horizon, alpha=1),
               KLUCB(K), ThompsonSampling(K)]
algorithmes


# Pour les légendes, on a besoin des noms des algorithmes :

# In[99]:


noms = ["MoyenneEmpirique",
        "UCB1(alpha=4)", "UCB1(alpha=1)", "UCB1(alpha=0.5)",
        "UCB1(alpha=0.1)", "UCB1(alpha=0.01)", "UCB1(alpha=0.001)",
        "UCBV(alpha=1)", "UCBH(alpha=1)",
        "KLUCB", "ThompsonSampling"]


# On peut commencer la simulation, pour chaque algorithme.

# In[100]:


get_ipython().run_cell_magic('time', '', 'N = len(algorithmes)\nrecompenses, choix = np.zeros((N, repetitions, horizon)), np.zeros((N, repetitions, horizon))\n\n# Pour chaque répétitions\nfor rep in tqdm(range(repetitions), desc="Répétitions"):\n    for i, alg in enumerate(algorithmes):\n        rec, ch = simulation(bras, alg, horizon)\n        recompenses[i, rep] = rec\n        choix[i, rep] = ch')


# In[101]:


# On moyenne
recompenses_moy = np.mean(recompenses, axis=1)
choix_moy = np.mean(choix, axis=1)
print("Dimension de 'recompenses_moy' =", np.shape(recompenses_moy))  # juste pour vérifier

# On garde la distribution à t=T
recompenses_fin = np.sum(recompenses, axis=2)
choix_fin = np.sum(choix, axis=2)
print("Dimension de 'recompenses_fin' =", np.shape(recompenses_fin))  # juste pour vérifier


# Cette fois, les statistiques accumulées ne sont plus entières.

# In[102]:


recompenses_moy, choix_moy


# On affiche et vérifie les résultats attendus :

# In[103]:


choix_moy = np.floor(choix_moy)


# In[104]:


affiche_selections(choix_moy, noms, kstar)


# On commence à voir une différence de vitesse de convergence, pour l'identification du meilleur bras.

# In[105]:


affiche_recompenses(recompenses_moy, noms)


# Difficile de différence quel algorithme est le plus efficace, même si clairement les plus grandes valeurs de $\alpha = 4, 1$ pour UCB semblent avoir moins bien fonctionner.

# In[106]:


affiche_recompenses_moyennes(recompenses_moy, noms)


# En terme de récompenses moyennes au cours du temps, les 4 algorithmes les plus efficaces convergent vers $\mu^* = \mu_1 = 0.9$.

# In[107]:


affiche_regret(recompenses_moy, noms, mustar=mus[kstar])


# In[108]:


affiche_hist_regret(recompenses_fin, noms, horizon, mustar=mus[kstar])


# Cette fois, cette autre simulation permet de renforcer les conclusions précédentes :
# 
# - `MoyenneEmpirique` converge rapidement au début, mais son regret $\mathcal{R}(t)$ ne semble pas avoir un profil logarithmique (il faudrait essayer de plus grands horizons pour le confirmer). De plus, sur l'histogramme on voit que pour certaines expériences ses performances sont très mauvaises.
# - Les différents `UCB1` semblent tous avoir un regret logarithmique, i.e., $\mathcal{R}(t) = \mathcal{O}(\log t)$, et plus le $\alpha$ est petit, plus le regret est bas,
# - Mais si $\alpha$ est trop petit (e.g., $\alpha = 10^{-3}$), `UCB1(alpha)` n'est pas assez exploiteur, et pour ce problème à $K=15$ bras, il ne fonctionne plus bien,
# - `ThompsonSampling` et `KLUCB` fonctionnent généralement aussi bien qu'un `UCB1` avec "la bonne constante".

# ## Une autre politique d'indice : ApproximatedFHGittins
# 
# Je propose de terminer par l'implémentation d'un dernier algorithme, ressemblant beaucoup à `UCB1`, mais qui utilise des indices un peu plus compliqués à calculer.
# 
# Il s'agit de l'algorithme proposé en 2016 par Tor Lattimore, dans [cet article](http://www.jmlr.org/proceedings/papers/v49/lattimore16.pdf) (et [sa présentation à COLT'16](https://youtu.be/p8AwKiudhZ4?t=276)), nommé `ApproximatedFHGittins`, pour *Approximated Finite-Horizon Gittins index*, ou Approximation *des Indices de Gittins à Horizon Fini* en français.
# 
# Cet algorithme *exige de connaître l'horizon* $T$, et calcule l'indice suivant, au temps $t$ et après $N_k(t)$ sélections du bras $k$ :
# $$ I_k(t) = \frac{X_k(t)}{N_k(t)} + \sqrt{\frac{\alpha}{2 N_k(t)} \log\left( \frac{m}{N_k(t) \log^{1/2}\left( \frac{m}{N_k(t)} \right)} \right)}, \\
# \text{où}\;\; m = T - t + 1.$$
# 
# - Notez que ce terme $\log^{1/2}(\dots) = \sqrt(\log(\dots))$ peut être *indéfini*, dès que $m < N_k(t)$, donc en pratique, $\sqrt(\max(0, \log(\dots))$ est préférable, ou alors un horizon *un peu plus grand* peut être utilisé à la place, pour rendre $m$ un peu plus grand (e.g., $T' = 1.1 T$).
# - Si besoin, voir [mon implémentation](http://banditslilian.gforge.inria.fr/docs/Policies.ApproximatedFHGittins.html#Policies.ApproximatedFHGittins.ApproximatedFHGittins.computeIndex).

# In[109]:


class ApproximatedFHGittins(MoyenneEmpirique):
    """Algorithme ApproximatedFHGittins de Tor Lattimore."""
    
    def __init__(self, K, horizon, alpha=1):
        """Crée l'instance de l'algorithme. Par défaut, alpha=1."""
        super(ApproximatedFHGittins, self).__init__(K)  # On laisse la classe mère faire le travaille
        self.horizon = horizon
        assert alpha >= 0, "Erreur : alpha doit etre >= 0."
        self.alpha = alpha
    
    def choix(self):
        """Si on a vu tous les bras, on prend celui d'indice le plus grand."""
        self.t += 1      # Nécessaire ici
        # 1er cas : il y a encore des bras qu'on a jamais vu
        if np.min(self.tirages) == 0:
            k = np.min(np.where(self.tirages == 0)[0])
        # 2nd cas : tous les bras ont été essayé
        else:
            # D'abord les moyennes
            moyennes_empiriques = self.recompenses / self.tirages
            # Puis le terme supplémentaire
            m = self.horizon - self.t + 1
            m_sur_Nk = m / self.tirages
            logdemi = np.sqrt(np.maximum(0, np.log(m_sur_Nk)))
            terme_sup = np.sqrt(self.alpha * np.log(m_sur_Nk / logdemi) / (2. * self.tirages))
            indices = moyennes_empiriques + terme_sup
            k = np.argmax(indices)
        return k


# ### Comparaison de `ApproximatedFHGittins` avec les autres algorithmes
# 
# Sur le même problème que précédemment, on va vérifier que ce dernier algorithme est plus efficace que les autres.

# In[110]:


horizon = 10000
repetitions = 10
mus = [0.3, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.02, 0.02, 0.02, 0.01, 0.01, 0.005, 0.005, 0.001, 0.001]
bras = [ Bernoulli(mu) for mu in mus ]
K = len(mus)
kstar = np.argmax(mus)


# In[111]:


horizon, repetitions, mus, bras, K, kstar


# In[112]:


algorithmes = [UCB1(K, alpha=1), UCB1(K, alpha=0.5),
               UCBV(K, alpha=1), UCBH(K, horizon, alpha=1),
               KLUCB(K), ThompsonSampling(K),
               ApproximatedFHGittins(K, 1.1 * T, alpha=4),
               ApproximatedFHGittins(K, 1.1 * T, alpha=1),
               ApproximatedFHGittins(K, 1.1 * T, alpha=0.5)
              ]
algorithmes


# In[113]:


noms = ["UCB1(alpha=1)", "UCB1(alpha=0.5)",
        "UCBV(alpha=1)", "UCBH(alpha=1)",
        "KLUCB", "ThompsonSampling",
        "ApproximatedFHGittins(T, alpha=4)",
        "ApproximatedFHGittins(T, alpha=1)",
        "ApproximatedFHGittins(T, alpha=0.5)"
       ]


# On peut commencer la simulation, pour chaque algorithme.

# In[114]:


get_ipython().run_cell_magic('time', '', 'N = len(algorithmes)\nrecompenses, choix = np.zeros((N, repetitions, horizon)), np.zeros((N, repetitions, horizon))\n\n# Pour chaque répétitions\nfor rep in tqdm(range(repetitions), desc="Répétitions"):\n    for i, alg in enumerate(algorithmes):\n        rec, ch = simulation(bras, alg, horizon)\n        recompenses[i, rep] = rec\n        choix[i, rep] = ch')


# In[115]:


# On moyenne
recompenses_moy = np.mean(recompenses, axis=1)
choix_moy = np.mean(choix, axis=1)
print("Dimension de 'recompenses_moy' =", np.shape(recompenses_moy))  # juste pour vérifier

# On garde la distribution à t=T
recompenses_fin = np.sum(recompenses, axis=2)
choix_fin = np.sum(choix, axis=2)
print("Dimension de 'recompenses_fin' =", np.shape(recompenses_fin))  # juste pour vérifier


# Cette fois, les statistiques accumulées ne sont plus entières.

# In[116]:


recompenses_moy, choix_moy


# On affiche et vérifie les résultats attendus :

# In[117]:


choix_moy = np.floor(choix_moy)


# In[118]:


affiche_selections(choix_moy, noms, kstar)


# On commence à voir une différence de vitesse de convergence, pour l'identification du meilleur bras.

# In[119]:


affiche_recompenses(recompenses_moy, noms)


# Difficile de différence quel algorithme est le plus efficace, même si clairement les plus grandes valeurs de $\alpha = 4, 1$ pour UCB semblent avoir moins bien fonctionner.

# In[120]:


affiche_recompenses_moyennes(recompenses_moy, noms)


# En terme de récompenses moyennes au cours du temps, les 4 algorithmes les plus efficaces convergent vers $\mu^* = \mu_1 = 0.9$.

# In[121]:


affiche_regret(recompenses_moy, noms, mustar=mus[kstar])


# > Note : un regret négatif n'est pas possible, mais sur peu d'expériences, on a une forte variance, et les échantillons tirés peuvent être suffisamment favorables pour avoir un regret faiblement négatif (comme c'est le cas ici pour un des `ApproximatedFHGittins`).

# In[122]:


affiche_regret(recompenses_moy[2:], noms[2:], mustar=mus[kstar])


# In[124]:


affiche_hist_regret(recompenses_fin, noms, horizon, mustar=mus[kstar])


# ----
# ## Conclusion
# 
# J'espère que ce petit document a pu vous aider à mieux comprendre les bases de la simulation et l'implémentation de problèmes et d'algorithmes de bandits.
# 
# J'ai adopté une approche très modulaire, pour chaque composant de la simulation (bras, algorithmes, fonctions de simulation, d'affichages etc).
# C'est une façon de faire, bien-sûr ce n'est pas nécessaire, mais ça me semble clair, efficace et facile à lire et à compléter (si vous voulez rajouter un algorithme de plus).
# 
# > - Pour plus de détails, je recommande de lire en détails [ce petit article, datant de 2017, en français, écrit par Émilie Kaufmann](http://chercheurs.lille.inria.fr/ekaufman/Matapli_Kaufmann.pdf).
# > - Cette petite simulation s'inspire de mon environnement plus lourd et plus complet, [AlgoBandits](http://banditslilian.gforge.inria.fr/).
