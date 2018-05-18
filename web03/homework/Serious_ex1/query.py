from models.service import Service
import mlab

mlab.connect()

item = Service.objects()

for i in item:
    if i is not None:
        i.delete() # lệnh xóa dictionary tìm thấy đc ( )
        print('item deleted ....')
    else:
        print("service not found")
