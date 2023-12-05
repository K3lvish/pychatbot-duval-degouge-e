from functions import *
def token(car):
    car = polir(car)
    tabmot = car.split(" ")
    for el in tabmot:
        if el == "":
            tabmot.remove(el)
    return tabmot
  

