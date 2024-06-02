# app/services/content_service.py
from app.dal.content_repository import get_all_content_paginated,get_content_by_id, search_content_by_query

def get_all_content(page, per_page):
    content_items, total, pages, current_page = get_all_content_paginated(page, per_page)
    return content_items, total, pages, current_page
    
def get_content(content_id):
    return get_content_by_id(content_id)
    
def search_content(query):
    return search_content_by_query(query)
    
