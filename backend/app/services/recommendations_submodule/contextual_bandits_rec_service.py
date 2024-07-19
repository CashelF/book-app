# app/services/recommendation_service.py
from datetime import timedelta
import numpy as np
from app.dal.recommendations_repository import RecommendationsRepository
from app.models.interaction_model import InteractionType

# Frequency capping duration (e.g., do not show the same book within 7 days)
FREQUENCY_CAPPING_DURATION = timedelta(days=7)

class ContextualBanditsRecommendationService:
    @staticmethod
    def get_recommendations(user_id, num_recommendations=1):
        books_parameters = RecommendationsRepository.get_all_parameters()

        user_vector = RecommendationsRepository.get_user_context(user_id)
        recommendations = []

        for book_parameters in books_parameters:
            if len(recommendations) >= num_recommendations:
                break
            book_vector = np.array(book_parameters['parameters'])
            score = np.dot(user_vector, book_vector)
            recommendations.append((book_parameters['id'], score))
            
        recommendations.sort(key=lambda x: x[1], reverse=True)
        
        print(user_vector)

        return [book_id for book_id, _ in recommendations]

    @staticmethod
    def calculate_reward(interaction_type, duration=None):
        if interaction_type == InteractionType.LIKE:
            return 0.5
        elif interaction_type == InteractionType.SAVE:
            return 1.0
        elif interaction_type == InteractionType.VIEW:
            if duration is None:
                raise ValueError("Duration must be provided for viewed interactions")

            max_duration = 300  # Cap at 5 minutes
            normalized_duration = min(duration, max_duration) / max_duration
            return normalized_duration
        else:
            raise ValueError("Unknown interaction type")