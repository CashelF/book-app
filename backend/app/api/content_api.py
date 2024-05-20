# app/api/content_api.py
from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from app.services.content_service import create_content, fetch_contents, fetch_content, edit_content, remove_content

content_bp = Blueprint('content_bp', __name__)

@content_bp.route('/contents', methods=['POST'])
@jwt_required()
def create_content():
    data = request.get_json()
    return create_content(data)

@content_bp.route('/contents', methods=['GET'])
def fetch_contents():
    return fetch_contents()

@content_bp.route('/contents/<int:id>', methods=['GET'])
def fetch_content(id):
    return fetch_content(id)

@content_bp.route('/contents/<int:id>', methods=['PUT'])
@jwt_required()
def edit_content(id):
    data = request.get_json()
    return edit_content(id, data)

@content_bp.route('/contents/<int:id>', methods=['DELETE'])
@jwt_required()
def remove_content(id):
    return remove_content(id)
