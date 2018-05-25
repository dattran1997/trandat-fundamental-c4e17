from models.collection import Service
import mlab
from random import choice
from faker import Faker

mlab.connect()
status_list = [True,False]
fake = Faker()

while True:
    measurement_list = []

    name = input('enter  name: ')
    yob = input('enter yob (eg: 1990): ')
    gender = input('enter gender: ')
    height = input('enter height: ')
    address = input('enter address: ')
    image = input('enter image link: ')
    discription = input('enter discription: ')
    for i in range (3):
        size = input('enter measurement {0}:'.format(i+1))
        measurement_list.append(size)

    service = Service(name = name,
                    yob = yob,
                    gender = gender,
                    height = height,
                    phone = fake.phone_number(),
                    address = address,
                    status = choice(status_list),
                    image = image,
                    discription = discription,
                    measurement = measurement_list
                    )
    service.save()
    print('save data....')
    print('ctrl + c to stop')
