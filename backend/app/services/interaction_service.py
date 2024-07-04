# app/services/interaction_service.py
from app.dal.interaction_repository import InteractionRepository
from datetime import datetime

interaction_repository = InteractionRepository()

def record_interaction(user_id, book_id, interaction_type, duration=None):
    interaction_repository.add_interaction(user_id, book_id, interaction_type, datetime.now(), duration)
    
def get_all_interactions():
    return interaction_repository.dal_get_all_interactions()
    
def get_user_interactions(user_id):
    return interaction_repository.dal_get_user_interactions(user_id)
