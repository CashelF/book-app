# app/__init__.py

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from app.dal.database import engine, Base
from app.api.auth_api import auth_bp
from app.api.user_api import user_bp
from app.api.content_api import content_bp
from app.config import DevelopmentConfig, TestingConfig, ProductionConfig
import os

bcrypt = Bcrypt()
db = SQLAlchemy()

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config_class)
    app.static_url_path = '/static'

    jwt = JWTManager(app)
    bcrypt.init_app(app)
    db.init_app(app)

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(user_bp, url_prefix='/api/user')
    app.register_blueprint(content_bp, url_prefix='/api')

    return app


config_class = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}.get(os.getenv('FLASK_ENV', 'development'), DevelopmentConfig)

app = create_app(config_class)