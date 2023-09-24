n=int(input("Enter the Number : "))
print("Factors are :")
for i in range(1,n+1):
    if((n%i)==0):
        print(i)
print("Prime Factors are :")
d=2
for i in range(1,n+1):
    while n % d == 0:
        print(d)
        n //=d
    d=d+1
         
