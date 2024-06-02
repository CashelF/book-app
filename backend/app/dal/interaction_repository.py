# app/dal/interaction_repository.py
from app.models.interaction_model import Interaction
from app.dal.database import db

def add_interaction(user_id, content_id, interaction_type, reward):
    interaction = Interaction(
        user_id=user_id,
        content_id=content_id,
        interaction_type=interaction_type,
        reward=reward
    )
    db.session.add(interaction)
    db.session.commit()

def get_interactions_by_content_id(content_id):
    return Interaction.query.filter_by(content_id=content_id).all()

def get_user_interactions(user_id):
    return Interaction.query.filter_by(user_id=user_id).all()