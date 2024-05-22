import openai
import numpy as np
from app import create_app
from app.dal.database import db
from app.models.content_model import Content

# OpenAI API key
openai.api_key = 'openai_api_key'

def generate_embedding(text):
    response = openai.Embedding.create(input=text, model="text-embedding-ada-002")
    return np.array(response['data'][0]['embedding'])

def store_embedding(content_id, embedding):
    binary_embedding = embedding.tobytes()
    content = Content.query.get(content_id)
    content.embedding = binary_embedding
    db.session.commit()
    

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        # Fetch all content descriptions that don't have embeddings yet
        contents = Content.query.filter(Content.embedding.is_(None)).all()
        for content in contents:
            if content.description:
                embedding = generate_embedding(content.description)
                store_embedding(content.id, embedding)
                print(f"Stored embedding for content_id {content.id}")
