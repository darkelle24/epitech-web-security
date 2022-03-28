from functools import wraps
from flask_jwt_extended import get_jwt_identity
from app.models.Users import Users

def token_optionnal(function):
    @wraps(function)
    def decorated(*args, **kwargs):
        user_id = get_jwt_identity()
        if user_id:
          user = Users.objects(id=user_id).exclude('password').first()
        else:
          return function('noauth', *args, **kwargs)
        return function(user, *args, **kwargs)
    return decorated
