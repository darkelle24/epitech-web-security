from app.routes.user.email import email
from app.routes.authentication.token import token
from app.routes.authentication.login import login
from app.routes.authentication.register import register
from app.routes.user.me import me
from app.routes.testing.hello import testing
from app.routes.admin.users import admin_users
from app.routes.admin.ban import admin_users_ban
from app.routes.admin.admin import admin_users_admin
from config import app
from werkzeug.exceptions import HTTPException
from flask import jsonify
import sys
import os
sys.path.append(os.path.abspath(os.path.join('.', 'app')))


app.register_blueprint(testing)

# AUTHENTICATION ROUTES
app.register_blueprint(register, url_prefix="/users")
app.register_blueprint(login, url_prefix="/users")
app.register_blueprint(token, url_prefix="/users/token")


# USERS ROUTES
app.register_blueprint(me, url_prefix="/users")
app.register_blueprint(email, url_prefix="/users/email")

# ADMIN ROUTES
app.register_blueprint(admin_users, url_prefix="/admin")
app.register_blueprint(admin_users_ban, url_prefix="/admin")
app.register_blueprint(admin_users_admin, url_prefix="/admin")


@app.errorhandler(Exception)
def handle_error(error):
    code = 500
    if isinstance(error, HTTPException):
        code = error.code
    return jsonify(error=str(error)), code


app.run(host="0.0.0.0")
