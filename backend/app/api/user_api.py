# app/api/user_api.py
from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.user_service import get_user_by_id

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    user = get_user_by_id(user_id)
    return {
        'username': user.username,
        'email': user.email
    }, 200