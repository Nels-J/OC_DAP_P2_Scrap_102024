import os

import requests

from booktoscrap.book import (
    get_book_infos,
    generate_all_book_urls_from_category_page,
)
from booktoscrap.category import (
    get_categories_from_home,
    list_product_page_links_from_category,
)
from booktoscrap.csv_generator import create_books_informations_csv_file


def scrapbooks(category_url, category_name):

    # Génère la liste des pages liées à chacune des catégories listées (pagination)
    for category_page in list_product_page_links_from_category(category_url):
        for book_url in generate_all_book_urls_from_category_page(category_page):
            book_info = get_book_infos(book_url)
            book_info["category_name"] = category_name
            yield book_info

def download_image(category_name, image_url, book_upc):
    # Ecrire ici le code pour svg les images. Nommage des fichiers category_name + UPC
        response= requests.get(image_url)

        # Isoler l'extension image dans l'url, puis reconstituer le nom
        file_extension = os.path.splitext(image_url)[-1].lower()
        filename = f"{category_name.lower()}_upc_{book_upc}{file_extension}"

        # Créer un dossier par catégorie
        dirname = f"{category_name.lower()}_books_images"
        if not os.path.exists(dirname):
            os.makedirs(dirname)

        file_path = os.path.join(dirname, filename)

        # Enregistrer l'image dans le dossier
        with open(file_path, 'wb') as file:
            file.write(response.content)

        print(f"Fichier image enregistrée sous: {file_path}")

if __name__ == "__main__":
    for category_name, category_url in get_categories_from_home(
        "https://books.toscrape.com/"
    ):
        category_books = scrapbooks(category_url, category_name)
        for book in create_books_informations_csv_file(f"{category_name}.csv", category_books):
            download_image(category_name=category_name, image_url=book['image_url'], book_upc=book['universal_product_code (upc)'] )
