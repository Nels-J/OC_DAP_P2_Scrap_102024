import csv
import time


def create_books_informations_csv_file(filename: str, fieldnames: list[str], book_data: list[dict[str, str]]):
    start_time = time.time()
    with open(filename, 'w') as csv_output_file:
        writer = csv.DictWriter(csv_output_file, fieldnames=fieldnames)

        # Écrire l'en-tête
        writer.writeheader()

        # Écrire les données des livres
        for book in book_data:
            writer.writerow(book)

    end_time = time.time()
    print(f"Temps d'écriture : {end_time - start_time} secondes")

if __name__ == '__main__':
    pass