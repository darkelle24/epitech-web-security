from flask import request, jsonify, Blueprint, make_response

from flask_jwt_extended import jwt_required, get_jwt_identity

from app.middleware.bouncer import admin_required
from app.models.Users import Users
from app.errors import *

admin_users = Blueprint('admin_users', __name__)


@admin_users.route('/users/<user_id>', methods=['GET'])
@jwt_required()
@admin_required
def list_users_(user_id):
    try:
        user = Users.objects(id=user_id).fields(
            password=False, account__is_active=False, created=False)
        return jsonify(user), 200
    except:
        return try_except_error(), 500
