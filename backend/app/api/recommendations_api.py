# app/api/recommendations_api.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.recommendations_submodule.contextual_bandits_rec_service import ContextualBanditsRecommendationService
from app.services.recommendations_submodule.content_filtering_rec_service import ContentFilteringRecService

recommendations_bp = Blueprint('recommendations_bp', __name__)

@recommendations_bp.route('/contextual-bandits', methods=['GET'])
@jwt_required()
def recommendations():
    user_id = get_jwt_identity()
    num_recommendations = int(request.args.get('num_recommendations', 10))

    recommended_books = ContextualBanditsRecommendationService.get_recommendations(user_id, num_recommendations=num_recommendations)

    return jsonify([book.to_dict() for book in recommended_books])

@recommendations_bp.route('/content-based', methods=['GET'])
@jwt_required()
def recommend_content_based():
    user_id = get_jwt_identity()
    if not user_id:
        return jsonify({"error": "user_id is required"}), 400
    
    recommendations = ContentFilteringRecService.get_content_based_recommendations(user_id)
    return jsonify([book.to_dict() for book in recommendations])