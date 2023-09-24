def STR_FNC(arg):
     if(len(arg)<2):
         print("Insufficient Length to process")
     elif(len(arg)==2):
        arg=arg+"ing"
        print("Modified String : ",arg)
     elif(len(arg)==3):
        c=arg[2]
        c=c+"ed"
        print("Modified String : ",c)
     else:
        n=len(arg)
        s=" "
        s=arg[0]+arg[1]
        s=s+arg[n-2]+arg[n-1]
        print("Modified String : ",s)

x='y'
while x=='y':
    arg=input("Enter the String : ")
    STR_FNC(arg)
    x=input("Enter y to continue : ")
