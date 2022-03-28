from flask import request, jsonify, Blueprint, make_response

from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token

from app.models.Users import Users
from app.errors import *

login = Blueprint('login', __name__)


@login.route('/login', methods=['POST'])
def login_():
    body = request.get_json()
    if 'email' not in body or 'password' not in body or len(body) != 2:
        return jsonify(login_field_invalid()), 403
    user = Users.objects(email=body['email']).first()
    if not user:
        return jsonify(email_does_not_exist()), 404
    if not Users.password_check(user, body['password']):
        return login_invalid(), 401

    if user.account.is_banned:
        return user_banned(), 401

    access_token = create_access_token(identity=str(user.id))
    refresh_token = create_refresh_token(identity=str(user.id))

    user.verify_email()

    resp = make_response(({
        "access_token": access_token,
        "refresh_token": refresh_token
    }))

    resp.set_cookie('refresh_token', refresh_token)
    return resp, 200
