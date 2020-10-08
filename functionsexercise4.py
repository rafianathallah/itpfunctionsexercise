def calc_new_height():
    cw = float(input("Enter the current width: "))
    print(cw)
    ch = float(input("Enter the current height: "))
    print(ch)
#ratio is 10:7 i think???? idk how this works
    dw = float(input("Enter the desired width: "))
    print(dw)
    dh = float((dw / 10) * 7)
    print("The corresponding height is: ",dh)
    
calc_new_height()