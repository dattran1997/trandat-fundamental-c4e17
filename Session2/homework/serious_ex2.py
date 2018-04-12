n = int(input("enter a number: "))
factorial = 1
factorial1n = 1

for i in range (1,n+1):
    factorial *= i

    factorial1n *= 1/i

print("n!= ",factorial)
print("(1/n)!= ",factorial1n)
