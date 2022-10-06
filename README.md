L'objectif de ce projet est d'extraire des informations. Nous devons récupérer diverses informations issues du site     "http://books.toscrape.com/" qui vend des livres. Les informations à extraire sont entre autres : l'URL des différentes catégories de livres, les livres associés ainsi que les informations associées au livre. (images, prix, auteur, description....)
Il faut également créer un fichier csv dans lequel il faudra inscrire les informations issues du site web. Puis également extraire et stocker les images des livres.




# Installer :




## Cloner le référentiel :

`git clone https://github.com/boukaii/p2-scraping_books.git`






## Déplacer vers le nouveau dossier

`cd p2-scraping_books`




## Créez l'environnement virtuel :


Maintenant créez l'environnement virtuel en tapant cette commande :

`python -m venv env`


## Activez l'environnement virtuel :

Pour macOS et Linux:  `env/bin/activate`

Pour Windows:  `env\Scripts\activate`


## Installez les packages :

`pip install -r requirements.txt`


# Script :


## Lancer le script :

`Python scrap_all_categories.py`




## Voici a quoi correspond le contenu du script:



`scrap_all_categories.py :` 
  Ce script récupère toutes les informations et les images de tous les livres de toutes les catégories.


# Configuration :



## Fichiers CSV :

Pour ouvrir correctement les fichiers CSV, veillez à bien configurer les options suivantes:

- Encodage UTF-8

- `virgule` comme séparateur
