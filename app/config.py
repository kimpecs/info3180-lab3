import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config(object):
    """Base Config Object"""
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')

    # Flask-Mail Configuration with Mailtrap
    MAIL_SERVER = "sandbox.smtp.mailtrap.io"
    MAIL_PORT = 2525
    MAIL_USERNAME = "e2914076f402dc"
    MAIL_PASSWORD = "fac7fde1847812"
    MAIL_USE_TLS = True  
    MAIL_USE_SSL = False  
