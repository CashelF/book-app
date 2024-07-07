import sys
import os

# Adjust the PYTHONPATH to include the project directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
from app import create_app
from app.dal.database import db
from app.models.book_parameters_model import BookParameters
from app.models.book_model import Book
from app.dal.user_repository import UserRepository
from app.dal.recommendations_repository import RecommendationsRepository

def generate_random_parameters(size):
    return np.random.rand(size).astype(np.float32)

def store_parameters_embedding(book_id, embedding):
    try:
        binary_embedding = embedding.tobytes()
        
        book_parameters = BookParameters.query.filter_by(book_id=book_id).first()
        if book_parameters is None:
            book_parameters = BookParameters(book_id=book_id, parameters=binary_embedding)
            db.session.add(book_parameters)
        else:
            book_parameters.parameters = binary_embedding
        
        db.session.commit()
        print(f"Stored parameters for book_id {book_id}")
    except Exception as e:
        db.session.rollback()
        print(f"Error storing parameters for book_id {book_id}: {e}")

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        # Fetch all books whose parameters embeddings are not yet populated
        books = Book.query.filter(
            ~BookParameters.query.filter(BookParameters.book_id == Book.id).exists()
        ).all()

        # Use an example user to determine the size of the user context vector
        example_user = UserRepository.get_user_by_id(1)
        if example_user:
            user_vector_size = len(RecommendationsRepository.get_user_context(example_user.id))

            for book in books:
                embedding = generate_random_parameters(user_vector_size)
                store_parameters_embedding(book.id, embedding)
        else:
            print("No example user found to determine user vector size.")
