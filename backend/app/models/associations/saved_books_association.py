# app/models/associations/saved_books_association.py
from app.dal.database import db

saved_books = db.Table('saved_books',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('book_id', db.Integer, db.ForeignKey('books.id'), primary_key=True)
)
