# app/services/content_service.py
from app.dal.content_repository import get_all_content_paginated,get_content_by_id, search_content_by_query

def get_all_content(page, per_page):
    content_items, total, pages, current_page = get_all_content_paginated(page, per_page)
    return [
        {
            "id": content.id,
            "title": content.title,
            "description": content.description,
            "cover_image": content.cover_image
        } for content in content_items
    ], total, pages, current_page
    
def get_content(content_id):
    content = get_content_by_id(content_id)
    if not content:
        return {'message': 'Content not found'}, 404
    return {
        'id': content.id,
        'title': content.title,
        'author': content.author,
        'description': content.description
    }, 200
    
def search_content(query):
    content_items = search_content_by_query(query)
    return [
        {
            "id": content.id,
            "title": content.title,
            "description": content.description,
            "cover_image": content.cover_image_url
        } for content in content_items
    ]
