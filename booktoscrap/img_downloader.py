import os

import requests


def download_image(category_name, image_url, book_upc):
        response = requests.get(image_url)

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