from app.dal.content_repository import get_all_content
from bandits.thompson_sampling import bandit
from app.utils.context_utils import get_user_context
import numpy as np

def get_recommendations(user):
    context = get_user_context(user)
    all_content = get_all_content()
    recommendations = []

    for content in all_content:
        if content.embedding is not None:
            embedding = np.frombuffer(content.embedding, dtype=np.float32)
            features = np.concatenate((context, embedding))
            action_value = bandit.get_action(features)
            recommendations.append((action_value, content))

    recommendations.sort(reverse=True, key=lambda x: x[0])
    recommended_books = [rec[1] for rec in recommendations[:10]]  # Return top 10 recommendations

    return recommended_books
