# app/services/user_service.py
import numpy as np
from transformers import BertModel, BertTokenizer
from app.models.interaction_model import InteractionType
from app.dal.user_repository import UserRepository
from app.dal.reading_history_repository import ReadingHistoryRepository

# tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
# model = BertModel.from_pretrained('bert-base-uncased')

class UserService:
    
    # @staticmethod
    # def get_book_embedding(description):
    #     inputs = tokenizer(description, return_tensors='pt', truncation=True, padding=True, max_length=512)
    #     outputs = model(**inputs)
    #     embedding = outputs.last_hidden_state.mean(dim=1).detach().numpy()
    #     return embedding

    @staticmethod
    def generate_user_preference_embedding(user_id):
        user = UserRepository.get_user_by_id(user_id)
        
        if not user:
            return np.array([])
        
        reading_history = UserRepository.get_user_reading_history(user_id)
        
        book_embeddings = []
        for entry in reading_history:
            # Convert from binary to float32 array
            embedding = np.frombuffer(entry.book.embedding, dtype=np.float32)
            book_embeddings.append(embedding)
        
        if book_embeddings:
            book_embeddings = np.vstack(book_embeddings)
            user_embedding = np.mean(book_embeddings, axis=0)
        else:
            user_embedding = np.zeros((1536,), dtype=np.float32)
        
        UserRepository.save_user_preferences_embedding(user_id, user_embedding)

        return user_embedding


    @staticmethod
    def get_user_by_id(user_id):
        return UserRepository.get_user_by_id(user_id)
    
    @staticmethod
    def get_user_saved_books(user_id):
        user = UserRepository.get_user_by_id(user_id)
        return [book.to_dict() for book in user.saved_books]
    
    @staticmethod
    def get_user_liked_books(user_id):
        liked_books = UserRepository.get_user_liked_books(user_id)
        return [book.to_dict() for book in liked_books]
    
    @staticmethod
    def update_user_info(user_id, age, gender):
        UserRepository.update_user_info(user_id, age, gender)
        
    @staticmethod
    def add_reading_history(user_id, book_id):
        if not ReadingHistoryRepository.exists(user_id, book_id):
            ReadingHistoryRepository.add_reading_history(user_id, book_id)
        
    @staticmethod
    def delete_reading_history(user_id, book_id):
        ReadingHistoryRepository.delete_reading_history(user_id, book_id)
        