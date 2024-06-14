# app/services/recommendation_service.py
from datetime import timedelta
from app.dal.recommendations_repository import RecommendationsRepository
import numpy as np

# Frequency capping duration (e.g., do not show the same book within 7 days)
FREQUENCY_CAPPING_DURATION = timedelta(days=7)

def get_recommendations(user_id):
    user_context = RecommendationsRepository.get_user_context(user_id)
    books_parameters = RecommendationsRepository.get_all_parameters()

    user_vector = np.array(user_context['preferences'])
    best_score = float('-inf')
    best_book_id = None

    for book_parameters in books_parameters:
        book_vector = np.array(book_parameters['parameters'])
        score = np.dot(user_vector, book_vector)

        if score > best_score:
            best_score = score
            best_book_id = book_parameters['id']

    return best_book_id