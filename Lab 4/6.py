
def password(s):
    c=False
    si=False
    d=False
    sr=False
    if len(s)>=8 and len(s)<20 :
        for x in s:
            if ord(x)>=65 and ord(x)<=90:
                c=True
            elif ord(x)>=97 and ord(x)<=122:
                sr=True
            elif ord(x)>=48 and ord(x)<=57:
                d= True
            elif x=="*" or x=='$' or x=='#':
                si=True
    else:
        print("Password Length doesn't met Criteria ")
    if( si and c and d and sr):
        print("Password Accepted ")
    else:
        print("Password doesn't met Criteria ")
        print(si,c,d,sr)
st=input("Enter the password string : ")
password(st)
