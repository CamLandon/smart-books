# scripts/data_cleaning.py

"""
Data Cleaning Script for Smart Book Discoveries
- Load books_dataset_updated.csv
- Clean and preprocess the data
- Save cleaned data to books_dataset_cleaned.csv
"""

import pandas as pd

# Step 1: Load the updated dataset
print("📚 Loading dataset...")
books_df = pd.read_csv('../data/books_dataset_updated.csv')

# Step 2: Basic Data Cleaning
print("🧹 Cleaning data...")

# 2.1 Drop duplicates (if any)
books_df.drop_duplicates(inplace=True)

# 2.2 Remove books missing important fields
# (We'll require title, author, and description to exist)
required_columns = ['title', 'author', 'description']
books_df.dropna(subset=required_columns, inplace=True)

# 2.3 Fill missing numeric values
# (Page count and average rating)

if 'pageCount' in books_df.columns:
    books_df['pageCount'].fillna(0, inplace=True)

if 'averageRating' in books_df.columns:
    books_df['averageRating'].fillna(0, inplace=True)   # ✅ NEW LINE TO ADD

# 2.4 Standardize text columns (remove leading/trailing spaces)
text_columns = ['title', 'author', 'description', 'categories']
for col in text_columns:
    if col in books_df.columns:
        books_df[col] = books_df[col].astype(str).str.strip()

# 2.5 (Optional) Clean up categories
def clean_categories(cat):
    if isinstance(cat, list) or isinstance(cat, dict):
        return ', '.join(cat)  # flatten lists
    return str(cat)

if 'categories' in books_df.columns:
    books_df['categories'] = books_df['categories'].apply(clean_categories)

# Step 3: Save the cleaned dataset
print("💾 Saving cleaned dataset...")
books_df.to_csv('../data/books_dataset_cleaned.csv', index=False)

print("✅ Data cleaning complete! Cleaned file saved as 'books_dataset_cleaned.csv'")
