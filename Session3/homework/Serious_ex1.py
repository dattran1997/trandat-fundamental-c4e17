import sys
sys.stdout.write("\033[1;34m")

list = ["T-shirt"," Sweeter"]

while True:
    option = input("Welcome to our shop, what do you want (C, R, U, D)?")
    print("ctrl +c to exit !")
    if option == "R":
        print(*list, sep=", ")
    elif option == "C":
        create = input("Enter new item: ")
        list.append(create)
        print(*list, sep=", ")
    elif option == "U":
        position = int(input("Update position? "))
        new_item = input("New item? ")
        list[position-1] = new_item
        print(*list, sep=", ")
    elif option == "D":
        D_position = int(input("Delete position? "))
        del list[D_position - 1]
        print(*list, sep=", ")
    else:
        print("invalid function!")
