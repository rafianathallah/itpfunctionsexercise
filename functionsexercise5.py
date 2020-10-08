def convert_temp():
    t = float(input("Enter a temperature in fahrenheit: "))
    print(t)
    tf = t
    print("The temperature in fahrenheit is:",tf)
    tc = (t - 32) * (5/9)
    print("The temperature in celcius is:",tc)
    tk = tc + 273.15
    print("The temperature in kelvin is:",tk)

convert_temp()