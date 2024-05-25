from app.dal.interaction_repository import add_interaction, get_interactions_by_content_id, get_user_interactions
from app.dal.interaction_repository import get_user_interactions as dal_get_user_interactions
from app.dal.user_repository import get_user_by_id
from app.dal.content_repository import get_content_by_id
from .bandits.thompson_sampling import bandit
from app.utils.context_utils import get_user_context
import numpy as np

def record_interaction(user_id, content_id, interaction_type, reward):
    user = get_user_by_id(user_id)
    content = get_content_by_id(content_id)
    context = get_user_context(user)

    if content.embedding is not None:
        embedding = np.frombuffer(content.embedding, dtype=np.float32)
        features = np.concatenate((context, embedding))
        bandit.update(content_id, reward, features)
    
    add_interaction(user_id, content_id, interaction_type, reward)

def get_interactions_for_content(content_id):
    return get_interactions_by_content_id(content_id)
    
def get_user_interactions(user_id):
    return dal_get_user_interactions(user_id)
