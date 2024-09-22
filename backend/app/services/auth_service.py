# app/services/auth_service.py
from app.models.user_model import User
from app.dal.user_repository import UserRepository
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token

bcrypt = Bcrypt()

class AuthService:
    @staticmethod
    def register_user(data):
        hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        new_user = User(username=data['username'], email=data['email'], password_hash=hashed_password)
        UserRepository.add_user(new_user)
        access_token = create_access_token(identity=new_user.id)
        return {'access_token': access_token}

    @staticmethod
    def login_user(data):
        user = UserRepository.get_user_by_email(data['email'])
        if user and bcrypt.check_password_hash(user.password_hash, data['password']):
            access_token = create_access_token(identity=user.id)
            return {'access_token': access_token, 
                    'username': user.username,
                    'email': user.email}
        return {'message': 'Invalid credentials'}
