import sys
import os

# Adjust the PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.dal.database import engine, Base
import app.models

def create_tables():
    print(Base.metadata.tables.keys())
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_tables()
