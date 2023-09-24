#Recursion 3
def maximum(l,n,m):
    if(n>=0):
        if(m<l[n-1]):
            m=l[n-1]
        m=maximum(l,n-1,m)
    return m
l=[ ]
n=int(input("Enter the size of List : "))
for i in range(n):
    x=int(input("enter the number : "))
    l.append(x)
print("Greatest Number :",maximum(l,n,-9999))
