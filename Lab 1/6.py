print("Enter the size of the input : ")
n=int(input())
ps=0
ns=0
z=0
for i in range(n):
    ip=int(input("Enter the number : "))
    if(ip>0):
        ps=ip+ps
    elif(ip<0):
        ns=ns-ip
    else:
        z=z+1
print("Positive Integers Sum :",ps)
print("Negative Integers Sum :",ns)
print("Number of zeroes :",z)
