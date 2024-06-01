# app/models/associations/saved_books_association.py
from sqlalchemy import Table, Column, Integer, ForeignKey
from app.dal.database import db

saved_books = Table('saved_books', db.Model.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('book_id', Integer, ForeignKey('content.id'), primary_key=True)
)