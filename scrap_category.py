import requests
from bs4 import BeautifulSoup
import urllib.parse
import csv
import urllib




# fonction liens
def lien_pagination():
    for page in range(1, 7):
        # URL de la catégorie + les pages paginations
        url = "http://books.toscrape.com/catalogue/category/books/nonfiction_13/page-" + str(page) + ".html"
        response = requests.get(url)
        # création de la liste de toutes les urls
        list_urls = []
        soup = BeautifulSoup(response.text, "lxml")
        liens = soup.find_all("div", class_="image_container")
        # boucle
        for lien in liens:
            lien_relatif = lien.a['href']
            # additioner url et lien_relatif afin d'obtenir un lien URL complet
            lien_entier = urllib.parse.urljoin(url, lien_relatif)
            list_urls.append(lien_entier)
        return list_urls
list_urls = lien_pagination()


# fonction informations livres
def informations_book():
    for page in range(1, 7):
        # URL de la catégorie + les pages paginations
        url = "http://books.toscrape.com/catalogue/category/books/nonfiction_13/page-" + str(page) + ".html"
        response = requests.get(url)
        # création de la liste de toutes les urls
        list_urls = []
        soup = BeautifulSoup(response.text, "lxml")
        liens = soup.find_all("div", class_="image_container")
        # boucle
        for lien in liens:
            lien_relatif = lien.a['href']
            # additioner url et lien_relatif afin d'obtenir un lien URL complet
            lien_entier = urllib.parse.urljoin(url, lien_relatif)
            list_urls.append(lien_entier)
        print(list_urls)
        for url in list_urls:
            list_informations = []
            response = requests.get(url)
            if response.ok:
                soup = BeautifulSoup(response.text, "lxml")
                universal_product_code = soup.find_all("tr")[0].td.get_text()
                title = soup.find_all("h1")[0].get_text()
                price_including_tax = soup.find_all("tr")[3].td.get_text()
                price_excluding_tax = soup.find_all("tr")[2].td.get_text()
                number_available = soup.find_all("tr")[5].td.get_text()
                product_description = soup.find_all("p")[3].get_text()
                category = soup.find_all("a")[3].get_text()
                review_rating = soup.find_all("tr")[6].td.get_text()
                image_url = soup.find_all("img")[0]
                informations = [universal_product_code, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url]
                list_informations.append(informations)
            print(list_informations)
    return list_informations
list_informations = informations_book()


# fonction image
def image_categorie():
    for page in range(1, 7):
    # URL de la catégorie + les pages paginations
        url = "http://books.toscrape.com/catalogue/category/books/nonfiction_13/page-" + str(page) + ".html"
        response = requests.get(url)
        if response.ok:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, "html.parser")
            images = soup.find_all("img")
            list_images = []
            for image in images:
                src = image.get("src")
                list_images.append(requests.compat.urljoin(url, src))
            print(list_images)
    return list_images
list_images = image_categorie()


def fichier_csv():
    en_tete = ["universal_product_code", "title", "price_including_tax", "price_excluding_tax", "number_available", "product_description", "category", "review_rating", "image_url"]
    with open("test.csv", "w", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file, delimiter=",")
        writer.writerow(en_tete)
        for page in range(1, 7):
            url = "http://books.toscrape.com/catalogue/category/books/nonfiction_13/page-" + str(page) + ".html"
            response = requests.get(url)
            list_urls = []
            soup = BeautifulSoup(response.text, "lxml")
            liens = soup.find_all("div", class_="image_container")
            for lien in liens:
                lien_relatif = lien.a['href']
                lien_entier = urllib.parse.urljoin(url, lien_relatif)
                list_urls.append(lien_entier)
            writer.writerow(list_urls)
            for url in list_urls:
                list_informations = []
                response = requests.get(url)
                if response.ok:
                    soup = BeautifulSoup(response.text, "lxml")
                    universal_product_code = soup.find_all("tr")[0].td.get_text()
                    title = soup.find_all("h1")[0].get_text()
                    price_including_tax = soup.find_all("tr")[3].td.get_text()
                    price_excluding_tax = soup.find_all("tr")[2].td.get_text()
                    number_available = soup.find_all("tr")[5].td.get_text()
                    product_description = soup.find_all("p")[3].get_text()
                    category = soup.find_all("a")[3].get_text()
                    review_rating = soup.find_all("tr")[6].td.get_text()
                    image_url = soup.find_all("img")[0]
                    informations = [universal_product_code, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url]
                    list_informations.append(informations)
                writer.writerow(list_informations)
fichier_csv()




