import os

import requests


def download_image(
        category_dir: str,
        category_name: str,
        image_url: str,
        book_upc: str
):
    response = requests.get(image_url)

    # Isoler l'extension image dans l'url, puis reconstituer le nom
    file_extension = os.path.splitext(image_url)[-1].lower()
    filename = f"{category_dir}/{category_name}_upc_{book_upc}{file_extension}"

    with open(filename, 'wb') as file:
        file.write(response.content)

    print(f"Fichier image enregistrée sous: {filename}")
