# Repo Manager
## C'est quoi ce projet ?
Ce projet est une API Django qui sert à plusieurs objectifs :
- Créer et gérer des repositories de code
- Ajouter des fichiers à un repository
- Rechercher des fichiers par nom, langage ou type
- Détecter les fichiers critiques automatiquement  
## Fichiers critiques
Un fichier est considéré critique si :
- Sa taille dépasse 1 Mo
- Son type est "config" (fichier de configuration)
- Son type est "security" (fichier de sécurité)
- Il n'y a pas de description.
## Les routes
- /api/repositories/ — lister tous les repositories
- /api/repositories/<id>/ — voir le détail d'un repository
- /api/files/ — créer un fichier
- /api/files/search/ — rechercher des fichiers
- /api/files/critical/ — voir les fichiers critiques
## Installation
1. Créer un environnement virtuel et l'activer :
python -m venv env
env\Scripts\activate
2. Installer les dépendances :
pip install django djangorestframework
3. Créer le projet et l'application :
django-admin startproject repo_manager .
python manage.py startapp repositories
4. Appliquer les migrations :
python manage.py migrate
5. Lancer le serveur :
python manage.py runserver

## Lancer les tests
python manage.py test