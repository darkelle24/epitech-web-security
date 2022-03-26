import re
import datetime
from flask import request, jsonify, Blueprint
from flask_jwt_extended import create_access_token
from mongoengine.errors import ValidationError
from app.models.Users import Users, Users_account
from app.services.email.sender import validate_email_addr
from app.errors import *


register = Blueprint('register', __name__)


@register.route('/register', methods=['POST'])
def register_():
    body = request.get_json()
    if 'email' in body and Users.objects(email=body['email']):
        return email_already_exists(), 409
    if 'username' in body and Users.objects(username=body['username']):
        return username_already_exists(), 409
    if 'password' in body and not re.match(Users.password_strength(), body['password']):
        return password_invalid(), 403
    try:
        if (len(body) != 3):
            return register_field_invalid(), 403

        user_account = Users_account()
        user = Users(email=body.get('email'),
                     username=body.get('username'),
                     password=body.get('password'),
                     account=user_account)
        user.validate()
        user.password_hash()
        user = user.save()
        # validate_email_addr(user)

        return jsonify({"msg": "User successfully created"}), 201
    except ValidationError as error:
        return jsonify({'error': error._format_errors()}), 403
