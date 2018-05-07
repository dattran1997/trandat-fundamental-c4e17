from turtle import *

def draw_star(x,y,lenght):
    penup()
    setpos(x,y)
    pendown()
    for i in range (5):
        forward(lenght)
        right(144)

if __name__ == "__main__":
    draw_star(40,40,100)
    mainloop()
