from mongoengine import StringField, IntField, BooleanField, Document

#định dạng collection
class Customer(Document): # class + tên collection đung để chọn collection cần dùng(collection:chữ vàng),document = dictionary
     name = StringField()
     gender = IntField()
     email = StringField()
     phonenumber = StringField()
     job = StringField()
     company = StringField()
     contacted = BooleanField()
