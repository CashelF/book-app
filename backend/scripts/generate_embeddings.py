import sys
import os

# Adjust the PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from openai import OpenAI
import numpy as np
from app import create_app
from app.dal.database import db
from app.models.content_model import Content

client = OpenAI()

def generate_embedding(text, model="text-embedding-3-small"):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding

def store_embedding(content_id, embedding):
    embedding_array = np.array(embedding, dtype=np.float32)
    binary_embedding = embedding_array.tobytes()
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
