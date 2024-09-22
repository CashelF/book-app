# app/dal/user_repository.py
import numpy as np
from sqlalchemy import func
from app.models.user_model import User
from app.models.book_model import Book
from app.models.interaction_model import Interaction, InteractionType
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
        
    @staticmethod
    def add_user_saved_book(user_id, book_id):
        user = User.query.get(user_id)
        if not user:
            raise ValueError(f"User with id {user_id} not found")

        book = Book.query.get(book_id)
        if not book:
            raise ValueError(f"Book with id {book_id} not found")

        if book not in user.saved_books:
            user.saved_books.append(book)
            db.session.commit()
        else:
            print("Book already saved")
            
    @staticmethod
    def remove_user_saved_book(user_id, book_id):
        user = User.query.get(user_id)
        if not user:
            raise ValueError(f"User with id {user_id} not found")

        book = Book.query.get(book_id)
        if not book:
            raise ValueError(f"Book with id {book_id} not found")

        if book in user.saved_books:
            user.saved_books.remove(book)
            db.session.commit()
            
    @staticmethod
    def get_user_liked_books(user_id):
        latest_interaction_subquery = (
            db.session.query(
                Interaction.book_id,
                func.max(Interaction.timestamp).label('latest_interaction_time')
            )
            .filter(Interaction.user_id == user_id)
            .group_by(Interaction.book_id)
            .subquery()
        )

        # Main query to get books with latest interaction being 'like'
        return db.session.query(Book).join(Interaction, Interaction.book_id == Book.id).join(
            latest_interaction_subquery, 
            latest_interaction_subquery.c.book_id == Interaction.book_id
        ).filter(
            Interaction.timestamp == latest_interaction_subquery.c.latest_interaction_time,
            Interaction.interaction_type == 'like'
        ).all()
            
    @staticmethod
    def update_user_info(user_id, age, gender):
        user = User.query.get(user_id)
        if not user:
            raise ValueError(f"User with id {user_id} not found")
        if age is not None:
            user.age = int(age)
        if gender is not None:
            user.gender = gender
        db.session.commit()
        
    @staticmethod
    def get_user_preferences_embedding(user_id):
        user_pref_embedding = UserPreferencesEmbedding.query.filter_by(user_id=user_id).first()
        if user_pref_embedding is None:
            return None
        return np.frombuffer(user_pref_embedding.embedding, dtype=np.float32)