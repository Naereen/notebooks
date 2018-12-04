
# coding: utf-8

# # Table of Contents
#  <p><div class="lev1 toc-item"><a href="#Générer-des-fausses-citations-latines-du-Roi-Loth,-avec-Python,-Wikiquote-et-des-chaînes-de-Markov" data-toc-modified-id="Générer-des-fausses-citations-latines-du-Roi-Loth,-avec-Python,-Wikiquote-et-des-chaînes-de-Markov-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Générer des fausses citations latines du Roi Loth, avec Python, Wikiquote et des chaînes de Markov</a></div><div class="lev2 toc-item"><a href="#Dépendances" data-toc-modified-id="Dépendances-11"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Dépendances</a></div><div class="lev2 toc-item"><a href="#Récupérer-et-nettoyer-les-données" data-toc-modified-id="Récupérer-et-nettoyer-les-données-12"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Récupérer et nettoyer les données</a></div><div class="lev2 toc-item"><a href="#Exploration-de-chaînes-de-Markov-pour-la-génération-aléatoire" data-toc-modified-id="Exploration-de-chaînes-de-Markov-pour-la-génération-aléatoire-13"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Exploration de chaînes de Markov pour la génération aléatoire</a></div><div class="lev2 toc-item"><a href="#Fausses-locutions-latines" data-toc-modified-id="Fausses-locutions-latines-14"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Fausses locutions latines</a></div><div class="lev2 toc-item"><a href="#Fausses-citations-du-Roi-Loth" data-toc-modified-id="Fausses-citations-du-Roi-Loth-15"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Fausses citations du Roi Loth</a></div><div class="lev3 toc-item"><a href="#Premier-exemple" data-toc-modified-id="Premier-exemple-151"><span class="toc-item-num">1.5.1&nbsp;&nbsp;</span>Premier exemple</a></div><div class="lev3 toc-item"><a href="#Exemples" data-toc-modified-id="Exemples-152"><span class="toc-item-num">1.5.2&nbsp;&nbsp;</span>Exemples</a></div><div class="lev3 toc-item"><a href="#Générer-aléatoirement-les-métadonnées-de-l'épisode" data-toc-modified-id="Générer-aléatoirement-les-métadonnées-de-l'épisode-153"><span class="toc-item-num">1.5.3&nbsp;&nbsp;</span>Générer aléatoirement les métadonnées de l'épisode</a></div><div class="lev3 toc-item"><a href="#Générer-aléatoirement-les-explications-foireuses-du-Roi-Loth" data-toc-modified-id="Générer-aléatoirement-les-explications-foireuses-du-Roi-Loth-154"><span class="toc-item-num">1.5.4&nbsp;&nbsp;</span>Générer aléatoirement les explications foireuses du Roi Loth</a></div><div class="lev3 toc-item"><a href="#Combiner-le-tout-!" data-toc-modified-id="Combiner-le-tout-!-155"><span class="toc-item-num">1.5.5&nbsp;&nbsp;</span>Combiner le tout !</a></div><div class="lev3 toc-item"><a href="#Exemples" data-toc-modified-id="Exemples-156"><span class="toc-item-num">1.5.6&nbsp;&nbsp;</span>Exemples</a></div><div class="lev3 toc-item"><a href="#Joli-affichage" data-toc-modified-id="Joli-affichage-157"><span class="toc-item-num">1.5.7&nbsp;&nbsp;</span>Joli affichage</a></div><div class="lev3 toc-item"><a href="#Conclusion" data-toc-modified-id="Conclusion-158"><span class="toc-item-num">1.5.8&nbsp;&nbsp;</span>Conclusion</a></div>

# # Générer des fausses citations latines du Roi Loth, avec Python, Wikiquote et des chaînes de Markov
# 
# J'aimerai montrer ici comment générer des fausses citations latines, dignes du [Roi Loth](https://fr.wikipedia.org/wiki/Personnages_de_Kaamelott#Loth_d%E2%80%99Orcanie) de [Kaamelott](https://fr.wikiquote.org/wiki/Kaamelott), avec Python, des données extraites de [sa page Wikiquote](https://fr.wikiquote.org/wiki/Kaamelott/Loth) et des [chaînes de Markov](https://github.com/jilljenn/markov.py).
# 
# > Cf. [ce ticket](https://github.com/Naereen/notebooks/issues/13) pour l'idée initiale.
# 
# Exemple  de sortie :

# In[32]:


citation = citation_aleatoire(italic=True)
display(Markdown("> {}".format(citation)))


# ## Dépendances

# In[2]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-v -m -a "Lilian Besson (Naereen)" -p lea -g')


# In[3]:


import os
import random

from string import ascii_lowercase
from collections import Counter, defaultdict


# Le module [lea](https://bitbucket.org/piedenis/lea) sera très pratique pour manipuler les probabilités pour les chaînes de Markov.

# In[4]:


from lea import Lea


# ## Récupérer et nettoyer les données
# 
# J'ai utilisé [cette page Wikipédia](https://en.wikipedia.org/wiki/List_of_Latin_phrases_%28full%29) et deux lignes de Bash :

# In[5]:


get_ipython().run_cell_magic('bash', '', 'wget --no-verbose "https://en.wikipedia.org/wiki/List_of_Latin_phrases_(full)" -O /tmp/latin.html\ngrep -o \'<b>[^<]*</b>\' /tmp/latin.html | sed s_\'</\\?b>\'_\'\'_g | sort | uniq | sort | uniq > /tmp/data_latin.txt')


# In[6]:


get_ipython().system('head data/latin.txt')


# Ensuite il faut un peu de nettoyage pour enlever les lignes qui ont été incorrectement ajoutées dans le fichier (j'ai fait ça à la main).

# In[7]:


get_ipython().system('head data/latin.txt')


# In[8]:


get_ipython().system('ls -larth data/latin.txt')
get_ipython().system('wc data/latin.txt')


# On a 1571 citations latines, c'est déjà un corpus conséquent !

# ## Exploration de chaînes de Markov pour la génération aléatoire
# 
# J'utilise cette fonction [markov](https://github.com/jilljenn/markov.py/blob/master/markov.py#L10) écrite par [Jill-Jênn Vie](https://jilljenn.github.io/).

# In[9]:


def markov(corpus, start, length):
    # Counting occurrences
    next_one = defaultdict(Counter)
    for sentence in corpus:
        words = sentence.split()
        nb_words = len(words)
        for i in range(nb_words - 1):
            next_one[words[i]][words[i + 1]] += 1

    # Initializing states
    states = {}
    for word in next_one:
        states[word] = Lea.fromValFreqsDict(next_one[word])

    # Outputting visited states
    word = start
    words = [word]
    for _ in range(length - 1):
        word = states[word].random()
        words.append(word)
    return(words)


# Par exemple :

# In[10]:


corpus = [
    'je mange des cerises',
    'je mange des bananes',
    'je conduis des camions',
]
start = 'je'
length = 4


# Et on peut générer 3 phrases aléatoires :

# In[11]:


for _ in range(3):
    words = markov(corpus, start, length)
    print(' '.join(words))


# ## Fausses locutions latines
# 
# On va extraire le corpus, la liste des premiers mots, et la probabilité qu'un mot en début de citation commence par une majuscule.

# In[12]:


WORD_LIST = "data/latin.txt"
corpus = open(WORD_LIST).readlines()


# In[13]:


print("Exemple d'une citation :", corpus[0])
print("Il y a", len(corpus), "citations.")


# In[14]:


starts = [c.split()[0] for c in corpus]
start = random.choice(starts)
print("Exemple d'un mot de début de citation :", start)
print("Il y a", len(starts), "mots de débuts de citations.")


# In[15]:


proba_title = len([1 for s in starts if s.istitle()]) / len(starts)
print("Il y a {:.3%} chance de commencer une citation par une majuscule.".format(proba_title))


# Mais en fait, le Roi Loth commence toujours ses citations latines par une majuscule :

# In[16]:


proba_title = 1


# On va générer des locutions de 3 à 6 mots :

# In[17]:


length_min = 3
length_max = 6


# On a bientôt ce qu'il faut pour générer une locution latine aléatoire.
# Il arrive que la chaîne de Markov se bloque, donc on va juste essayer plusieurs fois avec des débuts différents.

# In[18]:


def markov_try_while_failing(corpus, starts, length_min, length_max, proba_title, nb_max_trial=100):
    # Try 100 times to generate a sentence
    start = random.choice(starts)
    length = random.randint(length_min, length_max)
    for trial in range(nb_max_trial):
        try:
            words = markov(corpus, start, length)
            if random.random() <= proba_title:
                words[0] = words[0].title()
            return words  # comment to debug
            print(' '.join(words))
            break
        except KeyError:
            start = random.choice(starts)
            length = random.randint(length_min, length_max)
            continue
    raise ValueError("Echec")


# On peut essayer :

# In[19]:


for _ in range(10):
    words = markov_try_while_failing(corpus, starts, length_min, length_max, proba_title)
    print(' '.join(words))


# Ça a déjà l'air pas mal latin !

# ## Fausses citations du Roi Loth
# 
# Pour générer une citation du Roi Loth, il ne suffit pas d'avoir des locutions latines.
# Il faut le contexte, l'explication, une fausse citation d'un épisode de Kaamelott etc...
# 
# ### Premier exemple
# Ecouter celle là : [Misa brevis, et spiritus maxima](https://kaamelott-soundboard.2ec0b4.fr/#son/tres_en_colere).
# <audio src="data/tres_en_colere.mp3" controls="controls">Your browser does not support the audio element.</audio>
# 
# ### Exemples
# 
# > *Ave Cesar, rosae rosam, et spiritus rex !* Ah non, parce que là, j’en ai marre !
# > -- François Rollin, Kaamelott, Livre III, L’Assemblée des rois 2e partie, écrit par Alexandre Astier.
# 
# > *Tempora mori, tempora mundis recorda*. Voilà. Eh bien ça, par exemple, ça veut absolument rien dire, mais l’effet reste le même, et pourtant j’ai jamais foutu les pieds dans une salle de classe attention !
# > -- François Rollin, Kaamelott, Livre III, L’Assemblée des rois 2e partie, écrit par Alexandre Astier.
# 
# > *Victoriae mundis et mundis lacrima.* Bon, ça ne veut absolument rien dire, mais je trouve que c’est assez dans le ton.
# > -- François Rollin, Kaamelott, Livre IV, Le désordre et la nuit, écrit par Alexandre Astier.
# 
# > *Misa brevis et spiritus maxima*, ça veut rien dire, mais je suis très en colère contre moi-même.
# > -- François Rollin, Kaamelott, Livre V, Misère noire, écrit par Alexandre Astier.
# 
# > *Deus minimi placet* : seul les dieux décident.
# > -- François Rollin, Kaamelott, Livre VI, Arturus Rex, écrit par Alexandre Astier.
# 
# > *"Mundi placet et spiritus minima"*, ça n'a aucun sens mais on pourrait très bien imaginer une traduction du type : *"Le roseau plie, mais ne cède... qu'en cas de pépin"* ce qui ne veut rien dire non plus.
# > -- François Rollin, Kaamelott, Livre VI, Lacrimosa, écrit par Alexandre Astier.

# ### Générer aléatoirement les métadonnées de l'épisode
# C'est facile.

# In[20]:


episodes = [
    "Livre III, L’Assemblée des rois 2e partie, écrit par Alexandre Astier.",
    "Livre III, L’Assemblée des rois 2e partie, écrit par Alexandre Astier.",  # présent deux fois
    "Livre IV, Le désordre et la nuit, écrit par Alexandre Astier.",
    "Livre V, Misère noire, écrit par Alexandre Astier.",
    "Livre VI, Arturus Rex, écrit par Alexandre Astier.",
    "Livre VI, Lacrimosa, écrit par Alexandre Astier."
]


# In[21]:


def metadonnee_aleatoire(episodes=episodes):
    episode = random.choice(episodes)
    return "D'après François Rollin, inspiré par Kaamelott, " + episode


# ### Générer aléatoirement les explications foireuses du Roi Loth
# C'est moins facile... Mais sans chercher à être parfait, on va juste prendre une explication parmi celles qui existent :

# In[22]:


explications = [
    ". Ah non, parce que là, j’en ai marre !",
    ". Voilà. Eh bien ça, par exemple, ça veut absolument rien dire, mais l’effet reste le même, et pourtant j’ai jamais foutu les pieds dans une salle de classe attention !",
    ". Bon, ça ne veut absolument rien dire, mais je trouve que c’est assez dans le ton.",
    ", ça veut rien dire, mais je suis très en colère contre moi-même.",
    " : seul les dieux décident.",
    """, ça n'a aucun sens mais on pourrait très bien imaginer une traduction du type : "Le roseau plie, mais ne cède... qu'en cas de pépin", ce qui ne veut rien dire non plus.""",
]


# Et quelques variations :

# In[23]:


explications += [
    ". Ah non, parce qu'au bout d'un moment, zut !",
    ". Voilà, ça ne veut rien dire, mais c'est assez dans le ton !",
    ". Bon, ça n'a aucun sens, mais j'aime bien ce petit ton décalé.",
    ". Le latin, ça impressionne ! Surtout les grouillots.",
    ", ça n'a aucun sens, mais je suis très en colère contre moi-même.",
    ", ça n'a aucun sens, mais je fais ça par amour.",
    " : la victoire par la sagesse.",
    " : les livres contiennent la sagesse des anciens.",
    " : à Rome seul compte le pouvoir.",
    " : seul les puissants agissent.",
    " : le mariage est une bénédiction.",
    " : ça veut rien dire, mais ça impressionne !",
    """, ça veut rien dire mais on pourrait très bien imaginer une traduction du type : "Le vent tourne pour ceux qui savent écouter", ce qui ne veut rien dire non plus.""",
    """, ça n'a aucun sens mais pourquoi pas une traduction du genre : "Les imbéciles dorment, les forts agissent mais dorment aussi", ce qui n'a aucun sens non plus.""",
]


# In[24]:


def explication_aleatoire():
    return random.choice(explications)


# ### Combiner le tout !
# C'est très facile :

# In[25]:


def citation_aleatoire(italic=False):
    metadonnee = metadonnee_aleatoire()
    explication = explication_aleatoire()
    words = markov_try_while_failing(corpus, starts, length_min, length_max, proba_title)
    locution = ' '.join(words)
    if italic:
        citation = '"*{}*"{} -- {}'.format(locution, explication, metadonnee)
    else:
        citation = '"{}"{} -- {}'.format(locution, explication, metadonnee)
    return citation


# ### Exemples

# In[26]:


for _ in range(10):
    print(">", citation_aleatoire(italic=True))


# ### Joli affichage

# In[27]:


from IPython.display import display, Markdown


# In[28]:


for _ in range(10):
    citation = citation_aleatoire(italic=True)
    display(Markdown("> {}".format(citation)))


# ### Conclusion
# 
# Alors, convaincus ?
# 
# > [Whoooo! Whoo! C'est mortel ! Whoua c'est mortel!](https://kaamelott-soundboard.2ec0b4.fr/#son/wooouuuhouhouhou_c_est_mortel) comme dirait Perceval.
# 
# Allez voir [ici pour d'autres Notebooks](https://github.com/Naereen/notebooks) écrits par Lilian Besson.
