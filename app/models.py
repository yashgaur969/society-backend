from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    email_id = db.Column(db.String())
    password = db.Column(db.String())


class AccessTokenTable(db.Model):
    access_token = db.Column(db.String(), primary_key=True)


class Society(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    management_id = db.Column(db.Integer, db.ForeignKey('management.id'))
    society_type = db.Column(db.String())
    is_fenced = db.Column(db.String())
    is_guarded = db.Column(db.String())
    buildings = db.relationship('Building', backref='society', lazy=True)
    apartments = db.relationship('Apartment', backref='society', lazy=True)


class Building(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number_of_floors = db.Column(db.Integer)
    number_of_flats = db.Column(db.Integer)
    total_flats = db.Column(db.Integer)
    society_id = db.Column(db.Integer, db.ForeignKey('society.id'))


#
class Apartment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number_of_wings = db.Column(db.Integer)
    number_of_floors = db.Column(db.Integer)
    number_of_flats = db.Column(db.Integer)
    total_flats = db.Column(db.Integer)
    society_id = db.Column(db.Integer, db.ForeignKey('society.id'))


class Management(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    contact = db.Column(db.String())
    email_id = db.Column(db.String())
    societies = db.relationship('Society', backref='society', lazy=True)


