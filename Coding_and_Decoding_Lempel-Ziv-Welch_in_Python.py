import typing

## Encodage de Lempel-Ziv-Welch

def encodage_LZW(mot: str) -> typing.List[int]:
    codes_ecrits = []
    dictionnaire = { chr(i): i for i in range(255) }
    prochain_code = 257
    mot_actuel = ""
    n = len(mot)
    i = 0
    while i < n:
        lettre = mot[i]
        mot_actuel = mot_actuel + lettre
        print("Lecture de lettre = {}, mot actuel = {}".format(
            lettre, mot_actuel))
        if mot_actuel in dictionnaire:
            i += 1
        else:
            print("Ajout de '{}' au dictionnaire, de code = {}".format(
                  mot_actuel, prochain_code))
            dictionnaire[mot_actuel] = prochain_code
            prochain_code += 1
            code_actuel = dictionnaire[mot_actuel[:-1]]
            codes_ecrits.append(code_actuel)
            print("On écrit {} dans le code de sortie...".format(code_actuel))
            mot_actuel = mot_actuel[-1]
            i += 1
    if mot_actuel in dictionnaire:
        # on écrit le dernier mot
        code_actuel = dictionnaire[mot_actuel]
        codes_ecrits.append(code_actuel)
        print("On écrit {} dans le code de sortie...".format(code_actuel))
    return codes_ecrits

assert encodage_LZW("barbapapa") == [98, 97, 114, 257, 112, 97, 261]


## Décodage de Lempel-Ziv-Welch

def decodage_LZW(code_lu: typing.List[int]) -> str:
    mot_lu = ""
    dictionnaire = { i: chr(i) for i in range(255) }
    prochain_code = 257
    mot_actuel = ""
    
    m = len(code_lu)
    if m == 0: return ""
    
    code_actuel = code_lu[0]
    mot_actuel = dictionnaire[code_actuel]
    mot_lu += mot_actuel
    w = mot_actuel

    i = 1
    while i < m:
        code_actuel = code_lu[i]
        if code_actuel in dictionnaire:
            mot_actuel = dictionnaire[code_actuel]
            print("Code lu = {}, mot correspondant = {}.".format(
                code_actuel, mot_actuel))
        elif code_actuel == prochain_code:
            mot_actuel = w + w[0]
            print("Code lu = {}, mot correspondant = {}.".format(
                code_actuel, mot_actuel))
        else:
            raise ValueError("Mauvaise compression code_actuel = {}".format(code_actuel))
        mot_lu += mot_actuel
        print("Ajout de {} au dictionnaire, de valeur = '{}'".format(
            prochain_code, mot_actuel))
        dictionnaire[prochain_code] = w + mot_actuel[0]
        prochain_code += 1
        i += 1
        w = mot_actuel
    return mot_lu


assert decodage_LZW([98, 97, 114, 257, 112, 97, 261]) == "barbapapa"
