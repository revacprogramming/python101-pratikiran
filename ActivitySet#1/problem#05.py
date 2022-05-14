# Functions



def computepay(h, r):
    pay = h * r
    if h > 40 :
        pay += (h - 40) * (r/2)
    return pay

hrs = float(input("Enter hours? "))
rte = float(input("Enter rate per hour? "))

p = computepay(hrs, rte)
print("Pay", p)
