# pos = [x,y]
# rec = [a,b,w,h]
def is_inside(pos,rec):
    if (rec[0] <= pos[0] <= (rec[0] + rec[2])) and (rec[1] <= pos[1] <= (rec[1] + rec[3])):
        print("is inside")
        return True
    else:
        print("is outside")
        return False
