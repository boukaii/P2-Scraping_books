import requests
from bs4 import BeautifulSoup


url = "http://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html"

response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")


list_informations = []

universal_product_code = soup.find_all("tr")[0].td.get_text()
title = soup.find_all("h1")[0].get_text()

price_including_tax = soup.find_all("tr")[3].td.get_text()
price_excluding_tax = soup.find_all("tr")[2].td.get_text()
number_available = soup.find_all("tr")[5].td.get_text()
product_description = soup.find_all("p")[3].get_text()
category = soup.find_all("a")[3].get_text()
review_rating = soup.find_all("tr")[6].td.get_text()

images = soup.find_all("img")[0]
src = images.get('src')
image_url_entier = requests.compat.urljoin(url, src)


informations = [universal_product_code, title, price_including_tax, price_excluding_tax, number_available,
                product_description, category, review_rating, image_url_entier]

list_informations.append(informations)
print(list_informations)


