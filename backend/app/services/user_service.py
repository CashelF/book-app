# app/services/user_service.py
from app.dal.user_repository import get_user_by_id as dal_get_user_by_id

def get_user_by_id(user_id):
    return dal_get_user_by_id(user_id)
    