# app/__init__.py

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from app.dal.database import db
from app.api.auth_api import auth_bp
from app.api.users_api import users_bp
from app.api.books_api import books_bp
from app.api.interactions_api import interactions_bp
from app.api.recommendations_api import recommendations_bp
from app.config import DevelopmentConfig, TestingConfig, ProductionConfig
import os

bcrypt = Bcrypt()
migrate = Migrate()

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(config_class)
    app.static_url_path = '/static'

    JWTManager(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    db.init_app(app)

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(users_bp, url_prefix='/api/users')
    app.register_blueprint(books_bp, url_prefix='/api/books')
    app.register_blueprint(interactions_bp, url_prefix='/api/interactions')
    app.register_blueprint(recommendations_bp, url_prefix='/api/recommendations')

    return app


config_class = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}.get(os.getenv('FLASK_ENV', 'development'), DevelopmentConfig)

app = create_app(config_class)