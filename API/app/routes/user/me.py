from flask import request, jsonify, Blueprint, make_response

from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models.Users import Users
from app.errors import *

from app.middleware.bouncer import ban_checking

me = Blueprint('me', __name__)


@me.route('/me', methods=['GET'])
@jwt_required()
@ban_checking
def me_():
    identity = get_jwt_identity()

    try:
        user = Users.objects(id=identity).fields(
            id=False, password=False, account__is_active=False, created=False).first()
        return jsonify(user), 200
    except:
        return try_except_error(), 500
