def computepay(hrs,rate):
    if hrs > 40:
        extra = hrs - 40
        extrapay = extra*(rate*(1.5))
        return ((40*rate) + extrapay)
    else:
        return hrs*rate

hrs = float(input("Enter hours:"))
rate= float(input("Enter rate per hour: "))
p = computepay(hrs,rate)
print("Pay",p)