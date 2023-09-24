import math as m
e1=int(input("Enter the edge of triangle : " ))
e2=int(input("Enter the edge of triangle : " ))
e3=int(input("Enter the edge of triangle : " ))
s=float((e1+e2+e3)/2)
ar=float(m.sqrt((s*(s-e1)*(s-e2)*(s-e3))))
print("Area : ",ar)
