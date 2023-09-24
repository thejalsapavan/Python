import math as m
x1=int(input("Enter the x1 value : "))
y1=int(input("Enter the y1 value : "))
x2=int(input("Enter the x2 value : "))
y2=int(input("Enter the y2 value : "))
d=(x2-x1)**2+(y2-y1)**2
dist=float(m.sqrt(d))
print("Distance : ",dist)
