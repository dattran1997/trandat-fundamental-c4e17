px =1
py =1
pxb =2
pyb =2
box= [{'x' :2, 'y' :2}, {'x':3, 'y':3}]

for b in box:
        while True:
            for y in range(4):
                for x in range(4):
                    if(x == b['x'] and y == b['y'] ):
                        print("B",end=" ")
                    if(x == px and y == py):
                        print("P",end=" ")
                    elif(x == 1 and y == 3):
                        print("G",end=" ")
                    else:
                        print("_",end=" ")
                print()

            option = input("your move ? W/A/S/D").upper()
            next_px = px
            next_py = py
            # next_pxb = pxb
            # next_pyb = pyb
            next_pxb = b['x']
            nexy_pyb = b['y']
            dx=0
            dy=0
            if (option == "D"):
                #next_px += 1
                dx = 1
            elif(option == "A"):
                #next_px -= 1
                dx = -1
            elif(option == "S"):
                #next_py += 1
                dy = 1
            elif(option == "W"):
                #next_py -= 1
                dy =-1

            next_px = next_px + dx
            next_py = next_py + dy

            if(pxb == next_px and pyb == next_py):
                next_pxb = next_pxb + dx
                next_pyb = next_pyb + dy

            if(0<= next_pxb <4):
                # pxb = next_pxb
                b['x'] = next_pxb

            if(0<= next_pyb <4):
                # pyb = next_pyb
                b['y'] = next_pyb

            if(0<= next_px <4):
                px = next_px

            if(0<= next_py <4):
                py = next_py
