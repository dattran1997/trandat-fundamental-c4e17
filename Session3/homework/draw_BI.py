from turtle import *

colors = ["red","blue","brown","yellow","gray" ]

color(colors[0 ])
left(60)
forward(100)
right(120)
forward(100)

color(colors[1])
left(150)
forward(100)
for i in range (2):
    left(90)
    forward(100)


color(colors[2])
right(162)
forward(100)
for i in range (3):
    right(72)
    forward(100)

color(colors[3])
left(168)
forward(100)
for i in range (4):
    left(60)
    forward(100)

color(colors[4])
right(172)
forward(100)
for i in range (6):
    right(51.5)
    forward(100)


mainloop()
