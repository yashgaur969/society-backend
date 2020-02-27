import os


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'dsbgfwohgbr'
    MAIL_SERVER = 'localhost'
    MAIL_PORT = 2525

    DEBUG = True
