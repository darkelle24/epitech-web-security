from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from app.models.Users import Users
from app.errors import RESOURCE_NOT_FOUND

def token_valid(function):
    @wraps(function)
    def decorated(*args, **kwargs):
        user_id = get_jwt_identity()
        user = Users.objects(id=user_id).exclude('password').first()
        if not user:
            return jsonify({'user': RESOURCE_NOT_FOUND}), 404
        return function(user, *args, **kwargs)
    return decorated
