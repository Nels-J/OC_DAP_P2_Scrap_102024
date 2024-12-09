import csv
import os
from typing import Iterable, Dict


def create_books_informations_csv_file(filename: str, book_data: Iterable[Dict[str, str]]):

    # Stockage des infos du 1er livre généré pour définir les entêtes
    first_book = next(book_data)

    # Créer un dossier avec le nom de la catégorie
    dirname = os.path.splitext(filename)[0].upper()

    if not os.path.exists(dirname):
        os.makedirs(dirname)

    filepath = os.path.join(dirname, filename)

    with open(filepath, "w", newline='', encoding='utf-8') as csv_output_file:
        writer = csv.DictWriter(csv_output_file, fieldnames=first_book.keys())
        writer.writeheader()
        writer.writerow(first_book)
        yield first_book        # Renvoi afin de télécharger l'image du premier livre

        for book in book_data:
            writer.writerow(book)
            yield book      # Renvoi afin de télécharger les images des autres livres
