from functions import *
from tfidf import *

print(dico_pres(files_names))
discours(files_names)
liste_fichier = list_of_files('cleaned','txt')

matrice = tfidf('cleaned')
dicomot = idf('cleaned')
compteur = 0
motuse = []
for keys in dicomot:
    dicomot[keys] = matrice[compteur]
    compteur += 1
for keys in dicomot:
    occurences = 0
    for el in dicomot[keys]:
        if float(el) == 0.0 :
            occurences += 1
    if occurences == len(liste_fichier):
        motuse.append(keys)

maximum = max(max(matrice))
for keys in dicomot:
    if maximum == max(dicomot[keys]):
        print(keys)

print("Le mot le plus utilisé par Chirac est : ")
maxi = 0
for el in liste_fichier:
    if 'Chirac' == el[11:-5]:
        with open('cleaned/' + el, 'r') as file:
            fichier = file.read()
            for keys in tf(fichier):
                if tf(fichier)[keys] > maxi and keys != '':
                    maxi = tf(fichier)[keys]
for el in liste_fichier:
    if 'Chirac' == el[11:-5]:
        with open('cleaned/' + el, 'r') as file:
            fichier = file.read()
            for keys in tf(fichier):
                if maxi == tf(fichier)[keys] and keys != '':
                    print(keys)
print("Les président ayant utilisé le mot 'nation' sont : ")
maxination = 0
presnation = 0
tabpres = []
for el in liste_fichier:
    with open('cleaned/' + el, 'r') as file:
        prestf = tf(file.read())
        nompres = re.sub(r'[0-9]', '', el)[11:-4]
        if "nation" in prestf.keys():
            if nompres not in tabpres:
                tabpres.append(nompres)
        for keys in prestf:
            if prestf[keys] > maxination:
                maxination = prestf[keys]
                presnation = re.sub(r'[0-9]', '', el)[11:-4]
for elem in tabpres:
    print(elem)
print("Le président ayant le plus utilisé le mot 'nation' est " + presnation)

print("Sakorzy est le premier président à parler d'écologie et de climat.")

dicouse = {}
for el in liste_fichier:
    with open('cleaned/' + el , 'r') as file:
        speech = file.read()
        for keys in tf(speech):
            if keys not in dicouse:
                dicouse[keys] = 1
            else:
                dicouse[keys] += 1
for keys in dicouse:
    if dicouse[keys] == len(liste_fichier) and keys not in motuse:
        print(keys)
