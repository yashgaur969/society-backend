from os import abort

from flask import request

from app import app, db
from app.models import User, AccessTokenTable, Society, Building, Apartment, Management
from flask_jwt_extended import create_access_token


@app.route('/hello-world')
def hello_world():
    return "hello world"


@app.route('/users/signup', methods=['POST'])
def new_user():
    if request.method == 'POST':
        first_name = request.json.get('first_name')
        last_name = request.json.get('last_name')
        email_id = request.json.get('email_id')
        password = request.json.get('password')
        # if first_name is None or password is None:
        #     abort()  # missing arguments
        # if User.query.filter_by(first_name=first_name).first() is not None:
        #     abort()  # existing user
        user = User(first_name=first_name, last_name=last_name, email_id=email_id, password=password)
        db.session.add(user)
        db.session.commit()
        return 'created new user {} with email {} '.format(user.first_name, user.email_id)


@app.route('/users/login', methods=['POST'])
def login():
    if request.method == 'POST':
        email_id = request.json.get('email_id')
        password = request.json.get('password')
        user = User.query.filter_by(email_id=email_id).first()
        if not user:
            return 'user with email {} does not exist'.format(email_id)
        if password == user.password:
            access_token = create_access_token(identity=user.email_id)
            access = AccessTokenTable(access_token=access_token)
            db.session.add(access)
            db.session.commit()
            return {
                'message': 'Logged in as {}'.format(user.email_id),
                'access_token': access_token
            }
        else:
            return 'wrong credentials'


@app.route('/users/logout/<access_token>', methods=['DELETE'])
def logout(access_token):
    if request.method == 'DELETE':
        AccessTokenTable.query.filter_by(access_token=access_token).delete()
        db.session.commit()
        return 'user successfully logout'


@app.route('/societyDetails', methods=['POST', 'GET'])
def society_details():
    if request.method == 'POST':
        society_type = request.json.get('society_type')
        is_fenced = request.json.get('is_fenced')
        is_guarded = request.json.get('is_guarded')
        new_society = Society(society_type=society_type, is_fenced=is_fenced, is_guarded=is_guarded)
        db.session.add(new_society)
        db.session.commit()
        return 'new society with given specifications is made'

    if request.method == 'GET':
        society_list = {}
        society = Society.query.all()                         # dictionary of all society rows
        society_object = [{"society_type": s.society_type,"is_fenced": s.is_fenced,"is_guarded": s.is_guarded} for s in society ]
        print(society_object)
        for s in society:
            society_list.update({s.id: {"society_type": s.society_type,
                                        "is_fenced": s.is_fenced,
                                        "is_guarded": s.is_guarded}})
        return {'data':society_object}


@app.route('/buildingDetails', methods=['POST'])
def building_details():
    if request.method == 'POST':
        number_of_floors = request.json.get('number_of_floors')
        number_of_flats = request.json.get('number_of_flats')
        total_flats = int(number_of_flats) * int(number_of_floors)
        new_building = Building(number_of_floors=number_of_floors, number_of_flats=number_of_flats,
                                total_flats=total_flats)
        db.session.add(new_building)
        db.session.commit()
        return 'new building with given specifications is made'


@app.route('/apartmentDetails', methods=['POST'])
def apartment_details():
    if request.method == 'POST':
        no_of_wings = request.json.get('no_of_wings')
        no_of_floors = request.json.get('no_of_floors')
        no_of_flats = request.json.get('no_of_flats')
        total_flats = int(no_of_flats) * int(no_of_floors) * int(no_of_wings)
        new_apartment = Apartment(number_of_wings=no_of_wings, number_of_floors=no_of_floors,
                                  number_of_flats=no_of_flats, total_flats=total_flats)
        db.session.add(new_apartment)
        db.session.commit()
        return 'new apartment with given specifications is made'


@app.route('/managementDetails', methods=['POST'])
def management_details():
    if request.method == 'POST':
        name = request.json.get('name')
        contact = request.json.get('contact')
        email_id = request.json.get('email_id')
        new_manager = Management(name=name, contact=contact, email_id=email_id)
        db.session.add(new_manager)
        db.session.commit()
        return 'new manager with given details; is made'
