p=int(input("Enter the Physics marks : "))
c=int(input("Enter the Chemistry marks : "))
b=int(input("Enter the Biology marks : "))
m=int(input("Enter the Mathematics marks : "))
cp=int(input("Enter the Computer marks : "))
t=(p+c+cp+b+m)/500
if(t>=90):
    print("Grade A ")
elif(t>=80 and t<90):
    print("Grade B ")
elif(t>=70 and t<80):
    print("Grade C ")
elif(t>=60 and t<70):
    print("Grade D ")
elif(t>=40 and t<60):
    print("Grade E ")
else :
    print("Grade F ")
