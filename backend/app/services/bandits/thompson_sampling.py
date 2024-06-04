# app/services/bandits/thompson_sampling.py
import numpy as np
# TODO: check if this is the correct implementation
class ThompsonSamplingBandit:
    def __init__(self, n_actions, n_features):
        self.n_actions = n_actions
        self.n_features = n_features
        self.means = np.zeros((n_actions, n_features))
        self.precisions = np.ones((n_actions, n_features))
    
    def get_action(self, context):
        sampled_means = np.random.normal(self.means, 1 / np.sqrt(self.precisions))
        action_values = np.dot(sampled_means, context)
        return np.argmax(action_values)
    
    def update(self, action, reward, context):
        precision = self.precisions[action]
        mean = self.means[action]
        
        precision += np.outer(context, context)
        mean += reward * context
        
        self.precisions[action] = precision
        self.means[action] = mean / precision

# OpenAI GPT embeddings are 768 dimensions
embedding_dim = 768
user_context_dim = 13 # Update this value if the user context dimension changes
n_features = embedding_dim + user_context_dim
bandit = ThompsonSamplingBandit(n_actions=20, n_features=n_features) # TODO: Update n_actions to the number of book items automatically, use the same bandit as the recommendation service
