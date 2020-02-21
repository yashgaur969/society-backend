from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String())
    gender = db.Column(db.String())
    user_email = db.Column(db.String())
    password_hash = db.Column(db.String())
