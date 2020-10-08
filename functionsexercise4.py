def calc_new_height():
    cw = float(input("Enter the current width: "))
    print(cw)
    ch = float(input("Enter the current height: "))
    print(ch)
    ratio = cw / ch
    dw = float(input("Enter the desired width: "))
    print(dw)
    dh = float(dw / ratio)
    print("The corresponding height is: ",dh)
    
calc_new_height()
