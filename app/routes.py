from os import abort

from flask import request

from app import app, db
from app.models import User
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


@app.route('/users/login', methods=['GET'])
def login():
    if request.method == 'GET':
        email_id = request.json.get('email_id')
        password = request.json.get('password')
        user = User.query.filter_by(email_id=email_id).first()
        if not user:
            return 'user with email {} does not exist'.format(email_id)
        if password == user.password:
            access_token = create_access_token(identity=user.email_id)
            return {
                'message': 'Logged in as {}'.format(user.email_id),
                'access_token': access_token
            }
        else:
            return 'wrong credentials'
