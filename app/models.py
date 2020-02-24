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
    society_type = db.Column(db.String())
    is_fenced = db.Column(db.String())
    is_guarded = db.Column(db.String())
    buildings = db.relationship('Building', backref='society', lazy=True, uselist=False)


#
class Building(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number_of_floors = db.Column(db.Integer)
    number_of_flats = db.Column(db.Integer)
    total_flats = db.Column(db.Integer)
    society_id = db.Column(db.Integer, db.ForeignKey('society.id'), nullable=False)

#
# class Apartment(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     # society_id = db.Column(db.Integer, db.ForeignKey('SocietyDetails.society_id'), nullable=False)
#     number_of_wings = db.Column(db.Integer)
#     number_of_floors = db.Column(db.Integer)
#     number_of_flats = db.Column(db.Integer)
#     total_flats = db.Column(db.Integer)
#
#
# class Management(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     # society_id = db.Column(db.Integer, db.ForeignKey('SocietyDetails.society_id'), nullable=False)
#     name = db.Column(db.String())
#     contact = db.Column(db.String())
#     email_id = db.Column(db.String())
#
#
# # class AdditionalInfo(db.Model):
# #     management_id = db.Column(db.Integer, db.ForeignKey('ManagementContactInfo.management_id'), nullable=False)
# #     has_lift = db.Column(db.String())
# #     lift_capacity = db.Column(db.Integer)
# #     has_parking = db.Column(db.String())
# #     has_any_restriction = db.Column(db.String())
# #     restriction_start_time = db.Column(db.String())
# #     restriction_end_time = db.Column(db.String())
# #     entry_validation = db.Column(db.String())
# #     amenities = db.Column(db.String())
