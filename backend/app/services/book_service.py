# app/services/book_service.py
from app.dal.book_repository import BookRepository

class BookService:
    @staticmethod
    def get_all_books(page, per_page):
        book_items, total, pages, current_page = BookRepository.get_all_books_paginated(page, per_page)
        return book_items, total, pages, current_page
        
    @staticmethod
    def get_books(book_id):
        return BookRepository.get_book_by_id(book_id)