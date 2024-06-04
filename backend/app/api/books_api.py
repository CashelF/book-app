# app/api/books_api.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.services.book_service import get_all_books, get_books, search_books

books_bp = Blueprint('books_bp', __name__)

@books_bp.route('/', methods=['GET'])
@jwt_required()
def fetch_all_book():
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        book_items, total, pages, current_page = get_all_books(page, per_page)
        book = [
            {
                "id": item.id,
                "title": item.title,
                "description": item.description,
                "cover_image": item.cover_image_url
            } for item in book_items
        ]
        return jsonify({
            'book': book,
            'total': total,
            'pages': pages,
            'current_page': current_page
        }), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500

@books_bp.route('/<int:id>', methods=['GET'])
def fetch_book(id):
    try:
        book = get_books(id)
        if not book:
            return jsonify({'message': 'book not found'}), 404
        authors = [
            {"id": author.id, "name": author.name}
            for author in book.authors
        ]
        return jsonify({
            'id': book.id,
            'title': book.title,
            'authors': authors,
            'description': book.description,
            'cover_image': book.cover_image_url
        }), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500

@books_bp.route('/search', methods=['GET'])
@jwt_required()
def search_book_endpoint():
    try:
        query = request.args.get('q', '', type=str)
        book_items = search_books(query)
        book = [
            {
                "id": item.id,
                "title": item.title,
                "description": item.description,
                "cover_image": item.cover_image_url
            } for item in book_items
        ]
        return jsonify(book), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500
