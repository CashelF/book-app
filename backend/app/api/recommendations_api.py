# app/api/recommendations_api.py
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.recommendation_service import get_recommendations
from app.services.user_service import get_user_by_id

recommendations_bp = Blueprint('recommendations_bp', __name__)

@recommendations_bp.route('/', methods=['GET'])
@jwt_required()
def recommendations():
    user_id = get_jwt_identity()
    num_recommendations = int(request.args.get('num_recommendations', 10))

    recommended_books = get_recommendations(user_id, num_recommendations=num_recommendations)

    return recommended_books