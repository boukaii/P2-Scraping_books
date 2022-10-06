L'objectif du projet est de collecter des informations concernant les livres en vente sur le site  "http://books.toscrape.com/" et de les mettre dans un fichier CSV.



La même chose devrait être faite pour l'image de chaque livre.



# Installer :


## Cloner le référentiel :

`git clone https://github.com/boukaii/p2-scraping_books.git`


## Créez l'environnement virtuel :

`cd p2-scraping_books`

`python -m venv env`


## Activez l'environnement virtuel :

Pour macOS et Linux:  `env/bin/activate`

Pour Windows:  `env\Scripts\activate`


## Installez les packages :

`pip install -r requirements.txt`




## Voici a quoi correspond le contenu du script:



`scrap_all_categories.py :` 
  Ce script récupère toutes les informations et les images de tous les livres de toutes les catégories.



## Fichiers CSV :

Pour ouvrir correctement les fichiers CSV, veillez à bien configurer les options suivantes:

- Encodage UTF-8

- `virgule` comme séparateur