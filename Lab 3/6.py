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

t.credit(de,500,6000)
t.credit(de,123,5000)
t.debit(de,1234,400)
