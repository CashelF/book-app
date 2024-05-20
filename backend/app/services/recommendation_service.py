from app.dal.book_repository import get_all_books
from thompson_sampling import ThompsonSamplingBandit
import numpy as np

# Initialize bandit with number of features (BERT embeddings are typically 768 dimensions)
n_features = 768
bandit = ThompsonSamplingBandit(n_actions=1000, n_features=n_features)

def get_user_context(user):
    # Example context vector (add more user features as needed)
    return np.array([
        user.age,
        1 if user.gender == 'male' else 0,
        1 if user.gender == 'female' else 0,
        user.location.latitude,
        user.location.longitude,
        user.reading_history.average_rating,
        user.reading_history.number_of_books_read,
        user.current_session.time_of_day,
        user.current_session.day_of_week,
        user.current_session.device_type
    ])

def get_recommendations_batch(user_id, start_index, batch_size):
    user = get_user_by_id(user_id)  # Assume a function that retrieves user data
    context = get_user_context(user)
    all_books = get_all_books()
    book_embeddings = np.array([book.embedding for book in all_books])
    bandit.n_actions = len(book_embeddings)

    # Get a batch of recommendations
    recommended_books = []
    for i in range(start_index, start_index + batch_size):
        action = bandit.get_action(context)
        recommended_book = all_books[action]
        recommended_books.append({
            "id": recommended_book.id,
            "title": recommended_book.title,
            "description": recommended_book.description,
            "cover_image": recommended_book.cover_image
        })
    
    return recommended_books

def record_interaction(user_id, book_id, interaction_type, reward):
    context = get_user_context(user_id)
    bandit.update(book_id, reward, context)
    add_interaction(user_id, book_id, interaction_type, reward)
