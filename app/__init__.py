from flask import Flask

from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.debug = True

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# app.config['JWT_SECRET_KEY'] = 'sdfjbpsibvaebfbh'
jwt = JWTManager(app)



from app import routes, models
