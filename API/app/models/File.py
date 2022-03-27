from datetime import datetime
from app.models.Users import Users
from mongoengine import Document, FileField, DateTimeField, BooleanField, StringField, ReferenceField
from mongoengine import CASCADE
from config import MONGO_DB_COMMON_ALIAS

class File(Document):
    fs = FileField()
    filename = StringField()
    public = BooleanField(default=True)
    owner = ReferenceField(Users, reverse_delete_rule=CASCADE)
    created = DateTimeField(default=datetime.now)
    meta = {'db_alias': MONGO_DB_COMMON_ALIAS, 'collection': 'files'}
