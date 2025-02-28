from flask import Flask
from flask_mail import Mail
from .config import Config  # Use a relative import

# Initialize Flask-Mail
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Load configuration from Config class

    # Initialize Flask-Mail with the app
    mail.init_app(app)

    # Import and register views
    from . import views
    app.register_blueprint(views.bp)

    return app
