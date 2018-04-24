px =1
py =1
pxb =2
pyb =2
p = {'x':1,'y':1}
pb = {'x':2,'y':2}


loop=True
while loop:
    for y in range(4):
        for x in range(4):
            if (x == p['x'] and y == p['y']):
                print("P",end=" ")
            elif(x == pb['x'] and y == pb['y'] ):
                print("B",end=" ")
            elif(x == 1 and y == 3):
                print("G",end=" ")
            else:
                print("_",end=" ")
        print()

    option = input("your move ? W/A/S/D").upper()
    next_px = p['x']
    next_py = p['y']
    next_pxb = pb['x']
    next_pyb = pb['y']
    if (option == "D"):
        next_px += 1
    elif(option == "A"):
        next_px -= 1
    elif(option == "S"):
        next_py += 1
    elif(option == "W"):
        next_py -= 1


    if(pb['x'] == next_px and pb['y'] == next_py):
        if (option == "D"):
            next_pxb = next_pxb + 1
        elif(option == "A"):
            next_pxb = next_pxb - 1
        elif(option == "S"):
            next_pyb = next_pyb + 1
        elif(option == "W"):
            next_pyb = next_pyb - 1

    if(0<= next_pxb <4):
        pb['x'] = next_pxb

    if(0<= next_pyb <4):
        pb['y'] = next_pyb

    if(0<= next_px <4):
        p['x'] = next_px

    if(0<= next_py <4):
        p['y'] = next_py

    if( pb['x'] == 1 and pb['y'] == 3):
        print("congrat!")
        loop = False
