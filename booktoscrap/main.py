from booktoscrap.book import get_book_informations, generate_all_book_urls_from_category_page
from booktoscrap.category import get_categories_from_home, list_product_page_links_from_category

if __name__ == '__main__':
    # Récupère dans la page d'accueil les catégories et leurs liens
    for category_name, category_url in get_categories_from_home('https://books.toscrape.com/'):
        # Génère la liste des pages liées à chacune des catégories listées (pagination)
        for category_page in list_product_page_links_from_category(category_url):
            # Pour chacune des pages, liste les liens url des livres
            for book_url in generate_all_book_urls_from_category_page(category_page):
                # Pour chaque livre récupère la grille d'informations
                book_info = get_book_informations(book_url)
                print(book_info)