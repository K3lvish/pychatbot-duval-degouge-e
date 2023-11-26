# pychatbot-duval-degouge-e
Projet réalisé par Kelvish Duval et Quentin De Gouge.

Ce projet est constitué de 2 dossier : speeches contenant 8 fichiers composé chacun d'un discours de présidents et cleaned, vide au début. Il est également constitué de 3 fichiers python :

functions.py composé des fonctions suivantes :

- list_of_files(directory, extension) prend en paramètre un dossier pour directory et le type de fichier qu'il comporte pour extension. Elle renvoit une liste composée de chaque fichiers du type renseigné contenus dans le dossier. Le module os y est utilisé.
- dico_pres(tab) prend en paramètre une liste. Elle renvoit un dictionnaire contenant le nom des présidents en clé et leur prénom en valeur à paritr de la liste donnée. Le module re y est utilisé pour enlever les éventuels chiffres présents dans les éléments de la liste.
- assigner(nom) prend en paramètre une chaîne de caractères. Elle renvoit le prénom du Président en fonction du nom qui lui a été donné.
- polir(txt) prend en paramètre une chaîne de caractères. Elle renvoit la chaîne de caractère donnée tout en lui enlevant sa ponctuation.
- discours(tab) prend en paramètre une liste composée de chaînes de caractères. Elle enlève des chaînes de caractère compris dans tab la ponctuation de chaque élément et stocke ce nouveau texte dans le dossier "cleaned" dans un dossier portant le nom du président ayant fait le texte.

tfidf.py composé des fonctions suivantes :

- tf(car) prend en paramètre une chaîne de caractère. Elle renvoie un dictionnaire comportant en clé chaque mot contenu dans car et en valeur le nombre de fois où il est apparu dans ce texte.
- idf(rep) prend en paramètre le nom d'un dossier. Elle renvoie un dictionnaire comportant en clé chaque mot contenu dans chaque fichier et en valeur le log du nombre de fichiers contenus dans le dossier divisé par le nombre de dossier comportant ce mot ci. La fonction log du module math y est utilisé.
- tfidf(rep) prend en paramètre le nom d'un dossier. Elle renvoie une matrice qui a pour nombres de ligne le nombre de mots différents présents dans chaque fichier du dossier et qui a pour nombre de colonnes le nombre de fichiers du dossier. Chaque élément de la matrice représente le score tf multiplié par le score idf d'un mot selon son document.

main.py composé d'instructions permettant d'utiliser concrètement les fonctions ci-dessus.

Le programme principal utilise les fonctions citées ci-dessus afin de créer dans le dossier "cleaned" des fichiers composés d'un discours de président duquel on a enlevé la ponctuation et mit toutes les lettres en miniscule et de créer un dictionnaire rempli du nom des présidents en clé et leur prénom en valeur.

Il permet également d'utiliser les discours de chaque président pour
- afficher la liste des mots les moins importants (= les moins utilisés),
- afficher les mots avec le score TF-IDF le plus élevé (= les mots les plus fréquents et utiles dans le texte),
- indiquer le(s) mot(s) le(s) plus utilisé(s) par le Président Chirac,
- indiquer le(s) nom(s) du(des) président(s) utilisant le mot "nation" et celui qui le fait le plus fréquemment,
- le nom du Président parlant d'écologie et/ou de climat en premier,
- les mots évoqués par tous les présidents ne figurant pas dans la liste des mots les moins importants.
