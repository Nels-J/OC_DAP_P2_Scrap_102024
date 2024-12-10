from booktoscrap.book import (
    get_book_infos,
    generate_all_book_urls_from_category_page,
)
from booktoscrap.category import (
    get_categories_from_home,
    list_product_page_links_from_category,
)
from booktoscrap.csv_generator import (
    create_books_informations_csv_file,
    create_directory,
)
from booktoscrap.img_downloader import download_image


def scrapbooks(category_url: str, category_name: str):

    # Génère la liste des pages liées à chacune des catégories listées (pagination)
    for category_page in list_product_page_links_from_category(category_url):
        for book_url in generate_all_book_urls_from_category_page(category_page):
            book_info = get_book_infos(book_url)
            book_info["category_name"] = category_name
            yield book_info


if __name__ == "__main__":
    for category_name, category_url in get_categories_from_home(
        "https://books.toscrape.com/"
    ):
        category_dir = create_directory(category_name)
        category_books = scrapbooks(category_url, category_name)

        for book in create_books_informations_csv_file(
                filename=f"{category_dir}/{category_name}.csv",
                book_data=category_books
        ):
            download_image(
                category_dir=category_dir,
                category_name=category_name,
                image_url=book['image_url'],
                book_upc=book['universal_product_code (upc)']
            )
