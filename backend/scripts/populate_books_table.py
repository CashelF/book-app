import sys
import os

# Adjust the PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from app import create_app, db
from app.config import ProductionConfig
from app.models import Book, Author

# List of required columns in the dataset
required_columns = ['ISBN', 'Name', 'PublishYear', 'Description', 'pagesNumber', 'CountsOfReview', 'Authors']
minimum_reviews = 200

# Define list of book CSV files to process
book_csv_files = [
    'book1-100k.csv',
    'book100k-200k.csv',
    'book200k-300k.csv',
    'book300k-400k.csv',
    'book400k-500k.csv',
    'book500k-600k.csv',
    'book600k-700k.csv',
    'book700k-800k.csv',
    'book800k-900k.csv',
    'book900k-1000k.csv',
    'book1000k-1100k.csv',
    'book1100k-1200k.csv',
    'book1200k-1300k.csv',
    'book1300k-1400k.csv',
    'book1400k-1500k.csv',
    'book1500k-1600k.csv',
    'book1600k-1700k.csv',
    'book1700k-1800k.csv',
    'book1800k-1900k.csv',
    'book1900k-2000k.csv',
    'book2000k-3000k.csv',
    'book3000k-4000k.csv',
    'book4000k-5000k.csv'
]

# Function to check if a book entry already exists in the database
def entry_exists(isbn, title):
    return Book.query.filter((Book.ISBN == isbn) | (Book.title == title)).first() is not None

# Function to populate the database directly from the Goodreads dataset
def populate_database_from_goodreads(df):
    df = df.dropna(subset=required_columns)
    df = df[df['CountsOfReview'] >= minimum_reviews]
    
    for _, row in df.iterrows():
        isbn = row['ISBN']
        if len(isbn) == 10:
            isbn = "978" + isbn
        title = row['Name']
        publication_year = row['PublishYear']
        description = row['Description']
        page_length = row['pagesNumber']
        cover_image_url = None  # Placeholder; you may update if URL data is available
        author_names = row['Authors'].split(",")

        # Skip if entry already exists in the database
        if entry_exists(isbn, title):
            continue
        
        # Create a new book entry
        book = Book(
            title=title,
            ISBN=isbn if not pd.isna(isbn) else None,
            publication_year=int(publication_year) if not pd.isna(publication_year) else None,
            description=description if not pd.isna(description) else None,
            page_length=int(page_length) if not pd.isna(page_length) else None,
            cover_image_url=cover_image_url,
            embedding=None  # Placeholder; add embedding processing if needed
        )
        
        # Add authors to the book
        for author_name in author_names:
            author_name = author_name.strip()
            # Check if the author already exists in the database
            author = Author.query.filter_by(name=author_name).first()
            if not author:
                # If not, create a new Author and add to the session
                author = Author(name=author_name)
                db.session.add(author)
            book.authors.append(author)  # Associate the author with the book
        
        # Add the book entry to the session
        db.session.add(book)
    
    # Commit the session to save all entries to the database
    db.session.commit()

if __name__ == "__main__":
    app = create_app(ProductionConfig)
    base_dir = os.path.dirname(os.path.dirname(__file__))
    app_dir = os.path.join(base_dir, 'app', 'services', 'recommendations_submodule', 'goodreads_data')
    with app.app_context():
        for file_name in book_csv_files:
            # Load each CSV file into a DataFrame
            df = pd.read_csv(os.path.join(app_dir, file_name))
            
            # Check if the DataFrame has all required columns
            missing_columns = set(required_columns) - set(df.columns)
            if missing_columns:
                print(f"Skipping {file_name} - Missing columns: {', '.join(missing_columns)}")
                continue
            
            # Populate database with filtered data
            populate_database_from_goodreads(df)
            print(f"Completed processing {file_name}")
