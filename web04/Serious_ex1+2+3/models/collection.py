from mongoengine import IntField, StringField, BooleanField, ListField, Document

class Service(Document):
    name = StringField()
    yob =IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()
    image = StringField()
    discription =StringField()
    measurement =ListField()

class User(Document):
    username = StringField()
    password = StringField()
    email = StringField()
    fullname = StringField()

class Order(Document):
    serviceid = StringField()
    userid = StringField()
    is_accepted = BooleanField()
