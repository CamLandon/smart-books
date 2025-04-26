# Smart Book Discoveries
A Machine Learning-Based Book Recommendation System

---

## Project Overview
Smart Book Discoveries is a book recommendation system designed to help readers find personalized book suggestions based on book metadata, user ratings, and textual similarity.  
The project combines data collection, exploration, modeling, and evaluation into a full machine learning pipeline.

---

## Tools and Technologies
- **Python 3**
- **Pandas**, **NumPy**, **Matplotlib**, **Scikit-learn**
- **Jupyter Notebooks** for analysis and exploration
- **VSCode** as the primary development environment
- **GitHub** for version control
- **Overleaf (LaTeX)** for project documentation and reporting

---

## Project Structure
smart-books/ 
├── data/ # Raw and cleaned datasets 
├── notebooks/ # Jupyter notebooks for EDA, modeling, testing 
├── scripts/ # Python scripts (e.g., data processing, modeling) 
├── figures/ # Charts, graphs, heatmaps, visual outputs 
├── reports/ # LaTeX files for Overleaf report writing ├── README.md # Project description and instructions 
├── .gitignore # Files and folders to exclude from GitHub 
├── requirements.txt # List of required Python packages


## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/CamLandon/smart-books.git
   cd smart-books

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt   


4. **Launch Juypyter Notebooks**
    ```bash
    jupyter notebooks