# app/services/interaction_service.py
from app.dal.interaction_repository import add_interaction
from app.dal.interaction_repository import get_user_interactions as dal_get_user_interactions
from app.dal.interaction_repository import get_all_interactions as dal_get_all_interactions
from datetime import datetime

def record_interaction(user_id, book_id, interaction_type, duration=None):
    add_interaction(user_id, book_id, interaction_type, datetime.now(), duration)
    
def get_all_interactions():
    return dal_get_all_interactions()
    
def get_user_interactions(user_id):
    return dal_get_user_interactions(user_id)
