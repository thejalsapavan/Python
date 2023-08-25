import math as m
def outer(x,n):
    for i in range(1,n+1):
        res=1
        y=m.pow(2,i-1)
        o=m.pow(-1,i-1)*m.pow(x,2*(i-1))
    def inner():
        nonlocal y
        nonlocal res
        if(y==0):
            res*=1
        else:
            res*=y
            y=1
    inner()
    ans=0
    ans+=(o/res)
    return ans
x=int(input("Enter the value of x :"))
n=int(input("Enter the no of terms :"))
r=x*m.pi/180
result=outer(r,n)
print("Value: ",result)
        
