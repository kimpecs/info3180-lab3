from flask import Flask
from flask_mail import Mail
from .config import Config  
# Create the Mail object (but don't initialize it yet)
mail = Mail()

def create_app():
    """Application factory function."""
    app = Flask(__name__)

    # Load configuration from Config class
    app.config.from_object(Config)

    # Initialize Flask-Mail with the app
    mail.init_app(app)

    # Register blueprints or other app setup here
    from .views import bp
    app.register_blueprint(bp)

    return app
