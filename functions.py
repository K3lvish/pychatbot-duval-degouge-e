import os
import re
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

directory = "./speeches"
files_names = list_of_files(directory, "txt")

def dico_pres(tab):
    dico = {}
    for pres in tab:
        nompres = re.sub(r'[0-9]', '', pres)[11:-4]
        if nompres not in dico:
            dico[nompres] = assigner(nompres)
    return dico

def assigner(nom):
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
    text = txt.replace(',', ' ')
    text = text.replace('?', ' ')
    text = text.replace('.', ' ')
    text = text.replace(';', ' ')
    text = text.replace(':', ' ')
    text = text.replace('!', ' ')
    text = text.replace('-', ' ')
    text = text.replace("'", ' ')
    return text

def discours(tab):
    for el in tab:
        with open("speeches/" + el, 'r') as raw:
            discours = polir(raw.read().lower())
            with open("cleaned/" + el, 'w') as clean:
                clean.write(discours)
