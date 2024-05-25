from datetime import datetime, timedelta
from flask import session
from app.dal.content_repository import get_content_batch
from app.services.interaction_service import get_user_interactions
from .bandits.thompson_sampling import bandit
from app.utils.context_utils import get_user_context
import numpy as np

# Frequency capping duration (e.g., do not show the same book within 7 days)
FREQUENCY_CAPPING_DURATION = timedelta(days=7)

def get_recommendations(user, batch_size=10, num_recommendations=10):
    context = get_user_context(user)
    user_id = user.id
    session_key = f"user_{user_id}_recommendations"

    if session_key not in session:
        session[session_key] = []

    interactions = get_user_interactions(user_id)
    viewed_books = {interaction.content_id for interaction in interactions if interaction.timestamp > datetime.now() - FREQUENCY_CAPPING_DURATION}

    offset = 0
    recommendations = []

    while len(recommendations) < num_recommendations:
        content_batch = get_content_batch(batch_size=batch_size, offset=offset)
        if not content_batch:
            break
        
        batch_recommendations = []

        for content in content_batch:
            if content.id in viewed_books:
                continue  # Skip content that has been viewed recently
            
            if content.embedding is not None:
                embedding = np.frombuffer(content.embedding, dtype=np.float32)
                features = np.concatenate((context, embedding))
                print("SHAPES::::", embedding.shape, features.shape)
                action_value = bandit.get_action(features)
                batch_recommendations.append((action_value, content))

        recommendations.extend(batch_recommendations)
        offset += batch_size

    recommendations.sort(reverse=True, key=lambda x: x[0])

    # Store the recommendations in the session and update the viewed books
    recommended_books = [rec[1] for rec in recommendations[:num_recommendations]]
    session[session_key] = [rec[1].id for rec in recommendations[:num_recommendations]]

    return recommended_books
