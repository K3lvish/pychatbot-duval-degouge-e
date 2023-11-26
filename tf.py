from math import log
import os
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names
    
def tf(car):
    cara = car.split(" ")
    dico = {}
    for el in cara:
        if el not in dico:
            dico[el] = 1
        else:
            dico[el] += 1
    return dico

def idf(rep):
    dicoidf = {}
    for el in list_of_files(rep, "txt"):
        with open(rep + "/" + el, 'r') as file:
            discours = file.read()
            dico = tf(discours)
            for keys in dico:
                if keys not in dicoidf:
                    dicoidf[keys] = 1
                else:
                    dicoidf[keys] += 1
    for el in dicoidf:
        dicoidf[el] = log(8/dicoidf[el])
    return dicoidf
