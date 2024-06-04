# app/models/associations/book_author_association.py
from app.dal.database import db

book_author_association = db.Table('book_author_association',
    db.Column('book_id', db.Integer, db.ForeignKey('books.id'), primary_key=True),
    db.Column('author_id', db.Integer, db.ForeignKey('author.id'), primary_key=True)
)
