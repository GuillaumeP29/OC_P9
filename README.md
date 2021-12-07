# OC_P9
### *LITReview*

---


# 1. Description du programme
Application web Django de critiques littéraires.

---


# 2. Importer le projet depuis github
Veuillez taper la commande suivante dans votre console : " *git clone https://github.com/GuillaumeP29/OC_P9.git* ".

---


# 3. se rendre dans le dossier OC_P9
Veuillez taper la commande suivante dans votre console : " *cd OC_P9* ".

---


# 4. Créer l'environnement virtuel puis l'activer
#### Windows :
* Créer l'environnement virtuel avec la commande du terminal suivante : "python -m venv env".
* Activer l'environnement virutel depuis le terminal grâce à la commande suivante : "env/scripts/activate".
#### Unix :
* Créer l'environnement virtuel avec la commande du terminal suivante : "virtutalenv -p env venv".
* Activer l'environnement virutel depuis le terminal grâce à la commande suivante : "source env/bin/activate".

---


# 5. Installer et Initialiser le git
* Si vous n'avez pas encore git, cliquer sur le lien suivant : [Installer git](https://git-scm.com/downloads) et suivez les instructions du site.
* Initialiser ensuite le git avec la commande suivante dans votre console (assurez-vous que vous vous situez bien dans le dossier qui va contenir votre projet avant de lancer la commande): " *git init* " (Fonctionne pour Windows et Unix).

---


# 6. Installation les dépendances
Afin d'installer automatiquement tous les dépendences nécessaires au projet, dans le terminal, utilisez la commande suivante :
#### Windows :
" *pip install -r requirements.txt* "
#### Unix :
" *python3 -m pip install -r requirments.txt* "
---


# 7. Lancer le serveur
* Rendez-vous dans le dossier src du projet à l'aide de la commande : " *cd src* ".
* Lancer la commande suivante :
#### Windows :
" *python manage.py runserver* "
#### Unix :
" *python3 manage.py runserver* "

---


# 8. Accéder au site web
* Ouvrez le navigateur de votre choix.
* Dans l'URL, veuillez rentrer l'adresse du serveur indiquée dans la console lors du démarrage du serveur. Par exemple " *http://127.0.0.1:8000/* "

---


# 9. Générer le rapport d'erreur flake8
#### Installer flake8 :
Celui-ci a normalement déjà été installé grâce au fichier requirements.txt.
Cependant, si vous n'avez pas pu l'installer de cette manière, veuillez entrer la commande suivante dans votre console : " *pip install flake8* "
Un fichier .flake8 est inclus au projet afin de faciliter la création du rapport flake8. Il est tout de même possible de le supprimer ou le modifier pour personnaliser le rapport.
Pour fonctionner correctement, il faut également installer le plugin html de flake8 à l'aide de la commande : " *pip install flake8-html* "
#### Lancer le rapport d'erreur :
Entrez la commande suivante dans votre console :
" *flake8* "
Cette commande sera configurée automatiquement par le fichier .flake8 inclus au projet.

---