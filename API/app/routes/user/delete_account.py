from flask import request, jsonify, Blueprint, make_response

from flask_jwt_extended import jwt_required, get_jwt_identity

from app.models.Users import Users
from app.errors import *

from app.middleware.bouncer import ban_checking

account_delete = Blueprint('account_delete', __name__)


@account_delete.route('/', methods=['POST'])
@jwt_required()
@ban_checking
def me_():
    identity = get_jwt_identity()

    try:
        user = Users.objects(id=identity)
        user.delete()
        return jsonify({"message": "Account successfully deleted"}), 200
    except:
        return try_except_error(), 500
