import Transaction as t
de=[]
n=int(input("Enter the no of customers : "))
for i in range(n):
    te=[]
    a=input("Enter the name of customer : ")
    b=int(input("Enter the Account Number:  "))
    c=float(input("Enter the Balance Amount : "))
    te.append(a)
    te.append(b)
    te.append(c)
    de.append(te)
print(de)
ni=int(input("Enter the no of transactions to be performed:"))
for i in range(ni):
    print("Enter the choice : \n1.Debit\n2.credit\n3.order")
    c=int(input())
    if c==1:
        s=int(input("Enter the Account No:"))
        am=float(input("Enter the amount to be debited:"))
        t.debit(de,s,am)
    elif c==2:
        s=int(input("Enter the Account No:"))
        am=float(input("Enter the amount to be credited:"))
        t.credit(de,s,am)
    else:
        t.order(de)
