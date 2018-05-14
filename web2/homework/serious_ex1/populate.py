from models.collection import Customer
import mlab
from random import randint, choice
from faker import Faker

booleanlist = [True,False]

mlab.connect()

fake = Faker()
# print(fake.email())
for i in range (20):
    print("load data .....")
    #tạo collection ten Customer de luu du lieu
    #mongoengine tu tao collection neu ko có , còn nếu trùng sẽ tự tạo và để tên khác
    data = Customer(name = fake.name(),
                        gender = randint(0,1),
                        email= fake.email(),
                        phonenumber= fake.phone_number(),
                        job= fake.job(),
                        company=fake.company(),
                        contacted=choice(booleanlist))
    data.save() #cho collection save du lieu
