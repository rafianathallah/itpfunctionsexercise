def convert_temp():
    t = float(input("Enter a temperature in fahrenheit: "))
    print(t)
    tf = t
    print("The temperature in fahrenheit is:",tf)

    def convert_to_celcius():
        tc = (t - 32) * (5/9)
        print("The temperature in celcius is:",tc)
        
    def convert_to_kelvin():
        tk = (t - 32) * (5/9) + 273.15
        print("The temperature in kelvin is:",tk)
        
    convert_to_celcius()
    convert_to_kelvin()

convert_temp()
