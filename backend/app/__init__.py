# app/__init__.py

from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from app.dal.database import db
from app.api.auth_api import auth_bp
from app.api.user_api import user_bp
from app.api.content_api import content_bp
from app.api.interaction_api import interaction_bp
from app.api.recommendation_api import recommendation_bp
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
    app.register_blueprint(user_bp, url_prefix='/api/user')
    app.register_blueprint(content_bp, url_prefix='/api/content')
    app.register_blueprint(interaction_bp, url_prefix='/api/interaction')
    app.register_blueprint(recommendation_bp, url_prefix='/api/recommendation')

    return app


config_class = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}.get(os.getenv('FLASK_ENV', 'development'), DevelopmentConfig)

app = create_app(config_class)