from app.dal.database import db
from app.models.user_model import User
from app.models.book_model import Book
from app.models.book_parameters_model import BookParameters
import numpy as np

class RecommendationsRepository:
    @staticmethod
    def get_user_context(user_id):
        user = User.query.get(user_id)
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

        user_vector = np.array(features, dtype=float).flatten()

        return user_vector
        
    @staticmethod
    def get_all_parameters():
        books = Book.query.all()
        return [{'id': book.id, 'title': book.title, 'parameters': np.frombuffer(book.parameters.parameters, dtype=np.float32)} for book in books]

    @staticmethod
    def update_book_parameters(book_id, parameters):
        book_parameters = BookParameters.query.filter_by(book_id=book_id).first()
        book_parameters.parameters = parameters
        db.session.commit()
