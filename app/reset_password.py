import datetime

from flask import request, render_template
from flask_jwt_extended import create_access_token, decode_token
from flask_restful import Resource

from app.models import User
from services.mail_service import send_email


class ForgotPassword(Resource):
    def post(self):
        url = request.host_url + 'reset/'
        body = request.get_json()
        email_id = body.get('email_id')

        user = User.objects.get(email_id=email_id)
        expires = datetime.timedelta(hours=24)
        reset_token = create_access_token(str(user.id), expires_delta=expires)

        return send_email('User Please Reset Your Password',
                          sender='yashgaur@gmail.com',
                          recipients=[user.email_id],
                          text_body=render_template('email/reset_password.txt',
                                                    url=url + reset_token),
                          html_body=render_template('email/reset_password.html',
                                                    url=url + reset_token))


class ResetPassword(Resource):
    def post(self):
        url = request.host_url + 'reset/'
        body = request.get_json()
        reset_token = body.get('reset_token')
        password = body.get('password')

        user_id = decode_token(reset_token)['identity']

        user = User.objects.get(id=user_id)

        user.modify(password=password)
        user.hash_password()
        user.save()

        return send_email('[Society-Hub] Password reset successful',
                              sender='support@movie-bag.com',
                              recipients=[user.email_id],
                              text_body='Password reset was successful',
                              html_body='<p>Password reset was successful</p>')

