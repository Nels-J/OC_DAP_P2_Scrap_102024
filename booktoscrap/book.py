from urllib.parse import urljoin

from booktoscrap.connection import get_soup


def get_book_informations(book_url: str) -> dict[str, str]:
    """
    Take a book url and return a dictionary of book information.

    Args:
        book_url: e.g. 'https://books.toscrape.com/catalogue/booktitle/index.html'

    Returns:
        book_informations: A dictionary of book information.
    """
    soup = get_soup(book_url)
    table = soup.find("table", class_="table table-striped")
    book_informations = {}
    for row in table.find_all("tr"):
        key = row.find("th").text.strip()
        value = row.find("td").text.strip()
        if "Price" or "Tax" in key:
            value = value.replace("Â£", "£").strip()
        book_informations[key] = value
    return book_informations


def generate_all_book_urls_from_category_page(category_page_url: str) -> list:
    """
        Take a category page url string to scrap all books url from that page.

    Args:
        category_page_url: e.g 'https://books.toscrape.com/catalogue/category/books/mystery_3/index.html'

    Yields:
        List of book urls found in the given category_page_url.

    """
    soup = get_soup(category_page_url)
    books_url = soup.select("article.product_pod h3>a")

    for link in books_url:
        href = link["href"].lstrip("../")
        full_url = urljoin("https://books.toscrape.com/catalogue/", href)
        yield full_url


if __name__ == "__main__":
    print(
        get_book_informations(
            "https://books.toscrape.com/catalogue/sorting-the-beef-from-the-bull-the-science-of-food-fraud-forensics_736/index.html"
        )
    )
    for book in generate_all_book_urls_from_category_page(
        "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
    ):
        print(book)
