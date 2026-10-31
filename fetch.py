"""Download web pages."""
import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; BeginnerScraper/1.0; learning project)"
}


def get_page(url, timeout=10):
    """Return the HTML of a page as text, or None if the request fails."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=timeout)
        response.raise_for_status()  # raises an error for 404, 500, etc.
        response.encoding = "utf-8"
        return response.text
    except requests.RequestException as error:
        print(f"Request failed for {url}: {error}")
        return None
