from datetime import datetime
from mongoengine import Document, EmbeddedDocument
from mongoengine import DateTimeField
from mongoengine.fields import BooleanField, EmbeddedDocumentField, EmailField, StringField
from config import MONGO_DB_COMMON_ALIAS
from config import bcrypt


class Users_account(EmbeddedDocument):
    is_active = BooleanField(default=False)
    is_email_verified = BooleanField(default=False)
    is_banned = BooleanField(default=False)
    is_admin = BooleanField(default=False)


class Users(Document):
    email = EmailField(unique=True, required=True, max_length=75)
    username = StringField(unique=True, required=True,
                           min_length=2, max_length=20)
    password = StringField(required=True, min_length=8, max_length=145)
    account = EmbeddedDocumentField(Users_account)
    profile_picture = StringField(required=False, max_length=300)
    created = DateTimeField(default=datetime.now)
    meta = {'db_alias': MONGO_DB_COMMON_ALIAS, 'collection': 'users'}

    @staticmethod
    def password_strength():
        return r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]"

    def password_hash(self):
        self.password = bcrypt.generate_password_hash(
            self.password).decode('utf8')

    def password_check(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def verify_email(self):
        self.account.is_email_verified = True
        self.save()

    def unverified_email(self):
        self.account.is_email_verified = False
        self.save()

    def ban_user(self):
        self.account.is_banned = True
        self.save()

    def unban_user(self):
        self.account.is_banned = False
        self.save()

    def op_user(self):
        self.account.is_admin = True
        self.save()

    def deop_user(self):
        self.account.is_admin = False
        self.save()
