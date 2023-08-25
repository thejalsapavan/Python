def credit(de,ac,amt):
    for i in range(0,len(de)):
        if ac in de[i]:
            de[i][2]=amt+de[i][2]
            print("Transaction successfull")
            break
    else:
        print("Account number not Found")
    print(de)
        
def debit(de,ac,amt):
    for i in range(0,len(de)):
        if ac in de[i]:
            if(de[i][2] >amt):
                de[i][2]=de[i][2]-amt
                print("Transaction successfull")
            else:
                print("Funds not Sufficient")
            break
    else:
        print("Account number not Found")
    print(de)

def order(de):
    n=len(de)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if de[j][2]>de[j+1][2]:
                temp=de[j][2];
                de[j][2]=de[j+1][2]
                de[j+1][2]=temp
    print(de)            
        
                                                        
    
    
