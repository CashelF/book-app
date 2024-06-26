# app/api/recommendation_api.py
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.recommendation_service import get_recommendations
from app.services.user_service import get_user_by_id

recommendation_bp = Blueprint('recommendation_bp', __name__)

@recommendation_bp.route('/', methods=['GET'])
@jwt_required()
def recommendations():
    user_id = get_jwt_identity()
    user = get_user_by_id(user_id)
    batch_size = int(request.args.get('batch_size', 10))
    num_recommendations = int(request.args.get('num_recommendations', 10))

    recommended_books = get_recommendations(user, batch_size=batch_size, num_recommendations=num_recommendations)

    return jsonify([book.to_dict() for book in recommended_books])