# src/data_collection.py

"""
Data Collection Script for Smart Book Discoveries
- Fetch book data from Goodreads and Google Books APIs
- Perform basic web scraping for missing information
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup
import time

# Example 1: Collecting book details from a CSV dataset
def load_csv_dataset(filepath):
    """
    Load initial book dataset from a CSV file.
    """
    return pd.read_csv(filepath)

# Example 2: Google Books API function
def fetch_google_books_data(title, author, api_key=None):
    """
    Search for a book on Google Books API based on title and author.
    """
    query = f"{title}+inauthor:{author}"
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}"
    if api_key:
        url += f"&key={api_key}"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "items" in data:
            book_info = data["items"][0]["volumeInfo"]
            return {
                "description": book_info.get("description"),
                "publishedDate": book_info.get("publishedDate"),
                "categories": book_info.get("categories"),
                "pageCount": book_info.get("pageCount")
            }
    return {}

# Example 3: Simple web scraping using BeautifulSoup
def scrape_goodreads_description(goodreads_url):
    """
    Scrape book description from a Goodreads page.
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(goodreads_url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        description_div = soup.find('div', {'id': 'description'})
        if description_div:
            spans = description_div.find_all('span')
            if spans:
                return spans[-1].get_text(strip=True)
    return None

# Example usage:
if __name__ == "__main__":
    # Load initial dataset
    books_df = load_csv_dataset('../data/books_dataset.csv')

    # Sample API call for one book
    sample_title = "The Night Circus"
    sample_author = "Erin Morgenstern"
    google_data = fetch_google_books_data(sample_title, sample_author)

    print("Fetched Google Books API Data:")
    print(google_data)

    # (Optional) Sample scrape if Goodreads URL is available
    # goodreads_url = "https://www.goodreads.com/book/show/9361589-the-night-circus"
    # description = scrape_goodreads_description(goodreads_url)
    # print("Scraped Goodreads Description:")
    # print(description)

    # Note: You would typically loop through your dataset and update missing fields
