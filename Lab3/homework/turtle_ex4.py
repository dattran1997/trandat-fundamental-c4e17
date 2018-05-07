from turtle_ex3 import square
from turtle import *

speed(0)
for i in range (30):
    square(i * 5,"red")
    left(17)
    penup()
    forward(i * 2)
    pendown()
mainloop()
