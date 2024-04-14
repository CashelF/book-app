from flask import Blueprint, request, jsonify, abort
from app.models.user_model import User
from app.services.user_service import UserService
from app.utils.hashing_utils import hash_password, verify_password

user_bp = Blueprint('user_bp', __name__)
user_service = UserService()

@user_bp.route('/users', methods=['GET'])
def get_users():
    try:
        users = user_service.list_users()
        return jsonify([user.to_dict() for user in users]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    try:
        name = data['name']
        email = data['email']
        password = data['password']  # Assuming the request contains a password field
        hashed_password = hash_password(password)
        user = user_service.create_user(name, email, hashed_password)
        return jsonify(user.to_dict()), 201
    except KeyError:
        return jsonify({"error": "Missing name, email or password in request"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@user_bp.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    try:
        name = data.get('name')
        email = data.get('email')
        user = user_service.update_user(user_id, name, email)
        return jsonify(user.to_dict()), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except KeyError:
        return jsonify({"error": "Missing name or email in update data"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@user_bp.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        result = user_service.delete_user(user_id)
        return jsonify(result), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@user_bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    email = data['email']
    provided_password = data['password']

    user = user_service.get_user_by_email(email)
    if user is None:
        return jsonify({"error": "Invalid email or password"}), 401

    if verify_password(user.password, provided_password):
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"error": "Invalid email or password"}), 401

@app.route('/get-user', methods=['GET'])
def get_user():
    email = request.args.get('email')
    if not email:
        return jsonify({'error': 'Email parameter is required'}), 400
    try:
        user = user_service.get_user_by_email(email)
        return jsonify(user.to_dict()), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': 'Server error'}), 500