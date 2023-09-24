import math as m
def compute(r=1,h=2):
    volume=m.pi*r*r*h
    return volume
v=compute()
print("using default values : ",v)
print("Enter the radius and height of the cylinder : ")
a=int(input())
b=int(input())
vol=compute(a,b)
print("Volume of the the cylinder:",vol)

