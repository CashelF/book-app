# app/api/content_api.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.services.content_service import get_all_content, get_content, search_content

content_bp = Blueprint('content_bp', __name__)

@content_bp.route('/', methods=['GET'])
@jwt_required()
def fetch_all_content():
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        content_items, total, pages, current_page = get_all_content(page, per_page)
        content = [
            {
                "id": item.id,
                "title": item.title,
                "description": item.description,
                "cover_image": item.cover_image_url
            } for item in content_items
        ]
        return jsonify({
            'content': content,
            'total': total,
            'pages': pages,
            'current_page': current_page
        }), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500

@content_bp.route('/<int:id>', methods=['GET'])
def fetch_content(id):
    try:
        content = get_content(id)
        if not content:
            return jsonify({'message': 'Content not found'}), 404
        return jsonify({
            'id': content.id,
            'title': content.title,
            'author': content.author,
            'description': content.description,
            'cover_image': content.cover_image_url
        }), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500

@content_bp.route('/search', methods=['GET'])
@jwt_required()
def search_content_endpoint():
    try:
        query = request.args.get('q', '', type=str)
        content_items = search_content(query)
        content = [
            {
                "id": item.id,
                "title": item.title,
                "description": item.description,
                "cover_image": item.cover_image_url
            } for item in content_items
        ]
        return jsonify(content), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500
