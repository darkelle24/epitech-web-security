from flask import jsonify, Blueprint

from flask_jwt_extended import jwt_required

from app.middleware.bouncer import admin_required
from app.models.Users import Users
from app.errors import *

admin_users_ban = Blueprint('admin_users_ban', __name__)


@admin_users_ban.route('/users/<user_id>/ban', methods=['POST'])
@jwt_required()
@admin_required
def ban_user_(user_id):
    try:
        user = Users.objects(id=user_id).first()

        if user.account.is_banned:
            return user_already_banned(), 401
        user.ban_user()

        return jsonify({"message": "User has been banned"}), 200
    except:
        return try_except_error(), 500


@admin_users_ban.route('/users/<user_id>/unban', methods=['POST'])
@jwt_required()
@admin_required
def unban_user_(user_id):
    try:
        user = Users.objects(id=user_id).first()

        if not user.account.is_banned:
            return user_already_unbanned(), 401

        user.unban_user()

        return jsonify({"message": "User has been unbanned"}), 200
    except:
        return try_except_error(), 500
