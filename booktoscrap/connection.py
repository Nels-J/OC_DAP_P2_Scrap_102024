import requests
from bs4 import BeautifulSoup
from requests import Response


def get_url_response(url: str) -> Response:
    """
        Takes an url use requests library to get a response object

    Args:
        url: An url as a string

    Returns:
        response: Response object
    """
    response = requests.get(url)
    response.raise_for_status()
    return response


def get_soup(url: str) -> BeautifulSoup:
    """
        Takes an url use bs4 library to get html content as a 'soup'

    Args:
        url: An url as a string

    Returns:
        html content: BeautifulSoup object
    """
    response = get_url_response(url)
    return BeautifulSoup(response.text, "html.parser")


if __name__ == "__main__":
    get_url_response("https://books.toscrape.com/index.html")
    print(get_soup("https://books.toscrape.com/index.html"))
