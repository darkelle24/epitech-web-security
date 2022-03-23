
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
