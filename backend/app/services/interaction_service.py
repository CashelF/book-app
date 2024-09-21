from app.dal.interaction_repository import InteractionRepository
from app.dal.user_repository import UserRepository
from datetime import datetime

class InteractionService:
    
    @staticmethod
    def save_interaction(user_id, book_id):
        InteractionRepository.add_interaction(user_id, book_id, 'save', datetime.now())
        UserRepository.add_user_saved_book(user_id, book_id)

    @staticmethod
    def unsave_interaction(user_id, book_id):
        # TODO: Add unsave interaction
        UserRepository.remove_user_saved_book(user_id, book_id)

    @staticmethod
    def like_interaction(user_id, book_id):
        InteractionRepository.add_interaction(user_id, book_id, 'like', datetime.now())

    @staticmethod
    def view_interaction(user_id, book_id, duration=None):
        InteractionRepository.add_interaction(user_id, book_id, 'view', datetime.now(), duration)

    @staticmethod
    def get_all_interactions():
        return InteractionRepository.dal_get_all_interactions()
        
    @staticmethod
    def get_user_interactions(user_id):
        return InteractionRepository.dal_get_user_interactions(user_id)
