# app/api/auth_api.py
from flask import Blueprint, request
from app.services.auth_service import AuthService

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    return AuthService.register_user(data)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    return AuthService.login_user(data)
