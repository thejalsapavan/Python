#Extract lines from code
def LinesEx(f):
    file=open(f,'r')
    s=file.read()
    y=s.split(".")
    for i in y:
        print("Lines :",i+"\n")

    
n=input("Enter the file name with extension : ")
LinesEx(n)

