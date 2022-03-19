from functools import wraps
from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity
from models.Bridges import Bridges
from models.Users import Users
from app.main import JWT_BRIDGE_KEY
import jwt
from app.middleware.errors import BRIDGE_NOT_FOUND, MISSING_TOKEN, INVALID_TOKEN

def bridge_access(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        if not request.headers.get('Authorization'):
            return jsonify({"error": MISSING_TOKEN}), 401
        
        token = request.headers.get('Authorization').split(' ')[1]
        try:
            decoded = jwt.decode(token, JWT_BRIDGE_KEY, algorithms=["HS256"])
        except:
            return jsonify({'error': INVALID_TOKEN}), 401    
        if not Bridges.objects(id=decoded['bridge']):
            return jsonify({'error': BRIDGE_NOT_FOUND}), 404
        

        bridge = Bridges.objects(id=decoded['bridge']).first()

        return func(bridge, *args, **kwargs)
    return decorator