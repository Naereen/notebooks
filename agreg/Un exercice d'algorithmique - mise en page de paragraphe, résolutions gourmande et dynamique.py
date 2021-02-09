#!/usr/bin/env python
# coding: utf-8

# <h1>Table de matières<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Un-exercice-d'algorithmique---mise-en-page-de-paragraphe,-résolutions-gourmande-et-dynamique" data-toc-modified-id="Un-exercice-d'algorithmique---mise-en-page-de-paragraphe,-résolutions-gourmande-et-dynamique-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Un exercice d'algorithmique - mise en page de paragraphe, résolutions gourmande et dynamique</a></span><ul class="toc-item"><li><span><a href="#Question-1." data-toc-modified-id="Question-1.-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Question 1.</a></span><ul class="toc-item"><li><span><a href="#Réponse-:-non-!" data-toc-modified-id="Réponse-:-non-!-1.1.1"><span class="toc-item-num">1.1.1&nbsp;&nbsp;</span>Réponse : non !</a></span></li><li><span><a href="#Contre-exemple-de-taille-fixée" data-toc-modified-id="Contre-exemple-de-taille-fixée-1.1.2"><span class="toc-item-num">1.1.2&nbsp;&nbsp;</span>Contre exemple de taille fixée</a></span></li><li><span><a href="#Faire-croître-la-différence-entre-les-deux-coûts-vers-l'infini" data-toc-modified-id="Faire-croître-la-différence-entre-les-deux-coûts-vers-l'infini-1.1.3"><span class="toc-item-num">1.1.3&nbsp;&nbsp;</span>Faire croître la différence entre les deux coûts vers l'infini</a></span></li><li><span><a href="#Bonus-:-faire-croître-le-rapport-vers-l'infini-?" data-toc-modified-id="Bonus-:-faire-croître-le-rapport-vers-l'infini-?-1.1.4"><span class="toc-item-num">1.1.4&nbsp;&nbsp;</span>Bonus : faire croître le <em>rapport</em> vers l'infini ?</a></span></li><li><span><a href="#Code-Python-pour-la-méthode-gloutonne" data-toc-modified-id="Code-Python-pour-la-méthode-gloutonne-1.1.5"><span class="toc-item-num">1.1.5&nbsp;&nbsp;</span>Code Python pour la méthode gloutonne</a></span></li><li><span><a href="#Exemples" data-toc-modified-id="Exemples-1.1.6"><span class="toc-item-num">1.1.6&nbsp;&nbsp;</span>Exemples</a></span></li></ul></li><li><span><a href="#Question-2." data-toc-modified-id="Question-2.-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Question 2.</a></span><ul class="toc-item"><li><span><a href="#Problème-d'optimisation-à-résoudre" data-toc-modified-id="Problème-d'optimisation-à-résoudre-1.2.1"><span class="toc-item-num">1.2.1&nbsp;&nbsp;</span>Problème d'optimisation à résoudre</a></span></li><li><span><a href="#Relation-de-récurrence" data-toc-modified-id="Relation-de-récurrence-1.2.2"><span class="toc-item-num">1.2.2&nbsp;&nbsp;</span>Relation de récurrence</a></span></li><li><span><a href="#Implémentation-naïve-par-mémoïsation" data-toc-modified-id="Implémentation-naïve-par-mémoïsation-1.2.3"><span class="toc-item-num">1.2.3&nbsp;&nbsp;</span>Implémentation naïve par mémoïsation</a></span></li><li><span><a href="#Exemples" data-toc-modified-id="Exemples-1.2.4"><span class="toc-item-num">1.2.4&nbsp;&nbsp;</span>Exemples</a></span></li></ul></li><li><span><a href="#Question-3." data-toc-modified-id="Question-3.-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Question 3.</a></span></li><li><span><a href="#Question-4.-Pourquoi-un-coût-cubique-et-pas-linéaire-?" data-toc-modified-id="Question-4.-Pourquoi-un-coût-cubique-et-pas-linéaire-?-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Question 4. Pourquoi un coût cubique et pas linéaire ?</a></span></li><li><span><a href="#Conclusion" data-toc-modified-id="Conclusion-1.5"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Conclusion</a></span></li></ul></li></ul></div>

# # Un exercice d'algorithmique - mise en page de paragraphe, résolutions gourmande et dynamique
# 
# > Source : http://lacl.fr/~lpellissier/Algo1/TD3.pdf, auteur : [Luc Pélissier](http://lacl.fr/~lpellissier/) (2020-21).
# 
# Le problème étudié est l’impression équilibrée d’un paragraphe sur une imprimante.
# Le texte d’entrée est modélisé comme une séquence de $n$ mots de longueurs $l_1,l_2, \dots, l_n$ (mesurées en caractères, que l'on suppose tous de même largeur - c'est le cas par exemple avec une police dite [*à chasse fixe*](https://fr.wikipedia.org/wiki/Police_d'%C3%A9criture_%C3%A0_chasse_fixe)).
# 
# On souhaite imprimer ce paragraphe de manière équilibrée sur un certain nombre de lignes qui contiennent un maximum de $M\geq1$ caractères chacune.
# Le critère d’équilibre est le suivant :
# Si une ligne donnée contient les mots $i$ à $j$ (avec $i \leq j$) et qu’on laisse exactement [une espace](https://fr.wikipedia.org/wiki/Espace_(typographie)) entre deux mots, le nombre de caractères d’espacements supplémentaires à la fin de la ligne est $f(M - j+i - \sum\limits_{k=i}^j l_k)$, qui doit être positif ou nul pour que les mots tiennent sur la ligne.
# L’objectif est de minimiser la somme, sur toutes les lignes *hormis la dernière*, des cubes des nombres de caractères d’espacement présents à la fin de chaque ligne : cela correspond à $f(s) = s^3$.
# 
# - Auteur: [Lilian Besson](https://github.com/Naereen/)
# - Date : jeudi 04/02/2021
# - Licence : [MIT](https://lbesson.mit-license.org/)
# - Lien : https://github.com/Naereen/notebooks/tree/master/agreg/

# *Remarque :* pour bien visualiser ces espaces en fin de fichier, je termine chaque ligne par `;`.

# ---
# ## Question 1.
# 
# **1. Est-ce que l’algorithme glouton consistant à remplir les lignes une à une en mettant à chaque fois le maximum de mots possibles sur la ligne en cours, fournit l’optimum ?**

# ### Réponse : non !

# ### Contre exemple de taille fixée
# 
# Comme le coût est la somme des cubes d'espaces en fin de ligne, on peut penser à un contre-exemple qui va exploiter le fait que $(2x)^3 >> 2 x^3$, et produire un texte qui aura deux lignes identiques (avec $k$ espaces en fin de lignes) lorsqu'on le met en page optimalement, et une ligne quasi complète mais une deuxième ligne quasi vide :

# In[6]:


get_ipython().run_cell_magic('bash', '', 'cat << EOF\nAA AA AA AA AA AA B                    ;\nAA AA AA AA AA AA B                    ;\nEOF > /tmp/test_nongreedy_optimal.txt')


# In[9]:


cat /tmp/test_nongreedy_optimal.txt


# In[7]:


get_ipython().run_cell_magic('bash', '', 'cat << EOF\nAA AA AA AA AA AA B AA AA AA AA AA AA ;\nB                                     ;\nEOF > test_greedy_suboptimal.txt')


# In[10]:


cat /tmp/test_greedy_suboptimal.txt


# Pour l'instant, j'ai codé ça vite fait en Bash pour calculer le coût des deux fichiers :

# In[11]:


get_ipython().run_cell_magic('bash', '', 'clear\nfor file in /tmp/test_*txt; do\n    echo $file\n    hr\n    cat $file\n    hr\n    n=0\n    echo $n\n    for line in $(cat $file | grep -o \' *;\' | sed s/\';\'/\'\'/g | tr \' \' \'X\'); do\n        echo $line; i=$(echo $line | wc -c)\n        i=$((i-1))\n        echo "n = $n, i = $i"; n=$((n + i*i*i))\n        echo "=> n = $n, i = $i"\n    done\ndone')


# On voit que la solution gourmande a un coût de 54873 alors que la solution non gourmande (optimale) a un coût de 16000.

# ### Faire croître la différence entre les deux coûts vers l'infini
# 
# On peut juste produire $n$ fois ces deux lignes, et le coût de la solution gourmande sera $54873 n$ et le coût optimal sera $16000 n$.
# Cela montre que la **différence** entre les deux coûts n'est pas bornée.

# ### Bonus : faire croître le *rapport* vers l'infini ?
# On devrait pouvoir aussi faire croître le rapport des deux coûts vers l'infini : plutôt que de générer ces $n$ lignes identiques, on a juste à augmenter la longueur de ces lignes (et n'en avoir que deux, mais très longues).
# Comme le coût est cubique en le nombre d'espaces, on aura bien un rapport non borné entre le coût gourmand (sous optimal) et le coût optimal.
# 
# **Corollaire :** cela montre que la solution gourmande n'est pas un k-approximation du problème étudié.
# 

# ### Code Python pour la méthode gloutonne
# 
# Même si elle n'est pas efficace, on va commencer par écrire cette méthode gloutonne :

# In[68]:


from typing import Tuple, List


# In[115]:


def longueur_ligne(ligne: List[str]) -> int:
    return sum(len(mot) for mot in ligne)


# In[130]:


def mise_en_page_paragraphe_gloutonne(longueur_max:int, mots: List[str]) -> List[List[str]]:
    print(f"Longueur maximum de la ligne = {longueur_max}")
    print(f"Longueur des mots = {longueurs_mots}")
    
    assert all(
        1 <= len(mot) <= longueur_max
        for mot in mots
    )
    
    mots = list(mots)[::-1]  # on les lit de la fin

    paragraphes = []
    ligne_actuelle = []
    longueur_ligne_actuelle = 0

    while mots:
        # print(f"mots = {mots}")
        mot_a_placer = mots.pop()
        # print(f"  mot_a_placer = {mot_a_placer}")
        # print(f"  ligne_actuelle = {ligne_actuelle}")
        
        if longueur_ligne(ligne_actuelle) + len(mot_a_placer) <= longueur_max:
            ligne_actuelle += [mot_a_placer]
            longueur_ligne_actuelle += len(mot_a_placer)
            if longueur_ligne_actuelle < longueur_max:
                ligne_actuelle += [" "]
                longueur_ligne_actuelle += 1

        # 1 + car on ajoute l'espace
        if longueur_ligne_actuelle + 1 >= longueur_max:
            paragraphes.append(ligne_actuelle)
            ligne_actuelle = []
            longueur_ligne_actuelle = 0

        # print(f"  ligne_actuelle = {ligne_actuelle}")
        # print(f"  paragraphes = {paragraphes}")
    
    # dernière ligne si pas encore ajoutée
    if ligne_actuelle:
        paragraphes.append(ligne_actuelle)

    # puis on complète avec des espaces en fin de lignes
    for ligne in paragraphes:
        espaces_fin_paragraphe = longueur_max - longueur_ligne(ligne)
        ligne += [" "] * espaces_fin_paragraphe
    
    assert all(
        longueur_ligne(ligne) == longueur_max
        for ligne in paragraphes
    )
    return paragraphes


# In[131]:


def print_paragraphes(paragraphes: List[List[str]]):
    print(f"\n# Mise en page finale d'un texte de {len(paragraphes)} lignes ")
    for ligne in paragraphes:
        print("".join(ligne) + ";")


# In[163]:


from typing import Callable


# In[164]:


def cout_paragraphes(paragraphes: List[List[str]], cout: Callable[[int], int]) -> int:
    lignes = [ "".join(ligne) for ligne in paragraphes ]
    espaces_de_fin = [
        len(ligne) - len(ligne.rstrip())
        for ligne in lignes
    ]
    return sum(cout(es) for es in espaces_de_fin)


# In[172]:


def print_couts(paragraphes):
    print("- Nombre d'espaces en fin de lignes =", cout_paragraphes(paragraphes, cout= lambda i: i))
    print("- Somme des carrés des nombres d'espaces en fin de lignes =", cout_paragraphes(paragraphes, cout= lambda i: i**2))
    print("- Somme des cubes des nombres d'espaces en fin de lignes =", cout_paragraphes(paragraphes, cout= lambda i: i**3))


# ### Exemples

# Un premier exemple simple :

# In[181]:


longueur_max = len("AA AA ")  # sans le ;
mots = ["AA", "AA", "AA", "B"]


# In[182]:


paragraphes = mise_en_page_paragraphe_gloutonne(longueur_max, mots)


# In[183]:


print_paragraphes(paragraphes)
print_couts(paragraphes)


# Peut-on retrouver la solution suivante, qui avait été calculée à la main ?

# In[184]:


cat /tmp/test_greedy_suboptimal.txt


# In[185]:


longueur_max = len("AA AA AA AA AA AA AA AA AA AA AA AA AA ")  # sans le ;
mots = ["AA"]*13 + ["B"]*1


# Vérifions cela :

# In[186]:


paragraphes = mise_en_page_paragraphe_gloutonne(longueur_max, mots)


# In[187]:


print_paragraphes(paragraphes)
print_couts(paragraphes)


# ---
# ## Question 2.
# 
# **2. Donner un algorithme de programmation dynamique résolvant le problème. Analyser sa complexité en temps et en espace. Et implémenter le dans le langage de votre choix. Vérifier qu'il donne la réponse optimale sur l'exemple trouvé en question 1. (ou en tous cas, une meilleure réponse).**

# On va déjà écrire le problème d'optimisation à résoudre, puis une relation de récurrence.
# En écrivant un algorithme récursif naïf mais avec mémoïsation, on obtiendra un algorithme de programmation dynamique.

# ### Problème d'optimisation à résoudre
# 
# On se donne $M\in\mathbb{N}^*$ la taille de ligne, et un nombre $N\in\mathbb{N}^*$ objets, de longueurs $l_k \in [1,\dots,M]$.
# On souhaite minimiser le coût suivant, qui dépend de :
# 
# - $L$ nombre de ligne,
# - $\forall x \in{1,\dots,L-1}, \ell_x$ indique l'indice de fin des mots présents en ligne $x$. Avec $\ell_0 = 0$ pour indiquer une ligne 0 vide.
# 
# $$
#     \min_{
#             L\in\{1,\dots,M\}, \\
#             \ell_1,\dots,\ell_{L-1}\in\{1,\dots,N\},\\
#             \forall x\in\{1,\dots,L-1\}, \ell_{x+1} \geq \ell_x + 1,
#         }
#         \sum_{x=1}^{L-1}
#         (M - \ell_{x+1} + \ell_x - \sum_{k=\ell_x}^{\ell_{x+1}} l_k)^3
# $$
# 
# - On ne compte pas les espaces de la dernière ligne, d'où le L-1 dans la somme.

# ### Relation de récurrence
# 
# **Initialisation :**
# S'il n'y a qu'un seul mot, la solution est triviale : on le place sur la première ligne, et on a terminé.
# 
# **Hérédité :**
# On considère le premier mot $l_1$ et le deuxième mot $l_2$.
# Le coût de la solution optimale est le minimum des coûts des deux solutions optimales aux sous-problèmes suivants (de taille strictement plus petite) :
# 
# 1. on place les deux premiers mots ensemble, et on remplace donc $l_1,l_2$ par $l_1' := l_1 + l_2 + 1$, et la suite des mots est juste décalée : $l_k' := l_{k+1}$. Ce cas a $N-1$ mots ;
# 2. on place le premier mot sur sa propre ligne (cas de base), et on résound avec les mots restants : $l_k' := l_{k+1}$. Ce cas a aussi $1$ et $N-1$ mots sur les deux sous-problèmes.

# TODO

# ### Implémentation naïve par mémoïsation

# In[15]:


from typing import List, Tuple


# In[14]:


from functools import lru_cache as memoize


# In[213]:


couts = {
    "lineaire": lambda i: i,
    "quadratique": lambda i: i**2,
    "cubique": lambda i: i**3,
}


# In[240]:


@memoize(maxsize=None)
def mise_en_page_paragraphe(
        longueur_max:int,
        mots: Tuple[str],
        choix_cout: str="cubique",
    ) -> List[List[str]]:
    print(f"Longueur maximum de la ligne = {longueur_max}")
    mots = list(mots)
    print(f"Longueur des mots = {mots}")
    
    assert len(mots) > 0
    if len(mots) == 1:
        return [ [mots[0]] ]
    
    else:
        cout = couts[choix_cout]
        
        # première possibilité, on regroupe les deux premiers mots ensemble
        mots1 = [mots[0] + " " + mots[1]] + mots[2:]
        cout1 = float('+inf')
        if len(mots1[0]) <= longueur_max:
            solution1 = mise_en_page_paragraphe(longueur_max, tuple(mots1))
            cout1 = cout_paragraphes(solution1, cout)
        
        # deuxième possibilité, on place mots[0] tout seul, et on résoud les autres mots
        sous_solution2 = mise_en_page_paragraphe(longueur_max, tuple(mots[1:]))
        morceau_gauche2 = [ mots[0] ] + [" "] * (longueur_max - len(mots[0]))
        solution2 = [ morceau_gauche2 ] + sous_solution2
        cout2 = cout_paragraphes(solution2, cout)

        if cout1 < cout2:
            recombinaison_1 = []
            for ligne in solution1:
                mots_ici = "".join(ligne).split(" ")
                ligne_ici = [ mots_ici[0] ]
                for mot in mots_ici[1:]:
                    if mot:
                        ligne_ici += [" ", mot] 
                ligne_ici += [" "] * (longueur_max - longueur_ligne(ligne_ici))
                recombinaison_1.append(ligne_ici)
            return recombinaison_1
        else:
            recombinaison_2 = solution2
            return recombinaison_2


# ### Exemples

# In[263]:


longueur_max = len("AA AA AA")

mots = ["AA", "AA", "AA", "B"]
mots = tuple(mots)  # pour le rendre Hashable pour le @memoize


# Vérifions cela :

# In[264]:


paragraphes = mise_en_page_paragraphe(longueur_max, mots)


# In[266]:


print_paragraphes(paragraphes)
print_couts(paragraphes)


# Peut-on retrouver la solution suivante, qui avait été calculée à la main ?

# In[280]:


cat /tmp/test_nongreedy_optimal.txt


# In[281]:


longueur_max = len("AA AA AA AA AA AA B                   ")

mots = (["AA"]*6 + ["B"]*1) * 2
mots = tuple(mots)  # pour le rendre Hashable pour le @memoize


# Vérifions cela :

# In[284]:


paragraphes = mise_en_page_paragraphe_gloutonne(longueur_max, mots)


# In[285]:


print_paragraphes(paragraphes)
print_couts(paragraphes)


# Et pour la solution dynamique :

# In[286]:


paragraphes = mise_en_page_paragraphe(longueur_max, mots)


# In[287]:


print_paragraphes(paragraphes)
print_couts(paragraphes)


# ---
# ## Question 3.
# 
# **3. Supposons que pour la fonction de coût à minimiser, on ait simplement choisi la somme des nombres de caractères d’espacement présents à la fin de chaque ligne. Est-ce que l’on peut faire mieux en complexité que pour la question ?**
# 
# Oui la solution gourmande, qui est donc au plus linéaire en temps et demande une mémoire de travail supplémentaire constante (ou bornée par la taille du plus long mot, selon de savoir si `len(mot)` est en $O(1)$ ou en $O(|\text{mot}|)$), sera optimale.

# ---
# ## Question 4. Pourquoi un coût cubique et pas linéaire ?
# 
# **4. *(Plus informel)* Qu’est-ce qui à votre avis peut justifier le choix de prendre les cubes plutôt quesimplement les nombres de caractères d’espacement en fin de ligne ?**
# 
# Si le coût est linéaire, alors la solution gourmande sera optimale (ou en tous cas une approximation à facteur constant).
# Mais c'est aussi que l'affichage ne fera pas de différence entre les deux exemples ci dessous, alors que l'on est clairement plus satisfait du rendu visuel du deuxième, qui équilibre mieux les deux lignes.
# 
# (*je ne suis pas trop sûr de tout ça*)
# 
# TODO mieux expliquer !

# On peut vérifier la solution trouvée avec un coût carré et pas cubique :

# In[292]:


paragraphes = mise_en_page_paragraphe(longueur_max, mots, choix_cout="quadratique")


# In[293]:


print_paragraphes(paragraphes)
print_couts(paragraphes)


# Sur cet exemple, on obtient exactement la même solution.
# 
# Mais je pense qu'on peut trouver des exemples où la solution avec un coût cubique est différente de celle avec un coût quadratique.

# ## Conclusion
# 
# Et si vous cherchiez à résoudre ça dans votre langage de programmation favori ?
# En Python ou en OCaml, cela ne devrait pas être trop difficile.
