import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config(object):
    """Base Config Object"""
    DEBUG = True
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')

    # Flask-Mail Configuration with Mailtrap
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 587)) 
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'True').lower() == 'True'
    MAIL_USE_SSL = os.getenv('MAIL_USE_SSL', 'True').lower() == 'True'
    MAIL_USERNAME = os.getenv('5be7211a3e65db')
    MAIL_PASSWORD = os.getenv('4db0310eb85ab7')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', 'noreply@example.com')