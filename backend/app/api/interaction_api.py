# app/api/interaction_api.py
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.interaction_service import record_interaction, get_interactions_for_content

interaction_bp = Blueprint('interaction_bp', __name__)

@interaction_bp.route('/record', methods=['POST'])
@jwt_required()
def record():
    user_id = get_jwt_identity()
    data = request.get_json()
    content_id = data.get('content_id')
    interaction_type = data.get('interaction_type')
    reward = data.get('reward')
    record_interaction(user_id, content_id, interaction_type, reward)
    return jsonify({"message": "Interaction recorded"}), 200

@interaction_bp.route('/content/<int:content_id>/interactions', methods=['GET'])
@jwt_required()
def get_content_interactions(content_id):
    interactions = get_interactions_for_content(content_id)
    return jsonify(interactions), 200
