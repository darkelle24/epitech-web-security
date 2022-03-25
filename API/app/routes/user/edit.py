import re
from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.Users import Users
from app.errors import *

from app.middleware.bouncer import ban_checking


edit = Blueprint('edit', __name__)


@edit.route('/', methods=['PUT'])
@jwt_required()
@ban_checking
def edit_():
    identity = get_jwt_identity()
    body = request.get_json()

    if not 'username' in body:
        return field_invalid_username(), 403
    try:
        user = Users.objects(id=identity).first()
        user.username = body['username']

        user.save()

        return jsonify({"msg": "Account successfully updated"}), 201
    except:
        return try_except_error(), 403


@edit.route('/password', methods=['PUT'])
@jwt_required()
@ban_checking
def edit_password_():
    identity = get_jwt_identity()
    body = request.get_json()

    if 'password' in body and not re.match(Users.password_strength(), body['password']):
        return password_invalid(), 403
    try:
        user = Users.objects(id=identity).first()
        user.password = body['password']

        user.password_hash()
        user.save()

        return jsonify({"msg": "Password successfully updated"}), 201
    except:
        return try_except_error(), 403


@edit.route('/email', methods=['PUT'])
@jwt_required()
@ban_checking
def edit_email_():
    identity = get_jwt_identity()
    body = request.get_json()

    if not 'email' in body:
        return field_invalid_email(), 403
    try:
        if Users.objects(email=body['email']):
            return email_already_exists(), 403

        user = Users.objects(id=identity).first()
        user.email = body['email']

        user.unverified_email()
        user.save()

        return jsonify({"msg": "Email successfully updated"}), 201
    except:
        return try_except_error(), 403
