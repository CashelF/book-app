# app/api/user_api.py
from flask import Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services.user_service import get_user_profile

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    return get_user_profile(user_id)
