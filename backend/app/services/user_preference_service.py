# app/services/user_preferences_service.py
import numpy as np
from app.dal.user_repository import UserRepository
from app.dal.book_repository import BookRepository

class UserPreferencesService:

    @staticmethod
    def generate_embedding(user_id):
        user = UserRepository.get_user_by_id(user_id)
        if not user:
            raise ValueError("User not found")

        saved_books = user.saved_books

        reading_history = UserRepository.get_user_reading_history(user_id)
        reading_history_books = [record.book for record in reading_history]

        all_books = saved_books + reading_history_books

        embeddings = [np.frombuffer(book.embedding, dtype=np.float32) for book in all_books if book.embedding is not None]

        if not embeddings:
            embedding_size = BookRepository.get_book_by_id(1).embedding.size
            random_embedding = np.random.rand(embedding_size).astype(np.float32)
            UserRepository.save_user_preferences_embedding(user_id, random_embedding)
            return random_embedding

        average_embedding = np.mean(embeddings, axis=0)

        UserRepository.save_user_preferences_embedding(user_id, average_embedding)

        return average_embedding