import os
from datetime import timedelta

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_mongoengine import MongoEngine
from flask_cors import CORS

app = Flask(__name__)
CORS(app,   supports_credentials=True)

bcrypt = Bcrypt(app)

MONGO_DB_COMMON_ALIAS = 'db_common'

EMAIL_SENDER_ADDR = os.environ.get('EMAIL_ADDR')
EMAIL_SENDER_PASSWD = os.environ.get('EMAIL_PWD')

DATABASE_URL = os.environ.get('DATABASE_URL')
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
JWT_VALIDATION_KEY = os.environ.get('JWT_VALIDATION_KEY')

app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=30)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)

if JWT_SECRET_KEY:
    app.config['JWT_SECRET_KEY'] = JWT_SECRET_KEY
    jwt = JWTManager(app)

if DATABASE_URL:
    app.config['MONGODB_SETTINGS'] = [
        {'host': DATABASE_URL, 'alias': MONGO_DB_COMMON_ALIAS}]
    db = MongoEngine()
    db.init_app(app)
