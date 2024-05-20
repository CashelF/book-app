# app/api/content_api.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.services.content_service import get_all_content, get_content, search_content

content_bp = Blueprint('content_bp', __name__)

@content_bp.route('/', methods=['GET'])
@jwt_required()
def get_all_content_endpoint():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    content_items, total, pages, current_page = get_all_content(page, per_page)
    return jsonify({
        'content': content_items,
        'total': total,
        'pages': pages,
        'current_page': current_page
    }), 200

@content_bp.route('/<int:id>', methods=['GET'])
def fetch_content(id):
    return get_content(id)

@content_bp.route('/search', methods=['GET'])
@jwt_required()
def search_content_endpoint():
    query = request.args.get('q', '', type=str)
    content_items = search_content(query)
    return jsonify(content_items), 200
