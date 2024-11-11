# scripts/index_books.py
import sys
import os

# Adjust the PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models.book_model import Book
from app.services.book_search_service import BookSearchService
from app.config import ProductionConfig

def index_books():
    app = create_app(ProductionConfig)
    with app.app_context():
        writer = BookSearchService.ix.writer()
        books = Book.query.all()
        for book in books:
            writer.add_document(
                title=book.title,
                author=", ".join([author.name for author in book.authors]),
                description=book.description,
                # genres=", ".join([genre.name for genre in book.genres]),
                isbn_13=book.ISBN
            )
        writer.commit()

if __name__ == "__main__":
    index_books()
