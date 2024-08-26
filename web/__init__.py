from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from .config import Config  # Import the Config class


# Initialize extensions
db = SQLAlchemy()
mail = Mail()

# Create the Flask app instance
app = Flask(__name__)

# Load configuration from config.py
app.config.from_object(Config)

# Initialize extensions with the app
db.init_app(app)
mail.init_app(app)

# Import routes
from web import routes
from .utility import send_message
