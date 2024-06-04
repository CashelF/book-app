# app/models/associations/book_genre_association.py
from app.dal.database import db

book_genre_association = db.Table('book_genre_association',
    db.Column('book_id', db.Integer, db.ForeignKey('books.id'), primary_key=True),
    db.Column('genre_id', db.Integer, db.ForeignKey('genre.id'), primary_key=True)
)
