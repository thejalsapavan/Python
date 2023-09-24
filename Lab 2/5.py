def calculate(l):
    h=[]
    t=[]
    pf=[]
    r=[]
    for k in range(0,len(l)):
        h.append(0.1*l[k])
        t.append(0.05*l[k])
        pf.append(0.04*l[k])
        r.append(0)
    def netsalary():
        for i in range(len(l)):
            r[i]=l[i]+h[i]+t[i]-pf[i]
    netsalary()
    return r

l=[ ]
print("Enter the number of Employees : ")
n=int(input())
print("Enter the salary of Employees : ")
for i in range(n):
    x=int(input())
    l.append(x)
rs=calculate(l)
print("The Net salary of the Employees are : ",rs)
