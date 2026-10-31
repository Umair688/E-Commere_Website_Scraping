# E-Commere_Website_Scraping
 Book Price Scraper

A beginner-friendly Python web scraping project. It collects book data
(title, price, rating, availability, link) from
[Books to Scrape](https://books.toscrape.com/) - a website made specifically
for practicing web scraping - and saves it to a CSV file.

## What you will learn

- Downloading web pages with `requests`
- Parsing HTML with `BeautifulSoup`
- Following "next page" links (pagination)
- Saving data to a CSV file
- Organizing code into small modules

## Project structure

```
book-price-scraper/
├── main.py              # Entry point - run this file
├── scraper/
│   ├── __init__.py
│   ├── fetch.py         # Downloads a page
│   ├── parse.py         # Extracts book data from HTML
│   └── save.py          # Writes data to CSV
├── data/
│   └── books.csv        # Output (created when you run the scraper)
├── requirements.txt     # Python libraries needed
├── .gitignore
└── README.md
```

## Setup

You need Python 3.8 or newer.

```bash
# 1. Create a virtual environment
python -m venv venv

# 2. Activate it
#    Windows (PowerShell):
venv\Scripts\Activate.ps1
#    Windows (Command Prompt):
venv\Scripts\activate.bat
#    macOS / Linux:
source venv/bin/activate

# 3. Install the libraries
pip install -r requirements.txt
```
