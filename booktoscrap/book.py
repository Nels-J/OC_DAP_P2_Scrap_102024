import re
from urllib.parse import urljoin

from booktoscrap.category import BASE_CATALOGUE_URL
from booktoscrap.connection import get_soup


def get_book_infos(book_url: str) -> dict[str, str]:
    """
    Take a book url and return a dictionary of book information.

    Args:
        book_url: e.g. '{BASE_CATALOGUE_URL}booktitle/index.html'

    Returns:
        book_informations: A dictionary of book information.
    """
    soup = get_soup(book_url)

    # On récupère le titre du livre qu'on ajoute à notre dictionnaire.
    book_informations = {"Title": soup.find("h1").text.strip()}

    # On récupère la classe représentant la note des lecteurs.
    star_rating = soup.find("p", class_="star-rating")
    if star_rating:
        # On liste les classes présentes dans le tag,
        # puis on extrait la classe additionnelle différente de 'star-rating'
        class_list = star_rating.get("class")
        additional_class = [cls for cls in class_list if cls != "star-rating"][0]
        # Transformation de la classe en 'nombre' pour faciliter l'exploitation.
        rating_dict = {"One": "1", "Two": "2", "Three": "3", "Four": "4", "Five": "5"}
        rating_value = rating_dict.get(additional_class, 0)  # Si non défini 0.
        # On ajoute cette note à notre dictionnaire
        book_informations["Rating"] = rating_value

    # On récupère les informations du livre présentes dans un tableau.
    table = soup.find("table", class_="table table-striped")
    for row in table.find_all("tr"):
        key = row.find("th").text.strip()
        value = row.find("td").text.strip()

        # On nettoie l'interprétation monétaire.
        if "Price" or "Tax" in key:
            value = value.replace("Â£", "£").strip()
            # On ajoute les infos au dictionnaire.
            book_informations[key] = value

        # On extrait que la quantité en stock et non le message.
        if "Availability" in key:
            match = re.search(r"\((\d+)\s+available\)", value)
            if match:
                book_informations[key] = match.group(1)

    return book_informations


# TODO get img_url


def generate_all_book_urls_from_category_page(category_page_url: str) -> list:
    """
        Take a category page url string to scrap all books url from that page.

    Args:
        category_page_url:
            e.g '{BASE_CATALOGUE_URL}category/books/mystery_3/index.html'

    Yields:
        List of book urls found in the given category_page_url.

    """
    soup = get_soup(category_page_url)
    books_url = soup.select("article.product_pod h3>a")

    for link in books_url:
        href = link["href"].lstrip("../")
        full_url = urljoin(f"{BASE_CATALOGUE_URL}", href)
        yield full_url


if __name__ == "__main__":
    print(get_book_infos(f"{BASE_CATALOGUE_URL}in-a-dark-dark-wood_963/index.html"))
    for book in generate_all_book_urls_from_category_page(
        f"{BASE_CATALOGUE_URL}category/books/mystery_3/index.html"
    ):
        print(book)
