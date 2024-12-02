import csv
from typing import Iterable

# TODO voir la gestion génerateur gpt dans old csv generator


def create_books_informations_csv_file(filename: str, book_data: Iterable[Tuple(str, str)]):
    # book_data tel que généré par book.py
    # {
    #     'title': 'In a Dark, Dark Wood',
    #     'product_page_url': 'https://books.toscrape.com/catalogue/in-a-dark-dark-wood_963/index.html',
    #     'category': 'Mystery',
    #     'review_rating': 1,
    #     'image_url': 'https://books.toscrape.com/media/cache/95/84/95840dfd67c020067c99d70451147e20.jpg',
    #     'product_description': "In a dark, dark wood Nora hasn't seen Clare for ten years. Not since Nora walked out of school one day and never went back. There was a dark, dark houseUntil, out of the blue, an invitation to Clare’s hen do arrives. Is this a chance for Nora to finally put her past behind her?And in the dark, dark house there was a dark, dark roomBut something goes wrong. Very wrong.And i In a dark, dark wood Nora hasn't seen Clare for ten years. Not since Nora walked out of school one day and never went back. There was a dark, dark houseUntil, out of the blue, an invitation to Clare’s hen do arrives. Is this a chance for Nora to finally put her past behind her?And in the dark, dark house there was a dark, dark roomBut something goes wrong. Very wrong.And in the dark, dark room.... Some things can’t stay secret for ever. ...more",
    #     'universal_product_code': '19ed25f4641d5efd',
    #     'price_excluding_tax': '£19.63',
    #     'price_including_tax': '£19.63',
    #     'number_available': 18
    # }

    new_headers = {
        'product_page_url': 'product_page_url',
        'universal_product_code': 'universal_product_code (upc)',  # Changement pour correspondre à la clé du book_data
        'title': 'title',
        'price_including_tax': 'Price (incl. tax)',  # Correspondance avec book_data
        'price_excluding_tax': 'Price (excl. tax)',  # Correspondance avec book_data
        'number_available': 'Availability',  # Correspondance avec book_data
        'product_description': 'product_description',
        'category': 'category',
        'review_rating': 'review_rating',
        'image_url': 'image_url',
    }

    # new_fieldnames = [new_headers[key] for key in book_data[0].keys() if key in new_headers]

    # fieldnames = [
    #     "title",
    #     "review_rating",
    #     "Availability",
    #     "Number of reviews",
    #     "Price (excl. tax)",
    #     "Price (incl. tax)",
    #     "Tax",
    #     "Product Type",
    #     "UPC",
    #     "image_url"
    # ]

    if book_data:
        # On suppose que book_data[0] est un dictionnaire
        print(f"LE TYPE DE BOOK DATAT EST {type(book_data)}")
        new_fieldnames = [new_headers[key] for key in book_data[0].keys() if key in new_headers]

    with open(filename, "w", encoding='utf-8') as csv_output_file:
        writer = csv.DictWriter(csv_output_file, fieldnames=new_fieldnames)

        # Écrire l'en-tête
        writer.writeheader()

        # Écrire les données des livres
        for book in book_data:
            renamed_lines = {new_headers[key]: value for key, value in book.items() if key in new_headers}
            writer.writerow(renamed_lines)
            #writer.writerow(book)
