def parking_charges(typ,hr):
    if typ=='c':
        r=10
    elif typ=='b':
        r=20
    else:
        r=5
    return hr*r
t=input("Enter the type of vechile :")
h=int(input("Enter the number of hours parked :"))
amount=parking_charges(t,h)
print("Amount charged :" ,amount)
