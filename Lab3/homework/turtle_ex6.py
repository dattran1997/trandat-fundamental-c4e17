from turtle import *
from turtle_ex5 import draw_star

speed(0)
color('blue')
for i in range(1000):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)
