# src/data_collection.py

"""
Data Collection Script for Smart Book Discoveries
- Fetch book data from Google Books API for thousands of books
- Save updated dataset with additional fields
"""

import requests
import pandas as pd
import time
from bs4 import BeautifulSoup

# Load initial book dataset
def load_csv_dataset(filepath):
    return pd.read_csv(filepath)

# Google Books API fetch function
def fetch_google_books_data(title, author, api_key=None):
    query = f"{title}+inauthor:{author}"
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}"
    if api_key:
        url += f"&key={api_key}"

    try:
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
    except Exception as e:
        print(f"Error fetching data for {title}: {e}")

    return {}

# Optional: Goodreads scraper (if you want to scrape missing info)
def scrape_goodreads_description(goodreads_url):
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

# Main workflow
if __name__ == "__main__":
    # 1. Load your dataset
    books_df = load_csv_dataset('../data/books_dataset.csv')

    # Add new empty columns to hold fetched data if they don't exist
    for col in ['description', 'publishedDate', 'categories', 'pageCount']:
        if col not in books_df.columns:
            books_df[col] = None

    # 2. Loop through each book
    for idx, row in books_df.iterrows():
        title = row['title']
        author = row['author']

        # Skip if already filled (optional, for reruns)
        if pd.notna(row.get('description')):
            continue

        print(f"Fetching data for: {title} by {author}")

        # Fetch from Google Books
        google_data = fetch_google_books_data(title, author)

        # Update dataset
        books_df.at[idx, 'description'] = google_data.get('description')
        books_df.at[idx, 'publishedDate'] = google_data.get('publishedDate')
        books_df.at[idx, 'categories'] = google_data.get('categories')
        books_df.at[idx, 'pageCount'] = google_data.get('pageCount')

        # Wait 1 second between API calls to be polite
        time.sleep(1)

    # 3. Save updated dataset
    books_df.to_csv('../data/books_dataset_updated.csv', index=False)

    print("✅ Data collection completed and saved to 'books_dataset_updated.csv'")
