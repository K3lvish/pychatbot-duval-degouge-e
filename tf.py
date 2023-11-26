def tf(car):
    cara = car.split(" ")
    dico = {}
    for el in cara:
        if el not in dico:
            dico[el] = 1
        else:
            dico[el] += 1
    return dico
