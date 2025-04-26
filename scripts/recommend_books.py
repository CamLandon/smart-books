# scripts/recommend_books.py

"""
Simple Book Recommender System
- Load cosine similarity matrix
- Load book dataset
- Recommend similar books based on title
"""

import pandas as pd
import pickle

# Step 1: Load the cleaned dataset with features
print("📚 Loading book dataset...")
books_df = pd.read_csv('../data/books_dataset_with_features.csv')

# Step 2: Load the cosine similarity matrix
print("💾 Loading cosine similarity matrix...")
with open('../data/cosine_similarity_matrix.pkl', 'rb') as f:
    cosine_sim = pickle.load(f)

# Step 3: Build a mapping from book titles to DataFrame indices
book_indices = pd.Series(books_df.index, index=books_df['title'].str.lower()).drop_duplicates()

# Step 4: Define the recommendation function
def recommend_books(title, num_recommendations=5):
    title = title.lower()

    if title not in book_indices:
        print(f"\n❗ Sorry, the book '{title.title()}' was not found in the dataset.\n")
        return

    idx = book_indices[title]

    # Get list of (index, similarity score) tuples
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort by similarity score (highest first)
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the top recommendations (skip the first one, it's the book itself)
    sim_scores = sim_scores[1:num_recommendations+1]

    # Print recommendations
    print(f"\n📖 Because you liked '{books_df.iloc[idx]['title']}' by {books_df.iloc[idx]['author']}, you might also like:\n")
    for i, score in sim_scores:
        print(f"- {books_df.iloc[i]['title']} by {books_df.iloc[i]['author']} (Similarity Score: {score:.2f})")

# Step 5: Main script to interact with user
if __name__ == "__main__":
    while True:
        user_input = input("\n🔎 Enter a book title (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("\n👋 Thanks for using the Smart Book Recommender. Goodbye!\n")
            break
        recommend_books(user_input)
