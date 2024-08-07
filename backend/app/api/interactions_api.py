# app/api/interactions_api.py
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.interaction_service import InteractionService

interactions_bp = Blueprint('interactions_bp', __name__)

@interactions_bp.route('/record', methods=['POST'])
@jwt_required()
def record():
    user_id = get_jwt_identity()
    data = request.get_json()
    book_id = data.get('book_id')
    interaction_type = data.get('interaction_type')
    duration = data.get('duration')  # Include duration for 'view' interactions if applicable
    
    if not book_id or not interaction_type:
        return jsonify({"error": "Book ID and interaction type are required"}), 400
    
    # Validate interaction type
    if interaction_type not in ['like', 'save', 'view']:
        return jsonify({"error": "Invalid interaction type"}), 400

    InteractionService.record_interaction(user_id, book_id, interaction_type, duration)
    return jsonify({"message": "Interaction recorded"}), 200
