# app/services/content_service.py
from app.models.content_model import Content
from app.dal.content_repository import add_content, get_all_contents, get_content_by_id, update_content, delete_content

def create_content(data):
    new_content = Content(title=data['title'], author=data['author'], description=data.get('description'))
    add_content(new_content)
    return {'message': 'Content added successfully'}, 201

def fetch_contents():
    contents = get_all_contents()
    result = []
    for content in contents:
        content_data = {
            'id': content.id,
            'title': content.title,
            'author': content.author,
            'description': content.description
        }
        result.append(content_data)
    return result, 200

def fetch_content(content_id):
    content = get_content_by_id(content_id)
    return {
        'id': content.id,
        'title': content.title,
        'author': content.author,
        'description': content.description
    }, 200

def edit_content(content_id, data):
    content = get_content_by_id(content_id)
    content.title = data['title']
    content.author = data['author']
    content.description = data.get('description')
    update_content(content)
    return {'message': 'Content updated successfully'}, 200

def remove_content(content_id):
    content = get_content_by_id(content_id)
    delete_content(content)
    return {'message': 'Content deleted successfully'}, 200
