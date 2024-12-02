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
        # Pour chacune des pages, liste les liens url des livres
        for book_url in generate_all_book_urls_from_category_page(category_page):
            # Pour chaque livre récupère la grille d'informations
            book_info = get_book_infos(book_url)
            book_info["category_name"] = category_name
            yield book_info


if __name__ == "__main__":
    for category_name, category_url in get_categories_from_home(
        "https://books.toscrape.com/"
    ):
        category_books = scrapbooks(category_url, category_name)
        create_books_informations_csv_file(f"{category_name}.csv", category_books)
