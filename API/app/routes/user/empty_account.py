from flask import request, jsonify, Blueprint, make_response

from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models.Users import Users
from app.errors import *

from app.middleware.bouncer import ban_checking

account_empty = Blueprint('account_empty', __name__)


@account_empty.route('/', methods=['POST'])
@jwt_required()
@ban_checking
def me_():
    identity = get_jwt_identity()

    try:
        return jsonify({"message": "Account successfully Empty"}), 200
    except:
        return try_except_error(), 500
