import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import urllib
import csv


# 1/ fonction avec tout les liens de toutes les catégories
def full_liens_category():
    # création de la liste des url
    categories = []
    # lien du site
    url = "http://books.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    liens = soup.find_all("ul", attrs={"class": "nav nav-list"})
    for lien in liens:
        partie = lien.find("li").find_all("a")
        for b in partie:
            if b["href"] != "catalogue/category/books_1/index.html":
                lien_relatif = b["href"]
                # additioner url et lien_relatif afin d'obtenir un lien URL complet
                lien_entier = urllib.parse.urljoin(url, lien_relatif)
                categories.append(lien_entier)

    return categories


# 2/ fonction avec tout les liens des livres
def full_liens_book(url_categorie):
    # création liste des urls des livres
    list_urls = []
    response = requests.get(url_categorie)
    soup = BeautifulSoup(response.text, "lxml")
    titre_categorie = soup.find_all("h1")[0].get_text()
    liens = soup.find_all("div", class_="image_container")
    for lien in liens:
        lien_relatif = lien.a['href']
        # additioner url et lien_relatif afin d'obtenir un lien URL complet
        lien_entier = urllib.parse.urljoin(url_categorie, lien_relatif)
        list_urls.append(lien_entier)

    return list_urls, titre_categorie


# 3/ fonction avec toutes les informations + csv images
def full_informations_book(url_book):
    list_informations = []
    response = requests.get(url_book)
    if response.ok:
        soup = BeautifulSoup(response.content, "html.parser")
        soup.encode("utf-8")
        universal_product_code = soup.find_all("tr")[0].td.get_text()
        title = soup.find_all("h1")[0].get_text()
        titles = title.replace(":", " ").replace("*", " ").replace("?", " ").replace(",", " ")\
            .replace("/", " ").replace(".", " ")\
            .replace("<", " ").replace(">", " ")\
            .replace('\"', ' ').replace("\'", " ")
        price_including_tax = soup.find_all("tr")[3].td.contents[0]
        price_excluding_tax = soup.find_all("tr")[2].td.get_text()
        number_available = soup.find_all("tr")[5].td.get_text()
        product_description = soup.find_all("p")[3].get_text()
        product_descriptions = product_description.replace(":", " ").replace("*", " ").replace("?", " ") \
            .replace('\"', " ").replace(",", " ").replace("/", " ").replace(".", " ").replace("-", " ")
        categorie = soup.find_all("a")[3].get_text()
        # review_rating = soup.find_all("tr")[6].td.get_text()
        review_rating = soup.select_one('.star-rating').attrs['class'][1]
        images = soup.find_all("img")[0]
        src = images.get('src')
        image_url_entier = urllib.parse.urljoin(url_book, src)
        img = requests.get(image_url_entier).content

        with open("images/" + categorie + " " + titles + ".jpg", 'wb') as f:
            f.write(img)

        list_informations = [
            url_book,
            universal_product_code,
            titles,
            price_including_tax,
            price_excluding_tax,
            number_available,
            product_descriptions,
            categorie,
            review_rating,
            image_url_entier
        ]

    return list_informations


# 4/ fonction pagination
def pagination():
    # création liste vide qui aura comme contenue les urls avec pagination
    pagination_list = []
    # boucle qui permet de récupérer tout les liens de toutes les catégories avec pagin et sans
    for categorie in categories:
        response = requests.get(categorie)
        soup = BeautifulSoup(response.text, "lxml")
        # condition: SI il y a le "text" page sur la page
        if soup.find("li", class_="current"):
            next_page = soup.find("li", class_="current").text.strip()
            # variable qui récupère le dernier élèment de la chaine de caractère qui permet de savoir le nb de pages total
            nb_page = next_page[len(next_page)-1]
            # création des liens pour chaque page de la catégorie en cours(catégorie avec pagination)
            for i in range(1, int(nb_page)+1):
                pagination_list.append(categorie.replace("index.html", "page-"+str(i)+".html"))
        # si pas de pagination
        else:
            pagination_list.append(categorie)

    return pagination_list


# 5/ fonction Boucle + CSV
def get_datas_book():
    for category in pagination_lists:
        list_urls, titre_categorie = full_liens_book(category)
        print()
        print(category)
        # CSV pour en_tete
        en_tete = ["liens", "universal_product_code", "title", "price_including_tax", "price_excluding_tax",
                   "number_available", "product_description", "category", "review_rating", "image_url"]
        chemin_fichier = "csv/" + titre_categorie + ".csv"
        if not os.path.exists(chemin_fichier):
            with open(chemin_fichier, 'w', encoding="utf-8", newline='') as csv_file:
                writer = csv.writer(csv_file, delimiter=",")
                writer.writerow(en_tete)
        # boucle sur tout les liens des livres
        for url in list_urls:
            list_informations = full_informations_book(url)
            print(list_informations)
           # CSV pour les informations des livres pour chaque catégorie
            with open(chemin_fichier, 'a', encoding="utf-8", newline='') as csv_file:
                writer = csv.writer(csv_file, delimiter=",")
                writer.writerow(list_informations)


categories = full_liens_category()
pagination_lists = pagination()
get_datas_book()
