
# coding: utf-8

# # Vérification de numéros de Cartes Bleues, RIB (IBAN) et NIRPP (sécu)
# 
# Ce petit notebook va implémenter les algorithmes de vérification des numéros de :
# 
# - cartes bleues, sur $4\times4$ chiffres, avec un chiffre de vérification,
# - RIB (identifiant de compte, sur les IBAN), avec deux chiffres de vérifications,
# - NIRPP (numéro de sécurité sociale en France), avec deux chiffres de vérifications.
# 
# > J'avais déjà implementé les deux derniers, cf. ces scripts : [check_IBAN.py](https://bitbucket.org/lbesson/bin/src/master/check_IBAN.py), et [check_NIRPP.py](https://bitbucket.org/lbesson/bin/src/master/check_NIRPP.py).
# 
# Si vous êtes curieux de l'aspect historique, [ce petit article](https://spectrum.ieee.org/tech-history/silicon-revolution/hans-peter-luhn-and-the-birth-of-the-hashing-algorithm) explique très bien les origines de ces chiffres de contrôles et de la [formule de Luhn](https://fr.wikipedia.org/wiki/Formule_de_Luhn).

# Je vais utiliser cette fonction plusieurs fois, qui permet de transformer une lettre 'A',...,'Z' en entier.

# In[1]:


def l_to_c(l):
    try:
        return str(int(l))
    except ValueError:
        return str(10 + ord(l.upper()) - ord('A'))


# In[2]:


for l in 'ABCDEFGHIJKLMNROPQRSTUVWXYZ':
    print("l = {} --> c = {}".format(l, l_to_c(l)))


# ## Cartes Bleues
# 
# - Références : https://www.hellolife.fr/article/a-quoi-correspondent-les-chiffres-sur-ma-carte-bancaire_a466/1 et https://fr.wikipedia.org/wiki/Carte_de_paiement#Num%C3%A9ro_de_carte_bancaire et https://fr.wikipedia.org/wiki/Formule_de_Luhn
# - Exemple :
# <img width="65%" src="data/Exemple_CB.jpg"/>

# In[3]:


exemple_cb = "4970 1012 3456 7890"  # pas valide


# D'abord l'algorithme de Luhn :

# In[4]:


def verifie_Luhn(numeros):
    numeros = numeros.replace(' ', '')
    nb_chiffres = len(numeros)
    parite = nb_chiffres % 2
    chiffres = [int(l_to_c(l)) for l in numeros]
    somme = chiffres[nb_chiffres - 1]
    for i in range(nb_chiffres - 2, -1, -1):
        chiffre = chiffres[i]
        if i % 2 == parite:
            chiffre *= 2
            if chiffre > 9:
                chiffre -= 9
        somme += chiffre
    return (somme % 10) == 0


# In[5]:


verifie_Luhn('972 487 086')


# In[6]:


verifie_Luhn('972 487 081')
verifie_Luhn('972 487 082')
verifie_Luhn('972 487 087')


# In[7]:


verifie_Luhn(exemple_cb)


# Ensuite la vérification pour un numéro de carte bleue :

# In[8]:


def verifie_cb(cb):
    print("\nVérification du numéro de CB '%s'..." % cb)
    check = verifie_Luhn(cb)
    if check:
        print("OK '%s' semble être un numéro de CB valide." % cb)
    else:
        print("[ATTENTION] PAS OK '%s' semble ne pas être un numéro de CB valide!" % cb)
    return check


# ### Exemples

# In[9]:


verifie_cb(exemple_cb)


# Avec un autre faux numéro mais conçu pour être vrai :

# In[10]:


verifie_cb("4976 5301 7218 3533")


# ## RIB/IBAN
# 
# - Référence : https://fr.wikipedia.org/wiki/International_Bank_Account_Number#Algorithme_de_v.C3.A9rification_de_l.27IBAN
# - Exemple :
# <img width="45%" src="data/Exemple_RIB.jpg"/>

# In[11]:


exemple_iban = "FR76 1254 8029 9838 3759 0150 071"


# In[12]:


def verifie_iban(iban):
    print("\nVérification du nombre IBAN '%s'..." % iban)
    ib = iban.replace(' ', '')
    ib = ib[4:] + ib[:4]
    print("  De longueur", len(ib))
    i = int(''.join(l_to_c(l) for l in ib))
    check = (i % 97) == 1
    if check:
        print("OK '%s' semble être un nombre IBAN valide." % iban)
    else:
        print("[ATTENTION] PAS OK '%s' semble ne pas être un nombre IBAN valide!" % iban)
    return check


# ### Exemples

# #### Compte français

# In[13]:


verifie_iban(exemple_iban)


# #### Compte anglais

# In[14]:


verifie_iban("GB87 BARC 2065 8244 9716 55")


# In[15]:


verifie_iban("GB87 BARC 2065 8244 9716 51")


# #### Compte belge

# In[16]:


verifie_iban("BE43 0689 9999 9501")


# In[17]:


verifie_iban("BE43 0689 9999 9500")


# ## NIRPP
# - Référence : https://fr.wikipedia.org/wiki/Num%C3%A9ro_de_s%C3%A9curit%C3%A9_sociale_en_France#cite_note-8
# - Exemple :
# <img width="40%" src="data/Exemple_CarteVitale.jpg"/>

# In[18]:


exemple_nirpp = "2 69 05 49 588 157 80"


# In[19]:


length_checksum = 2

def verifie_nirpp(nirpp, length_checksum=length_checksum):
    print("\nVérification du nombre NIRPP '%s' ..." % nirpp)
    ib = nirpp.replace(' ', '')
    checksum = int(ib[-length_checksum:])
    ib = ib[:-length_checksum]
    print("  De longueur", len(ib))
    num_nirpp = int(''.join(l_to_c(l) for l in ib))
    print("  De somme de contrôle num_nirpp =", num_nirpp)
    print("  Module à 97 =", (97 - (num_nirpp % 97)))
    print("  Et la somme de contrôle attendue était", checksum)
    check = (97 - (num_nirpp % 97)) == checksum
    if check:
        print("OK '%s' semble être un nombre NIRPP valide." % nirpp)
    else:
        print("[ATTENTION] PAS OK '%s' semble ne pas être un nombre NIRPP valide!" % nirpp)
    return check


# ### Exemples

# In[20]:


verifie_nirpp(exemple_nirpp)


# ### Bonus : affichage d'un NIRPP
# - Référence : https://fr.wikipedia.org/wiki/Num%C3%A9ro_de_s%C3%A9curit%C3%A9_sociale_en_France#Signification_des_chiffres_du_NIR
# 
# Il suffit de récupérer les informations de chaque morceau du code NIRPP, et les stocker comme ça :

# In[21]:


information_nirpp = {
    (0, 1): {
        "meaning": "sexe",
        "mapping": {
            "1": "homme",
            "2": "femme",
            "3": "personne étrangère de sexe masculin en cours d'immatriculation en France",
            "4": "personne étrangère de sexe féminin en cours d'immatriculation en France"
        }
    },
    (1, 2): {
        "meaning": "deux derniers chiffres de l'année de naissance",
        "mapping": {
            # DONE nothing to do for this information
        }
    },
    (3, 2): {
        "meaning": "mois de naissance",
        "mapping": {
            "01": "janvier",
            "02": "février",
            "03": "mars",
            "04": "avril",
            "05": "mai",
            "06": "juin",
            "07": "juillet",
            "08": "août",
            "09": "septembre",
            "10": "octobre",
            "11": "novembre",
            "12": "décembre",
        }
    },
    # Only case A : TODO implement case B and C
    (5, 2): {
        "meaning": "département de naissance métropolitain",
        "mapping": {  # Cf. http://www.insee.fr/fr/methodes/nomenclatures/cog/documentation.asp
            "01": "Ain",
            "02": "Aisne",
            "03": "Allier",
            "04": "Alpes-de-Haute-Provence",
            "05": "Hautes-Alpes",
            "06": "Alpes-Maritimes",
            "07": "Ardèche",
            "08": "Ardennes",
            "09": "Ariège",
            "10": "Aube",
            "11": "Aude",
            "12": "Aveyron",
            "13": "Bouches-du-Rhône",
            "14": "Calvados",
            "15": "Cantal",
            "16": "Charente",
            "17": "Charente-Maritime",
            "18": "Cher",
            "19": "Corrèze",
            "2A": "Corse-du-Sud",
            "2B": "Haute-Corse",
            "21": "Côte-d'Or",
            "22": "Côtes-d'Armor",
            "23": "Creuse",
            "24": "Dordogne",
            "25": "Doubs",
            "26": "Drôme",
            "27": "Eure",
            "28": "Eure-et-Loir",
            "29": "Finistère",
            "30": "Gard",
            "31": "Haute-Garonne",
            "32": "Gers",
            "33": "Gironde",
            "34": "Hérault",
            "35": "Ille-et-Vilaine",
            "36": "Indre",
            "37": "Indre-et-Loire",
            "38": "Isère",
            "39": "Jura",
            "40": "Landes",
            "41": "Loir-et-Cher",
            "42": "Loire",
            "43": "Haute-Loire",
            "44": "Loire-Atlantique",
            "45": "Loiret",
            "46": "Lot",
            "47": "Lot-et-Garonne",
            "48": "Lozère",
            "49": "Maine-et-Loire",
            "50": "Manche",
            "51": "Marne",
            "52": "Haute-Marne",
            "53": "Mayenne",
            "54": "Meurthe-et-Moselle",
            "55": "Meuse",
            "56": "Morbihan",
            "57": "Moselle",
            "58": "Nièvre",
            "59": "Nord",
            "60": "Oise",
            "61": "Orne",
            "62": "Pas-de-Calais",
            "63": "Puy-de-Dôme",
            "64": "Pyrénées-Atlantiques",
            "65": "Hautes-Pyrénées",
            "66": "Pyrénées-Orientales",
            "67": "Bas-Rhin",
            "68": "Haut-Rhin",
            "69": "Rhône",
            "70": "Haute-Saône",
            "71": "Saône-et-Loire",
            "72": "Sarthe",
            "73": "Savoie",
            "74": "Haute-Savoie",
            "75": "Paris",
            "76": "Seine-Maritime",
            "77": "Seine-et-Marne",
            "78": "Yvelines",
            "79": "Deux-Sèvres",
            "80": "Somme",
            "81": "Tarn",
            "82": "Tarn-et-Garonne",
            "83": "Var",
            "84": "Vaucluse",
            "85": "Vendée",
            "86": "Vienne",
            "87": "Haute-Vienne",
            "88": "Vosges",
            "89": "Yonne",
            "90": "Territoire de Belfort",
            "91": "Essonne",
            "92": "Hauts-de-Seine",
            "93": "Seine-Saint-Denis",
            "94": "Val-de-Marne",
            "95": "Val-d'Oise",
            # TODO support these too
            "971": "Guadeloupe",
            "972": "Martinique",
            "973": "Guyane",
            "974": "La Réunion",
            "975": "Saint-Pierre-et-Miquelon",
            "976": "Mayotte",
            "977": "Saint-Barthélemy",
            "978": "Saint-Martin",
            "984": "Terres australes et antarctiques françaises",
            "986": "Wallis-et-Futuna",
            "987": "Polynésie française",
            "988": "Nouvelle-Calédonie",
            "989": "Île de Clipperton"
        }
    },
    (7, 3): {
        "meaning": "code officiel de la commune de naissance",
        "mapping": {  # TODO
        }
    },
    (10, 3): {
        "meaning": "numéro d’ordre de la naissance dans le mois et la commune (ou le pays)",
        "mapping": {
            # DONE nothing to do for this information
        }
    }
}


# Pour les villes, on a besoin d'une base de donnée plus grande. J'ai récupéré [ce fichier](https://bitbucket.org/lbesson/bin/src/master/comsimp2016.txt) sur le site de l'INSEE (lien mort).

# In[22]:


get_ipython().system('ls data/')


# In[23]:


get_ipython().system('wc data/comsimp2016.txt')


# Il ressemble à ça :

# In[24]:


get_ipython().system('head data/comsimp2016.txt')


# Briançon est bien dans la liste :

# In[25]:


get_ipython().system('grep "BRIANCON" data/comsimp2016.txt')


# Allons-y :

# In[26]:


import subprocess
length_checksum = 2


def pprint_nirpp(nirpp, length_checksum=length_checksum):
    print("\nAffichage d'informations contenues dans le numéro NIRPP '%s' ..." % nirpp)
    nirpp = nirpp.replace(' ', '')
    ib = nirpp[:-length_checksum]
    # Printing
    for (i, l) in sorted(information_nirpp):
        n = nirpp[i: i + l]
        info = information_nirpp[(i, l)]
        if n in info["mapping"]:
            explain = "\"{}\"".format(info["mapping"][n])
        else:
            explain = n
        # For towns, durty hack to extract the town from the INSEE database
        if i == 7:
            try:
                args = [
                    "grep", "--", "',{},{},'".format(
                        nirpp[5: 5 + 2],
                        nirpp[7: 7 + 3]
                    ),
                    "data/comsimp2016.txt",
                    "|", "cut", "-d,", "-f10"
                ]
                command = ' '.join(args)
                # print("Executing subprocess.check_output to \"{}\"".format(command))
                explain = subprocess.check_output(command, shell=True)
                explain = explain[:-1].decode()
                # print("explain =", explain)
                explain = "{} (code {})".format(explain, nirpp[7: 7 + 3])
            except Exception as e:
                # print("e =", e)
                explain = n
        print("- Le nombre '{}' (indice {}:{}) signifie:\n\t\"{}\" : \t{}".format(
            n, i, i + l, info["meaning"], explain)
        )


# In[27]:


pprint_nirpp(exemple_nirpp)


# Avec un exemple assez proche de mon numéro de sécurité sociale (modifié) :

# In[28]:


pprint_nirpp("1 93 01 05 023 122 23")


# ## IMEI
# Les numéros d'identification des téléphones portables ([les IMEI](https://fr.wikipedia.org/wiki/International_Mobile_Equipment_Identity#Structure)) terminent aussi par un chiffre de contrôle, qui utilise aussi la [formule de Luhn](https://fr.wikipedia.org/wiki/Formule_de_Luhn).
# Je termine ce notebook en implémentant aussi cette vérification.
# 
# <img width="40%" src="data/Exemple_IMEI.jpg"/>

# In[29]:


exemple_imei = "448674 52 897641 0"  # avant 2014, 6-2-6-1


# In[30]:


def verifie_imei(imei):
    print("\nVérification du numéro IMEI '%s'..." % imei)
    check = verifie_Luhn(imei)
    if check:
        print("OK '%s' semble être un numéro IMEI valide." % imei)
    else:
        print("[ATTENTION] PAS OK '%s' semble ne pas être un numéro IMEI valide!" % imei)
    return check


# In[32]:


verifie_imei(exemple_imei)


# ### Exemples

# In[33]:


exemple_imei = "448674 52 897641 1"


# In[34]:


verifie_imei(exemple_imei)


# In[35]:


exemple_imei = "468674 52 897641 0"


# In[36]:


verifie_imei(exemple_imei)


# Avec un IMEI semblable à celui d'un de mes anciens téléphones :

# In[39]:


mon_faux_imei_1 = "35569508 262195 2"

verifie_imei(mon_faux_imei_1)


# In[40]:


mon_faux_imei_2 = "35569508 283295 5"

verifie_imei(mon_faux_imei_2)


# ## Conclusion
# 
# Voilà, c'est tout pour aujourd'hui !
# 
# > Allez lire [ici pour voir mes autres notebooks](https://GitHub.com/Naereen/notebooks).
