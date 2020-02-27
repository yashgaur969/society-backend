import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'my-secret-key'
    MAIL_SERVER = 'localhost'
    MAIL_PORT = 2525

    DEBUG = True
