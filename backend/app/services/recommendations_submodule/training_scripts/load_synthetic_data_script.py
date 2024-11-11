import sys
import os
import pandas as pd
import numpy as np
import random
import pickle

# Adjust the PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))

from app import create_app, db
from app.config import ProductionConfig
from app.models import User, Book, Interaction  # Ensure Interaction model is defined for user-book interactions
from app.dal.book_repository import BookRepository
from app.dal.recommendations_repository import RecommendationsRepository
from app.services.interaction_service import InteractionService
from app.services.user_service import UserService

# Define mapping from Goodreads ratings to interaction types and rewards
GOODREADS_TO_INTERACTION = {
    "it was amazing": ("save", 1.0),
    "really liked it": ("like", 0.7),
    "liked it": ("like", 0.5),
    "it was ok": ("view", 0.2),
    "did not like it": ("view", 0.0)
}

# Random user attribute settings
AGE_MEAN = 30
AGE_SD = 10
GENDERS = ['male', 'female']
MEAN_RATING = 4
STD_DEV_RATING = 0.5
NUM_BOOKS_LOG_MEAN = 2.5
NUM_BOOKS_LOG_STD_DEV = 1
THEMES = ['light', 'dark']
FONT_SIZE_MEAN = 14
FONT_SIZE_SD = 2
CTR_MEAN = 0.05
CTR_SD = 0.02
ENGAGEMENT_MEAN = 0.3
ENGAGEMENT_SD = 0.1

PICKLE_FILE_PATH = "synthetic_data.pkl"

def create_random_user(user_id):
    """Generate a user with random attributes and return the user instance."""
    user = User(
        id=user_id,
        username=f"user_{user_id}",
        email=f"email_{user_id}",
        password_hash="hashed_password",
        created_at=pd.Timestamp.now(),
        age=round(random.gauss(AGE_MEAN, AGE_SD)),
        gender=random.choice(GENDERS),
        location_latitude=random.uniform(-90, 90),
        location_longitude=random.uniform(-180, 180),
        average_rating = max(1, min(5, random.gauss(MEAN_RATING, STD_DEV_RATING))),
        number_of_books_read=max(0, int(random.lognormvariate(NUM_BOOKS_LOG_MEAN, NUM_BOOKS_LOG_STD_DEV))),
        theme=random.choice(THEMES),
        font_size=int(random.gauss(FONT_SIZE_MEAN, FONT_SIZE_SD)),
        click_through_rate=round(random.gauss(CTR_MEAN, CTR_SD), 2),
        engagement_rate=round(random.gauss(ENGAGEMENT_MEAN, ENGAGEMENT_SD), 2)
    )
    db.session.add(user)
    return user

def load_synthetic_data_from_csv(file_paths):
    # Initialize an empty list to accumulate data from all CSV files
    all_data = []

    for file_path in file_paths:
        # Load CSV data into a pandas DataFrame
        df = pd.read_csv(file_path)
        
        # Map ratings to interaction types and rewards
        df[['interaction_type', 'reward']] = df['Rating'].map(GOODREADS_TO_INTERACTION).apply(pd.Series)
        
        # Retrieve book IDs based on title (assume `get_book_by_title` exists in BookRepository)
        df['book_id'] = df['Name'].apply(lambda title: getattr(BookRepository.get_book_by_title(title), 'id', None))
        
        # Filter rows where book_id is found
        df = df.dropna(subset=['book_id'])
        
        # Convert to a list of tuples (user_id, book_id, interaction_type, reward)
        data = list(zip(df['ID'].astype(int), df['book_id'].astype(int), df['interaction_type'], df['reward']))
        
        # Append data from the current file to all_data
        all_data.extend(data)
        
        print(f"Loaded {len(data)} interactions from {file_path}")
    
    return all_data

def load_synthetic_data(file_paths):
    """Load synthetic data from a pickle file if available, otherwise from CSV and pickle it."""
    if os.path.exists(PICKLE_FILE_PATH):
        print("Loading synthetic data from pickle file...")
        with open(PICKLE_FILE_PATH, "rb") as f:
            synthetic_data = pickle.load(f)
    else:
        print("Loading synthetic data from CSV files...")
        synthetic_data = load_synthetic_data_from_csv(file_paths)
        # Save the loaded data to a pickle file for faster future loading
        with open(PICKLE_FILE_PATH, "wb") as f:
            pickle.dump(synthetic_data, f)
            print("Synthetic data saved to pickle file.")
    
    return synthetic_data

def populate_users_and_interactions(synthetic_data):
    existing_user_ids = set()
    
    for user_id, book_id, interaction_type, reward in synthetic_data:
        # Add user if not already added
        if user_id not in existing_user_ids:
            user = create_random_user(user_id)
            existing_user_ids.add(user_id)
        else:
            user = User.query.get(user_id)
        
        # Handle "saved" interactions separately using InteractionService
        if interaction_type == "save":
            UserService.add_reading_history(user_id, book_id)
            InteractionService.save_interaction(user_id, book_id)
        else:
            # Create a "like" or "view" interaction directly
            interaction = Interaction(
                user_id=user.id,
                book_id=book_id,
                interaction_type=interaction_type,
                duration=1 if interaction_type == "view" and reward == 0.2 else 0
            )
            db.session.add(interaction)
    
    # Commit all users and interactions at once for better performance
    db.session.commit()
    print(f"Inserted {len(existing_user_ids)} users and their interactions.")
    
if __name__ == '__main__':
    # Initialize Flask app context
    app = create_app(ProductionConfig)
    
    # List of CSV file paths
    csv_file_paths = [
        '../goodreads_data/user_rating_0_to_1000.csv',
        '../goodreads_data/user_rating_1000_to_2000.csv',
        '../goodreads_data/user_rating_2000_to_3000.csv',
        '../goodreads_data/user_rating_3000_to_4000.csv',
        '../goodreads_data/user_rating_4000_to_5000.csv',
        '../goodreads_data/user_rating_5000_to_6000.csv',
        '../goodreads_data/user_rating_6000_to_11000.csv'
    ]

    with app.app_context():
        # Load synthetic data from all CSV files
        synthetic_data = load_synthetic_data(csv_file_paths)
        
        if not synthetic_data:
            print("No data found in CSV files. Exiting.")
        else:
            # Start training with the combined synthetic data
            populate_users_and_interactions(synthetic_data)
