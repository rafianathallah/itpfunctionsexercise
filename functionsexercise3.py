def num_atoms(ew, aw = 196.97):
    m = ew / aw
    a = m * 6.022 * (10 ** 23)
    print(a)
    
num_atoms(10)
num_atoms(10, 12.001)
num_atoms(10, 1.008)