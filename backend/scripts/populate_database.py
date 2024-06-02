import sys
import os

# Adjust the PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import requests
import pandas as pd
import time
from flask import Flask
from app import create_app, db
from app.models import Content, Author, Genre, Category

# Google Books API key
API_KEY = 'AIzaSyCXtMtLoWlOUAGC1zWnyqfebxEq65mck9U'
MIN_REVIEWS = 100  # A threshold for the minimum number of reviews

# Function to search for data using the Google Books API
def search_data(isbn):
    url = f'https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}&key={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error: {response.status_code}')
        return None

# Function to extract useful information from the API response
def extract_info(data, ratings_count):
    items = []
    for item in data.get('items', []):
        volume_info = item.get('volumeInfo', {})
        
        entry = {
            'title': volume_info.get('title'),
            'authors': volume_info.get('authors', []),
            'publisher': volume_info.get('publisher'),
            'publishedDate': volume_info.get('publishedDate'),
            'description': volume_info.get('description'),
            'pageCount': volume_info.get('pageCount'),
            'categories': volume_info.get('categories', []),
            'averageRating': volume_info.get('averageRating'),
            'ratingsCount': ratings_count,
            'thumbnail': volume_info.get('imageLinks', {}).get('thumbnail'),
            'language': volume_info.get('language'),
            'previewLink': volume_info.get('previewLink'),
            'isbn_10': None,
            'isbn_13': None,
            'series': volume_info.get('seriesInfo', {}).get('title')
        }
        
        for identifier in volume_info.get('industryIdentifiers', []):
            if identifier['type'] == 'ISBN_10':
                entry['isbn_10'] = identifier['identifier']
            elif identifier['type'] == 'ISBN_13':
                entry['isbn_13'] = identifier['identifier']
        
        items.append(entry)
    return items

# Function to check if an entry already exists in the database
def entry_exists(isbn_13, title, authors):
    query = Content.query.filter(
        (Content.ISBN == isbn_13) |
        (Content.title == title)
    )
    
    for entry in query:
        if all(author in [a.name for a in entry.authors] for author in authors):
            return True
    return False

# Function to populate the database
def populate_database(entries):

    for entry in entries:
        # Skip if the entry is already in the database
        if entry_exists(entry['isbn_13'], entry['title'], entry['authors']):
            continue
        
        content = Content(
            title=entry['title'],
            ISBN=entry['isbn_13'],
            type='book',
            publication_year=int(entry['publishedDate'].split('-')[0]) if entry.get('publishedDate') else None,
            description=entry['description'],
            page_length=entry['pageCount'],
            cover_image_url=entry['thumbnail']
        )
        
        # Add authors
        for author_name in entry['authors']:
            author = Author.query.filter_by(name=author_name).first()
            if not author:
                author = Author(name=author_name)
            content.authors.append(author)
        
        # Add genres
        for genre_name in entry['categories']:
            genre = Genre.query.filter_by(name=genre_name).first()
            if not genre:
                genre = Genre(name=genre_name)
            content.genres.append(genre)
        
        # Add categories
        for category_name in entry['categories']:
            category = Category.query.filter_by(name=category_name).first()
            if not category:
                category = Category(name=category_name)
            content.categories.append(category)

        db.session.add(content)
    
    db.session.commit()

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        df = pd.read_csv('scripts/filtered_books.csv')
        filtered_df = df[df['ratings_count'] >= MIN_REVIEWS]
        
        for _, row in filtered_df.iterrows():
            isbn = row['isbn13']
            ratings_count = row['ratings_count']
            data = search_data(isbn)
            if data:
                entries = extract_info(data, ratings_count)
                populate_database(entries)
                print(f"Database populated with entries for ISBN: {isbn}")
            # For the API rate limit
            time.sleep(1)
