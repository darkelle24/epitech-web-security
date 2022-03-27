from datetime import datetime
from mongoengine import CASCADE
from mongoengine import Document, DateTimeField, BooleanField, ReferenceField, ListField, FileField
from config import MONGO_DB_COMMON_ALIAS
from app.models.Users import Users

class File(Document):
    fs = FileField()
    public = BooleanField(default=False)
    owner = ReferenceField(Users, reverse_delete_rule=CASCADE)
    created = DateTimeField(default=datetime.now)
    meta = {'db_alias': MONGO_DB_COMMON_ALIAS, 'collection': 'files'}
