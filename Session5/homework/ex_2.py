
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory["pocket"] = ['seashell', 'strange berry', 'lint']
#in ra key + value trong dictionary
for key,value in inventory.items():
    print(key,":",value)

inventory['backpack'].remove('dagger') # xóa phân tử 'dagger' của key 'backpack' trong dictionary dưới dạng mảng
#in ra key + value trong dictionary
for key,value in inventory.items():
    print(key,":",value)

inventory['gold'] = [500,50] #them phan tu vao list trong dictionary
#in ra key + value trong dictionary
for key,value in inventory.items():
    print(key,":",value)
