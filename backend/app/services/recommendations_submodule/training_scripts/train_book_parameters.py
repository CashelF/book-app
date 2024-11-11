import sys
import os

# Adjust the PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))

import numpy as np
from app import create_app
from app.config import ProductionConfig
from app.dal.book_repository import BookRepository
from app.dal.interaction_repository import InteractionRepository
from app.dal.recommendations_repository import RecommendationsRepository
from app.services.recommendations_submodule.contextual_bandits_rec_service import ContextualBanditsRecommendationService
import random


def train_bandits_sgd():
    # Hyperparameters
    learning_rate = 0.01
    epochs = 10
    batch_size = 100

    # Fetch all interactions and all book parameters at once
    interactions = InteractionRepository.get_all_interactions()
    num_interactions = len(interactions)
    
    # Fetch all book parameters at once
    all_book_parameters = BookRepository.get_all_book_parameters_dict()

    for epoch in range(epochs):
        epoch_loss = 0
        total_predictions = 0
        
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
                interaction_value = ContextualBanditsRecommendationService.calculate_reward(interaction_type, interaction.duration)

                # Get the parameters for the current book from all_book_parameters
                parameters = all_book_parameters.get(book_id)
                if parameters is None:
                    parameters = user_vector.astype(np.float32)
                if isinstance(parameters, (bytes, str)):
                    parameters = np.frombuffer(parameters, dtype=np.float32).copy()
                
                # Normalize user_vector and parameters
                user_vector = user_vector / np.linalg.norm(user_vector)
                parameters = parameters / np.linalg.norm(parameters) if np.linalg.norm(parameters) != 0 else parameters

                # Prediction and error calculation
                prediction = np.dot(user_vector, parameters)
                error = prediction - interaction_value
                error = np.clip(error, -1e5, 1e5)
                epoch_loss += error ** 2
                total_predictions += 1
                
                # Gradient calculation and parameter update
                gradients = np.clip(error * user_vector, -1e3, 1e3)
                parameters -= learning_rate * gradients

                # Update the parameters in-memory
                all_book_parameters[book_id] = parameters

        # Save all updated parameters back to the database in one batch
        BookRepository.save_all_book_parameters_dict(all_book_parameters)
        
        
        avg_loss = epoch_loss / total_predictions
        print(f"Epoch {epoch + 1}/{epochs} completed. Avg Loss: {avg_loss:.4f}")

if __name__ == '__main__':
    app = create_app(ProductionConfig)

    with app.app_context():
        train_bandits_sgd()
