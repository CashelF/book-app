from flask import Flask
from flask_cors import CORS
from app.config import Config

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)
    app.static_url_path = '/static'

    from app.apis.user_api import user_bp

    app.register_blueprint(user_bp, url_prefix='/api/users')

    return app
