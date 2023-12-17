from tf_idf_tfidf import *
from functions import *

p1 = input("Voulez-vous voir les réponses de la première partie ? Répondez simplement par oui ou non.")
if p1.lower() == 'oui':
    print(dico_pres(noms_fichier))
    discours(noms_fichier)
    liste_fichier = liste_fichiers('cleaned','txt')

    matrice = tfidf('cleaned')
    dicomot = idf('cleaned')
    compteur = 0
    motut = []
    for cles in dicomot:
        dicomot[cles] = matrice[compteur]
        compteur += 1
    for cles in dicomot:
        occurences = 0
        for el in dicomot[cles]:
            if float(el) == 0.0 :
                occurences += 1
        if occurences == len(liste_fichier):
            motut.append(cles)

    maximum = max(max(matrice))
    for cles in dicomot:
        if maximum == max(dicomot[cles]):
            print(cles)

    print("Le mot le plus utilisé par Chirac est : ")
    maxi = 0
    for el in liste_fichier:
        if 'Chirac' == el[11:-5]:
            with open('cleaned/' + el, 'r') as fichiers:
                fichier = fichiers.read()
                for cles in tf(fichier):
                    if tf(fichier)[cles] > maxi and cles != '':
                        maxi = tf(fichier)[cles]
    for el in liste_fichier:
        if 'Chirac' == el[11:-5]:
            with open('cleaned/' + el, 'r') as fichiers:
                fichier = fichiers.read()
                for cles in tf(fichier):
                    if maxi == tf(fichier)[cles] and cles != '':
                        print(cles)
    print("Les président ayant utilisé le mot 'nation' sont : ")
    maxination = 0
    presnation = 0
    tabpres = []
for el in liste_fichier:
    with open('cleaned/' + el, 'r') as fichiers:
        prestf = tf(fichiers.read())
        nompres = re.sub(r'[0-9]', '', el)[11:-4]
        if "nation" in prestf.cles():
            if nompres not in tabpres:
                tabpres.append(nompres)
        for cles in prestf:
            if prestf[cles] > maxination:
                maxination = prestf[cles]
                presnation = re.sub(r'[0-9]', '', el)[11:-4]
for el in tabpres:
    print(el)
print("Le président ayant le plus utilisé le mot 'nation' est " + presnation)

print("Sakorzy est le premier président à parler d'écologie et de climat.")

dicouse = {}
for el in liste_fichier:
    with open('cleaned/' + el , 'r') as file:
         speech = file.read()
         for cles in tf(speech):
            if cles not in dicouse:
                dicouse[cles] = 1
            else:
                dicouse[cles] += 1
for cles in dicouse:
    if dicouse[cles] == len(liste_fichier) and cles not in motut:
        print(cles)
