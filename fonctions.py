import os
import re
def liste_fichiers(dossier, extension):
    """str,str -> list
    renvoie la liste des fichiers de directory de même extension que "extension" """
    noms_fichier = []
    for fichier in os.listdir(dossier):
        if fichier.endswith(extension):
            noms_fichier.append(fichier)
    return noms_fichier

def dico_pres(tab):
    """list -> dict
    renvoie un dictionnaire contenant le nom des présidents avec leur nom en objet et leur prénom en clé"""
    dico = {}
    for pres in tab:
        nompres = re.sub(r'[0-9]', '', pres)[11:-4]
        if nompres not in dico:
            dico[nompres] = assigner(nompres)
    return dico

def assigner(nom):
    """ str -> str
    assigne au président son prénom"""
    prenom = ""
    if nom == 'Chirac':
        prenom = "Jacques"
    elif nom == 'Giscard dEstaing':
        prenom = 'Valérie'
    elif nom == 'Hollande':
        prenom = 'François'
    elif nom == 'Macron':
        prenom = 'Emmanuel'
    elif nom == 'Mitterrand':
        prenom = 'François'
    elif nom == 'Sarkozy':
        prenom = 'Nicolas'
    return prenom

def polir(txt):
    """str -> str
    renvoie le texte entré sans aucune pontuation et avec un espace entre chaque mot"""
    caracteres_a_remplacer = [',', '?', '.', ';', ':', '!', '-', "'", '"']
    caractere_de_remplacement = ' '
    text=txt
    for caractere in caracteres_a_remplacer:
        text = text.replace(caractere, caractere_de_remplacement)
    return text


def discours(tab):
    """ "polis" les discours
    et les écrit dans le dossier clean"""
    for el in tab:
        with open("speeches/" + el, 'r') as brut:
            discours = polir(brut.read().lower())
            with open("cleaned/" + el, 'w') as poli:
                poli.write(discours)
