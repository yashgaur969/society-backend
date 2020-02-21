from os import abort

from flask import request

from app import app, db
from app.models import User


@app.route('/hello-world')
def hello_world():
    return "hello world"


@app.route('/users/signup', methods=['POST'])
def new_user():
    if request.method == 'POST':
        user_name = request.json.get('user_name')
        gender = request.json.get('gender')
        user_email = request.json.get('user_email')
        password_hash = request.json.get('password_hash')
        if user_name is None or password_hash is None:
            abort()  # missing arguments
        if User.query.filter_by(user_name=user_name).first() is not None:
            abort()  # existing user
        user = User(user_name=user_name, gender=gender, user_email=user_email, password_hash='password_hash')
        db.session.add(user)
        db.session.commit()
        return 'created new user {} with email {} '.format(user.user_name, user.user_email)
