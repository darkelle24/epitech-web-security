from flask import jsonify, Blueprint

from flask_jwt_extended import jwt_required

from app.middleware.bouncer import admin_required
from app.models.Users import Users
from app.errors import *

admin_users_admin = Blueprint('admin_users_admin', __name__)


@admin_users_admin.route('/users/<user_id>/op', methods=['POST'])
@jwt_required()
@admin_required
def deop_user_(user_id):
    try:
        user = Users.objects(id=user_id).first()

        if user.account.is_admin:
            return user_already_op(), 401

        user.op_user()

        return jsonify({"message": "User has been op"}), 200
    except:
        return try_except_error(), 500


@admin_users_admin.route('/users/<user_id>/deop', methods=['POST'])
@jwt_required()
@admin_required
def op_user_(user_id):
    try:
        user = Users.objects(id=user_id).first()

        if not user.account.is_admin:
            return user_already_deop(), 401

        user.deop_user()

        return jsonify({"message": "User has been deop"}), 200
    except:
        return try_except_error(), 500
