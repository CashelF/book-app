# app/config.py
import os
from dotenv import load_dotenv
import logging

# Load environment variables from a .env file if present
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', SECRET_KEY)
    
    if not SECRET_KEY:
        raise ValueError("No SECRET_KEY set for Flask application. Did you forget to set an environment variable?")
    if not JWT_SECRET_KEY:
        raise ValueError("No JWT_SECRET_KEY set for Flask application. Did you forget to set an environment variable?")
    
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://cashel:cashelpassword@localhost/bookapp"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_ECHO = False

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_ECHO = False
    LOGGING_LEVEL = logging.WARNING
