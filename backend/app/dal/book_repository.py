# app/dal/book_repository.py
import numpy as np
from sqlalchemy import func
from app.models.book_model import Book
from app.models.book_parameters_model import BookParameters
from app.dal.database import db

class BookRepository:
    @staticmethod
    def get_all_books():
        book_items = Book.query.all()
        return book_items

    @staticmethod
    def get_all_books_paginated(page, per_page):
        pagination = Book.query.paginate(page=page, per_page=per_page, error_out=False)
        return pagination.items, pagination.total, pagination.pages, pagination.page

    @staticmethod
    def get_book_batch(batch_size, offset):
        return Book.query.offset(offset).limit(batch_size).all()

    @staticmethod
    def get_book_by_id(book_id):
        book = Book.query.get(book_id)
        return book
    
    @staticmethod
    def get_books_by_ids(book_ids):
        return Book.query.filter(Book.id.in_(book_ids)) \
                          .order_by(func.field(Book.id, *book_ids)) \
                          .all()
    @staticmethod
    def get_book_by_title(title):
        return Book.query.filter(func.lower(Book.title) == func.lower(title)).first()
    
    @staticmethod
    def get_book_by_isbn(isbn_13):
        return Book.query.filter_by(ISBN=isbn_13).first()

    @staticmethod
    def search_books_by_query(query):
        book_items = Book.query.filter(
            Book.title.ilike(f'%{query}%') |
            Book.description.ilike(f'%{query}%')
        ).all()
        return book_items

    @staticmethod
    def get_book_parameters(book_id):
            book_parameters = BookParameters.query.filter_by(id=book_id).first()
            if book_parameters:
                return book_parameters.parameters
            else:
                return None
            
    @staticmethod
    def get_all_book_parameters_dict():
        all_parameters = {}

        books = (
            db.session.query(Book.id, BookParameters.parameters)
            .join(BookParameters, Book.id == BookParameters.book_id)
            .all()
        )

        for book_id, parameters in books:
            if isinstance(parameters, (bytes, str)):
                parameters = np.frombuffer(parameters, dtype=np.float32).copy()
            all_parameters[book_id] = parameters

        return all_parameters
            
    @staticmethod
    def save_book_parameters(book_id, parameters):
        book_parameters = BookParameters.query.filter_by(book_id=book_id).first()
        if book_parameters is None:
            book_parameters = BookParameters(book_id=book_id, parameters=parameters)
            db.session.add(book_parameters)
        else:
            book_parameters.parameters = parameters
        db.session.commit()
        
    @staticmethod
    def save_all_book_parameters_dict(all_book_parameters):
        for book_id, parameters in all_book_parameters.items():
            book_parameters = BookParameters.query.filter_by(book_id=book_id).first()
            if parameters is None:
                book_parameters = BookParameters(book_id=book_id, parameters=parameters)
                db.session.add(book_parameters)
            else:
                book_parameters.parameters = parameters
        db.session.commit()

    @staticmethod
    def get_all_book_embeddings():
        books = Book.query.filter(Book.embedding.isnot(None)).all()
        book_embeddings = [
            {'id': book.id, 'embedding': np.frombuffer(book.embedding, dtype=np.float32)}
            for book in books
        ]
        return book_embeddings
    
    @staticmethod
    def get_books_excluding(book_ids, limit):
        return Book.query.filter(~Book.id.in_(book_ids)).limit(limit).all()