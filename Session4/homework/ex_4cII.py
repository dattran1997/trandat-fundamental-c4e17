a = int(input("input row: "))
b = int(input("input col: "))

for i in range (a):
    for j in range (b):
        if ((i+j) % 2 == 0):
            print("1 ",end="")
        else:
            print ("0 ",end="")
    print()
