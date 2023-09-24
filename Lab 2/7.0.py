def gcd (a,b):
    if(b==0):
        return a
    else:
        return gcd(b,a%b)

def reverse(n):
    temp =0
    while(n!=0):
        d=n%10
        temp=temp*10 + d
        n=n//10
    return temp

a=int(input("a : "))
b=int(input("b : "))
r=gcd(a,b)
print("GCD : ",r)
n=int(input("Enter a number : "))
print("Reversed number : ",reverse(n))
