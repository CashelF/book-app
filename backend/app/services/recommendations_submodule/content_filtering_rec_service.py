# app/services/content_based.py

import numpy as np
from numpy.linalg import norm
from app.dal.user_repository import UserRepository
from app.dal.book_repository import BookRepository

class ContentFilteringRecService:
    @staticmethod
    def cosine_similarity(a, b):
        return np.dot(a, b) / (norm(a) * norm(b))

    @staticmethod
    def get_content_based_recommendations(user_id):
        user_embedding = UserRepository.get_user_preferences_embedding(user_id)
        if user_embedding is None:
            return []

        book_embeddings = BookRepository.get_all_book_embeddings()
        similarities = []
        
        for book in book_embeddings:
            similarity = ContentFilteringRecService.cosine_similarity(user_embedding, book['embedding'])
            similarities.append((book['id'], similarity))

        similarities.sort(key=lambda x: x[1], reverse=True)
        
        recommendations = BookRepository.get_books_by_ids([book_id for book_id, _ in similarities])

        return recommendations
