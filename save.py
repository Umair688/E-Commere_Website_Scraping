"""Save scraped data to a CSV file."""
import csv
import os

FIELDS = ["title", "price", "rating", "availability", "url"]


def save_to_csv(rows, filename):
    """Write a list of dicts to a CSV file (creates the folder if needed)."""
    folder = os.path.dirname(filename)
    if folder:
        os.makedirs(folder, exist_ok=True)

    with open(filename, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)
