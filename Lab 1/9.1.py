def binarysearch(ar,e):
    l,r=0,len(ar)-1
    while(l<=r):
        m=(l+r)//2
        if(ar[m]==e):
            return m
        elif ar[m]<e:
            l=m+1
        else:
            r=m-1
    return -1

n= int(input("Enter the size of inputs : "))
li=[]
for i in range(n):
    no=int(input("Enter the data : "))
    li.append(no)
    
def bubblesort(ar):
    length=len(ar)
    for i in range(length):
        for j in range(0,n-i-1):
            if ar[j]>ar[j+1]:
                temp=ar[j]
                ar[j]=ar[j+1]
                ar[j+1]=temp
                
bubblesort(li)
print("Sorted order : ",li)
print("Enter the element to search : ")
s=int(input())
r=binarysearch(li,s);
if(r == -1):
    print("Element not found in list ")
else:
    print("Element found in the list ")
