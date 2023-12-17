from fonctions import *
from tf_idf_tfidf import *
from math import sqrt

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


def produit_scal(A, B):
    """ list,list -> float
    renvoie le produit scalaire de A et B"""
    somme = 0
    for i in range(len(A)):
        somme += A[i] * B[i]
    return somme

def norme(vecteur):
    """ list -> float
    renvoie la norme de vecteur"""
    somme = 0
    for el in vecteur:
        somme += el*2
    return sqrt(somme)

def similaire(A, B):
    """list,list -> float
    renvoie l'écart entre les vecteurs A et B"""
    return produit_scal(A, B)/(norme(A)*norme(B))

def comparer(vec, tabnom):
    """list,list -> str
    renvoie le fichier avec le vecteur le plus proche de vec (vecteur de la question)"""
    maxi = tabnom[0]
    vecmax = list()
    with open("cleaned/" + maxi,'r') as texte:
        vecmax = similaire(vec, vecteur(texte.read()))
    for el in tabnom:
        with open("cleaned/" + el, 'r') as texte:
            veccomp = similaire(vec, vecteur(texte.read()))
            if vecmax < veccomp:
                vecmax = veccomp
                maxi = el
    return maxi

def dictionnaire(quest):
    """str -> dict
    renvoie la matrice de quest """
    dicotf = tf(quest)
    dicogidf = idf('cleaned')
    dicoidf = {}
    for cles in dicogidf:
        if cles in recherche(quest, dicogidf):
            dicoidf[cles] = (dicotf[cles] * dicogidf[cles])
        else:
            dicoidf[cles] = 0
    return dicoidf 
def tfidf_max(quest):
    """str -> str
    renvoie le mot de quest avec le plus grand tfidf"""
    dicotfidf = dictionnaire(quest)
    clemax = 0
    maxi = -1
    for el in dicotfidf:
        if dicotfidf[el] > maxi:
            maxi = dicotfidf[el]
            clemax = el
    return clemax
