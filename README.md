# pychatbot-duval-degouge-e
Projet réalisé par Kelvish Duval et Quentin De Gouge.

Ce projet est constitué de 2 dossier : speeches contenant 8 fichiers composé chacun d'un discours de présidents et cleaned, vide au début. Il est également constitué de 4 fichiers python :

functions.py composé des fonctions suivantes :

- list_of_files(directory, extension) prend en paramètre un dossier pour directory et le type de fichier qu'il comporte pour extension. Elle renvoit une liste composée de chaque fichiers du type renseigné contenus dans le dossier. Le module os y est utilisé.
- dico_pres(tab) prend en paramètre une liste. Elle renvoit un dictionnaire contenant le nom des présidents en clé et leur prénom en valeur à paritr de la liste donnée. Le module re y est utilisé pour enlever les éventuels chiffres présents dans les éléments de la liste.
- assigner(nom) prend en paramètre une chaîne de caractères. Elle renvoit le prénom du Président en fonction du nom qui lui a été donné.
- polir(txt) prend en paramètre une chaîne de caractères. Elle renvoit la chaîne de caractère donnée tout en lui enlevant sa ponctuation.
- discours(tab) prend en paramètre une liste composée de chaînes de caractères. Elle enlève des chaînes de caractère compris dans tab la ponctuation de chaque élément et stocke ce nouveau texte dans le dossier "cleaned" dans un dossier portant le nom du président ayant fait le texte.

tf_idf_tfidf.py composé des fonctions suivantes :

- tf(car) prend en paramètre une chaîne de caractère. Elle renvoie un dictionnaire comportant en clé chaque mot contenu dans car et en valeur le nombre de fois où il est apparu dans ce texte.
- idf(rep) prend en paramètre le nom d'un dossier. Elle renvoie un dictionnaire comportant en clé chaque mot contenu dans chaque fichier et en valeur le log du nombre de fichiers contenus dans le dossier divisé par le nombre de dossier comportant ce mot ci. La fonction log du module math y est utilisé.
- tfidf(rep) prend en paramètre le nom d'un dossier. Elle renvoie une matrice qui a pour nombres de ligne le nombre de mots différents présents dans chaque fichier du dossier et qui a pour nombre de colonnes le nombre de fichiers du dossier. Chaque élément de la matrice représente le score tf multiplié par le score idf d'un mot selon son document.

functions_partie2.py composé des fonctions suivantes:
- token(car) prend en paramètre une chaîne de caractère. Elle renvoie la liste des mots qui la composent sans les espaces.
- recherche(quest, dico) prend en paramètre une chaîne de caractère et un dictionnaire. Elle renvoit la liste des mots présents à la fois dans la question et le dictionnaire.
- vecteur(quest) prend en paramètre une chaîne de caractère. Elle renvoit une liste composée des scores tfidf des mots du corpus de documents en fonction du score tf de la chaîne de caractère.
- dictionnaire(quest) prend en paramètre une chaîne de caractère. Elle fait la même chose que la fonction précédente mais renvoit les renvoit sous forme de dictionnaire ayant pour clé le mot et pour valeur le socre tfidf.
- produit_scal(A, B) prend en paramètre deux listes. Elle calcule le produit scalaire des vecteurs représentant ces listes.
- norme(vecteur) prend en paramètre une liste. Elle renvoit la norme du vecteur représentant cette liste.
- similaire(A, B) prend en paramètre deux listes. Elle renvoit l'écart entre les vecteurs représentant les deux listes.
- comparer(vec, tabnom) prend en paramètre deux listes. Elle renvoit la chaîne de caractère de la liste tabnom dont le vecteur tfidf du fichier est le plus proche de celui de celle pris en paramètre.
- tfidf_max(quest) prend en paramètre une chaîne de caractère. Elle renvoit le mot de la chaîne de caractère possédant le score tfidf le plus élevé.
- réponse(quest): prend en paramètre une question. Elle renvoit la première phrase comportant le mot de la chaîne de caractère avec le score tfidf le plus élevé.

main.py composé d'instructions permettant d'utiliser concrètement les fonctions ci-dessus.


Le programme principal demande tout d'abord à l'utilisateur s'il veut accéder aux réponses de la première partie du projet à savoir celles permettant de:
- remplir le fichier "cleaned" de discours de président desquels on a enlevé la ponctuation et mit toutes les lettres en miniscule,
- créer un dictionnaire rempli du nom des présidents en clé et leur prénom en valeur.
- afficher la liste des mots les moins importants (= les moins utilisés),
- afficher les mots avec le score TF-IDF le plus élevé (= les mots les plus fréquents et utiles dans le texte),
- indiquer le(s) mot(s) le(s) plus utilisé(s) par le Président Chirac,
- indiquer le(s) nom(s) du(des) président(s) utilisant le mot "nation" et celui qui le fait le plus fréquemment,
- le nom du Président parlant d'écologie et/ou de climat en premier,
- les mots évoqués par tous les présidents ne figurant pas dans la liste des mots les moins importants.

Si l'utilisateur répond oui, alors chacune des fonctions énoncées ci-dessus seront effectués.
S'il répond non, il pourra alors directement poser sa question au chatbot et recevoir sa réponse. A noter que la question du chatbot se pose également s'il répond oui.
