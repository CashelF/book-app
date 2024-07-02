# app/services/recommendation_service.py
from datetime import timedelta
import numpy as np
from app.dal.recommendations_repository import get_all_parameters
from app.dal.user_repository import UserRepository

user_repository = UserRepository()

# Frequency capping duration (e.g., do not show the same book within 7 days)
FREQUENCY_CAPPING_DURATION = timedelta(days=7)

def get_recommendations(user_id, num_recommendations=1):
    books_parameters = get_all_parameters()

    user_vector = get_user_vector(user_id)
    recommendations = []

    for book_parameters in books_parameters:
        if len(recommendations) >= num_recommendations:
            break
        book_vector = np.array(book_parameters.parameters)
        score = np.dot(user_vector, book_vector)
        recommendations.append((score, book_parameters['id']))

    return [book_id for _, book_id in recommendations]


def get_user_vector(user_id):
    user = user_repository.get_user_by_id(user_id)
    
    if not user:
        return np.array([])
    
    features = [
        user.age if user.age is not None else 0,
        1 if user.gender == 'male' else (2 if user.gender == 'female' else 0),
        user.location_latitude if user.location_latitude is not None else 0,
        user.location_longitude if user.location_longitude is not None else 0,
        user.average_rating if user.average_rating is not None else 0,
        user.number_of_books_read if user.number_of_books_read is not None else 0,
        1 if user.theme == 'dark' else 0,
        user.font_size if user.font_size is not None else 0,
        user.click_through_rate if user.click_through_rate is not None else 0,
        user.engagement_rate if user.engagement_rate is not None else 0
    ]

    user_vector = np.array(features, dtype=float)

    return user_vector