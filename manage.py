from ratsnake.app import create_app
from flask_migrate import Migrate
from ratsnake.ext import db


app = create_app()
migrate = Migrate(app, db)