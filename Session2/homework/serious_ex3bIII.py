n = int(input("put in a number: "))
array = []

for i in range (n):
    if i % 2 == 0:
        array.append('x')
    else:
        array.append('*')

print(array)
