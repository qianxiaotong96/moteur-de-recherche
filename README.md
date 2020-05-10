# moteur-de-recherche
# installation nécessaire
pip3 install Flask

# avant d'exécuter il faut mettre tous les fichiers du projet dans un même répertoire(celui de la partie qualité et index_inversé)
# ensuite il faut changer le "import" en haut du fichier "server.py" en incluant le fichier index_inverse.py
# exécuter le serveur en utilisant
python server.py

# puis lancer un navigateur et saisir 
"http://127.0.0.1:5000/"

# cliquer le bouton"Valider" sans mot-clef, il renvoie la pageA
# entrer le mot-clef, et cliquer le bouton"Valider", il renvoie la pageB

# pour tester j'ajoute un fichier test.py qui renvoie tous les pages du répertoire pages_web dans pageB
# le but c'est juste montrer l'affichage du pageB et interaction entre la pageA et la pageB
# pour tester il faut mettre le répertoire pages_web et test.py dans un même répertoire ainsi que pageA.html et pageB.html  
python test.py
# puis lancer un navigateur et saisir 
"http://127.0.0.1:5000/"
