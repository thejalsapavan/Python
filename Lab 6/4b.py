#Extract all charactes at multiples of 5 places
def Extract(fname):
    file=open(fname,'r')
    s=file.read()
    out=open("op4b.txt","w")
    y=s.split(" ")
    for i in y:
        s=i
        l=len(s)
        l=l-1
        while(l%5==0):
            out.write(s[l])
            l=l-1
      
            
n=input("Enter the file name with extension : ")
Extract(n)

