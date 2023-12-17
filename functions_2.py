from functions import *
from tfidf import *

def token(car):
    """str -> list
    renvoie sous forme de liste les mot de l'entrée"""
    tabmot = car.split(" ")
    for el in tabmot:
        if el == "":
            tabmot.remove(el)
    return tabmot
