# app/dal/book_repository.py
from app.models.book_model import Book
from app.dal.database import db

def get_all_books():
    book_items = Book.query.all()
    return book_items

def get_all_books_paginated(page, per_page):
    pagination = Book.query.paginate(page=page, per_page=per_page, error_out=False)
    return pagination.items, pagination.total, pagination.pages, pagination.page

def get_book_batch(batch_size, offset):
    return Book.query.offset(offset).limit(batch_size).all()

def get_book_by_id(book_id):
    book = Book.query.get(book_id)
    return book

def search_books_by_query(query):
    book_items = Book.query.filter(
        Book.title.ilike(f'%{query}%') |
        Book.description.ilike(f'%{query}%')
    ).all()
    return book_items
