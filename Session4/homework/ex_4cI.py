a = int(input("input row: "))
b = int(input("input col: "))

for i in range (1,a+1):
    for j in range (1,b+1):
        if (i*j < 10):
            print("",i*j,end=" ")
        else:
            print (i*j,end=" ")
    print()
