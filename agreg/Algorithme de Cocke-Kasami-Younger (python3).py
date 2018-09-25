
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#Table-des-matières" data-toc-modified-id="Table-des-matières-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Table des matières</a></div><div class="lev1 toc-item"><a href="#1.-Agrégation-externe-de-mathématiques" data-toc-modified-id="1.-Agrégation-externe-de-mathématiques-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>1. Agrégation externe de mathématiques</a></div><div class="lev2 toc-item"><a href="#1.1-Leçon-orale,-option-informatique" data-toc-modified-id="1.1-Leçon-orale,-option-informatique-21"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>1.1 Leçon orale, option informatique</a></div><div class="lev4 toc-item"><a href="#Feedbacks?" data-toc-modified-id="Feedbacks?-2101"><span class="toc-item-num">2.1.0.1&nbsp;&nbsp;</span>Feedbacks?</a></div><div class="lev1 toc-item"><a href="#2.-Algorithme-de-Cocke-Kasami-Younger" data-toc-modified-id="2.-Algorithme-de-Cocke-Kasami-Younger-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>2. Algorithme de Cocke-Kasami-Younger</a></div><div class="lev3 toc-item"><a href="#2.0.1-Implémentation-d'un-développement-pour-les-leçons-906,-907,-910,-923." data-toc-modified-id="2.0.1-Implémentation-d'un-développement-pour-les-leçons-906,-907,-910,-923.-301"><span class="toc-item-num">3.0.1&nbsp;&nbsp;</span>2.0.1 Implémentation d'un développement pour les leçons 906, 907, 910, 923.</a></div><div class="lev3 toc-item"><a href="#2.0.2-Références-:" data-toc-modified-id="2.0.2-Références-:-302"><span class="toc-item-num">3.0.2&nbsp;&nbsp;</span>2.0.2 Références :</a></div><div class="lev2 toc-item"><a href="#2.1-Classes-pour-répresenter-une-grammaire" data-toc-modified-id="2.1-Classes-pour-répresenter-une-grammaire-31"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>2.1 Classes pour répresenter une grammaire</a></div><div class="lev3 toc-item"><a href="#2.1.1-Du-typage-en-Python-?!" data-toc-modified-id="2.1.1-Du-typage-en-Python-?!-311"><span class="toc-item-num">3.1.1&nbsp;&nbsp;</span>2.1.1 Du typage en Python ?!</a></div><div class="lev3 toc-item"><a href="#2.1.2-La-classe-Grammaire" data-toc-modified-id="2.1.2-La-classe-Grammaire-312"><span class="toc-item-num">3.1.2&nbsp;&nbsp;</span>2.1.2 La classe <code>Grammaire</code></a></div><div class="lev3 toc-item"><a href="#2.1.3-Premier-exemple-de-grammaire-(non-Chomsky)" data-toc-modified-id="2.1.3-Premier-exemple-de-grammaire-(non-Chomsky)-313"><span class="toc-item-num">3.1.3&nbsp;&nbsp;</span>2.1.3 Premier exemple de grammaire (non-Chomsky)</a></div><div class="lev3 toc-item"><a href="#2.1.4-Second-exemple-de-grammaire-(non-Chomsky)" data-toc-modified-id="2.1.4-Second-exemple-de-grammaire-(non-Chomsky)-314"><span class="toc-item-num">3.1.4&nbsp;&nbsp;</span>2.1.4 Second exemple de grammaire (non-Chomsky)</a></div><div class="lev3 toc-item"><a href="#2.1.5-Dernier-exemple-de-grammaire" data-toc-modified-id="2.1.5-Dernier-exemple-de-grammaire-315"><span class="toc-item-num">3.1.5&nbsp;&nbsp;</span>2.1.5 Dernier exemple de grammaire</a></div><div class="lev2 toc-item"><a href="#2.2-Vérifier-qu'une-grammaire-est-bien-formée" data-toc-modified-id="2.2-Vérifier-qu'une-grammaire-est-bien-formée-32"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>2.2 Vérifier qu'une grammaire est bien formée</a></div><div class="lev2 toc-item"><a href="#2.3-Vérifier-qu'une-grammaire-est-en-forme-normale-de-Chomsky" data-toc-modified-id="2.3-Vérifier-qu'une-grammaire-est-en-forme-normale-de-Chomsky-33"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>2.3 Vérifier qu'une grammaire est en forme normale de Chomsky</a></div><div class="lev2 toc-item"><a href="#2.4-(enfin)-L'algorithme-de-Cocke-Kasami-Younger" data-toc-modified-id="2.4-(enfin)-L'algorithme-de-Cocke-Kasami-Younger-34"><span class="toc-item-num">3.4&nbsp;&nbsp;</span>2.4 (enfin) L'algorithme de Cocke-Kasami-Younger</a></div><div class="lev2 toc-item"><a href="#2.5-Exemples" data-toc-modified-id="2.5-Exemples-35"><span class="toc-item-num">3.5&nbsp;&nbsp;</span>2.5 Exemples</a></div><div class="lev3 toc-item"><a href="#2.5.1-Avec-$G_3$" data-toc-modified-id="2.5.1-Avec-$G_3$-351"><span class="toc-item-num">3.5.1&nbsp;&nbsp;</span>2.5.1 Avec <span class="MathJax_Preview" style="color: inherit;"><span class="MJXp-math" id="MJXp-Span-545"><span class="MJXp-msubsup" id="MJXp-Span-546"><span class="MJXp-mi MJXp-italic" id="MJXp-Span-547" style="margin-right: 0.05em;">G</span><span class="MJXp-mn MJXp-script" id="MJXp-Span-548" style="vertical-align: -0.4em;">3</span></span></span></span><script type="math/tex" id="MathJax-Element-96">G_3</script></a></div><div class="lev3 toc-item"><a href="#2.5.2-Avec-$G_6$" data-toc-modified-id="2.5.2-Avec-$G_6$-352"><span class="toc-item-num">3.5.2&nbsp;&nbsp;</span>2.5.2 Avec <span class="MathJax_Preview" style="color: inherit;"><span class="MJXp-math" id="MJXp-Span-556"><span class="MJXp-msubsup" id="MJXp-Span-557"><span class="MJXp-mi MJXp-italic" id="MJXp-Span-558" style="margin-right: 0.05em;">G</span><span class="MJXp-mn MJXp-script" id="MJXp-Span-559" style="vertical-align: -0.4em;">6</span></span></span></span><script type="math/tex" id="MathJax-Element-98">G_6</script></a></div><div class="lev2 toc-item"><a href="#2.6-Mise-en-forme-normale-de-Chomsky-(bonus)" data-toc-modified-id="2.6-Mise-en-forme-normale-de-Chomsky-(bonus)-36"><span class="toc-item-num">3.6&nbsp;&nbsp;</span>2.6 Mise en forme normale de Chomsky <em>(bonus)</em></a></div><div class="lev3 toc-item"><a href="#2.6.1-Exemple-pour-$G_1$" data-toc-modified-id="2.6.1-Exemple-pour-$G_1$-361"><span class="toc-item-num">3.6.1&nbsp;&nbsp;</span>2.6.1 Exemple pour <span class="MathJax_Preview">G_1</span><script type="math/tex">G_1</script></a></div><div class="lev3 toc-item"><a href="#2.6.2-Exemple-pour-$G_6$" data-toc-modified-id="2.6.2-Exemple-pour-$G_6$-362"><span class="toc-item-num">3.6.2&nbsp;&nbsp;</span>2.6.2 Exemple pour <span class="MathJax_Preview">G_6</span><script type="math/tex">G_6</script></a></div>

# # Table des matières
# * [1. Agrégation externe de mathématiques](#1.-Agrégation-externe-de-mathématiques)
# 	* [1.1 Leçon orale, option informatique](#1.1-Leçon-orale,-option-informatique)
# * [2. Algorithme de Cocke-Kasami-Younger](#2.-Algorithme-de-Cocke-Kasami-Younger)
# 	* &nbsp;
# 		* [2.0.1 Implémentation d'un développement pour les leçons 906, 907, 910, 923.](#2.0.1-Implémentation-d'un-développement-pour-les-leçons-906,-907,-910,-923.)
# 		* [2.0.2 Références :](#2.0.2-Références-:)
# 	* [2.1 Classes pour répresenter une grammaire](#2.1-Classes-pour-répresenter-une-grammaire)
# 		* [2.1.1 Du typage en Python ?!](#2.1.1-Du-typage-en-Python-?!)
# 		* [2.1.2 La classe ``Grammaire``](#2.1.2-La-classe-Grammaire)
# 		* [2.1.3 Premier exemple de grammaire (non-Chomsky)](#2.1.3-Premier-exemple-de-grammaire-%28non-Chomsky%29)
# 		* [2.1.4 Second exemple de grammaire (non-Chomsky)](#2.1.4-Second-exemple-de-grammaire-%28non-Chomsky%29)
# 		* [2.1.5 Dernier exemple de grammaire](#2.1.5-Dernier-exemple-de-grammaire)
# 	* [2.2 Vérifier qu'une grammaire est bien formée](#2.2-Vérifier-qu'une-grammaire-est-bien-formée)
# 	* [2.3 Vérifier qu'une grammaire est en forme normale de Chomsky](#2.3-Vérifier-qu'une-grammaire-est-en-forme-normale-de-Chomsky)
# 	* [2.4 (enfin) L'algorithme de Cocke-Kasami-Younger](#2.4-%28enfin%29-L'algorithme-de-Cocke-Kasami-Younger)
# 	* [2.5 Exemples](#2.5-Exemples)
# 		* [2.5.1 Avec $G_3$](#2.5.1-Avec-$G_3$)
# 		* [2.5.2 Avec $G_6$](#2.5.2-Avec-$G_6$)
# 	* [2.6 Mise en forme normale de Chomsky *(bonus)*](#2.6-Mise-en-forme-normale-de-Chomsky-*%28bonus%29*)
# 		* [2.6.1 Exemple pour $G_1$](#2.6.1-Exemple-pour-$G_1$)
# 		* [2.6.2 Exemple pour $G_6$](#2.6.2-Exemple-pour-$G_6$)
# 

# # 1. Agrégation externe de mathématiques

# ## 1.1 Leçon orale, option informatique

# > - Ce [notebook Jupyter](http://jupyter.org/) est une implémentation d'un algorithme constituant un développement pour l'option informatique de l'agrégation externe de mathématiques.
# > - Il s'agit de l'[algorithme de Cocke-Kasami-Younger](https://fr.wikipedia.org/wiki/Algorithme_de_Cocke-Younger-Kasami).
# > - Cette implémentation (partielle) a été rédigée par [Lilian Besson](http://perso.crans.org/besson/) ([sur GitHub ?](https://github.com/Naereen/), [sur Bitbucket ?](https://bitbucket.org/lbesson)), et [est open-source](https://github.com/Naereen/notebooks/blob/master/agreg/Algorithme%20de%20Cocke-Kasami-Younger%20%28python3%29.ipynb).
# 
# > #### Feedbacks?
# > - Vous avez trouvé un bug ? → [Signalez-le moi svp !](https://github.com/Naereen/notebooks/issues/new), merci d'avance.
# > - Vous avez une question ? → [Posez la svp !](https://github.com/Naereen/ama.fr) [![Demandez moi n'importe quoi !](https://img.shields.io/badge/Demandez%20moi-n'%20importe%20quoi-1abc9c.svg)](https://GitHub.com/Naereen/ama.fr)
# 
# ----

# # 2. Algorithme de Cocke-Kasami-Younger

# ### 2.0.1 Implémentation d'un développement pour les leçons 906, 907, 910, 923.

# L'algorithme de Cocke-Kasami-Younger (CYK) permet de résoudre le problème du mot en temps $\mathcal{O}(|w|^3)$, par programmation dynamique.
# La grammaire $G$ doit déjà avoir été mise en forme de [forme normale de Chomsky](https://fr.wikipedia.org/wiki/Forme_normale_de_Chomsky), ce qui prend un temps $\mathcal{O}(|G|^2)$ et produit une grammaire équivalente $G'$ de taille $\mathcal{O}(|G|^2)$ en partant de $G$ (qui doit être bien formée).

# ### 2.0.2 Références :

# - [Cocke-Kasami-Younger sur Wikipedia](https://fr.wikipedia.org/wiki/Algorithme_de_Cocke-Younger-Kasami),
# - Bien traité dans ["Hopcroft, Ullman", Ch7.4.4, p298](https://catalogue.ens-cachan.fr/cgi-bin/koha/opac-detail.pl?biblionumber=23694),
# - Esquissé dans ["Carton", Ex4.7 Fig4.2 p170](https://catalogue.ens-cachan.fr/cgi-bin/koha/opac-detail.pl?biblionumber=41719),
# - [Développement tapé en PDF par Theo Pierron (2014)](http://perso.eleves.ens-rennes.fr/~tpier758/agreg/dvpt/info/CYK.pdf),
# - [Ces slides d'un cours sur les langages et les grammaires](http://pageperso.lif.univ-mrs.fr/~alexis.nasr/Ens/M2/pcfg.pdf).
# 
# ----

# ## 2.1 Classes pour répresenter une grammaire

# Au lieu de types formels définis en OCaml, on utilise des classes en Python, pour répresenter une grammaire (pas seulement en forme normale de Chomsky mais dans une forme un peu plus générale).

# ### 2.1.1 Du typage en Python ?!

# Mais comme je veux frimer en utilisant des types formels, on va utiliser des [annotations de types en Python](https://www.python.org/dev/peps/pep-0484/).
# C'est assez nouveau, disponible **à partir de Python 3.5**. Si vous voulez en savoir plus, une bonne première lecture peut être [cette page](https://mypy.readthedocs.io/en/latest/builtin_types.html).
# 
# *Note :* ces annotations de types ne sont PAS nécessaires.

# In[1]:


# On a besoin de listes et de tuples
from typing import List, Tuple  # Module disponible en Python version >= 3.5


# On définit les types qui nous intéressent :

# In[2]:


# Type pour une variable, juste une chaine, e.g. 'X' ou 'S'
Var = str
# Type pour un alphabet
Alphabet = List[Var]
# Type pour une règle : un symbole transformé en une liste de symboles
Regle = Tuple[Var, List[Var]]


# *Note :* ces annotations de types ne sont là que pour illustrer et aider le programmeur, Python reste un langage dynamiquement typé (i.e. on fait ce qu'on veut...).

# ### 2.1.2 La classe ``Grammaire``

# Une grammaire $G$ est définie par :
# 
# - $\Sigma$ son alphabet de production, qui sont les lettres dans les mots produits à la fin, e.g., $\Sigma = \{ a, b\}$,
# - $V$ son alphabet de travail, qui sont les lettres utilisées dans la génération de mots, mais pas dans les mots à la fin, e.g., $V = \{S, A\}$,
# - $S$ est le symbole de travail initial,
# - $R$ est un ensemble de règles, qui sont de la forme $U \rightarrow x_1 \dots x_n$ pour $U \in V$ une variable de travail (***pas* de production**), et $x_1, \dots, x_n$ sont variables de production ou de travail (dans $\Sigma \cup V$), e.g., $R = \{ S \rightarrow \varepsilon, S \rightarrow A S b, A \rightarrow a, A \rightarrow a a \}$.
# 
# 
# Et ainsi on peut definir un classe ``Grammaire``, qui n'est rien d'autre qu'un moyen d'encapsuler ces différentes valeurs $\Sigma$, $V$, $S$, et $R$ (en OCaml, ce serait un type avec des champs d'enregistrement, défini par exemple par ``type grammar = { sigma : string list; v: string list; s: string; r: (string, strin list) list; };;``).
# 
# On ajoute aussi une méthode ``__str__`` à cette classe ``Grammaire`` pour afficher la grammaire joliment.

# In[3]:


class Grammaire(object):
    """ Type pour les grammaires algébriques (en forme de Chomsky). """
    def __init__(self, sigma: Alphabet, v: Alphabet, s: Var, r: List[Regle], nom="G"):
        """ Grammaire en forme de Chomsky :
            - sigma : alphabet de production, type Alphabet,
            - v : alphabet de travail, type Alphabet,
            - s : symbol initial, type Var,
            - r : liste de règles, type List[Regle].
        """
        # On se contente de stocker les champs :
        self.sigma = sigma
        self.v = v
        self.s = s
        self.r = r
        self.nom = nom
        
    def __str__(self) -> str:
        """ Permet d'afficher une grammaire."""
        str_regles = ', '.join(
            "{} -> {}".format(regle[0], ''.join(regle[1]) if regle[1] else 'ε')
            for regle in self.r
        )
        return r"""Grammaire {} :
    - Alphabet Σ = {},
    - Non terminaux V = {},
    - Symbole initial : '{}',
    - Règles : {}.""".format(self.nom, set(self.sigma), set(self.v), self.s, str_regles)


# ### 2.1.3 Premier exemple de grammaire (non-Chomsky)

# On commence avec un premier exemple basique, la grammaire $G_1$ avec pour seule règle : $S \rightarrow aSb \;|\; \varepsilon$.
# C'est la grammaire naturelle, bien formée, pour les mots de la forme $a^n b^n$ pour tout $n \geq 0$.
# Cf. [cet exemple sur Wikipedia](https://fr.wikipedia.org/wiki/Grammaire_non_contextuelle#Exemple_1).
# Par contre, elle n'est pas en forme normale de Chomsky.

# In[4]:


g1 = Grammaire(
    ['a', 'b'],  # Alphabet de production
    ['S'],       # Alphabet de travail
    'S',         # Symbole initial (un seul)
    [            # Règles
        ('S', []),  # S -> ε
        ('S', ['a', 'S', 'b']),  # S -> a S b
    ],
    nom="G1"
)
print(g1)


# ### 2.1.4 Second exemple de grammaire (non-Chomsky)

# Voici un autre exemple basique, la grammaire $G_2$ qui engendre les expressions arithmétiques
# en trois variables $x$, $y$ et $z$, correctement parenthésées.
# Une seule règle de production, ou une union de règle de production, suffit :
#     $$ S \rightarrow x \;|\; y \;|\; z \;|\; S+S \;|\; S-S \;|\; S∗S \;|\; S/S \;|\; (S). $$
# 
# Cf. [cet autre exemple sur Wikipedia](https://fr.wikipedia.org/wiki/Grammaire_non_contextuelle#Exemple_2).

# In[5]:


g2 = Grammaire(
    ['x', 'y', 'z', '+', '-', '*', '/', '(', ')'],  # Alphabet de production
    ['S'],  # Alphabet de travail
    'S',    # Symbole initial (un seul)
    [       # Règles
        ('S', ['x']),            # S -> x
        ('S', ['y']),            # S -> y
        ('S', ['z']),            # S -> z
        ('S', ['S', '+', 'S']),  # S -> S + S
        ('S', ['S', '-', 'S']),  # S -> S - S
        ('S', ['S', '*', 'S']),  # S -> S * S
        ('S', ['S', '/', 'S']),  # S -> S / S
        ('S', ['(', 'S', ')']),   # S -> (S)
    ],
    nom="G2"
)
print(g2)


# ### 2.1.5 Dernier exemple de grammaire

# Voici un dernier exemple, moins basique, la grammaire $G_3$ qui engendre des phrases "simples" (et très limitées) en anglais.
# [Inspirée de cet exemple sur Wikipedia (en anglais)](https://en.wikipedia.org/wiki/CYK_algorithm#Example).
# Cette grammaire $G_3$ est sous forme normale de Chomsky.

# In[6]:


g3 = Grammaire(
    # Alphabet de production, des vrais mots anglais (avec une espace pour que la phrase soit lisible
    ['she ', 'eats ', 'with ', 'fish ', 'fork ', 'a ', 'an ', 'ork ', 'sword '],
    # Alphabet de travail, des catégories de mots : V pour verbes, P pour pronom etc.
    ['S', 'NP ', 'VP ', 'PP ', 'V ', 'Det ', 'DetVo ', 'N ', 'NVo ', 'P '],
    # Det = a : déterminant
    # DetVo = an : déterminant avant un nom commençant par une voyelle
    # N = (fish, fork, sword) : un nom
    # NVo = ork : un nom commençant par une voyelle
    # NP = she | a (fish, fork, sword) | an ork : un sujet
    # V = eats : verbe conjugué
    # P = with : conjonction de coordination
    # VP = eats : verbe conjugué suivi d'un objet
    # PP : with NP : complément d'objet direct
    'S',    # Symbole initial (un seul)
    [       # Règles
        # Règles de constuction de phrase
        ( 'S',      ['NP ', 'VP '] ),      # 'S'  -> 'NP' 'VP'
        ( 'VP ',    ['VP ', 'PP '] ),      # 'VP' -> 'VP' 'PP'
        ( 'VP ',    ['V ', 'NP '] ),       # 'VP' -> 'V' 'NP'
        ( 'PP ',    ['P ', 'NP '] ),       # 'PP' -> 'P' 'NP'
        ( 'NP ',    ['Det ', 'N '] ),      # 'NP' -> 'Det' 'N'
        ( 'NP ',    ['DetVo ', 'NVo '] ),  # 'NP' -> 'DetVo' 'NVo'
        # Règles de création de mots
        ( 'VP ',    ['eats '] ),   # 'VP'    -> 'eats '
        ( 'NP ',    ['she '] ),    # 'NP'    -> 'she '
        ( 'V ',     ['eats '] ),   # 'V'     -> 'eats '
        ( 'P ',     ['with '] ),   # 'P'     -> 'with '
        ( 'N ',     ['fish '] ),   # 'N'     -> 'fish '
        ( 'N ',     ['fork '] ),   # 'N'     -> 'fork '
        ( 'N ',     ['sword '] ),  # 'N'     -> 'sword '
        ( 'NVo ',   ['ork '] ),    # 'NVo'   -> 'ork '
        ( 'Det ',   ['a '] ),      # 'Det'   -> 'a '
        ( 'DetVo ', ['an '] ),     # 'DetVo' -> 'an '
    ],
    nom="G3"
)
print(g3)


# Nous utiliserons ces exemples de grammaire plus tard, pour vérifier que nos fonctions sont correctement écrites.
# 
# ----

# ## 2.2 Vérifier qu'une grammaire est bien formée

# On veut pouvoir vérifier qu'une grammaire $G$ (i.e., un objet instance de ``Grammaire``) est bien formée (cf. votre cours de langage formel pour une définition propre) :
# 
# - $S$ doit être une variable de travail, i.e., $S \in V$,
# - Les variables de production et les variables de travail doivent être distinctes, i.e., $\Sigma \cap V = \emptyset$,
# - Pour chaque règle, $r = A \rightarrow w$, les membres gauches des règles sont réduits à une seule variable de travail, et les membres droits sont des mots, vides ou constitués de variables de production ou de travail, i.e., $A \in V$, et $w \in (\Sigma \cup V)^{\star}$,
# 
# On vérifie ça facilement avec la fonction suivante :

# In[7]:


def estBienFormee(self: Grammaire) -> bool:
    """ Vérifie que G est bien formée. """
    sigma, v, s, regles = set(self.sigma), set(self.v), self.s, self.r
    tests = [
        s in v,  # s est bien une variable de travail
        sigma.isdisjoint(v),  # Lettres et variables de travail sont disjointes
        all(
            regle[0] in v  # Les membres gauches de règles sont des variables
            and  # Les membres droits de règles sont des variables ou des lettres
            all(r in sigma | v for r in regle[1])
            for regle in regles
        )
    ]
    return all(tests)

# On ajoute la fonction comme une méthode (au cas où...)
Grammaire.estBienFormee = estBienFormee


# In[8]:


for g in [g1, g2, g3]:
    print(g)
    print("La grammaire", g.nom, "est-elle bien formée ?", estBienFormee(g))
    print()


# On peut définir une autre grammaire qui n'est pas bien formée, pour voir.
# Cette grammaire $G_4$ engendre les mots de la forme $a^{n+k} b^n$ pour $n,k \in \mathbb{N}$, mais on lui donne une règle de dédoublement des $a$ : $a \rightarrow a a$ (notez que $a$, une variable de production, est à gauche d'une règle).

# In[9]:


g4 = Grammaire(
    ['a', 'b'],  # Alphabet de production
    ['S'],       # Alphabet de travail
    'S',         # Symbole initial (un seul)
    [            # Règles
        ('S', []),               # S -> ε
        ('S', ['a', 'S', 'b']),  # S -> a S b
        ('a', ['a', 'a']),       # a -> a a, cette règle n'est pas en forme normale
    ],
    nom="G4"
)
print(g4)
print("La grammaire", g4.nom, "est-elle bien formée ?", estBienFormee(g4))


# Juste par curiosité, la voici transformée pour devenir bien formée, ici on a juste eu besoin d'ajouter une variable de travail $A$ qui peut donner $a$ ou $A A$ :

# In[10]:


g5 = Grammaire(
    ['a', 'b'],  # Alphabet de production
    ['S', 'A'],  # Alphabet de travail
    'S',         # Symbole initial (un seul)
    [            # Règles
        ('S', []),               # S -> ε
        ('S', ['A', 'S', 'b']),  # S -> A S b
        ('A', ['A', 'A']),       # A -> A A, voila comment on gère a -> a a
        ('A', ['a']),            # A -> a
    ],
    nom="G5"
)
print(g5)
print("La grammaire", g5.nom, "est-elle bien formée ?", estBienFormee(g5))


# ## 2.3 Vérifier qu'une grammaire est en forme normale de Chomsky

# On veut maintenant pouvoir vérifier qu'une grammaire $G$ (i.e., un objet instance de ``Grammaire``) est bien en forme normale de Chomsky.
# En effet, l'algorithme CKY n'a aucune chance de fonctionner si la grammaire n'est pas sous la bonne forme.
# 
# Pour que $G$ soit en forme normale de Chomsky :
# - elle doit d'abord être bien formée (cf. ci-dessus),
# - et chaque règle doit être
#    - soit de la forme $S \rightarrow \varepsilon$,
#    - soit de la forme $A \rightarrow a$ pour $(A, a)$ dans $V \times \Sigma$,
#    - soit de la forme $A \rightarrow B C$ pour $(A, B, C)$ dans $V^3$ (certains ouvrages demandent à ce qu'il n'y ait aucune production de $S$ le symbole initial, i.e., $B,C \neq S$, mais ça ne change rien pour l'algorithme qu'on implémente plus bas).
#    
# On vérifie ça facilement, point par point, dans la fonction suivante :

# In[11]:


def estChomsky(self: Grammaire) -> bool:
    """ Vérifie que G est sous forme normale de Chomksy. """
    sigma, v, s, regles = set(self.sigma), set(self.v), self.s, self.r
    estBienChomsky = all(
        (   # S -> epsilon
            regle[0] == s and not regle[1]
        ) or (  # A -> a
            len(regle[1]) == 1
            and regle[1][0] in sigma  # a in Sigma
        ) or (  # A -> B C
            len(regle[1]) == 2
            and regle[1][0] in v  # B in V, not Sigma
            and regle[1][1] in v  # C in V, not Sigma
        )
        for regle in regles
    )
    return estBienChomsky and estBienFormee(self)

# On ajoute la fonction comme une méthode (au cas où...)
Grammaire.estChomsky = estChomsky


# On peut tester avec les cinq grammaires definies plus haut ($G_1$, $G_2$, $G_3$, $G_4$, $G_5$).
# Seule la grammaire $G_3$ est de Chomsky.

# In[12]:


for g in [g1, g2, g3, g4, g5]:
    print(g)
    print("La grammaire", g.nom, "est-elle de bien formée ?", estBienFormee(g))
    print("La grammaire", g.nom, "est-elle de Chomsky ?", estChomsky(g))
    print()


# À la main, on peut transformer $G_5$ pour la mettre en forme de Chomsky (et après, on passe à CYK).
# Notez que cette transformation est automatique, elle est implémentée dans le cas general (d'une grammaire $G$ bien formée), ci-dessus en partie 5.

# In[13]:


g6 = Grammaire(
    ['a', 'b'],            # Alphabet de production
    ['S', 'T', 'A', 'B'],  # Alphabet de travail
    'S',                   # Symbole initial (un seul)
    [                      # Règles
        ('S', []),               # S -> ε, on efface S si on veut produire le mot vide
        # On coupe la règle S -> A S B en deux :
        ('S', ['A', 'T']),       # S -> A T
        ('T', ['S', 'B']),       # T -> S B
        ('A', ['A', 'A']),       # A -> A A, voilà comment on gère a -> a a
        # Production de lettres
        ('A', ['a']),            # A -> a
        ('B', ['b']),            # B -> b
    ],
    nom="G6"
)
print(g6)
print("La grammaire", g6.nom, "est-elle bien formée ?", estBienFormee(g6))
print("La grammaire", g6.nom, "est-elle de Chomsky ?", estChomsky(g6))


# ## 2.4 (enfin) L'algorithme de Cocke-Kasami-Younger

# On passe *enfin* à l'algorithme de Cocke-Kasami-Younger.
# 
# L'algorithme va prendre une grammaire $G$, bien formée, de taille $|G|$ (definie comme la somme des longueurs de $\Sigma$ et $V$ et la somme des tailles des règles), ainsi qu'un mot $w$ de taille $n = |w|$ (**attention**, ce n'est pas une ``str`` mais une liste de variables ``List[Var]``, i.e., une liste de ``str``).
# 
# Le but est de vérifier si le mot $w$ peut être engendrée par la grammaire $G$, i.e., de déterminer si $w \in L(G)$.
# Pour le détail de fonctionnement, cf. le code Python ci dessous, ou [la page Wikipedia](https://fr.wikipedia.org/wiki/Algorithme_de_Cocke-Younger-Kasami).
# 
# L'algorithme aura :
# 
# - une complexité en mémoire en $\mathcal{O}(|G| + |w|^2)$,
# - une complexité en temps en $\mathcal{O}(|G| \times |w|^3)$, ce qui montrera que le problème du mot pour les grammaires en forme de Chomsky est dans $\mathcal{P}$ (en temps polynomial, c'est déjà cool) et en temps raisonnable (cubique en $n = |w|$, c'est encore mieux !).
# 
# On va utiliser une table de hachage ``E`` contiendra, à la fin du calcul, les $E_{i, j}$ définis par :
# $$ E_{i, j} := \{ A \in V : w[i, j] \in L_G(A) \}.$$
# Ou l'on a noté $w[i, j] = w_i \dots w_j$ le sous-mot d'indices $i,\dots,j$, et $L_G(A)$ le langage engendré par $G$ en partant du symbole $A$ (et pas du symbole initial $S$).
# 
# *Note :* la table de hachage n'est pas vraiment requise, une liste de liste fonctionnerait aussi mais la notation en serait moins proche de celle utilisée en maths.

# In[14]:


def cocke_kasami_younger(self, w):
    """ Vérifie si le mot w est dans L(G). """
    assert estChomsky(self), "Erreur : {} n'est pas en forme de Chomsky, l'algorithme de Cocke-Kasami-Younger ne fonctionnera pas.".format(self.nom)
    sigma, v, s, regles = set(self.sigma), set(self.v), self.s, self.r
    n = len(w)
    E = dict()  # De taille n^2
    # Cas special pour tester si le mot vide est dans L(G)
    if n == 0:
        return (s, []) in regles, E
    # Boucle en O(n^2)
    for i in range(n):
        for j in range(n):
            E[(i, j)] = set()
    # Boucle en O(n x |G|)
    for i in range(n):
        for regle in regles:
            # Si regle est de la forme : A -> a
            if len(regle[1]) == 1:
                A = regle[0]
                a = regle[1][0]
                if w[i] == a:  # Notez que c'est le seul moment ou utilise le mot w !
                    E[(i, i)] = E[(i, i)] | {A}
    # Boucle en O(n^3 x |G|)
    for d in range(1, n):          # Longueur du morceau
        for i in range(n - d):     # Début du morceau
            j = i + d              # Fin du morceau, on regarde w[i]..w[j]
            for k in range(i, j):  # Parcourt du morceau, ..w[k].., sans la fin
                for regle in regles:
                    # Si regle est de la forme A -> B C
                    if len(regle[1]) == 2:
                        A = regle[0]
                        B, C = regle[1]
                        if B in E[(i, k)] and C in E[(k + 1, j)]:
                            E[(i, j)] = E[(i, j)] | {A}
    # On a fini, il suffit maintenant d'utiliser la table créée par programmation dynamique
    return s in E[(0, n - 1)], E

# On ajoute la fonction comme une méthode (au cas où...)
Grammaire.genere = cocke_kasami_younger


# ----

# ## 2.5 Exemples

# On présente ici des exemples d'utilisation de cette fonction ``cocke_kasami_younger`` avec les grammaires $G_i$ présentées plus haut et quelques examples de mots $w$.

# In[15]:


def testeMot(g, w):
    """ Joli affichage pour un test """
    print("# Test si w in L(G) :")
    print("  Pour", g.nom, "et w =", w)
    estDansLG, E = cocke_kasami_younger(g, w)
    if estDansLG:
        print("  ==> Ce mot est bien engendré par G !")
    else:
        print("  ==> Ce mot n'est pas engendré par G !")
    return estDansLG, E


# ### 2.5.1 Avec $G_3$

# In[16]:


print(g3)
print(estChomsky(g3))


# In[17]:


w1 = [ "she ", "eats ", "a ", "fish ", "with ", "a ", "fork " ]  # True
estDansLG1, E1 = testeMot(g3, w1)


# Pour cet exemple, on peut afficher la table ``E`` (en ne montrant que les cases qui ont un $E_{i, j}$ non-vide) :

# In[18]:


for k in E1.copy():
    if k in E1 and not E1[k]:  # On retire les clés qui ont un E[(i, j)] vide
        del(E1[k])
print(E1)


# ----

# In[19]:


w2 = [ "she ", "attacks ", "a ", "fish ", "with ", "a ", "fork " ]  # False
estDansLG2, E2 = testeMot(g3, w2)


# In[20]:


w3 = [ "she ", "eats ", "an ", "ork ", "with ", "a ", "sword " ]  # True
estDansLG3, E3 = testeMot(g3, w3)


# D'autres exemples :

# In[21]:


w4 = [ "she ", "eats ", "an ", "fish ", "with ", "a ", "fork " ]  # False
estDansLG4, E4 = testeMot(g3, w4)
w5 = [ "she ", "eat ", "a ", "fish ", "with ", "a ", "fork " ]  # False
estDansLG5, E5 = testeMot(g3, w5)
w6 = [ "she ", "eats ", "a ", "fish ", "with ", "a ", "fish " , "with ", "a ", "fish " , "with ", "a ", "fish " , "with ", "a ", "fish " ]  # True
estDansLG6, E6 = testeMot(g3, w6)


# ### 2.5.2 Avec $G_6$

# In[22]:


print(g6)
for w in [ [], ['a', 'b'], ['a', 'a', 'a', 'b', 'b', 'b'],  # True, True, True
          ['a', 'a', 'a', 'a', 'b', 'b', 'b'],  # True
          ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b', 'b'],  # True
          ['a', 'b', 'a'], ['a', 'a', 'a', 'b', 'b', 'b', 'b'],  # False, False
          ['c'], ['a', 'a', 'a', 'c'],  # False, False
         ]:
    testeMot(g6, w)


# ----

# ## 2.6 Mise en forme normale de Chomsky *(bonus)*

# On pourrait aussi implémenter la mise en forme normale de Chomsky, comme exposée et prouvée dans le développement.
# 
# La preuve faite dans le développement garantit que la fonction ci-dessous transforme une grammaire $G$ en grammaire équivalente $G'$, avec l'éventuelle perte du mot vide $\varepsilon$ :
# $$ L(G') = L(G) \setminus \{ \varepsilon \}. $$
# 
# L'algorithme aura :
# 
# - une complexité en mémoire en $\mathcal{O}(|G|)$,
# - une complexité en temps en $\mathcal{O}(|G| |\Sigma_G|)$.
# 
# C'est un algorithme en deux étapes :
# 
# 1. D'abord, on transforme $G$ en $G'$ : on ajoute des variables de travail pour chaque lettre de production, $V_a \in V$ pour $a \in \Sigma$, on remplace chaque $a$ dans des membres gauches de règles par la nouvelle $V_a$, et ensuite on ajoute des règles de production de lettre $V_a \rightarrow a$ dans $R$,
# 2. Ensuite, $G''$ est obtenue en découpant les règles de $G$ qui sont de tailles $> 2$ : une règle $S \rightarrow S_1 \dots S_n$ devient $n-1$ règles : $S \rightarrow S_1 S_2'$, $S_i' \rightarrow S_i S_{i+1}'$ (pour $i = 2,\dots,n - 2$), et $S_{n-1}' \rightarrow S_{n-1} S_n$. Il faut aussi ajouter toutes ces nouvelles variables $S_i'$ (en s'assurant qu'elles sont uniques, pour chaque règle), on ajoute pour cela le numéro de la règle : $S_i'=$ ``A'_k`` pour la ``k`` -ième règle et le symbole $S_i=$ ``A``.

# In[23]:


def miseChomsky(self):
    """ Met en forme normale de Chomsky la grammaire self, qui doit être bien formée.
    
    - On suppose que l'alphabet Sigma est dans {a,..,z},
    - On suppose que l'alphabet v est dans {A,..,Z}.
    """
    assert estBienFormee(self), "Erreur : {} n'est pas en bien formée, la mise en forme normale de Chomsky ne fonctionnera pas.".format(self.nom)
    sigma, v, s, regles = set(self.sigma), set(self.v), self.s, self.r
    if estChomsky(self):
        print("Info : la grammaire {} est déjà en forme normale de Chomsky, il n'y a rien à faire.".format(self.nom))
        return Grammaire(sigma, v, s, regles)
    assert sigma < set(chr(i) for i in range(ord('a'), ord('z') + 1)), "Erreur : {} n'a pas ses lettres de production Sigma dans 'a'..'z' ...".format(self.nom)
    assert v < set(chr(i) for i in range(ord('A'), ord('Z') + 1)), "Erreur : {} n'a pas ses lettres de travail V dans 'A'..'Z' ...".format(self.nom)

    # Algorithme en deux étapes, G --> G', puis G' --> G''
    
    # 1. G --> G' : On ajoute des variables de travail et on substitue a -> V_a dans les autres règles
    # On pose les attributs de G', qui vont être changés
    sigma2 = list(sigma)
    v2 = set(v)
    s2 = s
    regles2 = []

    V_ = lambda a: 'V_{}'.format(a)
    for a in sigma:
        v2.add(V_(a))
        regles2.append([V_(a), [a]])  # Ajout de la règle V_a -> a (production de la lettre correspondante)
    substitutionLettre = lambda b: V_(b) if (b in sigma) else b
    substitutionMot = lambda lb: [substitutionLettre(b) for b in lb]
    for regle in regles:
        S = regle[0]
        w = regle[1]
        if len(w) >= 2:  # Si ce n'est pas une règle A -> epsilon
            regles2.append([S, substitutionMot(w)])
        else:  # Ici on devrait garder la possibilte de creer le mot vide
            regles2.append([S, w])
    nom2 = self.nom + "'"
    print(Grammaire(list(sigma2), list(v2), s2, regles2, nom=nom2))
    
    # 2. G' --> G'' : On découpe les règles A -> A1..An qui ont n > 2
    # On pose les attributs de G'', qui vont être changés
    sigma3 = list(sigma2)
    v3 = set(v2)
    s3 = s2
    regles3 = []
    
    for k, regle in enumerate(regles2):
        S = regle[0]
        w = regle[1]  # w = S1 .. Sn
        n = len(w)
        if n > 2:
            prime = lambda Si: "%s'_%d" % (Si, k)  # Ajouter le k dans le nom assure que les nouvelles variables de travail sont toutes uniques
            # Premiere règle : S -> S_1 S'_2
            regles3.append([S, [w[0], prime(w[1])]])
            v3.add(prime(w[1]))
            for i in range(1, len(w) - 2):
                # Pour chaque règle intermédiaire : S'_i -> S_i  S'_{i+1}
                regles3.append([prime(w[i]), [w[i], prime(w[i + 1])]])
                v3.add(prime(w[i]))
                v3.add(prime(w[i + 1]))
            # Dernière règle : S'_{n-1} -> S_{n-1} S_n
            regles3.append([prime(w[n - 2]), [w[n - 2], w[n - 1]]])
            v3.add(prime(w[n - 2]))
        else:
            regles3.append([S, w])
    # Terminé
    nom3 = self.nom + "''"
    return Grammaire(list(sigma3), list(v3), s3, regles3, nom=nom3)

# On ajoute la fonction comme une méthode (au cas où...)
Grammaire.miseChomsky = miseChomsky


# ### 2.6.1 Exemple pour $G_1$

# In[24]:


print(g1)
print("\n(Non) La grammaire", g1.nom, "est-elle de Chomsky ?", estChomsky(g1))
print("\nOn essaie de la mettre sous forme normale de Chomksy...\n")
g1_Chom = miseChomsky(g1)
print(g1_Chom)
print("\n  ==> La grammaire", g1_Chom.nom, "est-elle de Chomsky ?", estChomsky(g1_Chom))


# ### 2.6.2 Exemple pour $G_6$

# In[25]:


print(g5)
print("\n(Non) La grammaire", g5.nom, "est-elle de Chomsky ?", estChomsky(g5))
print("\nOn essaie de la mettre sous forme normale de Chomksy...\n")
g5_Chom = miseChomsky(g5)
print(g5_Chom)
print("\n  ==> La grammaire", g5_Chom.nom, "est-elle de Chomsky ?", estChomsky(g5_Chom))


# ----
# 
# > *C'est tout pour aujourd'hui les amis !*
# > [Allez voir d'autres notebooks](https://github.com/Naereen/notebooks/tree/master/agreg) si vous voulez.
