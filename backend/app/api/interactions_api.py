# app/api/interactions_api.py
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.interaction_service import InteractionService

interactions_bp = Blueprint('interactions_bp', __name__)

# Save interaction
@interactions_bp.route('/save', methods=['POST'])
@jwt_required()
def save_book():
    user_id = get_jwt_identity()
    data = request.get_json()
    book_id = data.get('book_id')
    if not book_id:
        return jsonify({"error": "Book ID is required"}), 400
    
    InteractionService.save_interaction(user_id, book_id)
    return jsonify({"message": "Book saved"}), 200

# Unsave interaction
@interactions_bp.route('/unsave', methods=['POST'])
@jwt_required()
def unsave_book():
    user_id = get_jwt_identity()
    data = request.get_json()
    book_id = data.get('book_id')
    if not book_id:
        return jsonify({"error": "Book ID is required"}), 400
    
    InteractionService.unsave_interaction(user_id, book_id)
    return jsonify({"message": "Book unsaved"}), 200

# Like interaction
@interactions_bp.route('/like', methods=['POST'])
@jwt_required()
def like_book():
    user_id = get_jwt_identity()
    data = request.get_json()
    book_id = data.get('book_id')
    if not book_id:
        return jsonify({"error": "Book ID is required"}), 400
    
    InteractionService.like_interaction(user_id, book_id)
    return jsonify({"message": "Book liked"}), 200

# View interaction
@interactions_bp.route('/view', methods=['POST'])
@jwt_required()
def view_book():
    user_id = get_jwt_identity()
    data = request.get_json()
    book_id = data.get('book_id')
    duration = data.get('duration')  # Optionally include duration of the view

    if not book_id:
        return jsonify({"error": "Book ID is required"}), 400
    
    InteractionService.view_interaction(user_id, book_id, duration)
    return jsonify({"message": "Book viewed"}), 200
