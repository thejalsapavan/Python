sl=int(input("Enter the basic pay : "))
if(sl<=10000):
    hra=float((0.2*sl))
    da=float((0.8*sl))
elif(sl<=20000 and sl>10000):
    hra=float((0.25*sl))
    da=float((0.9*sl))
else:
     hra=float((0.3*sl))
     da=float((0.95*sl))
print("Gross salary : ",sl+hra+da)
