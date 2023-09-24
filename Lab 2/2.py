import math as m
def standard_Deviation(p):
    t=0
    s=0
    c=0
    for i in p:
        t=t+i
        c=c+1
    mean=t/c
    for i in p:
        s=s+(i-mean)*(i+mean)
    sd=m.sqrt(s/c)
    return sd
a=int(input("enter a num : "))
b=int(input("enter a num : "))
c=int(input("enter a num : "))
d=int(input("enter a num : "))
e=int(input("enter a num : "))
p=a,b,c,d,e
res=standard_Deviation(p)
print("SD : ",res)
