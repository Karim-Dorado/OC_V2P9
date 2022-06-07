# OC_V2P9 - Développez une application Web en utilisant Django

LITReview est une application codée avec le framework Django, elle utilise les langages :
- Python
- HTML
- CSS

Cette application permet à un utilisateur de :
- Se créer un compte
- Se connecter à son compte
- Créer un ticket permettant de demander des critiques de livres ou d’articles
- Publier des critiques de livres ou d’articles
- S'abonner/désabonner à d'autres d'utilisateurs


## 1. Récupérer le projet :

    $ git clone https://github.com/Karim-Dorado/OC_V2P9.git


## 2. Créer et activer un environnement virtuel :

    $ python3 -m venv env

Sous macOS ou Linux :

    $ env/bin/activate

Sous Windows :

    $ env\Scripts\activate.bat
    
    
## 3. Installer les dépendances :

    $ pip install -r requirements.txt

## 4. Lancer l'application :

    $ cd LITReview/
    $ py manage.py runserver

Le site sera accéssible via l'adresse local : 127.0.0.1:8000


Il existe 3 utilisateurs crées : "Toto", "Tata" et "Tutu". 
Mot de passe : 123

Vous pouvez vous connecter à l'interface d'administration via l'adresse suivante :  127.0.0.1:8000/admin
utilisateur : admin
Mot de passe "admin123"
