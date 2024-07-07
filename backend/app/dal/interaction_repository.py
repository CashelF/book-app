# app/dal/interaction_repository.py
from app.models.interaction_model import Interaction, InteractionType
from app.dal.database import db

class InteractionRepository:
    @staticmethod
    def add_interaction(user_id, book_id, interaction_type, timestamp, duration=None):
        interaction = Interaction(
            user_id=user_id,
            book_id=book_id,
            interaction_type=InteractionType(interaction_type),
            timestamp=timestamp,
            duration=duration if interaction_type == 'view' else None
        )
        db.session.add(interaction)
        db.session.commit()

    @staticmethod
    def get_all_interactions():
        return Interaction.query.all()

    @staticmethod
    def get_user_interactions(user_id):
        return Interaction.query.filter_by(user_id=user_id).all()