li=[]
def rem_dup(li):
    n=len(li)
    i=0
    while i<n:
        if li[i]==li[i-1]:
            a=li[i]
            li.remove(a)
            n-=1
        else:
            i+=1


n=int(input("Enter the size of list : "))
for i in range(n):
    c=int(input("Enter the Element : "))
    li.append(c)      
rem_dup(li)
print( "After Removing : ",li)


            
    
    
    
