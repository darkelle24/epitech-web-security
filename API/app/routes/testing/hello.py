from flask import jsonify, Blueprint
from app.errors import *

testing = Blueprint('testing', __name__)


@testing.route('/hello', methods=['GET'])
def hello_():
    return jsonify({'msg': 'Hello, what can I do for you ?'}), 200
