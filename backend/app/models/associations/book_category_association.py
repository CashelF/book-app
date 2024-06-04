# app/models/associations/book_category_association.py
from app.dal.database import db

book_category_association = db.Table('book_category_association',
    db.Column('book_id', db.Integer, db.ForeignKey('books.id'), primary_key=True),
    db.Column('category_id', db.Integer, db.ForeignKey('category.id'), primary_key=True)
)
