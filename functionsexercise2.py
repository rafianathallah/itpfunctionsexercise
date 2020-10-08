def calc_weight_on_planet(w, g = 23.1):
    m = w / 9.8
    wp = m * g
    print(wp)

calc_weight_on_planet(120, 9.8)
calc_weight_on_planet(120)
calc_weight_on_planet(120, 23.1)