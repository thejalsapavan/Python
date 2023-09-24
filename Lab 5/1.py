#digitcounting using recursion
def digitcount(ps,count):
    if(ps>0):
        count=count+1
        count=digitcount(ps//10,count)
    return count
ps=int(input("Enter the number :"))

print("No of digits in given  number are :",digitcount(ps,0))
