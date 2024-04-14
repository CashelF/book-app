from flask import Flask
from flask_cors import CORS
from app.config import Config

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config)
    app.static_url_path = '/static'

    from app.apis.user_api import user_bp
    from app.apis.image_api import image_bp
    from app.apis.ml_api import ml_bp

    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(image_bp, url_prefix='/api/images')
    app.register_blueprint(ml_bp, url_prefix='/api/ml')

    return app
