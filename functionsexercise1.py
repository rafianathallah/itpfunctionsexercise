def convert_to_days():
    h = float(input("Enter number of hours: "))
    print(h)
    m = float(input("Enter number of minutes: "))
    print(m)
    s = float(input("Enter number of seconds: "))
    print(s)
    d = round(((h/24) + (m/1440) + (s/86400)), 4)
    print("The number of days is:",d)

convert_to_days()