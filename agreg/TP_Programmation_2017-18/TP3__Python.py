#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#TP-3---Programmation-pour-la-préparation-à-l'agrégation-maths-option-info" data-toc-modified-id="TP-3---Programmation-pour-la-préparation-à-l'agrégation-maths-option-info-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>TP 3 - Programmation pour la préparation à l'agrégation maths option info</a></span></li><li><span><a href="#Arbres-binaires-de-recherche" data-toc-modified-id="Arbres-binaires-de-recherche-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Arbres binaires de recherche</a></span><ul class="toc-item"><li><span><a href="#Exercice-1-:-ABR" data-toc-modified-id="Exercice-1-:-ABR-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Exercice 1 : ABR</a></span><ul class="toc-item"><li><span><a href="#Définition-du-type-Abr-et-exemples-de-valeurs" data-toc-modified-id="Définition-du-type-Abr-et-exemples-de-valeurs-2.1.1"><span class="toc-item-num">2.1.1&nbsp;&nbsp;</span>Définition du type Abr et exemples de valeurs</a></span></li><li><span><a href="#Compter-les-clés-d'un-Abr" data-toc-modified-id="Compter-les-clés-d'un-Abr-2.1.2"><span class="toc-item-num">2.1.2&nbsp;&nbsp;</span>Compter les clés d'un Abr</a></span></li></ul></li><li><span><a href="#Exercice-2-:-trouve" data-toc-modified-id="Exercice-2-:-trouve-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Exercice 2 : <code>trouve</code></a></span></li><li><span><a href="#Exercice-3-:-insertion" data-toc-modified-id="Exercice-3-:-insertion-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Exercice 3 : <code>insertion</code></a></span></li><li><span><a href="#Exercice-4-:-suppression" data-toc-modified-id="Exercice-4-:-suppression-2.4"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>Exercice 4 : <code>suppression</code></a></span></li><li><span><a href="#Exercice-5-:-fusion" data-toc-modified-id="Exercice-5-:-fusion-2.5"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>Exercice 5 : <code>fusion</code></a></span></li><li><span><a href="#Exercice-6" data-toc-modified-id="Exercice-6-2.6"><span class="toc-item-num">2.6&nbsp;&nbsp;</span>Exercice 6</a></span><ul class="toc-item"><li><span><a href="#Avantages-et-les-inconvénients-des-ABR" data-toc-modified-id="Avantages-et-les-inconvénients-des-ABR-2.6.1"><span class="toc-item-num">2.6.1&nbsp;&nbsp;</span>Avantages et les inconvénients des ABR</a></span></li><li><span><a href="#Autres-structures-de-données-(clef,-valeur)" data-toc-modified-id="Autres-structures-de-données-(clef,-valeur)-2.6.2"><span class="toc-item-num">2.6.2&nbsp;&nbsp;</span>Autres structures de données (clef, valeur)</a></span></li></ul></li></ul></li><li><span><a href="#Tas-binaire-min-(ou-max)" data-toc-modified-id="Tas-binaire-min-(ou-max)-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Tas binaire min (ou max)</a></span><ul class="toc-item"><li><span><a href="#Solution-concise-:-tas-binaire-avec-des-arbres" data-toc-modified-id="Solution-concise-:-tas-binaire-avec-des-arbres-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Solution concise : tas binaire avec des arbres</a></span></li><li><span><a href="#Exercice-7-:-arbre-tournoi" data-toc-modified-id="Exercice-7-:-arbre-tournoi-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Exercice 7 : arbre tournoi</a></span></li><li><span><a href="#Exercice-8-:-parent,-fils_gauche-et-fils_droit" data-toc-modified-id="Exercice-8-:-parent,-fils_gauche-et-fils_droit-3.3"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>Exercice 8 : <code>parent</code>, <code>fils_gauche</code> et <code>fils_droit</code></a></span></li><li><span><a href="#Exercice-9-:-echange" data-toc-modified-id="Exercice-9-:-echange-3.4"><span class="toc-item-num">3.4&nbsp;&nbsp;</span>Exercice 9 : <code>echange</code></a></span></li><li><span><a href="#Exercice-10-:-insertion" data-toc-modified-id="Exercice-10-:-insertion-3.5"><span class="toc-item-num">3.5&nbsp;&nbsp;</span>Exercice 10 : <code>insertion</code></a></span></li><li><span><a href="#Exercice-11-:-creation" data-toc-modified-id="Exercice-11-:-creation-3.6"><span class="toc-item-num">3.6&nbsp;&nbsp;</span>Exercice 11 : <code>creation</code></a></span></li><li><span><a href="#Exercice-12-:-diminue_clef" data-toc-modified-id="Exercice-12-:-diminue_clef-3.7"><span class="toc-item-num">3.7&nbsp;&nbsp;</span>Exercice 12 : <code>diminue_clef</code></a></span></li><li><span><a href="#Exercice-13-:-extraire_min" data-toc-modified-id="Exercice-13-:-extraire_min-3.8"><span class="toc-item-num">3.8&nbsp;&nbsp;</span>Exercice 13 : <code>extraire_min</code></a></span></li><li><span><a href="#Exercice-14-:-tri-par-tas" data-toc-modified-id="Exercice-14-:-tri-par-tas-3.9"><span class="toc-item-num">3.9&nbsp;&nbsp;</span>Exercice 14 : tri par tas</a></span></li></ul></li><li><span><a href="#Union-Find" data-toc-modified-id="Union-Find-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Union-Find</a></span><ul class="toc-item"><li><span><a href="#Exercice-15-:-Union-Find-avec-tableaux" data-toc-modified-id="Exercice-15-:-Union-Find-avec-tableaux-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Exercice 15 : Union-Find avec tableaux</a></span></li><li><span><a href="#Exercice-16-:-Union-Find-avec-forêts" data-toc-modified-id="Exercice-16-:-Union-Find-avec-forêts-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>Exercice 16 : Union-Find avec forêts</a></span></li><li><span><a href="#Exercice-17-:-Bonus-&amp;-discussions" data-toc-modified-id="Exercice-17-:-Bonus-&amp;-discussions-4.3"><span class="toc-item-num">4.3&nbsp;&nbsp;</span>Exercice 17 : Bonus &amp; discussions</a></span></li><li><span><a href="#Bonus-:-algorithme-de-Kruskal" data-toc-modified-id="Bonus-:-algorithme-de-Kruskal-4.4"><span class="toc-item-num">4.4&nbsp;&nbsp;</span>Bonus : algorithme de Kruskal</a></span><ul class="toc-item"><li><span><a href="#Représentations-de-graphe-pondérés" data-toc-modified-id="Représentations-de-graphe-pondérés-4.4.1"><span class="toc-item-num">4.4.1&nbsp;&nbsp;</span>Représentations de graphe pondérés</a></span></li><li><span><a href="#Algorithme-de-Kruskal" data-toc-modified-id="Algorithme-de-Kruskal-4.4.2"><span class="toc-item-num">4.4.2&nbsp;&nbsp;</span>Algorithme de Kruskal</a></span></li></ul></li></ul></li><li><span><a href="#Conclusion" data-toc-modified-id="Conclusion-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Conclusion</a></span></li></ul></div>

# # TP 3 - Programmation pour la préparation à l'agrégation maths option info

# - En Python.

# In[221]:


import sys
print(sys.version)


# ----
# # Arbres binaires de recherche

# ## Exercice 1 : ABR

# ### Définition du type Abr et exemples de valeurs

# Comme au TP1 et TP2, plutôt que d'utiliser des classes, je préfère utiliser des dictionnaires avec une seule clé et une seule valeur pour représenter des structures arborescentes.
# La valeur est ici `None` s'il n'y a rien à stocker (pour une feuille `Leaf` par exemple), ou un tuple `k, v, l, r` pour un `Node`.
# 
# Cela simule la syntaxe de OCaml pour la création de valeurs, et le *pattern matching* (filtrage) est simulé par des `if/elif/else` testant la clé.

# In[222]:


Leaf = {"Leaf": None}

def Node(k: int, v: str, l: dict, r: dict) -> dict:
    """ Crée un arbre binaire avec un noeud de clé k, de valeur v, de fils gauche l et de fils droit r."""
    return {"Node": (k, v, l, r)}


# On peut aussi utiliser une approche objet, et définir une classe.
# L'avantage sera un accès plus rapide aux différentes valeurs stockées : `arbre.l` donne le fils gauche.

# In[223]:


class NodeClass():
    def __init__(self, k: int, v: str, l, r):
        self.k = k
        self.v = v
        self.l = l
        self.r = r


# ##### Note sur le typage en Python
# En Python, avec le module [`typing`](https://docs.python.org/3/library/typing.html), on peut définir des alias de types (non récursifs), comme en OCaml.
# 
# On peut ensuite ajouter *indications* de typage, à des définitions de variables ou de fonctions.

# In[17]:


from typing import Dict, List, Any, Union, Tuple

Abr = Dict[str, Union[str, Tuple[int, str, Any, Any]]]


# ##### Exemples d'arbres binaires

# In[35]:


exemple_arbre_binaire1: Abr = Node(1, "a", Leaf, Leaf)
print(exemple_arbre_binaire1)

exemple_arbre_binaire2: Abr = Node(2, "b", exemple_arbre_binaire1, Leaf)
print(exemple_arbre_binaire2)

exemple_arbre_binaire3: Abr = Node(3, "c", exemple_arbre_binaire1, exemple_arbre_binaire2)
print(exemple_arbre_binaire3)


# Pour afficher joliment des structures arborescentes on peut utiliser `pprint.pprint` :

# In[36]:


from pprint import pprint


# In[38]:


pprint(exemple_arbre_binaire2)


# In[39]:


pprint(exemple_arbre_binaire3)


# En OCaml on pouvait définir un type **récursif** comme cela (observez comment `abr` intervient dans la définition de `anode` qui intervient dans la définition de `abr`...), mais en Python ce n'est pas possible.

# ```ocaml
# type 'a abr =
#     | Leaf
#     | Node of 'a anode
# 
# and 'b anode = {
#     key   : int;
#     value : 'b;
#     left  : 'b abr; (* pour toute clé [k] dans [left],  [k] < [key] *)
#     right : 'b abr  (* pour toute clé [k] dans [right], [key] < [k] *)
# }
# ;;
# ```

# ### Compter les clés d'un Abr
# Compter les clés est facile :

# In[240]:


def nb_keys(a: Abr) -> int:
    """ Calcule le nombre de clés d'un arbre binaire a."""
    # on simule "match a with ..." avec des if/elif/else
    if "Leaf" in a:  # simule | Leaf ->
        return 0
    elif "Node" in a:
        _, _, l, r = a["Node"]
        return 1 + nb_keys(l) + nb_keys(r)
    else:  # ce cas n'arrive jamais
        return -1


# En OCaml, l'avantage du *pattern matching* est qu'il nous prévient si le test n'est pas exhaustif.
# En Python, on ne peut pas avoir ce genre d'aide.

# ```ocaml
# let rec nb_keys (a : 'a abr) : int =
#     match a with
#     (* si on oublie le cas de base : | Leaf -> 0 *)
#     | Node n -> 1 + nb_keys n.left + nb_keys n.right
# ;;
# (* Cette fonction sera bien typée, mais pas correcte :
# l'interprète ou le compilateur prévient par un Warning :
# Warning 8: this pattern-matching is not exhaustive.
# Here is an example of a case that is not matched:
# Leaf
# *)
# ```

# Il faut prendre l'habitude de vérifier vos fonctions sur tous les exemples définis précédemment :

# In[241]:


print("L'arbre binaire suivant :")
pprint(exemple_arbre_binaire1)
print("contient", nb_keys(exemple_arbre_binaire1), "clés.")


# In[242]:


print("L'arbre binaire suivant :")
pprint(exemple_arbre_binaire2)
print("contient", nb_keys(exemple_arbre_binaire2), "clés.")


# In[243]:


print("L'arbre binaire suivant :")
pprint(exemple_arbre_binaire3)
print("contient", nb_keys(exemple_arbre_binaire3), "clés.")


# ##### Extraire une liste des clés
# Bonus : on peut extraire une liste des clés, très facilement :

# In[244]:


def list_keys(a: Abr) -> List[str]:
    """ Extraire la liste des clés d'un arbre binaire a (parcours en profondeur)."""
    # on simule "match a with ..." avec des if/elif/else
    if "Leaf" in a:  # simule | Leaf ->
        return []
    elif "Node" in a:
        v, k, l, r = a["Node"]
        return [k] + list_keys(l) + list_keys(r)
    else:  # ce cas n'arrive jamais
        return []


# In[245]:


print("L'arbre binaire suivant :")
pprint(exemple_arbre_binaire1)
print("contient ces clés :", list_keys(exemple_arbre_binaire1))


# In[246]:


print("L'arbre binaire suivant :")
pprint(exemple_arbre_binaire2)
print("contient ces clés :", list_keys(exemple_arbre_binaire2))


# In[247]:


print("L'arbre binaire suivant :")
pprint(exemple_arbre_binaire3)
print("contient ces clés :", list_keys(exemple_arbre_binaire3))


# ## Exercice 2 : `trouve`

# In[264]:


def trouve(a: Abr, x: int) -> Union[int, None]:
    # Optional[int] is equivalent to Union[int]
    if "Leaf" in a:
        return None
    elif "Node" in a:
        k, v, l, r = a["Node"]
        if k == x:   # on a trouvé la valeur v associée à la clé k = x
            return v
        elif x < k:
            # on cherche dans le sous arbre de gauche si la valeur cherchée
            # est plus petite que la clé du noeud
            return trouve(l, x)
        elif x > k:
            # sinon on cherche dans le sous arbre de droite
            return trouve(r, x)
        # ce dernier cas ne doit pas arriver
        else: raise ValueError("Incapable de trouver {} dans l'arbre binaire {}".format(x, a))


# In[265]:


print("En cherchant la clé 1 dans l'arbre binaire suivant")
pprint(exemple_arbre_binaire1)
print("on trouve la valeur associée =", trouve(exemple_arbre_binaire1, 1))


# In[266]:


print("En cherchant la clé 3 dans l'arbre binaire suivant")
pprint(exemple_arbre_binaire3)
print("on trouve la valeur associée =", trouve(exemple_arbre_binaire3, 3))


# Exemple de recherche qui ne fonctionne pas (sans renvoyer d'erreur, juste un `None`) :

# In[267]:


print("En cherchant la clé 42 dans l'arbre binaire suivant")
pprint(exemple_arbre_binaire3)
print("on trouve la valeur associée =", trouve(exemple_arbre_binaire3, 42))


# Si on veut que la recherche **échoue** si la clé cherchée n'est pas présente, on peut changer le code et écrire :

# In[268]:


def trouve_avec_erreur(a: Abr, x: int) -> int:  # notez que le type de retour est juste un entier désormais
    if "Leaf" in a:
        raise ValueError("Incapable de trouver {} dans l'arbre binaire {}".format(x, a))
    elif "Node" in a:
        k, _, l, r = a["Node"]
        if k == x:   # on a trouvé la valeur v associée à la clé k = x
            return v
        elif x < k:  # on cherche dans le sous arbre de gauche
            return trouve_avec_erreur(l, x)
        elif x > k:  # on cherche dans le sous arbre de droite
            return trouve_avec_erreur(r, x)
        # ce dernier cas ne doit pas arriver
        else: raise ValueError("Incapable de trouver {} dans l'arbre binaire {}".format(x, a))


# In[269]:


print("En cherchant la clé 42 dans l'arbre binaire suivant")
pprint(exemple_arbre_binaire3)
print("on trouve la valeur associée =", trouve_avec_erreur(exemple_arbre_binaire3, 42))


# La `traceback` (affichage de l'erreur) nous montre même les appels récursifs qui ont menés à l'erreur. (ici, deux appels récursifs sur le fils droit, puisque 42 était plus grand que les deux clés successives 3 et 2).

# ## Exercice 3 : `insertion`

# In[270]:


def insertion(a: Abr, k: int, v: str) -> Abr:
    if "Leaf" in a:  # a arbre vide, on crée un noeud ayant deux fils vides
        return Node(k, v, Leaf, Leaf)
    elif "Node" in a:
        ka, va, l, r = a["Node"]
        if k == ka:   # on ne change pas les fils
            return Node(k, v, l, r) # change va -> v
        elif k < ka:  # on change le fils gauche
            return Node(ka, va, insertion(l, k, v), r)
        elif k > ka:  # on change le fils droit
            return Node(ka, va, l, insertion(r, k, v))
        # ce dernier cas ne doit pas arriver
        else:
            raise ValueError("Incapable d'insérer {}:{} dans l'arbre binaire {}".format(k, v, a))


# Quelques tests :

# In[271]:


pprint(insertion(insertion(Leaf, 2, "deux"), 1, "un"))
print("Valeur trouvée pour la clé 1 =", trouve(insertion(insertion(Leaf, 2, "deux"), 1, "un"), 1))


# In[272]:


pprint(insertion(insertion(Leaf, 2, "deux"), 1, "un"))
print("Valeur trouvée pour la clé 2 =", trouve(insertion(insertion(Leaf, 2, "deux"), 1, "un"), 2))


# In[273]:


pprint(insertion(insertion(Leaf, 2, "deux"), 1, "un"))
print("Valeur trouvée pour la clé 3 =", trouve(insertion(insertion(Leaf, 2, "deux"), 1, "un"), 3))


# ## Exercice 4 : `suppression`

# `minimum a` renvoie le couple `(key, value)` de l'arbre `a` avec `key` minimal dans `a`.
# Lance une exception si `a` est vide.

# In[274]:


def minimum(a: Abr) -> Tuple[int, str]:
    if "Leaf" in a:
        raise ValueError("Arbre vide")
    elif "Node" in a:
        k, v, l, r = a["Node"]
        if "Leaf" in l: # sous-arbre gauche vide : le minimum est le noeud actuel
            return (k, v)
        else:  # sinon, le minimum de l'arbre actuel est à chercher dans le sous-arbre gauche
            return minimum(l)
    else:
        raise ValueError("Incapable de trouver le minimum dans l'arbre binaire {}".format(a))


# On pourrait être plus élégant que ces tests `"Leaf" in a` et `"Node" in a`, et utiliser deux fonctions `is_leaf(a)` et `is_node(a)`. Cela permettrait de cacher un peu plus les détails d'implémentations.

# In[275]:


def is_leaf(a: Abr) -> bool:
    return "Leaf" in a  # ou Leaf == a

def is_node(a: Abr) -> bool:
    return "Node" in a


# In[276]:


minimum(insertion (insertion(Leaf, 1, "un"), 2, "deux"))


# In[277]:


minimum(insertion (insertion(Leaf, 2, "deux"), 1, "un"))


# La suppression se fait dans le cas où la clé `x` est trouvée :

# In[278]:


def suppression(a: Abr, x: int) -> Abr:
    if "Leaf" in a:  # rien à supprimer
        return Leaf
    elif "Node" in a:
        k, v, l, r = a["Node"]
        if k == x:  # trouvé
            if "Leaf" in r:  # sous-arbre droit vide : on renvoie le sous-arbre gauche
                return l
            else:
                # on va remonter le minimum de sous-arbre droit au noeud actuel et aller supprimer ce minimum
                k_min, v_min = minimum(r)
                return Node(k_min, v_min, l, suppression(r, k_min))
                # de façon équivalente, on pourrait écrire
                # k_max, v_max = maximum(l)
                # return Node(k_max, v_max, suppression(l, k_max), r)
        elif x < k:  # à chercher à gauche
            return Node(k, v, suppression(l, k), r)
        elif x > k:  # à chercher à droite
            return Node(k, v, l, suppression(r, k))
        else: # n'arrive jamais
            raise ValueError("Incapable de supprimer {} dans l'arbre binaire {}".format(x, a))


# Deux exemples :

# In[279]:


print(trouve (suppression (insertion (insertion(Leaf, 2, "deux"), 1, "un"), 1), 1))
print(trouve (suppression (insertion (insertion(Leaf, 2, "deux"), 1, "un"), 1), 2))


# ## Exercice 5 : `fusion`

# `decoupe a k` sépare l'arbre `a` en deux arbres `(a1, a2)` tels que l'union des clés-valeurs de `a1` et `a2` est égale à l'ensemble des clés-valeurs de `a` (privé de l'association liée à `k` si elle était présente dans `a`).
# 
# - Les clés de `a1` sont `<` à `k`.
# - Les clés de `a2` sont `>` à `k`.

# In[280]:


def decoupe(a: Abr, x: int) -> Tuple[Abr, Abr]:
    """
   [decoupe a k] sépare l'arbre [a] en deux arbres [(a1, a2)]
   tels que l'union des clés-valeurs de [a1] et [a2] est égale à
   l'ensemble des clés-valeurs de [a] (privé de l'association
   liée à [k] si elle était présente dans [a]).
   Les clés de [a1] sont < à [k].
   Les clés de [a2] sont > à [k].
   """
    if "Leaf" in a:  # rien à supprimer
        return (Leaf, Leaf)
    elif "Node" in a:
        k, v, l, r = a["Node"]
        if k == x:  # trouvé
            return (l, r)
        elif x < k:  # à chercher à gauche
            left1, left2 = decoupe(l, x)
            return (left1, Node(k, v, left2, r))
        elif x > k:  # à chercher à droite
            right1, right2 = decoupe(r, x)
            return (Node(k, v, l, right1), right2)
        else: # n'arrive jamais
            raise ValueError("Incapable de découper dans l'arbre binaire {}".format(x, a))
    else: # n'arrive jamais
        raise ValueError("Incapable de découper dans l'arbre binaire {}".format(x, a))


# Et maintenant la fusion n'est pas très difficile :

# In[281]:


def fusion(a1: Abr, a2: Abr) -> Abr:
    """ Fusionne les deux arbres binaires de recherche a1 et a2.
    Convention : si une clé est présente dans les deux arbres, nous gardons celle de [a1]
    """
    if "Leaf" in a1:  # rien à supprimer
        return a2
    elif "Node" in a1:
        k, v, l, r = a1["Node"]
        left2, right2 = decoupe(a2, k)
        return Node(k, v, fusion(l, left2), fusion(r, right2))
    else: # n'arrive jamais
        raise ValueError("Incapable de fusionner les arbres binaires {} et {}".format(a1, a2))


# In[283]:


a1 = insertion (insertion(Leaf, 2, "deux"), 1, "un")
a2 = insertion (insertion(Leaf, 2, "two"), 3, "three")

print(trouve (fusion(a1, a2), 1))  # "un" depuis a1
print(trouve (fusion(a1, a2), 2))  # "deux" depuis a1 et pas "two" from a2
print(trouve (fusion(a1, a2), 3))  # "three" from a2
print(trouve (fusion(a1, a2), 4))  # None : pas trouvé !


# ## Exercice 6
# ### Avantages et les inconvénients des ABR
# 
# > Discussions durant la séance...
# 
# ### Autres structures de données (clef, valeur)
# 
# - Les **tables de hashage**
# - autres idées ? envoyez moi un mail : lilian.besson at ens-rennes.fr ou [ouvrez un ticket sur GitHub](https://github.com/Naereen/notebooks/issues/new)

# ----
# # Tas binaire min (ou max)
# 
# Un tas binaire est un arbre binaire dans lequel tous les étages sont remplis sauf éventuellement le dernier qui doit être bien tassé à gauche.
# 
# Un tas binaire *min* signifie en plus que l'arbre est tournoi min c'est-à-dire que pour tout sous-arbre, la valeur de la racine est plus petite que les valeurs de tous les autres noeuds.
# 
# Un tas binaire *max* vérifie la même propriété mais la valeur de la racine est plus grande que les valeurs de tous les autres noeuds, pour tout sous-arbre.
# On les appelle également files de priorité (min, max).
# 
# La structure de tas min intervient dans de nombreux algorithmes comme ceux de Dijkstra et de Prim mais également dans les systèmes d'exploitation (ordonnancement des tâches et des processus).
# 
# Contrairement aux arbres binaires de recherche qui stockent des couples (clef, valeur), ici on stockera des couples (rang, valeur).

# ## Solution concise : tas binaire avec des arbres
# 
# Pour commencer, je préfère donner une première implémentation qui ne sera pas la plus efficace en mémoire, mais la plus simple à comprendre.
# Les tas binaires peuvent être représentés avec des arbres binaires, exactement comme dans l'exercice précédent.
# 
# > Référence: Chris Okasaki, "*Purely Functional Data Structures*".

# On utilise la même représentation que précédemment : un tas binaire est soit vide (`E`) soit un noeud ayant exactement deux fils (qui sont des tas binaires, éventuellement vides).
# Un noeud contient une valeur entière (`v`) à laquelle on donne un rang entier (`rang`), un fils gauche (`l`) et un fils droit (`d`) :

# In[226]:


E = {"E": None}
T = lambda rang, v, l, r: {"T": (rang, v, l, r)}

TasBinaire = Union[
    Dict[str, None],  # pour E = {"E": None}
    Dict[str, Tuple[int, str, dict, dict]]  # pour T = {"T" : (k, v, l, r)}
    # ici si on pouvait écrire des types récursifs, il faudrait écrire
    # Dict[str, Tuple[int, str, TasBinaire, TasBinaire]]
]


# In[107]:


def rank(t: TasBinaire) -> int:
    """ Rang d'un tas binaire, r lu depuis le champ T(r, _, _, _)."""
    if "E" in t:
        return 0
    else:
        r, _, _, _ = t["T"]
        return r


# La première primitive est la création d'un tas avec la clé `x`, et deux sous-tas `a` et `b`.
# Le rang est minimisé.

# In[122]:


def make(x: int, a: TasBinaire, b: TasBinaire) -> TasBinaire:
    """ Créer un tas binaire de clé x avec deux sous-tas a et b, minimisant le rang."""
    ra = rank(a)
    rb = rank(b)
    if ra >= rb:
        return T(rb + 1, x, a, b)
    else:
        return T(ra + 1, x, b, a)


# ##### Exemples de tas binaires

# In[113]:


tas1 = make(10, E, E)
pprint(tas1)


# In[114]:


tas2 = make(120, tas1, E)
pprint(tas2)


# In[284]:


tas3 = make(150, tas2, E)
pprint(tas3)


# On peut vérifier si un tas est vide, ou créer le tas vide.

# In[109]:


empty: TasBinaire = E


# In[123]:


def is_empty(a: TasBinaire) -> bool:
    """ Teste si le tas binaire a est vide ou non."""
    if "E" in a:
        return True
    else:
        return False


# In[111]:


# plus rapidement
def is_empty(a: TasBinaire) -> bool:
    return "E" in a


# In[285]:


is_empty(E)


# In[286]:


is_empty(tas1), is_empty(tas2), is_empty(tas3)


# La fusion est assez naturelle : on procède par récurrence, en joignant deux tas et en continuant la fusion pour les tas plus petits.
# On garde la plus petite clé à la racine, pour conserver la propriété *tournoi*.

# In[289]:


def merge(h1: TasBinaire, h2: TasBinaire) -> TasBinaire:
    """ Fusionne les deux tas binaires h1 et h2."""
    if "E" in h1:
        return h2
    elif "E" in h2:
        return h1
    else:
        r1, x, a1, b1 = h1["T"]
        r2, y, a2, b2 = h2["T"]
        if x <= y:
            return make(x, a1, merge(b1, h2))
        else:
            return make(y, a2, merge(h1, b2))


# On peut désormais créer les tas précédemment définis correctement, pour qu'ils soient bien équilibrés :

# In[294]:


tas1 = make(10, E, E)
pprint(tas1)


# In[295]:


tas2 = merge(tas1, make(120, E, E))
pprint(tas2)


# In[297]:


tas3 = merge(make(150, E, E), tas2)
pprint(tas3)


# In[298]:


print("Fusion du tas vide et du tas1 suivant")
pprint(tas1)
pprint(merge(E, tas1))

print("Fusion de tas1 et tas2 suivants")
pprint(tas1)
pprint(tas2)
pprint(merge(tas1, tas2))

print("Fusion de tas2 et tas3 suivants")
pprint(tas2)
pprint(tas3)
pprint(merge(tas2, tas3))


# On voit que les fusions respectent bien la propriété du tas binaire.

# L'insertion correspond à la fusion d'un tas avec une seule clé et du tas courant :

# In[299]:


def insert(x: int, h: TasBinaire) -> TasBinaire:
    """ Solution naive pour insérer une nouvelle valeur x dans le tas binaire h."""
    return merge(T(1, x, E, E), h)
    # return merge(make(x, E, E), h)  # équivalent


# La lecture de la plus petite clé est triviale :

# In[300]:


class Empty(Exception):
    pass


# In[301]:


def mini(a: TasBinaire) -> int:
    """ Calcule le minimum du tas binaire a (première valeur)."""
    if "E" in a:
        raise Empty
    else:
        _, x, _, _ = a["T"]
        return x


# Et l'extraction n'est pas compliquée : il suffit de fusionner les deux sous-tas, ce qui va produire un tas tournoi avec les clés restantes.

# In[302]:


def extract_min(a: TasBinaire) -> Tuple[int, TasBinaire]:
    """ Extraie le minimum et renvoie un tas binaire sans cette valeur."""
    if "E" in a:
        raise Empty
    else:
        _, x, a, b = a["T"]
        return (x, merge(a, b))


# Et maintenant pour le tri par tas :
# 
# 1. On crée un tas vide,
# 2. Dans lequel on insère les valeurs du tableau à trier, une par une,
# 3. Puis on déconstruit le tas en extrayant le minimum, un par un, et en les stockant dans un tableau,
# 4. Le tableau obtenu est trié dans l'ordre croissant.

# In[128]:


def triParTas(a: List[int]) -> List[int]:
    """ Tri par tas"""
    n = len(a)
    tas = E  # tas vide
    for i in range(n):
        tas = insert(a[i], tas)
    a2 = [-1] * n  # aussi [-1 for i in range(n)]
    for i in range(n):
        m, t = extract_min(tas)
        a2[i] = m
        tas = t
    return a2


# Complexité :
# 
# 1. L'étape 1. est en $\mathcal{O}(1)$,
# 2. L'étape 2. est en $\mathcal{O}(\log n)$ pour chacune des $n$ valeurs,
# 3. L'étape 3. est aussi en $\mathcal{O}(\log n)$ pour chacune des $n$ valeurs,
# 
# $\implies$ L'algorithme de tri par tas est en $\mathcal{O}(n \log n)$ en temps et en $\mathcal{O}(n)$ en mémoire externe.

# Un premier exemple :

# In[303]:


triParTas([])


# In[304]:


triParTas([10, 3, 4, 1, 2, 7, 8, 5, 9, 6])


# ##### Quelques essais numériques rapides

# In[134]:


def isSorted(tableau: List) -> bool:
    return tableau == sorted(tableau)


# In[140]:


import numpy as np


# In[141]:


def randomTableau(n: int) -> List[int]:
    return list(np.random.randint(-n*10, n*10, n))


# In[212]:


get_ipython().run_line_magic('time', 'isSorted(triParTas([10, 3, 4, 1, 2, 7, 8, 5, 9, 6]*100))')


# In[213]:


get_ipython().run_line_magic('time', 'isSorted(triParTas(randomTableau(10*100)))')


# In[214]:


get_ipython().run_line_magic('time', 'isSorted(triParTas([10, 3, 4, 1, 2, 7, 8, 5, 9, 6]*1000))')


# In[215]:


get_ipython().run_line_magic('time', 'isSorted(triParTas(randomTableau(10*1000)))')


# In[216]:


get_ipython().run_line_magic('time', 'isSorted(triParTas([10, 3, 4, 1, 2, 7, 8, 5, 9, 6]*10000))')


# In[217]:


get_ipython().run_line_magic('time', 'isSorted(triParTas(randomTableau(10*10000)))')


# In[218]:


get_ipython().run_line_magic('time', 'isSorted(sorted(randomTableau(10*10000)))')


# In[219]:


get_ipython().run_line_magic('time', 'isSorted(triParTas([10, 3, 4, 1, 2, 7, 8, 5, 9, 6]*100000))')


# In[220]:


get_ipython().run_line_magic('time', 'isSorted(triParTas(randomTableau(10*100000)))')


# On observe que la fonction implémentée a une complexité sur-linéaire, et sous-quadratique. En affichant plus de valeurs, on pourrait reconnaître un profil pseudo-linéaire (ie, $\Theta(n \log(n))$).

# In[321]:


import numpy as np
import timeit
valeurs_n = np.logspace(2, 6, num=30, dtype=int)
temps = []
for n in valeurs_n:
    code = "triParTas(randomTableau({}))".format(n)
    essais = 100 if n < 1e4 else 10
    print("- Chronométrons le code", code)
    temps_n = timeit.timeit(
        code,
        number=essais, globals=globals()
    )
    print("qui a pris un temps moyen de", temps_n, "secondes pour", essais, "essais.")
    temps.append(temps_n)


# In[322]:


import matplotlib.pyplot as plt


# In[342]:


plt.figure(figsize=(10, 7))
plt.plot(valeurs_n, temps, "ro-")
plt.xlabel("Taille n du tableau à trier")
plt.ylabel("Temps de calcul en secondes")
plt.title("Pour notre fonction implémentant le tri par tas")
# plt.legend()
plt.show()


# Cette première courbe semble linéaire, ou quasi-linéaire.
# 
# Pour vérifier que le temps de calcul a vraiment un profil ressemblant à une courbe $cst * n * \log(n)$, une méthode rapide et simple est la suivante :
# 
# - on affiche $f(n) / n$ (ici en <span style="color: red;">rouge o-</span>), en espérant que son profil ressemble bien à un $cst * log(n)$,
# - on calcul cst comme la dernière valeur de $f(n) / (n * log(n)$,
# - et on affiche $\log(n)$ (ici en <span style="color: blue;">bleu +:</span>).

# In[341]:


plt.figure(figsize=(10, 7))
plt.plot(valeurs_n[15:], np.array(temps[15:]) / valeurs_n[15:], "ro-", label="Temps de calcul / n")
cst = temps[-1] / valeurs_n[-1]
cst = cst / np.log(valeurs_n[-1])
plt.plot(valeurs_n[15:], np.log(valeurs_n[15:]) * cst, "b+:", label="cst * log(n)")
plt.xlabel("Taille n du tableau à trier")
plt.ylabel("Temps de calcul en secondes\ndivisé par la valeur de n")
plt.title("Pour notre fonction implémentant le tri par tas")
plt.legend()
plt.savefig("TP3__Python__temps_calcul_normalise_triParTas.png")
plt.show()


# Là on constate que la courbe $f(n) / n$ ressemble bien à un logarithme.
# Bien sûr, tout cela est juste expérimental pour de petites valeurs, cela ne suffit PAS DU TOUT à prouver que $f(n) = \Theta(n \log(n))$.

# ![](TP3__Python__temps_calcul_normalise_triParTas.png)

# ----
# ## Exercice 7 : arbre tournoi

# Ici je donne une autre implémentation, généralement celle présentée dans les ouvrages de références en algorithmique.
# Plutôt que d'utiliser une structure arborescente explicite (avec des pointeurs vers des fils gauche et droit et un type récursif), on peut utiliser utiliser un tableau de taille $n$ pour représenter en place les $n$ éléments du tas min.
# 
# Le fils gauche de la racine i (eg si on indice à partir de i=1) sera à l'indice $2*i$ (eg T[2]) et le fils droit de la racine i (eg i=1) sera à l'indice $2*i+1$ (eg T[3]).
# 
# La référence pour cette implémentation vient du Cormen, des éléments sont aussi dans Beauquier & Bernstel, et sur Internet [sur la page Wikipédia](https://fr.wikipedia.org/wiki/Tas_binaire) des tas binaires.
# 
# - Hypothèse : on ne stocke que des entiers positifs, et le tableau, `a` contiendra `-1` pour un élément non utilisé.
# - On doit retenir le nombre `n` d'éléments dans l'arbre, qui peut être modifié.
# 
# On peut donc utiliser une petite classe avec deux champs `n` et `a` :

# In[343]:


Arbre = List[int]

class ArbreTournoi():
    def __init__(self, n: int, a: Arbre):
        self.n = n
        self.a = a


# Par exemple, l'arbre suivant s'écrit comme suit :
# ![arbre_tournoi.svg](arbre_tournoi.svg)

# In[344]:


arbre_test  = ArbreTournoi(7, [1,2,3,4,5,6,7])
arbre_test2 = ArbreTournoi(6, [2,1,3,4,5,6,-1, -1])


# In[345]:


def capacite(an: ArbreTournoi) -> int:
    """ Capacité d'un arbre tournoi, taille du tableau a (nb max de valeurs)."""
    return len(an.a)


# In[346]:


def nb_element(an: ArbreTournoi) -> int:
    """ Nombre d'éléments d'un arbre tournoi."""
    n = an.n
    m = len(an.a)
    assert n <= m
    return n


# In[347]:


print(capacite (arbre_test))
print(nb_element (arbre_test))

print(capacite(arbre_test2))
print(nb_element (arbre_test2))


# In[348]:


def a_racine(an: ArbreTournoi) -> bool:
    return an.n > 0


# In[349]:


def est_racine(n: int) -> bool:
    return n == 0


# In[350]:


def racine(an: ArbreTournoi) -> Tuple[int, int]:
    if 0 >= an.n:
        raise ValueError("Pas de racine")
    return (0, an.a[0])


# In[351]:


racine(arbre_test)


# In[352]:


def a_noeud(an: ArbreTournoi, i: int) -> bool:
    return an.n > i


# In[353]:


def noeud(an: ArbreTournoi, i: int) -> Tuple[int, int]:
    if i >= an.n:
        raise ValueError("Pas de noeud i = {} et an.n = {}".format(i, an.n))
    return (i, an.a[i])


# In[354]:


def valeur(an: ArbreTournoi, i: int) -> int:
    return (noeud(an, i))[1]


# In[355]:


noeud(arbre_test, 0)


# In[356]:


def a_gauche(an: ArbreTournoi, i: int) -> bool:
    return an.n > 2*i + 1


# In[357]:


def gauche(an: ArbreTournoi, i: int) -> Tuple[int, int]:
    if 2*i + 1 >= an.n:
        raise ValueError("Pas de fils gauche i = {}, 2*i+1 = {} and an.n = {}".format(i, (2*i+1), an.n))
    return (2*i + 1, an.a[2*i + 1])


# In[358]:


gauche(arbre_test, 0)


# In[359]:


def a_droite(an: ArbreTournoi, i: int) -> bool:
    return an.n > 2*i + 2


# In[360]:


def droite(an: ArbreTournoi, i: int) -> Tuple[int, int]:
    if 2*i + 2 >= an.n:
        raise ValueError("Pas de fils droit i = {}, 2i+2={} and an.n = {}".format(i, (2*i+2), an.n))
    return (2*i + 2, an.a[2*i + 2])


# Une et deux descentes à droite, par exemple :

# In[361]:


droite(arbre_test, 0)


# In[362]:


i, _ = droite(arbre_test, 0)
droite(arbre_test, i)


# On parcourt les sous-arbres pour trouver le minimum :

# In[363]:


def min_sous_arbre(an: ArbreTournoi, i: int) -> int:
    ag = a_gauche(an, i)
    ad = a_droite(an, i)
    if not ag and not ad:
        return float("+inf")
    elif ag and not ad:
        g, vg = gauche(an, i)
        return min(vg, min_sous_arbre(an, g))
    elif not ag and ad:
        d, vd = droite(an, i)
        return min(vd, min_sous_arbre(an, d))
    else:  # a droite et a gauche
        g, vg = gauche(an, i)
        d, vd = droite(an, i)
        return min(min(vg, vd), min(min_sous_arbre(an, g), min_sous_arbre(an, d)))


# In[364]:


print("arbre_test: n = {}, a = {}".format(arbre_test.n, arbre_test.a))
min_sous_arbre(arbre_test, 0)


# Et enfin la solution pour la fonction testant si un arbre binaire est un tas tournoi, qui doit être récursive et descendre dans les deux sous-arbres gauche et droite tant qu'ils existent :

# In[365]:


def est_tournoi(an: ArbreTournoi) -> bool:
    def depuis(i: int) -> bool:
        r, vr = noeud(an, i)
        min_v = min_sous_arbre(an, i)
        res = vr < min_v
        if res and a_gauche(an, i):
            g, vg = gauche(an, i)
            res = depuis(g)
        if res and a_droite(an, i):
            d, vd = droite(an, i)
            res = depuis(d)
        return res
    return depuis(0)


# In[366]:


est_tournoi(arbre_test)


# In[367]:


print("arbre_test2: n = {}, a = {}".format(arbre_test2.n, arbre_test2.a))
est_tournoi(arbre_test2)


# ## Exercice 8 : `parent`, `fils_gauche` et `fils_droit`

# In[368]:


def parent(an: ArbreTournoi, i: int) -> Tuple[int, int]:
    return noeud(an, ((i - 1) // 2))


# In[369]:


print("arbre_test: n = {}, a = {}".format(arbre_test.n, arbre_test.a))

print(noeud(arbre_test, 1))
print(parent(arbre_test, 1))
print(noeud(arbre_test, 2))
print(parent(arbre_test, 2))


# In[370]:


print(noeud(arbre_test, 4))
print(parent(arbre_test, 4))
print(gauche(arbre_test, 1))
print(droite(arbre_test, 1)) # 4

print(noeud(arbre_test, 5))
print(parent(arbre_test, 5))
print(gauche(arbre_test, 2)) # 5
print(droite(arbre_test, 2))


# ## Exercice 9 : `echange`

# In[371]:


def echange(a: List[Any], i: int, j: int) -> None:
    a[i], a[j] = a[j], a[i]  # very Pythonic
    """
    vi, vj = a[i], a[j]
    a[i] = vj
    a[j] = vi
    """
    """
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp
    """


# ## Exercice 10 : `insertion`

# Si besoin, en insérant un élément dans un tableau déjà plein, on doit doubler sa capacité. Ce n'est pas compliqué : d'abord on double le tableau, puis on fait l'insertion normale.

# In[372]:


def double_capacite(an: ArbreTournoi) -> ArbreTournoi:
    c = capacite(an)
    a2 = [-1] * (2*c)  # [-1 for _ in range(2*c)]
    for i in range(an.n):
        a2[i] = an.a[i]
    return ArbreTournoi(an.n, a2)


# L'opération élémentaire s'appelle une "percolation haute" : pour rétablir si nécessaire la propriété d'ordre du tas binaire : tant que `x` n'est pas la racine de l'arbre et que `x` est strictement inférieur (tas min) à son père on échange les positions entre `x` et son père.

# In[373]:


def percolation_haute(an: ArbreTournoi, i: int) -> None:
    p, _ = parent(an, i)
    while valeur(an, p) > valeur(an, i):
        echange(an.a, i, p)
        i = p
        p, _ = parent(an, i)


# Maintenant, l'insertion a proprement dite :

# In[374]:


def insertion(an: ArbreTournoi, x: int) -> ArbreTournoi:
    n, c = an.n, capacite(an)
    if n == c:
        an2 = double_capacite(an)
        return insertion(an2, x)
    else:
        an2 = ArbreTournoi(n + 1, an.a[:]) # tableau[:] fait une copie
        an2.a[n] = x  # ajoute la valeur x à la fin
        percolation_haute(an2, n) # percolation haute depuis la fin du tas
        return an2


# In[375]:


print("arbre_test: n = {}, a = {}".format(arbre_test.n, arbre_test.a))

a2 = insertion(arbre_test, 40)
print("a2: n = {}, a = {}".format(a2.n, a2.a))
# on l'a vu doubler !
a3 = insertion(a2, 20)
print("a3: n = {}, a = {}".format(a3.n, a3.a))


# In[376]:


a4 = ArbreTournoi(6, [100, 123, 135, 136, 354, 462])
print("a4: n = {}, a = {}".format(a4.n, a4.a))

a5 = insertion(a4, 40)
print("a5: n = {}, a = {}".format(a5.n, a5.a))

a6 = insertion(a5, 20)
print("a6: n = {}, a = {}".format(a6.n, a6.a))


# ## Exercice 11 : `creation`

# La sémantique de cette fonction est de créer un tas min à partir d'un tableau de valeur.

# In[377]:


def creation(a: List[int]) -> ArbreTournoi:
    n = len(a)
    a_vide = [-1] * n
    an = ArbreTournoi(0, a_vide)
    for i in range(n):
        an = insertion(an, a[i])
    return an


# In[378]:


arbre_test3 = creation([20, 1, 3, 5, 7])
print("arbre_test3: n = {}, a = {}".format(arbre_test3.n, arbre_test3.a))


# Notez que cet arbre est bien tournoi, mais n'est pas trié.

# In[379]:


print("Est tournoi ?", est_tournoi(arbre_test3))

print("Est trié ?", arbre_test3.a == sorted(arbre_test3.a))


# ## Exercice 12 : `diminue_clef`

# On peut augmenter ou diminuer la priorité (la clé) d'un nœud mais il faut ensuite satisfaire la contrainte d'ordre. Si l'on augmente la clé on fera donc une percolation-haute à partir de notre nœud et si l'on diminue la clé on fera un percolation-basse.

# > Faites le vous-même.

# ## Exercice 13 : `extraire_min`

# On fait une percolation basse pour déplacer la racine jusqu'à une feuille, puis on inverse la feuille avec la dernière valeur du tableau (la feuille la plus à droite), et on met une valeur arbitraire (`-1`) dedans et on diminue la taille du tas (`{ n with n = n - 1 }`).

# D'abord, on a besoin de récupérer un des deux fils si l'un des deux a une clé plus petite.

# In[380]:


def indice_min_fils(an: ArbreTournoi, i: int) -> int:
    g = i
    d = i
    if a_gauche(an, i):
        g, _ = gauche(an, i)
    if a_droite(an, i):
        d, _ = droite(an, i)
    if valeur(an, g) < valeur(an, d):
        return g
    else:
        return d


# La percolation basse n'est pas trop compliquée :

# In[381]:


def percolation_basse(an: ArbreTournoi, i: int) -> None:
    f = indice_min_fils(an, i)
    while valeur(an, f) < valeur(an, i):
        echange(an.a, i, f)
        i = f
        f = indice_min_fils(an, i)


# Enfin l'extraction du minimum est facile.

# In[386]:


def extraire_min(an: ArbreTournoi) -> Tuple[int, ArbreTournoi]:
    an2 = ArbreTournoi(an.n, an.a[:])  # copie !
    if a_gauche(an2, 0):
        m = an2.a[0]  # racine
        an2.n = an2.n - 1  # on enlève un élément
        echange(an2.a, 0, an2.n)  # on place la racine à la fin, à un endroit désormais inutilisé
        an2.a[an2.n] = -1  # on place -1 la valeur par défaut, donc on efface
        percolation_basse(an2, 0)  # on redescend la nouvelle racine tant que possible
        return m, an2
    else:
        _, racine_an = racine(an2)
        # arbre vide une fois qu'on a extraie la racine
        return (racine_an, ArbreTournoi(0, []))


# Et pour un exemple :

# In[387]:


a = creation([20, 1, 3, 5, 7])
print("a: n = {}, a = {}".format(a.n, a.a))

m, a = extraire_min(a)  # m = 1
print("m = {}, et a: n = {}, a = {}".format(m, a.n, a.a))

m, a = extraire_min(a)  # m = 3
print("m = {}, et a: n = {}, a = {}".format(m, a.n, a.a))

m, a = extraire_min(a)  # m = 5
print("m = {}, et a: n = {}, a = {}".format(m, a.n, a.a))

m, a = extraire_min(a)  # m = 7
print("m = {}, et a: n = {}, a = {}".format(m, a.n, a.a))

m, a = extraire_min(a)  # m = 20
print("m = {}, et a: n = {}, a = {}".format(m, a.n, a.a))


# Remarquez comment le redimensionement du tableau n'arrive qu'à la fin.

# 
# ## Exercice 14 : tri par tas

# La meilleure façon de vérifier notre implémentation est d'implémenter le tri par tas :
# 
# - on construit un tas depuis la liste de valeur,
# - on extrait le minimum successivement.

# In[391]:


def triParTas2(a: List[int]) -> List[int]:
    n = len(a)
    avide = [-1] * n
    an = creation(a)  # tas contenant les valeurs de a, bien placées
    for i in range(n):
        m, an2 = extraire_min(an)
        avide[i] = m  # minimum du tas an, placé en ième position
        an = an2      # nouveau tas avec une valeur en moins
    return avide


# In[395]:


array1 = [10, 3, 4, 1, 2, 7, 8, 5, 9, 6]
array2 = triParTas2(array1)
print("array1 =", array1)
print("trié en array2 =", array2, "par triParsTas2")
assert sorted(array1) == array2


# ----
# # Union-Find

# ## Exercice 15 : Union-Find avec tableaux

# Version simple avec des tableaux simples.

# In[397]:


Representant = Union[None, int]
# Representant = Optional[int]

UnionFind = List[Representant]


# En OCaml, on pourrait écrire ces types :
# ```ocaml
# type representant = Aucun | Element of int;; (* [int option] pourrait suffire *)
# type unionfind = representant array;;
# ```

# In[398]:


def create_uf(n: int) -> UnionFind:
    return [None] * n


# In[399]:


def makeset(uf: UnionFind, i: int) -> None:
    if len(uf) < i:
        uf = uf + [None] * (i - len(uf))
    if uf[i] is None:
        uf[i] = i
    else:
        raise ValueError("makeset avec uf = {} et i = {} : impossible d'ajouter i car déja présent".format(uf, i))


# L'union est assez rapide aussi :

# In[400]:


def union(uf: UnionFind, i: int, j: int) -> None:
    n = len(uf)
    if uf[i] is None or uf[j] is None:
        raise ValueErrorrror("Élement i = {} ou j = {} absent de l'UnionFind uf = {}".format(i, j, uf))
    for k in range(n):
        # tous les éléments dont le représentant est j vont avoir comme représentant i
        if uf[k] == j:
            uf[j] = i


# La recherche est aussi très facile, il suffit de donner la valeur stockée en case i :

# In[401]:


def find(uf: UnionFind, i: int) -> int:
    if uf[i] is None:
        raise ValueError("Élement i = {} absent de l'UnionFind uf = {}".format(i, uf))
    else:
        return uf[i]


# Tests :

# In[405]:


uf_test = create_uf(6)
print("UnionFind uf vide = {}".format(uf_test))

for i in range(0, 5+1):
    makeset(uf_test, i)
print("UnionFind uf rempli par i=0..5 = {}".format(uf_test))

print("find(uf_test, 5) =", find(uf_test, 5))
union(uf_test, 0, 1)
print("Union de 0 et 1 dans uf, désormais uf = {}".format(uf_test))

union(uf_test, 2, 3)
print("Union de 2 et 3 dans uf, désormais uf = {}".format(uf_test))

union(uf_test, 1, 5)
print("Union de 1 et 5 dans uf, désormais uf = {}".format(uf_test))

print("find(uf_test, 0) =", find(uf_test, 0))
print("find(uf_test, 1) =", find(uf_test, 1))

print("find(uf_test, 0) = find(uf_test, 5) ? ", find(uf_test, 0) == find(uf_test, 5))
print("find(uf_test, 3) = find(uf_test, 5) ? ", find(uf_test, 3) == find(uf_test, 5))


# ## Exercice 16 : Union-Find avec forêts

# Version avancée avec des forêts.

# In[460]:


aucun = False
racine = True
Position = Union[bool, int]
# malheureusement, Python va calculer ce type comme étant int,
# et n'affichera pas ça comme Position ou Union[bool, int],
# car bool est un sous type de int

UnionFindForest = List[Position]


# Créer une union-find vide revient à créer un tableau avec chaque élément n'ayant pas de représentant, donc valant `aucun`.

# In[458]:


def create_uf(n: int) -> UnionFindForest:
    return [aucun] * n


# Rajouter un singleton $\{i\}$ dans l'union-find revient à mettre la case `i` du tableau à `racine` :

# In[420]:


def makeset(uf: UnionFindForest, i: int) -> None:
    if uf[i] == aucun:
        uf[i] = racine  # i devient son propre représentant
    else:
        raise ValueError("Élément i = {} déjà présent dans l'UnionFindForest uf = {}".format(i, uf))


# La recherche est un peu plus compliquée et on propose une première optimisation, qui va servir à "aplatir" la forêt.

# In[421]:


def find(uf: UnionFindForest, i: int) -> int:
    uf_i = uf[i]
    if uf[i] == aucun:
        raise ValueError("Élément i = {} absent de l'UnionFindForest uf = {}".format(i, uf))
    elif uf[i] == racine:  # i est son propre représentant
        return i
    else:
        j = uf[i]  # représentant courant de i
        r = find(uf, j)  # trouve le représentant de j
        uf[i] = r  # modifie la forêt pour faire pointer le représentant de i vers r
        return r


# Pour l'union, on fait ici le choix arbitraire de préférer la racine de i, on devrait préférer celle de l'arbre le plus petit pour "écraser" la forêt. Cf. [Papadimitriou] ou [Cormen] (ou Wikipédia).

# In[422]:


def union(uf: UnionFindForest, i: int, j: int) -> None:
    if uf[i] == aucun or uf[j] == aucun:
        raise ValueError("Élément i = {} ou j = {} absent de l'UnionFindForest uf = {}".format(i, j, uf))
    else:
        r_i = find(uf, i)
        uf[r_i] = j
        # c'est un des choix possibles, on peut faire l'inverse
        # r_j = find(uf, j)
        # uf[r_j] = i
        # on peut aussi chercher la racine de l'arbre le plus petit
        #  pour "écraser" (aplatir) la forêt, mais c'est plus compliqué.


# On vérfie avec le même test que pour la première implémentation :

# In[423]:


uf_test = create_uf(6)
print("UnionFindForest uf vide = {}".format(uf_test))

for i in range(0, 5+1):
    makeset(uf_test, i)
print("UnionFindForest uf rempli par i=0..5 = {}".format(uf_test))

print("find(uf_test, 5) =", find(uf_test, 5))
union(uf_test, 0, 1)
print("Union de 0 et 1 dans uf, désormais uf = {}".format(uf_test))

union(uf_test, 2, 3)
print("Union de 2 et 3 dans uf, désormais uf = {}".format(uf_test))

union(uf_test, 1, 5)
print("Union de 1 et 5 dans uf, désormais uf = {}".format(uf_test))

print("find(uf_test, 0) =", find(uf_test, 0))
print("find(uf_test, 1) =", find(uf_test, 1))

print("find(uf_test, 0) = find(uf_test, 5) ? ", find(uf_test, 0) == find(uf_test, 5))
print("find(uf_test, 3) = find(uf_test, 5) ? ", find(uf_test, 3) == find(uf_test, 5))


# ## Exercice 17 : Bonus & discussions

# En classe.
# 
# Je recommande aussi la lecture de [ce document (en anglais)](http://jeffe.cs.illinois.edu/teaching/algorithms/notes/17-unionfind.pdf), si tout ça vous intéresse et si vous envisagez d'en faire un développement. Ce document contient notamment une analyse bien propre de la complexité amortie de l'opération Find pour l'algorithme optimisé, qui donne une complexité en $\mathcal{O}(\alpha(n))$ (pour $n$ valeurs dans la structure Union-Find, et si $\alpha$ est la fonction inverse d'Ackermann, cf. Theorem 4 page 9).

# ## Bonus : algorithme de Kruskal

# ### Représentations de graphe pondérés

# In[444]:


from typing import Optional
Sommet = int
Poids = int
AreteMatrix = Optional[Poids]
GrapheMatrix = List[List[AreteMatrix]]

Destination = Tuple[Sommet, Poids]
GrapheList = List[List[Destination]]  # liste d'adjacence


# In[427]:


def taille_GrapheMatrix(g: GrapheMatrix) -> int:
    n = len(g)
    assert all([ len(g[i]) == n for i in range(n) ])
    return n

def taille_GrapheList(g: GrapheList) -> int:
    n = len(g)
    return n


# Il est facile d'obtenir la liste d'arête, représentées comme un triplet `(i, j, p)` si l'arête $i \arrow j$ de poids $p$ est présente dans le graphe.
# 
# Par exemple avec les graphes représentés par listes d'adjancences :

# In[445]:


Arete = Tuple[Sommet, Sommet, Poids]


# In[446]:


def liste_aretes_GrapheList(g: GrapheList) -> List[Arete]:
    n = taille_GrapheList(g)
    resultat = [
        (i, j, p)
        for i in range(n)
        for (j, p) in g[i]
    ]
    return resultat


# In[447]:


graphe_test: GrapheList = [
    [(1, 11), (2, 2), (3, 1)],
    [(2, 7)],
    [],
    [(4, 5)],
    [(1, 1)]
]

liste_aretes_GrapheList(graphe_test)


# L'algorithme de Kruskal a besoin de trier les arêtes selon leur poids, par ordre croissant, et cela se fait facilement avec le fonction `sorted` de la libraire standard, à laquelle on donne un argument (optionnel) `key` qui est (ici) une fonction extrayant le poids `p` du triplet `(i, j, p)`.

# In[456]:


aretes = liste_aretes_GrapheList(graphe_test)

sorted(aretes,
        key = lambda a: a[2]
    )


# ### Algorithme de Kruskal
# 
# Je ne redonne pas d'explications ici, allez voir [Wikipédia](https://fr.wikipedia.org/wiki/Algorithme_de_Kruskal) ou un livre d'algorithmique de référence ([Cormen] ou [Beauquier, Berstel, Chrétienne] par exemple).
# Voir aussi [cette visualisation](https://www.cs.usfca.edu/~galles/visualization/Kruskal.html), et [cette autre implémentation en Python](https://perso.crans.org/besson/teach/info1_algo1_2019/notebooks/CoursMagistral_6.html#Algorithme-de-Kruskal) (donnée pour le cours d'ALGO1 en L3SIF en 2019).
# 
# > "L'algorithme de Kruskal est un algorithme de recherche d'arbre recouvrant de poids minimum ou arbre couvrant minimum dans un graphe connexe non-orienté et pondéré. Il a été conçu en 1956 par Joseph Kruskal."

# In[487]:


def kruskal(g: GrapheList) -> List[Arete]:
    aretes = liste_aretes_GrapheList(g)
    aretes = sorted(aretes,
        key = lambda a: a[2]
    )
    n = taille_GrapheList(g)
    uf = create_uf(n)
    for i in range(n):
        makeset(uf, i)
    # uf contient chaque sommet dans des singletons
    resultat = []  # liste des arêtes de l'arbre couvrant
    for (i, j, p) in aretes:
        if (find(uf, i) != find(uf, j)):
            resultat.append((i, j, p))
            union(uf, i, j)
    return resultat


# Cet algorithme donne bien un arbre couvrant, il faudrait vérifier sa minimalité.

# In[489]:


graphe_test


# In[488]:


kruskal(graphe_test)


# ----
# # Conclusion
# 
# Fin. À la séance prochaine.
