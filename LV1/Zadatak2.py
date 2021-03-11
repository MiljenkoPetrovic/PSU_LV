
unos = -1.0

while(float(unos)>= 1.0 or float(unos)<0.00):
    unos=input("molim vas unesite broj izmedu 0.0 i 1.0\n")

if float(unos)>=0.9:
    print("A")
elif float(unos)>=0.8 and float(unos)<0.9:
    print("B")
elif float(unos)>=0.7 and float(unos)<0.8:
    print("C")
elif float(unos)>=0.6 and float(unos)<0.7:
    print("D")
else:
    print("F")
