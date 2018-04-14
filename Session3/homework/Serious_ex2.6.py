import sys
sys.stdout.write("\033[1;34m")

list = [5,7,300,90,24,50,75]
list_max = []

while True :
    print("hello, my name is dat, these are my ship sizes: ", list)
    max1 = max(list)
    list_max.append(max1)
    print("now my biggest ship has size ",max1," let shear it !")
    index = list.index(max1)
    list[index] = 8
    print("After shearing here is my flock: ",list)


    n = int(input("input number of Month: "))
    print("ctrl + c to exit")
    for i in range (n):
        for j in range (7):
             list[j] += 50 # tăng mỗi số lên 50
        print("Month ",i+1)
        print("one month has passed, now here is my flock", list)
        max_for = max(list)
        list_max.append(max_for) # gán số max vào mảng
        index_max = list.index(max_for) #tìm địa chỉ số max
        print("Now my biggest ship has the sizes ",max(list)," let's shear it !")
        list[index_max] = 8 #gán số max = 8
        print("After shearing here is my flock",list)

    Total = sum(list_max)
    Price = Total * 2
    print("My flock has size in total",Total)
    print(Total,"* 2$ =",Price," $")

    print()
    print("press ctrl + c to exit")
