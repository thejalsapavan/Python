#Reverse the Special Characters
def Extract(fname):
    file=open(fname,'r')
    s=file.read()
    out=open("op4a.txt","w")
    x=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','t','s','u','v','w','x','y','z',0,1,2,3,4,5,6,7,8,9]
    y=s.split(" ")
    for i in y:
        s=i
        l=len(s)
        while(l>0):
            if s[l-1] not in x:
                out.write(s[l-1])
            l=l-1
      
            
n=input("Enter the file name with extension : ")
Extract(n)

