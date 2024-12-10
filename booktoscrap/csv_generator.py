import csv
import os
from typing import Iterable, Dict

def create_directory(category_name: str) -> str:
    """

        Check if path and directory already exist, if not it will be created

    Args:
        category_name: A given name for the directory to create

    Returns:
        A simple print confirmation of the creating process

    """

    # check if main directory path exist
    if not os.path.exists("Export"):
        os.makedirs("Export")

    # check if dedicated path exist
    if not os.path.exists(f"Export/{category_name}"):
        os.makedirs(f"Export/{category_name}")

    return f"Export/{category_name}"

def create_books_informations_csv_file(filename: str, book_data: Iterable[Dict[str, str]]):

    # Stockage des infos du 1er livre généré pour définir les entêtes
    first_book = next(book_data)

    with open(filename, "w", newline='', encoding='utf-8') as csv_output_file:
        writer = csv.DictWriter(csv_output_file, fieldnames=first_book.keys())
        writer.writeheader()
        writer.writerow(first_book)
        yield first_book        # Renvoi afin de télécharger l'image du premier livre

        for book in book_data:
            writer.writerow(book)
            yield book      # Renvoi afin de télécharger les images des autres livres
