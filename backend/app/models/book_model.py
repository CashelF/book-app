# app/models/book_model.py
from app.dal.database import db
from .associations.book_author_association import book_author_association
from .associations.book_genre_association import book_genre_association
from .associations.book_category_association import book_category_association
from .associations.saved_books_association import saved_books

class Book(db.Model):
    __tablename__ = 'books'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ISBN = db.Column(db.String(13))
    title = db.Column(db.String(255), nullable=False)
    type = db.Column(db.Enum('book', 'article'))
    publication_year = db.Column(db.Integer)
    description = db.Column(db.Text)
    page_length = db.Column(db.Integer)
    cover_image_url = db.Column(db.String(255))
    embedding = db.Column(db.LargeBinary, nullable=True)

    authors = db.relationship('Author', secondary=book_author_association, back_populates='books')
    genres = db.relationship('Genre', secondary=book_genre_association, back_populates='books')
    categories = db.relationship('Category', secondary=book_category_association, back_populates='books')
    interactions = db.relationship("Interaction", back_populates="book")
    saved_by_users = db.relationship('User', secondary=saved_books, back_populates='saved_books')
    parameters = db.relationship('BookParameters', back_populates='book', uselist=False)
    reading_history = db.relationship('ReadingHistory', back_populates='book')