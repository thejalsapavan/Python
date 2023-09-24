
#Reverse the words start with "I"
def Irevese():
    file=open("Story.txt",'r')
    s=file.read()
    y=s.split(" ")
    for i in y:
        if i.startswith("I"):
            ind=y.index(i)
            l=len(i)
            x=""
            while(l>0):
                x=x+i[l-1]
                l=l-1
            y.remove(i)
            y.insert(ind,x)
    z=" ".join(y)
    print(z)  

Irevese()

