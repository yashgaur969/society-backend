from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    email_id = db.Column(db.String())
    password = db.Column(db.String())


class AccessTokenTable(db.Model):
    access_token = db.Column(db.String(), primary_key=True)


# class SocietyDetails(db.Model):
#     society_type = db.Column(db.String())
#