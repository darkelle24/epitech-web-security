
# REGISTER

def email_already_exists():
    return {"error": "Resource already exists: ['email']"}


def username_already_exists():
    return {"error": "Resource already exists: ['username']"}


def password_invalid():
    return {"error": "At least 1 uppercase, 1 lowercase, 1 number, 1 special: ['password']"}


def register_field_invalid():
    return {"error": "Invalid resource provided, expect: ['email', 'username', 'password']"}

# LOGIN


def login_invalid():
    return {"error": "Email or password invalid"}


def email_does_not_exist():
    return {"error": "Resource does not exist: ['email']"}


def login_field_invalid():
    return {"error": "Invalid resource provided, expect: ['email', 'password']"}

# TOKEN


def token_identity_invalid():
    return {"error": "Invalid resource provided ['token']"}


# GENERAL

def try_except_error():
    return {"error": "An error has occured, retry in a few minutes"}


def field_invalid_email():
    return {"error": "Invalid resource provided, expect: ['email']"}


def field_invalid_username():
    return {"error": "Invalid resource provided, expect: ['username']"}


def user_banned():
    return {"error": "Acces denied"}

# ADMIN


def admin_access_refused():
    return {"error": "Admin access denied"}


def user_already_banned():
    return {"error": "User already banned"}


def user_already_unbanned():
    return {"error": "User already unbanned"}


def user_already_op():
    return {"error": "User already op"}


def user_already_deop():
    return {"error": "User already deop"}

RESOURCE_NOT_FOUND = 'Resource not found'
RESOURCE_ALREADY_EXISTS = 'Resource already exists'
FRIEND_REQUEST_FAILED = 'Invalid friend request'
FRIEND_ACCEPT_FAILED = 'Invalid friend request accept'
FRIEND_DENY_FAILED = 'Invalid friend request deny'
FRIEND_DELETE_FAILED = 'Invalid friend request delete'
LOGIN_FAILED = 'Invalid email or password'
LOGIN_INVALID = 'Invalid resources provided, expect: email, password'
REGISTER_INVALID = 'Invalid resources provided, expect: email, username, password'
PASSWORD_INVALID = 'At least 8 chars with 1 uppercase, 1 lowercase, 1 number, 1 special'
POST_ADD_INVALID = 'Invalid resources provided, expect: content'
POST_ADD_FAILED = 'Invalid request: probably wrong image file given'
REQUEST_FORM_INVALID = 'Invalid request: content-type multipart/form-data expected'
REQUEST_JSON_INVALID = 'Invalid request: content-type application/json expected'
ALREADY_ADMIN = 'User has already admin access'
ADMIN_FAILED = 'Invalid request you must be admin'
BAN_ARGUMENT_INVALID = 'Invalid parameter [duration] - must be [0-9]*[d-h]'
UNLIKE_FAILED = 'Invalid unlike request'
MESSAGE_INVALID = 'Invalid resources provided, expect: content'
MESSAGE_FAILED = 'Invalid message request'
CHAT_FAILED = 'Invalid chat request'
