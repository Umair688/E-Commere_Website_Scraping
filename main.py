"""Entry point: scrape book data and save it to a CSV file.

Run:
    python main.py              # scrape 3 pages (default)
    python main.py --pages 50   # scrape all 50 pages
"""
import argparse
import time

from scraper.fetch import get_page
from scraper.parse import parse_books, get_next_page_url
from scraper.save import save_to_csv

START_URL = "https://books.toscrape.com/catalogue/page-1.html"
OUTPUT_FILE = "data/books.csv"


def main():
    parser = argparse.ArgumentParser(description="Simple e-commerce scraper")
    parser.add_argument("--pages", type=int, default=3, help="How many pages to scrape")
    args = parser.parse_args()

    all_books = []
    url = START_URL

    for page_number in range(1, args.pages + 1):
        print(f"Scraping page {page_number}: {url}")
        html = get_page(url)
        if html is None:
            print("Could not download page, stopping.")
            break

        books = parse_books(html, url)
        all_books.extend(books)
        print(f"  Found {len(books)} books")

        url = get_next_page_url(html, url)
        if url is None:
            print("No more pages.")
            break

        time.sleep(1)  # be polite to the website

    save_to_csv(all_books, OUTPUT_FILE)
    print(f"\nDone! Saved {len(all_books)} books to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
