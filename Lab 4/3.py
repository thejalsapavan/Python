def pangram(s):
    a="abcdefghijklmnopqrstuvwxyz"
    for si in a:
        if si not in s.lower():
            return False
    return True
s=input("Enter the String : ")
q=pangram(s)
if(q):
    print("String is Pangram ")
else:
    print("Not a Pangram ")
        
