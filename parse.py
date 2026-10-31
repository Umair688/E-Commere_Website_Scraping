"""Extract data from the HTML of a page."""
from urllib.parse import urljoin

from bs4 import BeautifulSoup

RATING_WORDS = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}


def parse_books(html, page_url):
    """Return a list of dicts, one per book found on the page."""
    soup = BeautifulSoup(html, "html.parser")
    books = []

    for card in soup.select("article.product_pod"):
        title = card.h3.a["title"]
        price = card.select_one("p.price_color").get_text(strip=True)
        availability = card.select_one("p.instock.availability").get_text(strip=True)
        rating_class = card.select_one("p.star-rating")["class"][1]  # e.g. "Three"
        link = urljoin(page_url, card.h3.a["href"])

        books.append(
            {
                "title": title,
                "price": price.replace("Â", "").replace("£", ""),
                "rating": RATING_WORDS.get(rating_class, 0),
                "availability": availability,
                "url": link,
            }
        )

    return books


def get_next_page_url(html, page_url):
    """Return the URL of the next page, or None on the last page."""
    soup = BeautifulSoup(html, "html.parser")
    next_button = soup.select_one("li.next a")
    if next_button is None:
        return None
    return urljoin(page_url, next_button["href"])
