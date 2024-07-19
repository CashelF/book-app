import sys
import os

# Adjust the PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from openai import OpenAI
import numpy as np
from app import create_app
from app.dal.database import db
from app.models.book_model import Book
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def generate_embedding(text, model="text-embedding-3-small"):
   text = text.replace("\n", " ")
   return client.embeddings.create(input = [text], model=model).data[0].embedding

def store_embedding(book_id, embedding):
    embedding_array = np.array(embedding, dtype=np.float32)
    binary_embedding = embedding_array.tobytes()
    book = Book.query.get(book_id)
    book.embedding = binary_embedding
    db.session.commit()
    

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        # Fetch all book descriptions that don't have embeddings yet
        books = Book.query.filter(Book.embedding.is_(None)).all()
        for book in books:
            if book.description:
                embedding = generate_embedding(book.description)
                store_embedding(book.id, embedding)
                print(f"Stored embedding for book_id {book.id}")
