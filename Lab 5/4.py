#list of list
import palindrome as p
li=[ ]
n=int(input("Enter the size of outer list  : "))
ni=int(input("Enter the inner list size : "))
for i in range(n):
    temp=[ ]
    for j in range(ni):
        x=input("Enter the string : ")
        temp.append(x)
    li.append(temp)
for y in li:
    p.palindrome(y,ni-1)
