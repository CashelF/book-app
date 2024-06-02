# app/dal/content_repository.py
from app.models.content_model import Content
from app.dal.database import db

def get_all_content():
    content_items = Content.query.all()
    return content_items

def get_all_content_paginated(page, per_page):
    pagination = Content.query.paginate(page=page, per_page=per_page, error_out=False)
    return pagination.items, pagination.total, pagination.pages, pagination.page

def get_content_batch(batch_size, offset):
    return Content.query.offset(offset).limit(batch_size).all()

def get_content_by_id(content_id):
    content = Content.query.get(content_id)
    return content

def search_content_by_query(query):
    content_items = Content.query.filter(
        Content.title.ilike(f'%{query}%') |
        Content.description.ilike(f'%{query}%')
    ).all()
    return content_items
