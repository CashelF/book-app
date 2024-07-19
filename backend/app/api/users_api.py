# app/api/users_api.py
from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.user_service import UserService
from app.services.user_preference_service import UserPreferencesService

users_bp = Blueprint('users_bp', __name__)

@users_bp.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    user = UserService.get_user_by_id(user_id)
    return {
        'username': user.username,
        'email': user.email
    }, 200
    
@users_bp.route('/profile', methods=['POST'])
@jwt_required()
def update_profile():
    user_id = get_jwt_identity()
    data = request.get_json()
    age = data.get('age')
    gender = data.get('gender')
    
    UserService.update_user_info(user_id, age, gender)
    
    return jsonify({"msg": "User profile updated successfully"}), 200
    
@users_bp.route('/savedBooks', methods=['GET'])
@jwt_required()
def saved_books():
    user_id = get_jwt_identity()
    saved_books = UserService.get_user_saved_books(user_id)
    return {
        'savedBooks': saved_books
    }, 200
    
@users_bp.route('/readingHistory', methods=['POST'])
@jwt_required()
def add_reading_history():
    user_id = get_jwt_identity()
    data = request.get_json()
    book_ids = data.get('book_ids', [])

    for book_id in book_ids:
        UserService.add_reading_history(user_id, book_id)
    
    return jsonify({"msg": "Reading history added successfully"}), 201

@users_bp.route('/readingHistory', methods=['DELETE'])
@jwt_required()
def delete_reading_history():
    user_id = get_jwt_identity()
    data = request.get_json()
    book_id = data.get('book_id')

    if book_id is None:
        return jsonify({"msg": "book_id is required"}), 400

    UserService.delete_reading_history(user_id, book_id)
    
    return jsonify({"msg": "Reading history entry deleted successfully"}), 200

@users_bp.route('/preference-embedding', methods=['POST'])
@jwt_required()
def update_preference_embedding():
    user_id = get_jwt_identity()
    UserPreferencesService.generate_embedding(user_id)
    
    return jsonify({"msg": "User preferences updated successfully"}), 200