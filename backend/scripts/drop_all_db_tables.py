import sys
import os

# Adjust the PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.dal.database import db
from app import create_app

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all() 