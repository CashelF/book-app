# app/dal/user_repository.py
from app.models.user_model import User
from app.models.user_preferences_embedding_model import UserPreferencesEmbedding
from app.models.reading_history_model import ReadingHistory
from app.dal.database import db
from sqlalchemy.orm import joinedload

class UserRepository:
    
    @staticmethod
    def add_user(user):
        db.session.add(user)
        db.session.commit()

    @staticmethod
    def get_user_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def get_user_reading_history(user_id):
        return ReadingHistory.query.filter_by(user_id=user_id).options(joinedload(ReadingHistory.book)).all()

    @staticmethod
    def save_user_preferences_embedding(user_id, embedding):
        embedding_binary = embedding.tobytes()
        
        user_pref_embedding = UserPreferencesEmbedding.query.filter_by(user_id=user_id).first()
        if user_pref_embedding is None:
            user_pref_embedding = UserPreferencesEmbedding(user_id=user_id, embedding=embedding_binary)
        else:
            user_pref_embedding.embedding = embedding_binary
        
        db.session.add(user_pref_embedding)
        db.session.commit()