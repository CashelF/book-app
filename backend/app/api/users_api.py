# app/api/users_api.py
from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.user_service import UserService

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