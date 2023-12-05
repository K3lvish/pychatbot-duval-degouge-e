from functions import *
def token(car):
    car = polir(car)
    tabmot = car.split(" ")
    for el in tabmot:
        if el == "":
            tabmot.remove(el)
    return tabmot
  
def recherche(quest,dico):
    present=[]
    quest=token(quest)
    for i in range(len(quest)):
        if quest[i] in dico.keys() and quest[i] not in present:
            present.append(quest[i])
    return present
