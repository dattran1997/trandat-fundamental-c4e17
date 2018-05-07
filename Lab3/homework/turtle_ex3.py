from turtle import *

def square(lenght,colors):
    color(colors)
    for i in range (4):
        forward(lenght)
        left(90)

if __name__ == "__main__":
    lenght = int(input("enter lenght: "))
    colors = input("enter color: ")
    square(lenght,colors)
    mainloop()
