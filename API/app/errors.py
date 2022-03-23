
# REGISTER

def email_already_exists():
    return {"error": "Resource already exists: ['email']"}


def username_already_exists():
    return {"error": "Resource already exists: ['username']"}

# LOGIN


def password_invalid():
    return {"error": "At least 1 uppercase, 1 lowercase, 1 number, 1 special: ['password']"}


def register_field_invalid():
    return {"error": "Invalid resource provided, expect: ['email', 'username', 'password']"}


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
