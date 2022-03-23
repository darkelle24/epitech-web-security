import re
import datetime
from flask import request, jsonify, Blueprint, make_response
from flask_jwt_extended import create_access_token
from mongoengine.errors import ValidationError
from app.models.Users import Users
from config import JWT_VALIDATION_KEY
from app.errors import *

import jwt

email = Blueprint('email', __name__)


@email.route('/validate/<token>', methods=['GET'])
def verify_email_(token):

    decoded = jwt.decode(token, JWT_VALIDATION_KEY, algorithms=["HS256"])

    user = Users.objects(id=decoded["user"]).first()

    if not user:
        return jsonify(email_does_not_exist()), 404

    if not user.email == decoded["email"]:
        return jsonify("Your email address does not match"), 403

    user.verify_email()

    return jsonify("Your email has been verified successfully"), 200
