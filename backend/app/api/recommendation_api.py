from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.recommendation_service import get_recommendations_batch

recommendation_bp = Blueprint('recommendation_bp', __name__)

@recommendation_bp.route('/recommendations', methods=['GET'])
@jwt_required()
def recommendations():
    user_id = get_jwt_identity()
    start_index = int(request.args.get('start', 0))
    batch_size = int(request.args.get('size', 10))
    recommendations = get_recommendations_batch(user_id, start_index, batch_size)
    return jsonify(recommendations), 200
