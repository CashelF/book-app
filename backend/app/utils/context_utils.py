# app/utils/context_utils.py
import numpy as np
import datetime

def get_user_context(user):
    """
    Create a context for the user, including the current day of the week.
    Returns:
        dict: User context with various attributes.
    """
    day_of_week = datetime.datetime.today().weekday()
    return np.array([
        user.age if user.age is not None else 30,
        1 if user.gender == 'male' else 0,
        1 if user.gender == 'female' else 0,
        user.location_latitude if user.location_latitude is not None else 0.0,
        user.location_longitude if user.location_longitude is not None else 0.0,
        user.average_rating if user.average_rating is not None else 3.0,
        user.number_of_books_read if user.number_of_books_read is not None else 0,
        day_of_week if day_of_week is not None else 0,
        user.device_type if user.device_type is not None else 'unknown',
        user.theme if user.theme is not None else 'light',
        user.font_size if user.font_size is not None else 'medium',
        user.click_through_rate if user.click_through_rate is not None else 0.0,
        user.engagement_rate if user.engagement_rate is not None else 0.0
    ])
