number = [1,6,8,1,2,1,5,6]
a = number.count(1)
print("num 1 appear",a,"time")

count = 0
for i in range (len(number)):
    if number[i] == 1:
        count = count + 1
print("num 1 appear",count,"time")
