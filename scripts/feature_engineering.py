# scripts/feature_engineering.py

"""
Feature Engineering Script for Smart Book Discoveries
- Load cleaned book data
- Combine important text fields
- Create a TF-IDF matrix
- Calculate cosine similarity
- Save the similarity matrix for building the recommender system
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# Step 1: Load the cleaned dataset
print("📚 Loading cleaned book dataset...")
books_df = pd.read_csv('../data/books_dataset_cleaned.csv', on_bad_lines='skip', engine='python')

# Step 2: Combine text fields into one "combined_features" column
print("🧩 Combining important fields (title, author, description, categories)...")

# Fill missing text fields with empty string (just in case)
for col in ['title', 'author', 'description', 'categories']:
    books_df[col] = books_df[col].fillna('')

# Create the combined feature
books_df['combined_features'] = (
    books_df['title'] + ' ' +
    books_df['author'] + ' ' +
    books_df['description'] + ' ' +
    books_df['categories']
)

# Step 3: Create the TF-IDF matrix
print("🛠 Creating TF-IDF matrix...")

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(books_df['combined_features'])

print(f"✅ TF-IDF Matrix Shape: {tfidf_matrix.shape}")

# Step 4: Calculate cosine similarity between books
print("🔎 Calculating cosine similarity between books...")

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

print(f"✅ Cosine Similarity Matrix Shape: {cosine_sim.shape}")

# Step 5: Save the cosine similarity matrix
print("💾 Saving cosine similarity matrix to 'cosine_similarity_matrix.pkl'...")

with open('../data/cosine_similarity_matrix.pkl', 'wb') as f:
    pickle.dump(cosine_sim, f)

# (Optional) Save updated DataFrame with combined_features for reuse later
print("💾 Saving updated books dataset with combined_features to 'books_dataset_with_features.csv'...")
books_df.to_csv('../data/books_dataset_with_features.csv', index=False)

print("✅ Feature Engineering Complete!")
