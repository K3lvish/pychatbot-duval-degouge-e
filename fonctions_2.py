from fonctions import *
from tf_idf_tfidf import *

def token(car):
    """str -> list
    renvoie sous forme de liste les mot de l'entrée"""
    tabmot = car.split(" ")
    for el in tabmot:
        if el == "":
            tabmot.remove(el)
    return tabmot

def recherche(quest,dico):
    """ str,dict -> list
    renvoie la liste des mot de quest qui sont présent quelque part dans les textes"""
    present = []
    quest = token(quest)
    for i in range(len(quest)):
        if quest[i] in dico.keys() and quest[i] not in present:
            present.append(quest[i])
    return present

def vecteur(quest):
    """str -> list
    renvoie le vecteur tfidf de quest"""
    tabtf = tf(quest)
    dicogidf = idf('cleaned')
    vecidf = []
    for cles in dicogidf:
        if cles in recherche(quest, dicogidf):
            vecidf.append(tabtf[cles] * dicogidf[cles])
        else:
            vecidf.append(0)
    return vecidf
