li=[]
def rem_dup(li):
    n=len(li)
    i=0
    for i in range(n):
        if(li[i]==li[i-1]):
            a=li[i]
            li.remove(a)
            
        
n=int(input("Enter the size of list : "))
for i in range(n):
    c=int(input("Enter the Element : "))
    li.append(c)      
print(li)
rem_dup(li)
print(li)


            
    
    
    
