import numpy as np
from backend.app.dal.recommendations_repository import RecommendationsRepository

class LinearContextualBanditService:
    def __init__(self):
        self.alpha = 0.1  # Learning rate

    def recommend_books(self, user_id):
        user_context = RecommendationsRepository.get_user_context(user_id)
        books = RecommendationsRepository.get_all_parameters()

        user_vector = np.array(user_context['preferences'])
        best_score = float('-inf')
        best_book = None

        for book in books:
            book_vector = np.array(book['parameters'])
            score = np.dot(user_vector, book_vector)

            if score > best_score:
                best_score = score
                best_book = book

        return best_book
