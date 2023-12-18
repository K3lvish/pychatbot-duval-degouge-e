from math import log10
import os
def liste_fichiers(dossier, extension):
    """str,str -> list
    renvoie la liste des fichiers de directory de même extension que "extension" """
    noms_fichier = []
    for fichier in os.listdir(dossier):
        if fichier.endswith(extension):
            noms_fichier.append(fichier)
    return noms_fichier

def tf(car):
    """str -> dict
    renvoie un dictionnaire contenant tout les mots de car en clé et le nombre de fois qu'ils apparaissent en valeur"""
    cara = car.split(" ")
    dico = {}
    for el in cara:
        if el not in dico:
            dico[el] = 1
        else:
            dico[el] += 1
    return dico

def idf(rep):
    """répertoire de fichiers -> dict
     renvoie un ditionnaire associant à chaque mot son score IDF"""
    dicoidf = {}
    for el in liste_fichiers(rep, "txt"):
        with open(rep + "/" + el, 'r') as fichier:
            discours = fichier.read()
            dico = tf(discours)
            for cles in dico:
                if cles not in dicoidf:
                    dicoidf[cles] = 1
                else:
                    dicoidf[cles] += 1
    for el in dicoidf:
        dicoidf[el] = log10(8/dicoidf[el])
    return dicoidf

def tfidf(rep):
    """répertoire de fichiers -> list
    renvoie la matrice tfidf du répertoire"""
    matrice = []
    dicoidf = idf(rep)
    for cles in dicoidf:
        tab = []
        for el in liste_fichiers(rep, 'txt'):
            with open(rep + "/" + el, 'r') as fichier:
                dicotf = tf(fichier.read())
                if cles in dicotf:
                    tab.append(dicotf[cles] * dicoidf[cles])
                else:
                    tab.append(0)
        matrice.append(tab)
    return matrice
