import math as m
def outer(x,n):
    ans=0
    for i in range(n):
        res=0
        o=m.pow(x,i)
        def inner():
            nonlocal res
            res=m.factorial(i)
        inner()
        re=o/res
        ans=ans+re
    return ans
x=int(input("Enter the value of x :"))
n=int(input("Enter the no of terms :"))
result=outer(x,n)
print("Value: ",result)
