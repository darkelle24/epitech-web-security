from functools import wraps
from flask_jwt_extended import get_jwt_identity
from app.models.Users import Users
from app.errors import *


def admin_required(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        identity = get_jwt_identity()

        user = Users.objects(id=identity).first()
        if not user.account.is_admin:
            return admin_access_refused(), 401

        return func(*args, **kwargs)
    return decorator


def ban_checking(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        identity = get_jwt_identity()

        user = Users.objects(id=identity).first()
        if user.account.is_banned:
            return user_banned(), 401

        return func(*args, **kwargs)
    return decorator
