from mongoengine import StringField, IntField, BooleanField, Document


#design database
#create database
class Service(Document): # class + tên collection cần truy cập : dùng để truy cập collection nên tên cần giống tên collection
    name = StringField()
    yob =IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()
