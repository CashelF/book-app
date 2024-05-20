import sys
import os

# Adjust the PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.dal.database import engine, Base
import app.models # make sure all models are imported in app.models.__init__.py
from app import create_app
from app.config import DevelopmentConfig

def create_tables():
    app = create_app(DevelopmentConfig)
    with app.app_context():
        print("Registered tables:", Base.metadata.tables.keys())  # Debugging print statement
        Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    create_tables()
