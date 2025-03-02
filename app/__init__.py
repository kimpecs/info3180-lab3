from flask import Flask
from flask_mail import Mail
from .config import Config  # Use a relative import
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Initialize Flask-Mail
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Load configuration from Config class

    # Initialize Flask-Mail with the app
    mail.init_app(app)

    # Import and register views
    from .views import bp  # Import the blueprint from views.py
    app.register_blueprint(bp)

    return app
