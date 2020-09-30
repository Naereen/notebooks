#!/usr/bin/env python
# coding: utf-8

# # Brain storming - app for automatic inclusive writing

# In[1]:


from pprint import pprint
from tqdm.notebook import tqdm


# ## Premières expériences
# 
# On va récupérer une liste de mots depuis le dictionnaire `/usr/share/dict/french` :

# In[2]:


mots = []
with open("/usr/share/dict/french", "r") as f:
    mots = [ mot.replace("\n", "") for mot in f.readlines() ]
print(f"Il y a {len(mots)} mots différents dans ce dictionnaire.")


# On peut regarder les premiers mots :

# In[3]:


pprint(mots[:15])


# On voit qu'il n'y a pas les majuscules en début de mot, mais qu'il y a les conjugaisons.

# On aura souvent besoin de tester si un mot est présent, et c'est environ 50 fois plus rapide de tester l'appartenance à un `set` qu'à une `list` en Python :

# In[4]:


set_mots = frozenset(mots)  # pour des tests 'mot in mots' plus rapides


# In[5]:


get_ipython().run_line_magic('timeit', '"vociférée" in mots')
get_ipython().run_line_magic('timeit', '"vociférée" in set_mots')


# On définit une constante représentant le séparateur `·`:

# In[6]:


SEP = "-"
SEP = "."
SEP = "·"


# On va maintenir un dictionnaire qui stockera les alternatives que l'on peut proposer pour chaque mot :

# In[7]:


import collections
alternatives = collections.defaultdict(lambda: set())


# In[14]:


def del_alternatives(mots):
    """ Supprime des mots du dictionnaire alternatives, sans exception si le mot n'est pas encore présent."""
    for mot in mots:
        if mot in alternatives:
            del alternatives[mot]


# On va aussi garder une liste des mots inclusifs singuliers et pluriels créés au fur et à mesure.
# Cela permet d'afficher, à chaque traitement automatique, combien de nouveaux mots ont été créés.

# In[9]:


mots_inclusifs_singuliers = []
mots_inclusifs_pluriels = []


# ### Ajouter mot·e si `mot` et `mot`-e sont présents

# In[10]:


nouveaux_mots_inclusifs_singuliers = []
nouveaux_mots_inclusifs_pluriels = []

for mot in tqdm(mots):
    mot_feminin = f"{mot}e"
    if mot_feminin in set_mots:
        mot_inclusif = f"{mot}{SEP}e"
        print(f"{mot:<20} / {mot_feminin:<20} -> {mot_inclusif:<20}")
        nouveaux_mots_inclusifs_singuliers.append(mot_inclusif)
        alternatives[mot] |= {mot_inclusif}
        alternatives[mot_feminin] |= {mot_inclusif}

# on garde les mots nouveaux
print(f"Cela a donné {len(set(nouveaux_mots_inclusifs_singuliers) - set(mots_inclusifs_singuliers))} nouveaux mots singuliers.")
mots_inclusifs_singuliers = list(set(mots_inclusifs_singuliers + nouveaux_mots_inclusifs_singuliers))


# On voit qu'il y a des erreurs, par exemples :
# 
# - abord                / aborde               -> abord·e  
#   abord est un mot masculin, aborde la conjugaison de aborder et pas la version féminine de abord, abord-e n'a aucun sens
# - ai                   / aie                  -> ai·e  
#   ai est une conjugaison au présent simple, aie à l'impératif, et ai-e n'a aucun sens
# - devis                / devise               -> devis·e  
#   une devise n'est pas le féminin d'un devis
# - dos                  / dose                 -> dos·e
# - dot                  / dote                 -> dot·e
# - pal                  / pale                 -> pal·e
# - et plein d'autres (corrigés manuellement plus bas).

# Maintenant pour les mots pluriels :

# In[11]:


nouveaux_mots_inclusifs_pluriels = []

for mot in tqdm(mots):
    if mot.endswith("s") and mot[:-1] in set_mots:
        mot_feminin = f"{mot[:-1]}es"
        if mot_feminin in set_mots:
            mot_inclusif = f"{mot[:-1]}{SEP}e{SEP}s"
            print(f"{mot:<20} / {mot_feminin:<20} -> {mot_inclusif:<20}")
            nouveaux_mots_inclusifs_pluriels.append(mot_inclusif)
            alternatives[mot] |= {mot_inclusif}
            alternatives[mot_feminin] |= {mot_inclusif}

# on garde les mots nouveaux
print(f"Cela a donné {len(set(nouveaux_mots_inclusifs_pluriels) - set(mots_inclusifs_pluriels))} nouveaux mots pluriels.")
mots_inclusifs_pluriels = list(set(mots_inclusifs_pluriels + nouveaux_mots_inclusifs_pluriels))


# Encore des faux positifs :
# 
# - bais                 / baies                -> bais·e·s       
#   baies n'est pas la version féminine de bais...
# - vol                  / vols                 / voles                -> vol·e·s  
#   voles n'est pas la version féminine de vols mais une conjugaison...
# - et plein d'autres
#   
# Ces erreurs pourraient être corrigées si on avait une base de données disant si un mot est une conjugaison, un adjectif, un nom (ou plusieurs genres)...

# On enlève tous les mots qui n'ont pas de raison d'avoir des alternatives inclusives :
# (trier à la main les ~5500 mots m'a pris environ une heure)

# In[13]:


del_alternatives([
    "abord", "aborde", "abords", "abordes",
    "abus", "abuse", "abuss", "abuses",
    "accord", "accorde", "accords", "accordes",
    "agit", "agite", "agits", "agites",
    "agrément", "agrémente", "agréments", "agrémentes",
    "ai", "aie", "ais", "aies",
    "ail", "aile", "ails", "ailes",
    "air", "aire", "airs", "aires",
    "ajout", "ajoute", "ajouts", "ajoutes",
    "aliment", "alimente", "aliments", "alimentes",
    "allait", "allaite", "allaits", "allaites",
    "ans", "anse", "anss", "anses",
    "appoint", "appointe", "appoints", "appointes",
    "apport", "apporte", "apports", "apportes",
    "appui", "appuie", "appuis", "appuies",
    "arpent", "arpente", "arpents", "arpentes",
    "arrêt", "arrête", "arrêts", "arrêtes",
    "aval", "avale", "avals", "avales",
    "avis", "avise", "aviss", "avises",
    "bai", "baie", "bais", "baies",
    "bas", "base", "bass", "bases",
    "biais", "biaise", "biaiss", "biaises",
    "bis", "bise", "biss", "bises",
    "boit", "boite", "boits", "boites",
    "bond", "bonde", "bonds", "bondes",
    "bord", "borde", "bords", "bordes",
    "bous", "bouse", "bouss", "bouses",
    "box", "boxe", "boxs", "boxes",
    "boycott", "boycotte", "boycotts", "boycottes",
    "bris", "brise", "briss", "brises",
    "bruir", "bruire", "bruirs", "bruires",
    "bu", "bue", "bus", "bues",
    "bus", "buse", "buss", "buses",
    "but", "bute", "buts", "butes",
    "caban", "cabane", "cabans", "cabanes",
    "cahot", "cahote", "cahots", "cahotes",
    "cal", "cale", "cals", "cales",
    "calcul", "calcule", "calculs", "calcules",
    "camp", "campe", "camps", "campes",
    "cap", "cape", "caps", "capes",
    "capot", "capote", "capots", "capotes",
    "cas", "case", "cass", "cases",
    "chair", "chaire", "chairs", "chaires",
    "chais", "chaise", "chaiss", "chaises",
    "chemin", "chemine", "chemins", "chemines",
    "chut", "chute", "chuts", "chutes",
    "ciment", "cimente", "ciments", "cimentes",
    "clam", "clame", "clams", "clames",
    "clos", "close", "closs", "closes",
    "clou", "cloue", "clous", "cloues",
    "comment", "commente", "comments", "commentes",
    "complot", "complote", "complots", "complotes",
    "compost", "composte", "composts", "compostes",
    "concert", "concerte", "concerts", "concertes",
    "conduis", "conduise", "conduiss", "conduises",
    "contact", "contacte", "contacts", "contactes",
    "contredis", "contredise", "contrediss", "contredises",
    "cors", "corse", "corss", "corses",
    "coud", "coude", "couds", "coudes",
    "coudrai", "coudraie", "coudrais", "coudraies",
    "coup", "coupe", "coups", "coupes",
    "cour", "coure", "cours", "coures",
    "cours", "course", "courss", "courses",
    "court-circuit", "court-circuite", "court-circuits", "court-circuites",
    "cous", "couse", "couss", "couses",
    "coût", "coûte", "coûts", "coûtes",
    "crédit", "crédite", "crédits", "crédites",
    "crépit", "crépite", "crépits", "crépites",
    "cri", "crie", "cris", "cries",
    "cris", "crise", "criss", "crises",
    "crois", "croise", "croiss", "croises",
    "cross", "crosse", "crosss", "crosses",
    "cuir", "cuire", "cuirs", "cuires",
    "cuis", "cuise", "cuiss", "cuises",
    "cumul", "cumule", "cumuls", "cumules",
    "dans", "danse", "danss", "danses",
    "débit", "débite", "débits", "débites",
    "débours", "débourse", "débourss", "débourses",
    "début", "débute", "débuts", "débutes",
    "déclin", "décline", "déclins", "déclines",
    "dédis", "dédise", "dédiss", "dédises",
    "déduis", "déduise", "déduiss", "déduises",
    "défend", "défende", "défends", "défendes",
    "défi", "défie", "défis", "défies",
    "dégoût", "dégoûte", "dégoûts", "dégoûtes",
    "délai", "délaie", "délais", "délaies",
    "démord", "démorde", "démords", "démordes",
    "déni", "dénie", "dénis", "dénies",
    "dépend", "dépende", "dépends", "dépendes",
    "dépens", "dépense", "dépenss", "dépenses",
    "dépit", "dépite", "dépits", "dépites",
    "déplais", "déplaise", "déplaiss", "déplaises",
    "descend", "descende", "descends", "descendes",
    "désir", "désire", "désirs", "désires",
    "dessert", "desserte", "desserts", "dessertes",
    "dessin", "dessine", "dessins", "dessines",
    "destin", "destine", "destins", "destines",
    "détend", "détende", "détends", "détendes",
    "détruis", "détruise", "détruiss", "détruises",
    "dévêt", "dévête", "dévêts", "dévêtes",
    "devis", "devise", "deviss", "devises",
    "digest", "digeste", "digests", "digestes",
    "dis", "dise", "diss", "dises",
    "disert", "diserte", "diserts", "disertes",
    "dispos", "dispose", "disposs", "disposes",
    "distend", "distende", "distends", "distendes",
    "divers", "diverse", "diverss", "diverses",
    "dos", "dose", "doss", "doses",
    "dot", "dote", "dots", "dotes",
    "drain", "draine", "drains", "draines",
    "drap", "drape", "draps", "drapes",
    "droit", "droite", "droits", "droites",
    "écart", "écarte", "écarts", "écartes",
    "échafaud", "échafaude", "échafauds", "échafaudes",
    "éclair", "éclaire", "éclairs", "éclaires",
    "éclat", "éclate", "éclats", "éclates",
    "éconduis", "éconduise", "éconduiss", "éconduises",
    "édit", "édite", "édits", "édites",
    "élis", "élise", "éliss", "élises",
    "élit", "élite", "élits", "élites",
    "émeut", "émeute", "émeuts", "émeutes",
    "encart", "encarte", "encarts", "encartes",
    "encens", "encense", "encenss", "encenses",
    "enduis", "enduise", "enduiss", "enduises",
    "ensuit", "ensuite", "ensuits", "ensuites",
    "entend", "entende", "entends", "entendes",
    "envoi", "envoie", "envois", "envoies",
    "envol", "envole", "envols", "envoles",
    "épi", "épie", "épis", "épies",
    "essai", "essaie", "essais", "essaies",
    "essaim", "essaime", "essaims", "essaimes",
    "essor", "essore", "essors", "essores",
    "étai", "étaie", "étais", "étaies",
    "étal", "étale", "étals", "étales",
    "étend", "étende", "étends", "étendes",
    "exil", "exile", "exils", "exiles",
    "exploit", "exploite", "exploits", "exploites",
    "faillit", "faillite", "faillits", "faillites",
    "fan", "fane", "fans", "fanes",
    "fard", "farde", "fards", "fardes",
    "faufil", "faufile", "faufils", "faufiles",
    "faut", "faute", "fauts", "fautes",
    "favoris", "favorise", "favoriss", "favorises",
    "fend", "fende", "fends", "fendes",
    "ferment", "fermente", "ferments", "fermentes",
    "fient", "fiente", "fients", "fientes",
    "fil", "file", "fils", "files",
    "film", "filme", "films", "filmes",
    "flair", "flaire", "flairs", "flaires",
    "fleur", "fleure", "fleurs", "fleures",
    "foi", "foie", "fois", "foies",
    "fond", "fonde", "fonds", "fondes",
    "font", "fonte", "fonts", "fontes",
    "for", "fore", "fors", "fores",
    "fragment", "fragmente", "fragments", "fragmentes",
    "frais", "fraise", "fraiss", "fraises",
    "frein", "freine", "freins", "freines",
    "fris", "frise", "friss", "frises",
    "fui", "fuie", "fuis", "fuies",
    "fuit", "fuite", "fuits", "fuites",
    "gag", "gage", "gags", "gages",
    "gain", "gaine", "gains", "gaines",
    "galop", "galope", "galops", "galopes",
    "gaz", "gaze", "gazs", "gazes",
    "gît", "gîte", "gîts", "gîtes",
    "gland", "glande", "glands", "glandes",
    "golf", "golfe", "golfs", "golfes",
    "gourd", "gourde", "gourds", "gourdes",
    "goût", "goûte", "goûts", "goûtes",
    "grain", "graine", "grains", "graines",
    "granit", "granite", "granits", "granites",
    "gravit", "gravite", "gravits", "gravites",
    "grill", "grille", "grills", "grilles",
    "guérit", "guérite", "guérits", "guérites",
    "guis", "guise", "guiss", "guises",
    "habit", "habite", "habits", "habites",
    "hall", "halle", "halls", "halles",
    "handicap", "handicape", "handicaps", "handicapes",
    "hasard", "hasarde", "hasards", "hasardes",
    "heur", "heure", "heurs", "heures",
    "heurt", "heurte", "heurts", "heurtes",
    "incident", "incidente", "incidents", "incidentes",
    "index", "indexe", "indexs", "indexes",
    "indivis", "indivise", "indiviss", "indivises",
    "induis", "induise", "induiss", "induises",
    "instruis", "instruise", "instruiss", "instruises",
    "interdis", "interdise", "interdiss", "interdises",
    "interview", "interviewe", "interviews", "interviewes",
    "introduis", "introduise", "introduiss", "introduises",
    "jailli", "jaillie", "jaillis", "jaillies",
    "jardin", "jardine", "jardins", "jardines",
    "jas", "jase", "jass", "jases",
    "jerrican", "jerricane", "jerricans", "jerricanes",
    "jeun", "jeune", "jeuns", "jeunes",
    "labour", "laboure", "labours", "laboures",
    "lac", "lace", "lacs", "laces",
    "lambin", "lambine", "lambins", "lambines",
    "land", "lande", "lands", "landes",
    "leitmotiv", "leitmotive", "leitmotivs", "leitmotives",
    "lès", "lèse", "lèss", "lèses",
    "lest", "leste", "lests", "lestes",
    "lieu", "lieue", "lieus", "lieues",
    "lis", "lise", "liss", "lises",
    "lob", "lobe", "lobs", "lobes",
    "long", "longe", "longs", "longes",
    "lot", "lote", "lots", "lotes",
    "loup", "loupe", "loups", "loupes",
    "lux", "luxe", "luxs", "luxes",
    "lys", "lyse", "lyss", "lyses",
    "machin", "machine", "machins", "machines",
    "major", "majore", "majors", "majores",
    "mandat", "mandate", "mandats", "mandates",
    "mari", "marie", "maris", "maries",
    "mat", "mate", "mats", "mates",
    "médiat", "médiate", "médiats", "médiates",
    "médis", "médise", "médiss", "médises",
    "ment", "mente", "ments", "mentes",
    "mess", "messe", "messs", "messes",
    "meut", "meute", "meuts", "meutes",
    "mi", "mie", "mis", "mies",
    "microfilm", "microfilme", "microfilms", "microfilmes",
    "mil", "mile", "mils", "miles",
    "min", "mine", "mins", "mines",
    "mit", "mite", "mits", "mites",
    "mont", "monte", "monts", "montes",
    "mord", "morde", "mords", "mordes",
    "mors", "morse", "morss", "morses",
    "mur", "mure", "murs", "mures",
    "ni", "nie", "nis", "nies",
    "nuis", "nuise", "nuiss", "nuises",
    "octroi", "octroie", "octrois", "octroies",
    "os", "ose", "oss", "oses",
    "oubli", "oublie", "oublis", "oublies",
    "pal", "pale", "pals", "pales",
    "pans", "panse", "panss", "panses",
    "par", "pare", "pars", "pares",
    "parc", "parce", "parcs", "parces",
    "parfum", "parfume", "parfums", "parfumes",
    "pari", "parie", "paris", "paries",
    "parlement", "parlemente", "parlements", "parlementes",
    "part", "parte", "parts", "partes",
    "patin", "patine", "patins", "patines",
    "pavois", "pavoise", "pavoiss", "pavoises",
    "pays", "payse", "payss", "payses",
    "pend", "pende", "pends", "pendes",
    "perd", "perde", "perds", "perdes",
    "pers", "perse", "perss", "perses",
    "pivot", "pivote", "pivots", "pivotes",
    "plaid", "plaide", "plaids", "plaides",
    "plais", "plaise", "plaiss", "plaises",
    "pleur", "pleure", "pleurs", "pleures",
    "pli", "plie", "plis", "plies",
    "plomb", "plombe", "plombs", "plombes",
    "pogrom", "pogrome", "pogroms", "pogromes",
    "poignard", "poignarde", "poignards", "poignardes",
    "point", "pointe", "points", "pointes",
    "pond", "ponde", "ponds", "pondes",
    "pont", "ponte", "ponts", "pontes",
    "port", "porte", "ports", "portes",
    "pot", "pote", "pots", "potes",
    "prétend", "prétende", "prétends", "prétendes",
    "produis", "produise", "produiss", "produises",
    "profil", "profile", "profils", "profiles",
    "profit", "profite", "profits", "profites",
    "propos", "propose", "proposs", "proposes",
    "pu", "pue", "pus", "pues",
    "puis", "puise", "puiss", "puises",
    "puisqu", "puisque", "puisqus", "puisques",
    "qu", "que", "qus", "ques",
    "rabot", "rabote", "rabots", "rabotes",
    "raccord", "raccorde", "raccords", "raccordes",
    "raid", "raide", "raids", "raides",
    "rajout", "rajoute", "rajouts", "rajoutes",
    "rang", "range", "rangs", "ranges",
    "rapport", "rapporte", "rapports", "rapportes",
    "ravis", "ravise", "raviss", "ravises",
    "rebut", "rebute", "rebuts", "rebutes",
    "récit", "récite", "récits", "récites",
    "reconduis", "reconduise", "reconduiss", "reconduises",
    "reconstruis", "reconstruise", "reconstruiss", "reconstruises",
    "recru", "recrue", "recrus", "recrues",
    "recul", "recule", "reculs", "recules",
    "redis", "redise", "rediss", "redises",
    "réduis", "réduise", "réduiss", "réduises",
    "réélis", "réélise", "rééliss", "réélises",
    "refond", "refonde", "refonds", "refondes",
    "refont", "refonte", "refonts", "refontes",
    "refus", "refuse", "refuss", "refuses",
    "régal", "régale", "régals", "régales",
    "regard", "regarde", "regards", "regardes",
    "rein", "reine", "reins", "reines",
    "réintroduis", "réintroduise", "réintroduiss", "réintroduises",
    "rejailli", "rejaillie", "rejaillis", "rejaillies",
    "relis", "relise", "reliss", "relises",
    "remblai", "remblaie", "remblais", "remblaies",
    "remploi", "remploie", "remplois", "remploies",
    "rend", "rende", "rends", "rendes",
    "renvoi", "renvoie", "renvois", "renvoies",
    "répand", "répande", "répands", "répandes",
    "repart", "reparte", "reparts", "repartes",
    "repens", "repense", "repenss", "repenses",
    "reperd", "reperde", "reperds", "reperdes",
    "répond", "réponde", "réponds", "répondes",
    "report", "reporte", "reports", "reportes",
    "repos", "repose", "reposs", "reposes",
    "reproduis", "reproduise", "reproduiss", "reproduises",
    "respect", "respecte", "respects", "respectes",
    "ressent", "ressente", "ressents", "ressentes",
    "ressort", "ressorte", "ressorts", "ressortes",
    "retard", "retarde", "retards", "retardes",
    "retraduis", "retraduise", "retraduiss", "retraduises",
    "retrait", "retraite", "retraits", "retraites",
    "revend", "revende", "revends", "revendes",
    "revêt", "revête", "revêts", "revêtes",
    "rhum", "rhume", "rhums", "rhumes",
    "ri", "rie", "ris", "ries",
    "rit", "rite", "rits", "rites",
    "sabord", "saborde", "sabords", "sabordes",
    "sabot", "sabote", "sabots", "sabotes",
    "séduis", "séduise", "séduiss", "séduises",
    "sent", "sente", "sents", "sentes",
    "serin", "serine", "serins", "serines",
    "serpent", "serpente", "serpents", "serpentes",
    "signal", "signale", "signals", "signales",
    "sis", "sise", "siss", "sises",
    "ski", "skie", "skis", "skies",
    "soi", "soie", "sois", "soies",
    "sol", "sole", "sols", "soles",
    "sort", "sorte", "sorts", "sortes",
    "souci", "soucie", "soucis", "soucies",
    "souhait", "souhaite", "souhaits", "souhaites",
    "soupent", "soupente", "soupents", "soupentes",
    "soupir", "soupire", "soupirs", "soupires",
    "souri", "sourie", "souris", "souries",
    "sprint", "sprinte", "sprints", "sprintes",
    "statu", "statue", "status", "statues",
    "stock", "stocke", "stocks", "stockes",
    "su", "sue", "sus", "sues",
    "suc", "suce", "sucs", "suces",
    "suffis", "suffise", "suffiss", "suffises",
    "suint", "suinte", "suints", "suintes",
    "suit", "suite", "suits", "suites",
    "support", "supporte", "supports", "supportes",
    "sur", "sure", "surs", "sures",
    "surf", "surfe", "surfs", "surfes",
    "surgi", "surgie", "surgis", "surgies",
    "surplomb", "surplombe", "surplombs", "surplombes",
    "sursaut", "sursaute", "sursauts", "sursautes",
    "survol", "survole", "survols", "survoles",
    "suspend", "suspende", "suspends", "suspendes",
    "suspens", "suspense", "suspenss", "suspenses",
    "tais", "taise", "taiss", "taises",
    "tambourin", "tambourine", "tambourins", "tambourines",
    "tard", "tarde", "tards", "tardes",
    "tarif", "tarife", "tarifs", "tarifes",
    "tend", "tende", "tends", "tendes",
    "test", "teste", "tests", "testes",
    "tint", "tinte", "tints", "tintes",
    "tir", "tire", "tirs", "tires",
    "titan", "titane", "titans", "titanes",
    "tond", "tonde", "tonds", "tondes",
    "tord", "torde", "tords", "tordes",
    "tors", "torse", "torss", "torses",
    "tourment", "tourmente", "tourments", "tourmentes",
    "tournoi", "tournoie", "tournois", "tournoies",
    "trac", "trace", "tracs", "traces",
    "tract", "tracte", "tracts", "tractes",
    "traduis", "traduise", "traduiss", "traduises",
    "trait", "traite", "traits", "traites",
    "tram", "trame", "trams", "trames",
    "transit", "transite", "transits", "transites",
    "transport", "transporte", "transports", "transportes",
    "travers", "traverse", "traverss", "traverses",
    "trépan", "trépane", "trépans", "trépanes",
    "tri", "trie", "tris", "tries",
    "tricot", "tricote", "tricots", "tricotes",
    "trop", "trope", "trops", "tropes",
    "trou", "troue", "trous", "troues",
    "trust", "truste", "trusts", "trustes",
    "tu", "tue", "tus", "tues",
    "us", "use", "uss", "uses",
    "vaccin", "vaccine", "vaccins", "vaccines",
    "vals", "valse", "valss", "valses",
    "valu", "value", "valus", "values",
    "vas", "vase", "vass", "vases",
    "vend", "vende", "vends", "vendes",
    "vent", "vente", "vents", "ventes",
    "vers", "verse", "verss", "verses",
    "vêt", "vête", "vêts", "vêtes",
    "viol", "viole", "viols", "violes",
    "vis", "vise", "viss", "vises",
    "vit", "vite", "vits", "vites",
    "voir", "voire", "voirs", "voires",
    "vol", "vole", "vols", "voles",
])


# Cette première passe très simple a ajouté plein de mots, c'était rapide et facile mais au prix d'avoir plein de faux positifs (des mots qui ne devraient pas être rajoutés)...

# In[15]:


print(f"{len(mots_inclusifs_singuliers)} nouveaux mots inclusifs singuliers")  # 5813
print(f"{len(mots_inclusifs_pluriels)} nouveaux mots inclusifs pluriels")      # 5244


# ### Ajouter mot·x·se et mot·x·ses si `mot`-x, `mot`-se et `mot`-ses sont présents

# In[16]:


nouveaux_mots_inclusifs_singuliers = []
nouveaux_mots_inclusifs_pluriels = []

for mot in tqdm(mots):
    if mot.endswith("x") and len(mot) > 1:
        mot_feminin = f"{mot[:-1]}se"
        if mot_feminin in set_mots:
            mot_inclusif = f"{mot[:-1]}x{SEP}se"
            print(f"{mot:<20} / {mot_feminin:<20} -> {mot_inclusif:<20}")
            nouveaux_mots_inclusifs_singuliers.append(mot_inclusif)
            alternatives[mot] |= {mot_inclusif}
            alternatives[mot_feminin] |= {mot_inclusif}
        mot_feminin = f"{mot[:-1]}ses"
        if mot_feminin in set_mots:
            mot_inclusif = f"{mot[:-1]}x{SEP}se{SEP}s"
            print(f"{mot:<20} / {mot_feminin:<20} -> {mot_inclusif:<20}")
            nouveaux_mots_inclusifs_pluriels.append(mot_inclusif)
            alternatives[mot] |= {mot_inclusif}
            alternatives[mot_feminin] |= {mot_inclusif}

# on garde les mots nouveaux
print(f"Cela a donné {len(set(nouveaux_mots_inclusifs_singuliers) - set(mots_inclusifs_singuliers))} nouveaux mots singuliers.")
mots_inclusifs_singuliers = list(set(mots_inclusifs_singuliers + nouveaux_mots_inclusifs_singuliers))
print(f"Cela a donné {len(set(nouveaux_mots_inclusifs_pluriels) - set(mots_inclusifs_pluriels))} nouveaux mots pluriels.")
mots_inclusifs_pluriels = list(set(mots_inclusifs_pluriels + nouveaux_mots_inclusifs_pluriels))


# Je pense qu'il n'y a pas d'erreurs sur ces 340 mots.

# ### Ajouter mot·teur·trice et mot·teur·trice·s si `mot`-teur, `mot`-teurs, `mot`-trice et `mot`-trices sont présents

# In[17]:


nouveaux_mots_inclusifs_singuliers = []
nouveaux_mots_inclusifs_pluriels = []

for mot in tqdm(mots):
    if mot.endswith("teur") and len(mot) > 4 and mot + "s" in set_mots:
        mot_feminin = f"{mot[:-4]}trice"
        if mot_feminin in set_mots:
            for mot_inclusif in [
                f"{mot[:-4]}teur{SEP}trice",
                f"{mot[:-4]}trice{SEP}teur",  # on autorise les deux sens ici
            ]:
                print(f"{mot:<20} / {mot_feminin:<20} -> {mot_inclusif:<20}")
                nouveaux_mots_inclusifs_singuliers.append(mot_inclusif)
                alternatives[mot] |= {mot_inclusif}
                alternatives[mot_feminin] |= {mot_inclusif}
        mot_feminin = f"{mot[:-4]}trices"
        if mot_feminin in set_mots:
            for mot_inclusif in [
                f"{mot[:-4]}teur{SEP}trice{SEP}s",
                f"{mot[:-4]}trice{SEP}teur{SEP}s",  # on autorise les deux sens ici
            ]:
                print(f"{mot + 's':<20} / {mot_feminin:<20} -> {mot_inclusif:<20}")
                nouveaux_mots_inclusifs_pluriels.append(mot_inclusif)
                alternatives[f"{mot + 's'}"] |= {mot_inclusif}
                alternatives[mot_feminin] |= {mot_inclusif}

# on garde les mots nouveaux
print(f"Cela a donné {len(set(nouveaux_mots_inclusifs_singuliers) - set(mots_inclusifs_singuliers))} nouveaux mots singuliers.")
mots_inclusifs_singuliers = list(set(mots_inclusifs_singuliers + nouveaux_mots_inclusifs_singuliers))
print(f"Cela a donné {len(set(nouveaux_mots_inclusifs_pluriels) - set(mots_inclusifs_pluriels))} nouveaux mots pluriels.")
mots_inclusifs_pluriels = list(set(mots_inclusifs_pluriels + nouveaux_mots_inclusifs_pluriels))


# Je pense qu'il n'y a pas d'erreurs sur ces 448 mots.

# On voit qu'il manque des mots : "auteure" ou "autrice" n'est pas présent, car "auteure" n'est pas présent dans le dictionnaire chargé au début.

# In[18]:


alternatives["auteur"] |= {"auteur·e", "auteur·trice"}
alternatives["auteurs"] |= {"auteur·e·s", "auteur·trice·smots"}
alternatives["auteure"] |= {"auteur·e", "auteur·trice"}
alternatives["auteures"] |= {"auteur·e·s", "auteur·trice·smots"}


# ### Ajouter mot·eau·elle et mot·eaux·elles si `mot`-eau, `mot`-eaux, `mot`-elle et `mot`-elles sont présents

# In[19]:


nouveaux_mots_inclusifs_singuliers = []
nouveaux_mots_inclusifs_pluriels = []

for mot in tqdm(mots):
    if mot.endswith("eau") and len(mot) > 3 and mot + "x" in set_mots:
        mot_feminin = f"{mot[:-3]}elle"
        if mot_feminin in set_mots:
            mot_inclusif = f"{mot[:-3]}eau{SEP}elle"
            print(f"{mot:<20} / {mot_feminin:<20} -> {mot_inclusif:<20}")
            nouveaux_mots_inclusifs_singuliers.append(mot_inclusif)
            alternatives[mot] |= {mot_inclusif}
            alternatives[mot_feminin] |= {mot_inclusif}
        mot_feminin = f"{mot[:-3]}elles"
        if mot_feminin in set_mots:
            mot_inclusif = f"{mot[:-3]}eaux{SEP}elles"
            print(f"{mot + 'x':<20} / {mot_feminin:<20} -> {mot_inclusif:<20}")
            nouveaux_mots_inclusifs_pluriels.append(mot_inclusif)
            alternatives[mot + "x"] |= {mot_inclusif}
            alternatives[mot_feminin] |= {mot_inclusif}

# on garde les mots nouveaux
print(f"Cela a donné {len(set(nouveaux_mots_inclusifs_singuliers) - set(mots_inclusifs_singuliers))} nouveaux mots singuliers.")
mots_inclusifs_singuliers = list(set(mots_inclusifs_singuliers + nouveaux_mots_inclusifs_singuliers))
print(f"Cela a donné {len(set(nouveaux_mots_inclusifs_pluriels) - set(mots_inclusifs_pluriels))} nouveaux mots pluriels.")
mots_inclusifs_pluriels = list(set(mots_inclusifs_pluriels + nouveaux_mots_inclusifs_pluriels))


# On voit que là aussi ça donne plein d'erreur !
# Seuls les mots suivants fonts sens :
# 
# - beau                 / belle                -> b·eau·elle
# - jumeau               / jumelle              -> jum·eau·elle
# - nouveau              / nouvelle             -> nouv·eau·elle
# - puceau               / pucelle              -> puc·eau·elle

# In[23]:


del_alternatives([
    "carreau", "carrelle", "carreaux", "carrelles",
    "cerveau", "cervelle", "cerveaux", "cervelles",
    "chapeau", "chapelle", "chapeaux", "chapelles",
    "jouvenceau", "jouvencelle", "jouvenceaux", "jouvencelles",
    "morceau", "morcelle", "morceaux", "morcelles",
    "museau", "muselle", "museaux", "muselles",
    "niveau", "nivelle", "niveaux", "nivelles",
    "passereau", "passerelle", "passereaux", "passerelles",
    "peau", "pelle", "peaux", "pelles",
    "pruneau", "prunelle", "pruneaux", "prunelles",
    "renouveau", "renouvelle", "renouveaux", "renouvelles",
    "rideau", "ridelle", "rideaux", "ridelles",
    "rondeau", "rondelle", "rondeaux", "rondelles",
    "ruisseau", "ruisselle", "ruisseaux", "ruisselles",
    "sceau", "scelles", "sceaux", "scelless",
    "seau", "selles", "seaux", "selless",
    "tonneau", "tonnelles", "tonneaux", "tonnelless",
    "tourtereau", "tourterelles", "tourtereaux", "tourterelless",
    "vaisseau", "vaisselles", "vaisseaux", "vaisselless",
])


# Et aussi mot-au-elle et mot-aux-elles si mot-au, mot-aux, mot-elle et mot-elles sont présents ?

# In[21]:


nouveaux_mots_inclusifs_singuliers = []
nouveaux_mots_inclusifs_pluriels = []

for mot in tqdm(mots):
    if mot.endswith("au") and len(mot) > 2 and mot + "x" in set_mots:
        mot_feminin = f"{mot[:-2]}elle"
        if mot_feminin in set_mots:
            mot_inclusif = f"{mot[:-2]}au{SEP}elle"
            print(f"{mot:<20} / {mot_feminin:<20} -> {mot_inclusif:<20}")
            nouveaux_mots_inclusifs_singuliers.append(mot_inclusif)
            alternatives[mot] |= {mot_inclusif}
            alternatives[mot_feminin] |= {mot_inclusif}
        mot_feminin = f"{mot[:-2]}elles"
        if mot_feminin in set_mots:
            mot_inclusif = f"{mot[:-2]}aux{SEP}elle{SEP}s"
            print(f"{mot + 'x':<20} / {mot_feminin:<20} -> {mot_inclusif:<20}")
            nouveaux_mots_inclusifs_pluriels.append(mot_inclusif)
            alternatives[mot + "x"] |= {mot_inclusif}
            alternatives[mot_feminin] |= {mot_inclusif}

# on garde les mots nouveaux
print(f"Cela a donné {len(set(nouveaux_mots_inclusifs_singuliers) - set(mots_inclusifs_singuliers))} nouveaux mots singuliers.")
mots_inclusifs_singuliers = list(set(mots_inclusifs_singuliers + nouveaux_mots_inclusifs_singuliers))
print(f"Cela a donné {len(set(nouveaux_mots_inclusifs_pluriels) - set(mots_inclusifs_pluriels))} nouveaux mots pluriels.")
mots_inclusifs_pluriels = list(set(mots_inclusifs_pluriels + nouveaux_mots_inclusifs_pluriels))


# Ce dernier test est clairement une mauvaise idée, matérielle n'est PAS le féminin de matériau.

# In[24]:


del_alternatives([
    "matériau", "matérielle", "matériaux", "matérielles",
])


# ### Ajouter mot·er·ère et mot·er·ère·s si `mot`-er, `mot`-ers, `mot`-ère et `mot`-ères sont présents

# In[25]:


nouveaux_mots_inclusifs_singuliers = []
nouveaux_mots_inclusifs_pluriels = []

for mot in tqdm(mots):
    if mot.endswith("er") and len(mot) > 2:
        mot_feminin = f"{mot[:-2]}ère"
        if mot_feminin in set_mots:
            mot_inclusif = f"{mot[:-2]}er{SEP}ère"
            print(f"{mot:<20} / {mot_feminin:<20} -> {mot_inclusif:<20}")
            nouveaux_mots_inclusifs_singuliers.append(mot_inclusif)
            alternatives[mot] |= {mot_inclusif}
            alternatives[mot_feminin] |= {mot_inclusif}
        mot_feminin = f"{mot[:-2]}ères"
        if mot_feminin in set_mots:
            mot_inclusif = f"{mot[:-2]}er{SEP}ère{SEP}s"
            print(f"{mot + 's':<20} / {mot_feminin:<20} -> {mot_inclusif:<20}")
            nouveaux_mots_inclusifs_pluriels.append(mot_inclusif)
            alternatives[mot + "s"] |= {mot_inclusif}
            alternatives[mot_feminin] |= {mot_inclusif}

# on garde les mots nouveaux
print(f"Cela a donné {len(set(nouveaux_mots_inclusifs_singuliers) - set(mots_inclusifs_singuliers))} nouveaux mots singuliers.")
mots_inclusifs_singuliers = list(set(mots_inclusifs_singuliers + nouveaux_mots_inclusifs_singuliers))
print(f"Cela a donné {len(set(nouveaux_mots_inclusifs_pluriels) - set(mots_inclusifs_pluriels))} nouveaux mots pluriels.")
mots_inclusifs_pluriels = list(set(mots_inclusifs_pluriels + nouveaux_mots_inclusifs_pluriels))


# On voit que là aussi ça donne des erreurs :
# - alter                / altère               -> alter·ère  
#   alter est un mot latin, altère un nom qui n'a pas de forme féminine
# - carrier              / carrière             -> carrier·ère  
#   rien à voir
# - fouger               / fougère              -> fouger·ère  
#   rien à voir
# - lacer                / lacère               -> lacer·ère
#   lacer est un verbe, lacère la conjugaison de lacérer
# - mer                  / mère                 -> mer·ère  
#   mer et mère n'ont rien à voir
# - miser                / misère               -> miser·ère  
#   là encore, rien à voir
# 
# Ces erreurs pourraient être évitées si on disposait d'étiquettes sur chaque mot (verbe, nom, adjectif, etc).

# In[26]:


del_alternatives([
    "alter", "altère", "alters", "altères",
    "carrier", "carrière", "carriers", "carrières",
    "fouger", "fougère", "fougers", "fougères",
    "lacer", "lacère", "lacers", "lacères",
    "mer", "mère", "mers", "mères",
    "miser", "misère", "misers", "misères",
])


# ### Ajouter mot-l·le et mot-n·ne si `mot`-l, `mot`-lle ou `mot`-n et `mot`-nne sont présents (et pluriels)

# In[27]:


nouveaux_mots_inclusifs_singuliers = []
nouveaux_mots_inclusifs_pluriels = []

for mot in tqdm(mots):
    if mot.endswith("n") and len(mot) > 1 and mot + "s" in set_mots:
        mot_feminin = f"{mot[:-1]}nne"
        if mot_feminin in set_mots:
            mot_inclusif = f"{mot[:-1]}n{SEP}ne"
            print(f"{mot:<20} / {mot_feminin:<20} -> {mot_inclusif:<20}")
            nouveaux_mots_inclusifs_singuliers.append(mot_inclusif)
            alternatives[mot] |= {mot_inclusif}
            alternatives[mot_feminin] |= {mot_inclusif}
        mot_feminin = f"{mot[:-1]}nnes"
        if mot_feminin in set_mots:
            mot_inclusif = f"{mot[:-1]}n{SEP}ne{SEP}s"
            print(f"{mot + 's':<20} / {mot_feminin:<20} -> {mot_inclusif:<20}")
            nouveaux_mots_inclusifs_pluriels.append(mot_inclusif)
            alternatives[mot + "s"] |= {mot_inclusif}
            alternatives[mot_feminin] |= {mot_inclusif}

# on garde les mots nouveaux
print(f"Cela a donné {len(set(nouveaux_mots_inclusifs_singuliers) - set(mots_inclusifs_singuliers))} nouveaux mots singuliers.")
mots_inclusifs_singuliers = list(set(mots_inclusifs_singuliers + nouveaux_mots_inclusifs_singuliers))
print(f"Cela a donné {len(set(nouveaux_mots_inclusifs_pluriels) - set(mots_inclusifs_pluriels))} nouveaux mots pluriels.")
mots_inclusifs_pluriels = list(set(mots_inclusifs_pluriels + nouveaux_mots_inclusifs_pluriels))


# On voit que là aussi ça donne PLEIN d'erreurs :
# 
# - abandon              / abandonne            -> abandon·ne  
# - action               / actionne             -> action·ne  
# - addition             / additionne           -> addition·ne  
# - affection            / affectionne          -> affection·ne  
# - ambition             / ambitionne           -> ambition·ne  
# - audition             / auditionne           -> audition·ne  
# - badigeon             / badigeonne           -> badigeon·ne  
# - bâillon              / bâillonne            -> bâillon·ne  
# - béton                / bétonne              -> béton·ne  
# - bonbon               / bonbonne             -> bonbon·ne  
# - bouillon             / bouillonne           -> bouillon·ne  
# - bourdon              / bourdonne            -> bourdon·ne  
# - bourgeon             / bourgeonne           -> bourgeon·ne  
# - bouton               / boutonne             -> bouton·ne  
# - brouillon            / brouillonne          -> brouillon·ne  
# - canton               / cantonne             -> canton·ne  
# - carton               / cartonne             -> carton·ne  
# - caution              / cautionne            -> caution·ne  
# - chiffon              / chiffonne            -> chiffon·ne  
# - clairon              / claironne            -> clairon·ne  
# - cloison              / cloisonne            -> cloison·ne  
# - collation            / collationne          -> collation·ne  
# - collection           / collectionne         -> collection·ne  
# - colon                / colonne              -> colon·ne  
# - condition            / conditionne          -> condition·ne  
# - confection           / confectionne         -> confection·ne  
# - congestion           / congestionne         -> congestion·ne  
# - convention           / conventionne         -> convention·ne  
# - crampon              / cramponne            -> crampon·ne  
# - démission            / démissionne          -> démission·ne  
# - don                  / donne                -> don·ne  
# - échantillon          / échantillonne        -> échantillon·ne  
# - échelon              / échelonne            -> échelon·ne  
# - émotion              / émotionne            -> émotion·ne  
# - environ              / environne            -> environ·ne  
# - façon                / façonne              -> façon·ne  
# - foison               / foisonne             -> foison·ne  
# - fonction             / fonctionne           -> fonction·ne  
# - fraction             / fractionne           -> fraction·ne  
# - frisson              / frissonne            -> frisson·ne  
# - fusion               / fusionne             -> fusion·ne  
# - goudron              / goudronne            -> goudron·ne  
# - illusion             / illusionne           -> illusion·ne  
# - impression           / impressionne         -> impression·ne  
# - jalon                / jalonne              -> jalon·ne  
# - maintien             / maintienne           -> maintien·ne  
# - man                  / manne                -> man·ne  
# - manutention          / manutentionne        -> manutention·ne  
# - marron               / marronne             -> marron·ne  
# - mention              / mentionne            -> mention·ne  
# - moyen                / moyenne              -> moyen·ne  
# - non                  / nonne                -> non·ne  
# - occasion             / occasionne           -> occasion·ne·s  
# - ovation              / ovationne            -> ovation·ne·s  
# - pan                  / panne                -> pan·ne  
# - papillon             / papillonne           -> papillon·ne·s  
# - pardon               / pardonne             -> pardon·ne·s  
# - passion              / passionne            -> passion·ne·s  
# - peloton              / pelotonne            -> peloton·ne·s  
# - perfection           / perfectionne         -> perfection·ne  
# - perquisition         / perquisitionne       -> perquisition·ne  
# - pilon                / pilonne              -> pilon·ne·s  
# - ponction             / ponctionne           -> ponction·ne·s  
# - position             / positionne           -> position·ne·s  
# - précaution           / précautionne         -> précaution·ne  
# - provision            / provisionne          -> provision·ne  
# - question             / questionne           -> question·ne  
# - raison               / raisonne             -> raison·ne  
# - rançon               / rançonne             -> rançon·ne  
# - ration               / rationne             -> ration·ne  
# - rayon                / rayonne              -> rayon·ne  
# - réception            / réceptionne          -> réception·ne  
# - réquisition          / réquisitionne        -> réquisition·ne  
# - réveillon            / réveillonne          -> réveillon·ne  
# - révolution           / révolutionne         -> révolution·ne  
# - ronchon              / ronchonne            -> ronchon·ne  
# - sanction             / sanctionne           -> sanction·ne  
# - savon                / savonne              -> savon·ne  
# - section              / sectionne            -> section·ne  
# - sélection            / sélectionne          -> sélection·ne  
# - sermon               / sermonne             -> sermon·ne·s  
# - sillon               / sillonne             -> sillon·ne  
# - solution             / solutionne           -> solution·ne  
# - son                  / sonne                -> son·ne  
# - soumission           / soumissionne         -> soumission·ne  
# - soupçon              / soupçonne            -> soupçon·ne  
# - station              / stationne            -> station·ne  
# - subvention           / subventionne         -> subvention·ne  
# - suggestion           / suggestionne         -> suggestion·ne  
# - tampon               / tamponne             -> tampon·ne  
# - ton                  / tonne                -> ton·ne·s  
# - tronçon              / tronçonne            -> tronçon·ne  
# - van                  / vanne                -> van·ne  
# - vision               / visionne             -> vision·ne  
# 
# Ces erreurs pourraient être évitées si on disposait d'étiquettes sur chaque mot (verbe, nom, adjectif, etc).
# La plupart des erreurs viennent de mots qui sont un nom au masculin (sermon) et un verbe conjugué au présent de l'indicatif qui ressemble à une forme féminine du mot (sermonne).

# In[28]:


del_alternatives([
    "abandon", "abandonne", "abandons", "abandonnes",
    "action", "actionne", "actions", "actionnes",
    "addition", "additionne", "additions", "additionnes",
    "affection", "affectionne", "affections", "affectionnes",
    "ambition", "ambitionne", "ambitions", "ambitionnes",
    "audition", "auditionne", "auditions", "auditionnes",
    "badigeon", "badigeonne", "badigeons", "badigeonnes",
    "bâillon", "bâillonne", "bâillons", "bâillonnes",
    "béton", "bétonne", "bétons", "bétonnes",
    "bonbon", "bonbonne", "bonbons", "bonbonnes",
    "bouillon", "bouillonne", "bouillons", "bouillonnes",
    "bourdon", "bourdonne", "bourdons", "bourdonnes",
    "bourgeon", "bourgeonne", "bourgeons", "bourgeonnes",
    "bouton", "boutonne", "boutons", "boutonnes",
    "brouillon", "brouillonne", "brouillons", "brouillonnes",
    "canton", "cantonne", "cantons", "cantonnes",
    "carton", "cartonne", "cartons", "cartonnes",
    "caution", "cautionne", "cautions", "cautionnes",
    "chiffon", "chiffonne", "chiffons", "chiffonnes",
    "clairon", "claironne", "clairons", "claironnes",
    "cloison", "cloisonne", "cloisons", "cloisonnes",
    "collation", "collationne", "collations", "collationnes",
    "collection", "collectionne", "collections", "collectionnes",
    "colon", "colonne", "colons", "colonnes",
    "condition", "conditionne", "conditions", "conditionnes",
    "confection", "confectionne", "confections", "confectionnes",
    "congestion", "congestionne", "congestions", "congestionnes",
    "convention", "conventionne", "conventions", "conventionnes",
    "crampon", "cramponne", "crampons", "cramponnes",
    "démission", "démissionne", "démissions", "démissionnes",
    "don", "donne", "dons", "donnes",
    "échantillon", "échantillonne", "échantillons", "échantillonnes",
    "échelon", "échelonne", "échelons", "échelonnes",
    "émotion", "émotionne", "émotions", "émotionnes",
    "environ", "environne", "environs", "environnes",
    "façon", "façonne", "façons", "façonnes",
    "foison", "foisonne", "foisons", "foisonnes",
    "fonction", "fonctionne", "fonctions", "fonctionnes",
    "fraction", "fractionne", "fractions", "fractionnes",
    "frisson", "frissonne", "frissons", "frissonnes",
    "fusion", "fusionne", "fusions", "fusionnes",
    "goudron", "goudronne", "goudrons", "goudronnes",
    "illusion", "illusionne", "illusions", "illusionnes",
    "impression", "impressionne", "impressions", "impressionnes",
    "jalon", "jalonne", "jalons", "jalonnes",
    "maintien", "maintienne", "maintiens", "maintiennes",
    "man", "manne", "mans", "mannes",
    "manutention", "manutentionne", "manutentions", "manutentionnes",
    "marron", "marronne", "marrons", "marronnes",
    "mention", "mentionne", "mentions", "mentionnes",
    "moyen", "moyenne", "moyens", "moyennes",
    "non", "nonne", "nons", "nonnes",
    "occasion", "occasionne", "occasions", "occasionnes",
    "ovation", "ovationne", "ovations", "ovationnes",
    "pan", "panne", "pans", "pannes",
    "papillon", "papillonne", "papillons", "papillonnes",
    "pardon", "pardonne", "pardons", "pardonnes",
    "passion", "passionne", "passions", "passionnes",
    "peloton", "pelotonne", "pelotons", "pelotonnes",
    "perfection", "perfectionne", "perfections", "perfectionnes",
    "perquisition", "perquisitionne", "perquisitions", "perquisitionnes",
    "pilon", "pilonne", "pilons", "pilonnes",
    "ponction", "ponctionne", "ponctions", "ponctionnes",
    "position", "positionne", "positions", "positionnes",
    "précaution", "précautionne", "précautions", "précautionnes",
    "provision", "provisionne", "provisions", "provisionnes",
    "question", "questionne", "questions", "questionnes",
    "raison", "raisonne", "raisons", "raisonnes",
    "rançon", "rançonne", "rançons", "rançonnes",
    "ration", "rationne", "rations", "rationnes",
    "rayon", "rayonne", "rayons", "rayonnes",
    "réception", "réceptionne", "réceptions", "réceptionnes",
    "réquisition", "réquisitionne", "réquisitions", "réquisitionnes",
    "réveillon", "réveillonne", "réveillons", "réveillonnes",
    "révolution", "révolutionne", "révolutions", "révolutionnes",
    "ronchon", "ronchonne", "ronchons", "ronchonnes",
    "sanction", "sanctionne", "sanctions", "sanctionnes",
    "savon", "savonne", "savons", "savonnes",
    "section", "sectionne", "sections", "sectionnes",
    "sélection", "sélectionne", "sélections", "sélectionnes",
    "sermon", "sermonne", "sermons", "sermonnes",
    "sillon", "sillonne", "sillons", "sillonnes",
    "solution", "solutionne", "solutions", "solutionnes",
    "son", "sonne", "sons", "sonnes",
    "soumission", "soumissionne", "soumissions", "soumissionnes",
    "soupçon", "soupçonne", "soupçons", "soupçonnes",
    "station", "stationne", "stations", "stationnes",
    "subvention", "subventionne", "subventions", "subventionnes",
    "suggestion", "suggestionne", "suggestions", "suggestionnes",
    "tampon", "tamponne", "tampons", "tamponnes",
    "ton", "tonne", "tons", "tonnes",
    "tronçon", "tronçonne", "tronçons", "tronçonnes",
    "van", "vanne", "vans", "vannes",
    "vision", "visionne", "visions", "visionnes",
])


# Et pour les mots en `mot`-l et `mot`-lle :

# In[29]:


nouveaux_mots_inclusifs_singuliers = []
nouveaux_mots_inclusifs_pluriels = []

for mot in tqdm(mots):
    if mot.endswith("l") and len(mot) > 1 and mot + "s" in set_mots:
        mot_feminin = f"{mot[:-1]}lle"
        if mot_feminin in set_mots:
            mot_inclusif = f"{mot[:-1]}l{SEP}le"
            print(f"{mot:<20} / {mot_feminin:<20} -> {mot_inclusif:<20}")
            nouveaux_mots_inclusifs_singuliers.append(mot_inclusif)
            alternatives[mot] |= {mot_inclusif}
            alternatives[mot_feminin] |= {mot_inclusif}
        mot_feminin = f"{mot[:-1]}lles"
        if mot_feminin in set_mots:
            mot_inclusif = f"{mot[:-1]}l{SEP}le{SEP}s"
            print(f"{mot + 's':<20} / {mot_feminin:<20} -> {mot_inclusif:<20}")
            nouveaux_mots_inclusifs_pluriels.append(mot_inclusif)
            alternatives[mot + "s"] |= {mot_inclusif}
            alternatives[mot_feminin] |= {mot_inclusif}

# on garde les mots nouveaux
print(f"Cela a donné {len(set(nouveaux_mots_inclusifs_singuliers) - set(mots_inclusifs_singuliers))} nouveaux mots singuliers.")
mots_inclusifs_singuliers = list(set(mots_inclusifs_singuliers + nouveaux_mots_inclusifs_singuliers))
print(f"Cela a donné {len(set(nouveaux_mots_inclusifs_pluriels) - set(mots_inclusifs_pluriels))} nouveaux mots pluriels.")
mots_inclusifs_pluriels = list(set(mots_inclusifs_pluriels + nouveaux_mots_inclusifs_pluriels))


# On voit que là aussi ça donne des erreurs :
# 
# - accueil              / accueille            -> accueil·le  
# - appareil             / appareille           -> appareil·le  
# - appel                / appelle              -> appel·le  
# - bal                  / balle                -> bal·le  
# - chenil               / chenille             -> chenil·le  
# - col                  / colle                -> col·le  
# - conseil              / conseille            -> conseil·le  
# - détail               / détaille             -> détail·le  
# - éveil                / éveille              -> éveil·le  
# - fil                  / fille                -> fil·le  
# - fils                 / filles               -> fil·le·s  
# - fusil                / fusille              -> fusil·le  
# - gril                 / grille               -> gril·le  
# - rail                 / raille               -> rail·le  
# - recueil              / recueille            -> recueil·le  
# - réveil               / réveille             -> réveil·le  
# - sel                  / selle                -> sel·le  
# - vil                  / ville                -> vil·le          
# 
# Ces erreurs pourraient être évitées si on disposait d'étiquettes sur chaque mot (verbe, nom, adjectif, etc).

# In[31]:


del_alternatives([
    "accueil", "accueille", "accueils", "accueilles",
    "appareil", "appareille", "appareils", "appareilles",
    "appel", "appelle", "appels", "appelles",
    "bal", "balle", "bals", "balles",
    "chenil", "chenille", "chenils", "chenilles",
    "col", "colle", "cols", "colles",
    "conseil", "conseille", "conseils", "conseilles",
    "détail", "détaille", "détails", "détailles",
    "éveil", "éveille", "éveils", "éveilles",
    "fil", "fille", "fils", "filles",
    "fusil", "fusille", "fusils", "fusilles",
    "gril", "grille", "grils", "grilles",
    "rail", "raille", "rails", "railles",
    "recueil", "recueille", "recueils", "recueilles",
    "réveil", "réveille", "réveils", "réveilles",
    "sel", "selle", "sels", "selles",
    "vil", "ville", "vils", "villes",
])


# On a effacé l'alternative à fils/fille, il faut la rajouter manuellement :

# In[32]:


alternatives["fils"] |= {"fils·lle", "fils·lles"}
alternatives["fille"] |= {"fils·lle"}
alternatives["filles"] |= {"fils·lles"}


# ### Ajouter les cas spéciaux à la main

# In[33]:


alternatives["il"] |= {"iel", "ielle"}
alternatives["ils"] |= {"iels", "ielles"}
alternatives["elle"] |= {"iel", "ielle"}
alternatives["elles"] |= {"iels", "ielles"}


# J'ai des doutes sur ce cas là : celleux est le mot que j'utilise mais quid du cas singulier ?

# In[34]:


alternatives["celui"] |= {"celleu", "ceulle", "ceului"}  # ?
alternatives["ceux"] |= {"celleux", "ceulles"}
alternatives["celle"] |= {"celleu", "ceulle", "ceului"}  # ?
alternatives["celles"] |= {"celleux", "ceulles"}


# In[35]:


alternatives["tous"] |= {"toustes"}
alternatives["toutes"] |= {"toustes"}


# In[47]:


alternatives["loup"] |= {"loup·ve"}
alternatives["louve"] |= {"loup·ve"}
alternatives["loups"] |= {"loup·ve·s"}
alternatives["louves"] |= {"loup·ve·s"}


# <span style="color: red;">TODO</span> ajouter les mots qu'il manque ?

# ### Prendre un mot et proposer des variantes
# 
# C'est trivial, maintenant qu'on a construit le dictionnaire `alternatives` :

# On a construit BEAUCOUP de mots alternatifs :

# In[37]:


len(alternatives)


# In[38]:


pprint(alternatives)


# La fonction est HYPER simple :

# In[39]:


def proposer_variante(mot):
    return alternatives[mot]


# Quelques exemples :

# In[40]:


from numpy import random


# In[41]:


for mot in sorted(random.choice(list(alternatives.keys()), size=50, replace=False)):
    variantes = proposer_variante(mot)
    if len(variantes) > 1:
        print(f"Le mot {mot} a les variantes suivantes : {', '.join(variantes)}")
    else:
        print(f"Le mot {mot} a la variante suivante : {', '.join(variantes)}")


# ### Ajouter ces mots dans un fichier

# In[42]:


get_ipython().system('ls french_inclusive')
get_ipython().system('mv -vf french_inclusive /tmp/')


# In[43]:


with open("french_inclusive", "w") as f:
    for mot, alts in alternatives.items():
        for alt in alts:
            f.write(alt + "\n")
            f.write(alt.replace("·", "-") + "\n")


# In[49]:


get_ipython().system('ls -larth french_inclusive')
get_ipython().system('wc french_inclusive')


# On a rajouté quelques 50 000 mots à une liste qui en contenait 138 000 ! C'est DINGUE !

# In[46]:


get_ipython().system('head french_inclusive')
get_ipython().system('tail french_inclusive')


# In[48]:


get_ipython().system('cat french_inclusive | shuf -n10')


# Cette liste peut être utilisée pour ajouter ces mots au dictionnaire (`/usr/share/dict/french`) et permettre à la correction orthographique du système d'accepter les mots comme "abaissé-e" ou "abasourdi·e".

# ### Conclusion
# Fin pour aujourd'hui !
