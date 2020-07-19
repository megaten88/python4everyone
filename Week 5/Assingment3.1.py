hrs = float(input("Enter hours: "))
rate = float(input("Enter rate: "))

if hrs<=40:
    print(hrs*rate)
elif hrs>40:
    extra = hrs - 40
    extrapay = extra*(rate*(1.5))
    print ((40*rate) + extrapay)