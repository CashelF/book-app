import sys
import os

# Adjust the PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

import numpy as np
from app import create_app
from app.dal.book_repository import BookRepository
from app.dal.interaction_repository import InteractionRepository
from app.dal.recommendations_repository import RecommendationsRepository
from app.services.recommendation_service import RecommendationService
import random

def train_bandits_sgd():
    # Hyperparameters
    learning_rate = 0.01
    epochs = 100
    batch_size = 1

    # Fetch all interactions
    interactions = InteractionRepository.get_all_interactions()
    num_interactions = len(interactions)

    for epoch in range(epochs):
        for _ in range(num_interactions // batch_size):
            # Randomly sample a batch of interactions
            batch_interactions = random.sample(interactions, batch_size)

            for interaction in batch_interactions:
                user_id = interaction.user_id
                user_vector = RecommendationsRepository.get_user_context(user_id)
                if user_vector is None:
                    print(f"User {user_id} has no context. Skipping.")
                    continue
                book_id = interaction.book_id
                interaction_type = interaction.interaction_type
                interaction_value = RecommendationService.calculate_reward(interaction_type, interaction.duration)

                # Load or initialize parameters for the book
                parameters = BookRepository.get_book_parameters(book_id)
                if parameters is None:
                    num_features = len(user_vector)
                    parameters = np.random.rand(num_features)

                # Prediction and error calculation
                prediction = np.dot(user_vector, parameters)
                error = prediction - interaction_value

                # Gradient calculation
                gradients = error * user_vector

                # Parameter update
                parameters -= learning_rate * gradients

                # Save updated parameters
                BookRepository.save_book_parameters(book_id, parameters)

        print(f"Epoch {epoch + 1}/{epochs} completed.")

if __name__ == '__main__':
    app = create_app()

    with app.app_context():
        train_bandits_sgd()
