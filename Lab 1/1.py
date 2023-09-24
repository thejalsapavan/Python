import math as m
a=int(input("Enter the co ordinate of x^2 :"))
b=int(input("Enter the co ordinate of x :"))
c=int(input("Enter the constant value : "))
d=float(((b*b )-4*a*c))
d1=m.sqrt(d)
if(d>0):
    r1=float((-b+d1)/2*a)
    r2=float((-b-d1)/2*a)
    print("Roots are Real and distinct: ",r1,r2)
elif(d==0):
    r1=float((-b+d1)/2*a)
    print("Roots are Real and Egual : ",r1)
else:
    print("Roots are imaginary : ")

