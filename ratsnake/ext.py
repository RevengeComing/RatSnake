"""
Required flask extensions objects in RatSnake are created here.
"""

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()