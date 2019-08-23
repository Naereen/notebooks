#!/usr/bin/env python
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#But-de-ce-notebook" data-toc-modified-id="But-de-ce-notebook-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>But de ce notebook</a></div><div class="lev1 toc-item"><a href="#Règles-du-Jap-Jap" data-toc-modified-id="Règles-du-Jap-Jap-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Règles du <em>Jap Jap</em></a></div><div class="lev2 toc-item"><a href="#But-du-jeu" data-toc-modified-id="But-du-jeu-21"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>But du jeu</a></div><div class="lev2 toc-item"><a href="#Début-du-jeu" data-toc-modified-id="Début-du-jeu-22"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Début du jeu</a></div><div class="lev2 toc-item"><a href="#Tour-de-jeu" data-toc-modified-id="Tour-de-jeu-23"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Tour de jeu</a></div><div class="lev2 toc-item"><a href="#Fin-du-jeu" data-toc-modified-id="Fin-du-jeu-24"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>Fin du jeu</a></div><div class="lev1 toc-item"><a href="#Code-du-jeu" data-toc-modified-id="Code-du-jeu-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Code du jeu</a></div><div class="lev2 toc-item"><a href="#Code-pour-représenter-une-carte-à-jouer" data-toc-modified-id="Code-pour-représenter-une-carte-à-jouer-31"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Code pour représenter une carte à jouer</a></div><div class="lev2 toc-item"><a href="#Fin-du-jeu" data-toc-modified-id="Fin-du-jeu-32"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Fin du jeu</a></div><div class="lev2 toc-item"><a href="#Actions" data-toc-modified-id="Actions-33"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>Actions</a></div><div class="lev2 toc-item"><a href="#Valider-un-coup" data-toc-modified-id="Valider-un-coup-34"><span class="toc-item-num">3.4&nbsp;&nbsp;</span>Valider un coup</a></div><div class="lev2 toc-item"><a href="#Jeu-interactif" data-toc-modified-id="Jeu-interactif-35"><span class="toc-item-num">3.5&nbsp;&nbsp;</span>Jeu interactif</a></div><div class="lev2 toc-item"><a href="#Etat-du-jeu" data-toc-modified-id="Etat-du-jeu-36"><span class="toc-item-num">3.6&nbsp;&nbsp;</span>Etat du jeu</a></div><div class="lev2 toc-item"><a href="#Un-exemple-de-début-de-jeu" data-toc-modified-id="Un-exemple-de-début-de-jeu-37"><span class="toc-item-num">3.7&nbsp;&nbsp;</span>Un exemple de début de jeu</a></div><div class="lev2 toc-item"><a href="#Un-exemple-de-tour" data-toc-modified-id="Un-exemple-de-tour-38"><span class="toc-item-num">3.8&nbsp;&nbsp;</span>Un exemple de tour</a></div><div class="lev1 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Conclusion</a></div>

# ----
# # But de ce notebook
# 
# - Je vais expliquer les règles d'un jeu de carte, le "Jap Jap", qu'on m'a appris pendant l'été,
# - Je veux simuler ce jeu, en Python, afin de calculer quelques statistiques sur le jeu,
# - J'aimerai essayer d'écrire une petite intelligence artificielle permettant de jouer contre l'ordinateur,
# - Le but est de faire un prototype d'une application web ou mobile qui permettrait de jouer contre son téléphone !

# ----
# # Règles du *Jap Jap*
# 
# ## But du jeu
# - Le *Jap Jap* se joue à $n \geq 2$ joueur-euse-s (désignées par le mot neutre "personne"), avec un jeu de $52$ cartes classiques (4 couleurs, 1 à 10 + vallet/dame/roi).
# - Chaque partie du *Jap Jap* jeu se joue en plusieurs manches. A la fin de chaque manche, une personne gagne et les autres marquent des points. Le but est d'avoir le moins de point possible, et la première personne a atteindre $90$ points a perdu !
# - On peut rendre le jeu plus long en comptant la première personne à perdre $x \geq 1$ parties.
# 
# ## Début du jeu
# - Chaque personne reçoit 5 cartes,
# - et on révèle la première carte de la pioche.
# 
# ## Tour de jeu
# - Chaque personne joue l'une après l'autre, dans le sens horaire (anti trigonométrique),
# - A son tour, la personne a le choix entre jouer normalement, ou déclencher la fin de jeu si elle possède une main valant $v \leq 5$ points (voir "Fin du jeu" plus bas),
# - Jouer normalement consiste à jeter *une ou plusieurs* ($x \in \{1,\dots,5\}$) cartes de sa main dans la défausse, et prendre *une* carte et la remettre dans sa main. Elle peut choisir la carte du sommet de la pioche (qui est face cachée), ou *une* des $x' \in \{1,\dots,5\}$ cartes ayant été jetées par la personne précédente, ou bien la première carte de la défausse si c'est le début de la partie.
# 
# ## Fin du jeu
# - Dès qu'une personne possède une main valant $v \leq 5$ points, elle peut dire *Jap Jap !* au lieu de jouer à son tour.
#   + Si elle est la seule personne à avoir une telle main de moins de $5$ points, elle gagne !
#   + Si une autre personne a une main de moins de $5$ points, elle peut dire *Contre Jap Jap !*, à condition d'avoir *strictement* moins de points que le *Jap Jap !* ou le *Contre Jap Jap !* précédent. La personne qui remporte la manche est celle qui a eu le *Contre Jap Jap !* de plus petite valeur.
# - La personne qui a gagné ne marque aucun point, et les autres ajoutent à leur total actuel de point 
# - Si quelqu'un atteint $90$ points, elle perd la partie.

# ----
# # Code du jeu

# ## Code pour représenter une carte à jouer

# In[2]:


coeur   = "♥"
treffle = "♣"
pique   = "♠"
carreau = "♦"
couleurs = [coeur, treffle, pique, carreau]


# In[3]:


class Carte():
    def __init__(self, valeur, couleur):
        assert 1 <= valeur <= 13, "Erreur : valeur doit etre entre 1 et 13."
        self.valeur = valeur
        assert couleur in couleurs, "Erreur : couleur doit etre dans la liste {}.".format(couleurs)
        self.couleur = couleur
        
    def __str__(self):
        val = str(self.valeur)
        if self.valeur > 10:
            val = {11: "V" , 12: "Q" , 13: "K"}[self.valeur]
        return "{:>2}{}".format(val, self.couleur)
    
    __repr__ = __str__
    
    def val(self):
        return self.valeur


# In[4]:


def valeur_main(liste_carte):
    return sum(carte.val() for carte in liste_carte)


# In[5]:


import random

def nouveau_jeu():
    jeu = [
        Carte(valeur, couleur)
        for valeur in range(1, 13+1)
        for couleur in couleurs
    ]
    random.shuffle(jeu)
    return jeu


# In[6]:


nouveau_jeu()[:5]
valeur_main(_)


# ## Fin du jeu

# Pour représenter la fin du jeu :

# In[7]:


class FinDuneManche(Exception):
    pass


# In[8]:


class FinDunePartie(Exception):
    pass


# ## Actions
# Pour représenter une action choisie par une personne :

# In[9]:


class action():
    def __init__(self, typeAction="piocher", choix=None):
        assert typeAction in ["piocher", "choisir", "Jap Jap !"]
        self.typeAction = typeAction
        assert choix is None or choix in [0, 1, 2, 3, 4]
        self.choix = choix
    
    def __str__(self):
        if self.est_piocher(): return "Piocher"
        elif self.est_japjap(): return "Jap Jap !"
        elif self.est_choisir(): return "Choisir #{}".format(self.choix)

    def est_piocher(self):
        return self.typeAction == "piocher"

    def est_choisir(self):
        return self.typeAction == "choisir"

    def est_japjap(self):
        return self.typeAction == "Jap Jap !"

action_piocher = action("piocher")
action_japjap = action("Jap Jap !")
action_choisir0 = action("choisir", 0)
action_choisir1 = action("choisir", 1)
action_choisir2 = action("choisir", 2)
action_choisir3 = action("choisir", 3)
action_choisir4 = action("choisir", 4)


# Pour savoir si une suite de valeurs est bien continue :

# In[10]:


def suite_valeurs_est_continue(valeurs):
    differences = [ valeurs[i + 1] - valeurs[i] for i in range(len(valeurs) - 1) ]
    return all([d == 1 for d in differences])


# In[11]:


suite_valeurs_est_continue([5, 6, 7])
suite_valeurs_est_continue([5, 7, 8])


# ## Valider un coup
# Pour valider un coup choisie par une personne :

# In[12]:


def valide_le_coup(jetees):
    assert 1 <= len(jetees) <= 5
    # coup valide si une seule carte !
    if len(jetees) == 1:
        return True
    # si plus d'une carte
    elif len(jetees) >= 2:
        couleurs_jetees = [carte.couleur for carte in jetees]
        valeurs_jetees  = sorted([carte.valeur for carte in jetees])
        # coup valide si une seule couleur et une suite de valeurs croissantes et continues
        if len(set(couleurs_jetees)) == 1:
            return suite_valeurs_est_continue(valeurs_jetees)
        # coup valide si une seule valeur et différentes couleurs
        elif len(set(valeurs_jetees)) == 1:
            return len(set(couleurs_jetees)) == len(couleurs_jetees)
        return False


# Exemples de coups valides :

# In[13]:


valide_le_coup([Carte(4, coeur)])


# In[14]:


valide_le_coup([Carte(4, coeur), Carte(5, coeur)])


# In[15]:


valide_le_coup([Carte(4, coeur), Carte(5, coeur), Carte(3, coeur)])


# In[16]:


valide_le_coup([Carte(4, coeur), Carte(5, coeur), Carte(3, coeur), Carte(2, coeur), Carte(6, coeur)])


# In[17]:


valide_le_coup([Carte(4, coeur), Carte(4, carreau)])


# In[18]:


valide_le_coup([Carte(4, coeur), Carte(4, carreau), Carte(4, pique)])


# In[19]:


valide_le_coup([Carte(4, coeur), Carte(4, carreau), Carte(4, pique), Carte(4, treffle)])


# Exemples de coups pas valides :

# In[20]:


valide_le_coup([Carte(4, coeur), Carte(9, coeur)])


# In[21]:


valide_le_coup([Carte(4, coeur), Carte(4, coeur), Carte(3, coeur)])


# In[22]:


valide_le_coup([Carte(4, coeur), Carte(12, carreau)])


# In[23]:


valide_le_coup([Carte(4, coeur), Carte(4, carreau), Carte(4, pique)])


# In[24]:


valide_le_coup([Carte(4, coeur), Carte(4, carreau), Carte(4, pique), Carte(4, treffle)])


# ## Jeu interactif
# On va utiliser les widgets ipython pour construire le jeu interactif !

# In[25]:


# Voir https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20Asynchronous.html#Waiting-for-user-interaction
get_ipython().run_line_magic('gui', 'asyncio')


# In[26]:


import asyncio

def wait_for_change(widget, value):
    future = asyncio.Future()
    def getvalue(change):
        # make the new value available
        future.set_result(change.new)
        widget.unobserve(getvalue, value)
    widget.observe(getvalue, value)
    return future


# In[27]:


import ipywidgets as widgets
from IPython.display import display

style = {
    'description_width': 'initial',
}
style2boutons = {
    'description_width': 'initial',
    'button_width': '50vw',
}
style3boutons = {
    'description_width': 'initial',
    'button_width': '33vw',
}
style5boutons = {
    'description_width': 'initial',
    'button_width': '20vw',
}


# Pour savoir quoi jouer :

# In[28]:


def piocher_ou_choisir_une_carte_visible():
    return widgets.ToggleButtons(
        options=["Une carte dans la pioche ", "Une carte du sommet de la défausse "],
        index=0,
        tooltips=["invisible", "visibles"],
        icons=["question", "list-ol"],
        description="Action ?",
        style=style3boutons,
    )


# In[29]:


bouton = piocher_ou_choisir_une_carte_visible()
display(bouton)
print("Choix :", bouton.index)


# Pour savoir quoi jeter :

# In[30]:


exemple_de_main = [Carte(10, coeur), Carte(11, coeur), Carte(11, pique)]
exemple_de_main


# In[31]:


def faire_japjap(main):
    return widgets.ToggleButton(
        value=False,
        description="Jap Jap ? ({})".format(valeur_main(main)),
        button_style="success",
        tooltip="Votre main vaut moins de 5 points, donc vous pouvez terminer la partie !",
        icon="check",
        style=style,
    )

faire_japjap(exemple_de_main)


# In[32]:


b = faire_japjap(exemple_de_main)
display(b)
print("Choix :", b.value)


# In[33]:


def quoi_jeter(main):
    return widgets.SelectMultiple(
        options=main,
        index=[0],
        description="Quoi jeter ?",
        style=style,
    )

quoi_jeter(exemple_de_main)


# In[34]:


b = quoi_jeter(exemple_de_main)
display(b)
print("Choix :", b.index)


# In[35]:


from IPython.display import display


# In[36]:


qj = quoi_jeter(exemple_de_main)
display(qj)

def valider_action():
    return widgets.ToggleButton(description="Valider l'action ?")
validation = valider_action()
display(validation)

#pas_clique = True
#def on_validation_clicked(b):
#    pas_clique = False
#    print("Choix :", qj.index)
#validation.on_click(on_validation_clicked)

print("Choix :", qj.index)


# Pour savoir quoi piocher :

# In[37]:


exemple_de_visibles = [Carte(11, pique), Carte(10, treffle)]
exemple_de_visibles


# In[38]:


def quoi_prendre(visibles):
    return widgets.ToggleButtons(
        options=visibles,
        #index=0,
        description="Prendre quelle carte du sommet ?",
        style=style,
    )

quoi_prendre(exemple_de_visibles)


# Maintenant on peut tout combiner.

# In[39]:


async def demander_action(visibles=None, main=None, stockResultat=None):
    print("- Main : {} (valeur = {})".format(main, valeur_main(main)))
    print("- Sommet de la défausse  :", visibles)
    # 1. quoi jouer
    bouton1 = piocher_ou_choisir_une_carte_visible()
    validation = valider_action()
    display(widgets.VBox([bouton1, validation]))
    await wait_for_change(validation, 'value')
    piocher = bouton1.index == 0
    print("  ==> Choix :", bouton1.value)
    # 2.a. si piocher, rien à faire pour savoir quoi piocher
    if piocher:
        print("Okay, vous piochez.")
        typeAction = "piocher"
        choix = None
    # 2.b. si choisir carte
    else:
        typeAction = "choisir"
        print("Okay, vous choisissez dans le sommet de la défausse.")
        bouton2 = quoi_prendre(visibles)
        validation = valider_action()
        display(widgets.VBox([bouton2, validation]))
        await wait_for_change(validation, 'value')
        print("  ==> Choix :", bouton2.index)
        choix = bouton2.index
    # 3.a. si on peut faire jap jap, demander si on le fait ?
    if valeur_main(main) <= 5:
        print("Vous pouvez faire Jap Jap !")
        bouton3 = faire_japjap(main)
        validation = valider_action()
        display(widgets.VBox([bouton3, validation]))
        await wait_for_change(validation, 'value')
        print("  ==> Choix :", bouton3.value)
        if bouton3.value:
            typeAction = "Jap Jap !"
            jetees = None
    # 3. choisir quoi jeter
    if typeAction != "Jap Jap !":
        bouton4 = quoi_jeter(main)
        validation = valider_action()
        display(widgets.VBox([bouton4, validation]))
        await wait_for_change(validation, 'value')
        print("  ==> Choix :", bouton4.index)
        jetees = bouton4.index
    choix = action(typeAction=typeAction, choix=choix)
    if stockResultat is not None:
        stockResultat["choix"] = choix
        stockResultat["jetees"] = jetees
    return choix, jetees


# In[40]:


if False:
    stockResultat = {"choix": None, "jetees": None}

    asyncio.ensure_future(
        demander_action(
            visibles=exemple_de_visibles,
            main=exemple_de_main,
            stockResultat=stockResultat,
        )
    )

    stockResultat


# In[41]:


def demander_action_et_donne_resultat(visibles=None, main=None):
    stockResultat = {"choix": None, "jetees": None}

    asyncio.ensure_future(
        demander_action(
            visibles=visibles,
            main=main,
            stockResultat=stockResultat,
        )
    )

    return stockResultat["choix"], stockResultat["jetees"]


# ## Etat du jeu
# Maintenant on peut représenter un état du jeu.

# In[42]:


class EtatJeu():
    def __init__(self, nbPersonnes=2, nomsPersonnes=None,
                 scoreMax=90, malusContreJapJap=25, nbCartesMax=5):
        assert 2 <= nbPersonnes <= 5, "Le nombre de personnes pouvant jouer doit etre entre 2 et 5."
        self.nbPersonnes = nbPersonnes
        self.nomsPersonnes = nomsPersonnes
        self.scoreMax = scoreMax
        self.malusContreJapJap = malusContreJapJap
        self.nbCartesMax = nbCartesMax
        # on initialise le stockage interne
        self.personnes = [personne for personne in range(nbPersonnes)]
        self.scores = [
            0 for personne in self.personnes
        ]
        self.mains = [
            [ ] for personne in self.personnes
        ]
        self.visibles = []
        self.jeu = nouveau_jeu()
    
    def montrer_information_visibles(self):
        print("- Nombre de carte dans la pioche :", len(self.jeu))
        print("- Cartes visibles au sommet de la défausse :", len(self.visibles))
        for personne in self.personnes:
            nom = self.nomsPersonnes[personne] if self.nomsPersonnes is not None else personne
            main = self.mains[personne]
            score = self.scores[personne]
            print("    + Personne {} a {} carte{} en main, et un score de {}.".format(
                nom, len(main), "s" if len(main) > 1 else "", score)
            )

    def montrer_information_privee(self, personne=0):
        main = self.mains[personne]
        nom = self.nomsPersonnes[personne] if self.nomsPersonnes is not None else personne
        print("[{}] Carte{} en main : {}".format(nom, "s" if len(main) > 1 else "", main))
    
    # --- Mécanique de pioche et distribution initiale
    
    def prendre_une_carte_pioche(self):
        if len(self.jeu) <= 0:
            raise FinDuneManche
        premiere_carte = self.jeu.pop(0)
        return premiere_carte
    
    def debut_jeu(self):
        self.distribuer_mains()
        premiere_carte = self.prendre_une_carte_pioche()
        self.visibles = [premiere_carte]
    
    def donner_une_carte(self, personne=0):
        premiere_carte = self.prendre_une_carte_pioche()
        self.mains[personne].append(premiere_carte)
        
    def distribuer_mains(self):
        self.mains = [
            [ ] for personne in self.personnes
        ]
        premiere_personne = random.choice(self.personnes)
        self.personnes = self.personnes[premiere_personne:] + self.personnes[:premiere_personne]
        for nb_carte in range(self.nbCartesMax):
            for personne in self.personnes:
                self.donner_une_carte(personne)
    
    # --- Fin d'une manche
    
    def fin_dune_manche(self):
        self.jeu = nouveau_jeu()
        self.debut_jeu()
    
    # --- Enchainer les tours de jeux
    
    async def enchainer_les_tours(self):
        try:
            indice_actuel = 0
            while len(self.jeu) > 0:
                # dans la même manche, on joue chaque tour, pour la personne actuelle
                personne_actuelle = self.personnes[indice_actuel]
                
                # 1. on affiche ce qui est public, et privé
                self.montrer_information_visibles()
                self.montrer_information_privee(personne_actuelle)
                
                # 2. on demande l'action choisie par la personne
                # choix, jetees = demander_action_et_donne_resultat(
                choix, jetees = await demander_action(
                    visibles = self.visibles,
                    main = self.mains[personne_actuelle],
                )

                # 3. on joue l'action
                self.jouer(
                    personne = personne_actuelle,
                    action = choix,
                    indices = jetees,
                )
                
                # personne suivante
                indice_actuel = (indice_actuel + 1) % self.nbPersonnes
            if len(self.jeu) <= 0:
                print("\nIl n'y a plus de cartes dans la pioche, fin de la manche sans personne qui gagne.")
                raise FinDuneManche
        except FinDuneManche:
            print("\nFin d'une manche.")
            fin_dune_manche()
        except FinDunePartie:
            print("\n\nFin d'une partie.")
    
    # --- Un tour de jeu
    
    def jouer(self, personne=0, action=action_piocher, indices=None):
        if indices is not None:
            jetees = [ self.mains[personne][indice] for indice in indices ]
        else:
            jetees = self.visibles
        assert valide_le_coup(jetees)
        # et on en prend une nouvelle
        if action.est_piocher():
            # soit celle face cachée en sommet de pioche
            premiere_carte = self.prendre_une_carte_pioche()
        elif action.est_choisir():
            # soit une des cartes précedemmen visibles
            choix = action.choix
            carte_choisie = self.visibles.pop(choix)
            self.mains[personne].append(carte_choisie)
        elif action.est_japjap():
            # on vérifie que cette personne a bien jeté toute sa main
            assert jetees == self.mains[personne]
            # et qu'elle a bien un Jap Jap !
            valeur_du_premier_japjap = valeur_main(jetees)
            assert 1 <= valeur_du_premier_japjap <= 5
            gagnante = personne
            contre_JapJap = False

            # on vérifie les valeurs des mains des autres personnes
            valeurs_mains = [valeur_main(main) for main in self.mains]
            plus_petite_valeur = min([valeurs_mains[autre_personne] for autre_personne in [ p for p in personnes if p != gagnante ]])
            if plus_petite_valeur < valeur_du_premier_japjap:
                # si une personne a un jap jap plus petit, la personne ne gagne pas
                contre_JapJap = True
                # la personne gagnante est la première (ordre du jeu) à obtenir le jap jap
                # de valeur minimale, et en cas d'égalité c'est la personne obtenant
                # cette valeur en le nombre minimal de cartes !
                gagnantes = [ p for p in personnes if valeurs_mains[p] == plus_petite_valeur ]
                nombre_min_carte = min([len(self.mains[p]) for p in gagnantes])
                gagnante = min([p for p in gagnantes if len(self.mains[p]) == nombre_min_carte])

            # on marque les scores
            for autre_personne in [ p for p in personnes if p != gagnante ]:
                self.scores[autre_personne] += valeur_main(self.mains[autre_personne])
            # si la personne s'est prise un contre jap jap, elle marque +25 et pas son total de cartes en main
            if contre_JapJap:
                self.scores[personne] -= valeur_main(self.mains[personne])
                self.scores[personne] += self.malusContreJapJap
                
            # si un score est >= 90
            if max(self.scores) >= self.scoreMax:
                # quelqu'un a perdu cette partie !
                for personne in personnes:
                    score = self.scores[personne]
                    if score == max(self.scores):
                        nom = self.nomsPersonnes[personne] if self.nomsPersonnes is not None else personne
                        print("\n==> La personne {} a perdu, avec un score de {}.".format(nom, score))
                raise FinDunePartie
            raise FinDuneManche
        # on pose ses cartes jetées
        self.visibles = jetees
        # et ça continue


# ## Un exemple de début de jeu

# In[42]:


jeu = EtatJeu()


# In[43]:


jeu.jeu[:5]


# In[44]:


jeu.mains


# In[45]:


jeu.donner_une_carte(0)


# In[46]:


jeu.mains


# In[47]:


jeu.donner_une_carte(1)


# In[48]:


jeu.mains


# In[49]:


jeu.donner_une_carte(0)


# In[50]:


jeu.mains


# In[51]:


jeu.donner_une_carte(1)


# In[52]:


jeu.mains


# In[53]:


jeu.jeu[:5]


# ## Un exemple de tour

# In[43]:


jeu = EtatJeu(nomsPersonnes=["Alice", "Bob"])


# In[44]:


jeu.debut_jeu()


# In[45]:


import asyncio


# In[46]:


asyncio.ensure_future(jeu.enchainer_les_tours())


# # Conclusion

# In[ ]:




