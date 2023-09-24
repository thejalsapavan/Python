def conver(s):
    li=[]
    li=s.split("-")
    li.sort()
    print('-'.join(li))
s=input("Enter the string: ")
conver(s)
