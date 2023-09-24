e1=int(input("Enter the edge of triangle : " ))
e2=int(input("Enter the edge of triangle : " ))
e3=int(input("Enter the edge of triangle : " ))
if(e1==e2 and e2==e3):
    print("Equilateral")
elif(e1==e2 or e2==e3):
    print("Isosceles")
else:
    print("Scalene")
