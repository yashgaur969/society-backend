
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_mail import Mail

from config import Config

app = Flask(__name__)
app.debug = True

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

jwt = JWTManager(app)
mail = Mail(app)
from app import routes, models

