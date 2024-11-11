import csv
from typing import Iterable


def create_books_informations_csv_file(filename: str, book_data: Iterable):

    fieldnames = [
        "Title",
        "Rating",
        "Availability",
        "Number of reviews",
        "Price (excl. tax)",
        "Price (incl. tax)",
        "Tax",
        "Product Type",
        "UPC",
        "Picture"
    ]

    with open(filename, "w") as csv_output_file:
        writer = csv.DictWriter(csv_output_file, fieldnames=fieldnames)

        # Écrire l'en-tête
        writer.writeheader()

        # Écrire les données des livres
        for book in book_data:
            writer.writerow(book)
