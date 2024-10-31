from pprint import pprint

from booktoscrap.connection import get_soup


def get_categories_from_home(homepage_url: str):
    """
        Take the given homepage_url and discover available categories and their related url's.

    Args:
        homepage_url: The url of the homepage from the book.toscrape.com site. (i.e.: https://books.toscrape.com/index.html)

    Yields:
        tuple: Containing a category name and her related url.

    """
    soup = get_soup(homepage_url)
    categories_soup = soup.select('.side_categories ul>li>a')
    for link in categories_soup[1:]:
        yield link.get_text().strip(), 'https://books.toscrape.com/' + link['href']


def list_product_page_links_from_category(category_url: str) -> list[str]:
    """
        Take a category url and discover available other pages links (pagination).

    Args:
        category_url: The url of a category page from the book.toscrape.com site.

    Returns:
        list: A list of all product page links from a category

    """
    soup = get_soup(category_url)
    pager = soup.select_one('ul.pager li.current')
    if not pager:
        return [category_url]
    pages_count = int(pager.text.split('of ')[1].strip())
    base_category_url = category_url[:-10]
    return [f"{base_category_url}page-{page}.html" for page in range(1, pages_count + 1)]

if __name__ == '__main__':
    for category_name, category_url in get_categories_from_home('https://books.toscrape.com/index.html'):
        print(category_name, category_url)

    pprint(list_product_page_links_from_category('https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html'))
