# app/services/interaction_service.py
from app.dal.interaction_repository import add_interaction, get_interactions_by_content_id, get_user_interactions
from app.dal.interaction_repository import get_user_interactions as dal_get_user_interactions
from datetime import datetime

def record_interaction(user_id, content_id, interaction_type, duration=None):
    add_interaction(user_id, content_id, interaction_type, datetime.now(), duration)

def get_interactions_for_content(content_id):
    return get_interactions_by_content_id(content_id)
    
def get_user_interactions(user_id):
    return dal_get_user_interactions(user_id)
