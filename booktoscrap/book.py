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

    # On récupère le titre du livre son URL qu'on ajoute à notre dictionnaire.
    book_informations = {"title": soup.find("h1").text.strip(), "product_page_url": book_url}

    # On récupère la catégorie du livre qu'on ajoute à notre dictionnaire.
    book_category = soup.find('ul', class_='breadcrumb')
    breadcrumb_links = book_category.find_all('a')
    if breadcrumb_links:
        last_breadcrumb_link = breadcrumb_links[-1].get_text()
        book_informations["category"] = last_breadcrumb_link
    else:
        book_informations["category"] = "Undefined category"

    # On récupère la classe représentant la note des lecteurs.
    star_rating = soup.find("p", class_="star-rating")
    if star_rating:
        # On liste les classes présentes dans le tag,
        # puis on extrait la classe additionnelle différente de 'star-rating'
        class_list = star_rating.get("class")
        additional_class = [cls for cls in class_list if cls != "star-rating"][0]
        # Transformation de la classe en 'nombre entier' pour faciliter l'exploitation.
        rating_dict = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
        rating_value = rating_dict.get(additional_class, 0)  # Si non défini 0.
        # On ajoute cette note à notre dictionnaire
        book_informations["review_rating"] = rating_value

    # On récupère le lien relatif de l'image du livre, qu'on transforme en absolu.
    active_item = soup.find("div", class_="item active")
    base_url = BASE_CATALOGUE_URL[:-10]
    img_url = urljoin(base_url, active_item.find("img").attrs["src"])
    book_informations["image_url"] = img_url

    # On récupère la description produit.
    product_description = soup.select('#product_description + p')
    if product_description:
        book_informations["product_description"] = product_description[0].get_text()
    else:
        book_informations["product_description"] = "Unavailable description"


    # On récupère les informations du livre présentes dans le tableau.
    table = soup.find("table", class_="table table-striped")

    book_table_headers = {
        'UPC': 'universal_product_code (upc)',
        'Price (incl. tax)': 'price_including_tax',
        'Price (excl. tax)': 'price_excluding_tax',
        'Availability': 'number_available',
    }

    for row in table.find_all("tr"):
        key = row.find("th").text.strip()
        value = row.find("td").text.strip()
        if key not in book_table_headers:
            continue

        # On extrait la quantité dans un texte 'In stock (18 available)'
        elif key == "Availability":
            regex_pattern = r"""
                \(              # on récupère à partir de la parenthèse ouvrante
                (\d+)           # un ou plusieurs Digit qui seront
                \s+             # suivis d'un ou plusieurs eSpaces blancs
                available       # et du mot available
                \)              # on arrête la regex dès la parenthèse fermante
            """
            # L'emploi de verbose m'a permis de détailler la regex ci-dessus
            match = re.search(regex_pattern, value, re.VERBOSE)
            if match:
                value = int(match.group(1)) # groupe 0 est égal à la string entière

        book_informations[book_table_headers[key]] = value

    return book_informations


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
