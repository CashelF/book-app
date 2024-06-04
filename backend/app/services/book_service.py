# app/services/book_service.py
from app.dal.book_repository import get_all_books_paginated,get_book_by_id, search_books_by_query

def get_all_books(page, per_page):
    book_items, total, pages, current_page = get_all_books_paginated(page, per_page)
    return book_items, total, pages, current_page
    
def get_books(book_id):
    return get_book_by_id(book_id)
    
def search_books(query):
    return search_books_by_query(query)
    
