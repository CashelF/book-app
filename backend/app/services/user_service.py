# app/services/user_service.py
from app.dal.user_repository import get_user_by_id

def get_user_profile(user_id):
    user = get_user_by_id(user_id)
    return {
        'username': user.username,
        'email': user.email
    }, 200
