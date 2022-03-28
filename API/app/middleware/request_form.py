from functools import wraps
from flask import request, jsonify
from app.errors import REQUEST_FORM_INVALID

def request_form(function):
    @wraps(function)
    def decorated(*args, **kwargs):
        if not request.form:
            return jsonify({'error': REQUEST_FORM_INVALID}), 403
        return function(request.form, *args, **kwargs)
    return decorated
