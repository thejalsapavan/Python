sname=[]
rollno=[]
cgpa=[]
def inputs():
    n=int(input("Enter the no of students :"))
    for i in range(n):
        x=input("Enter the name of the student :")
        sname.append(x)
        y=int(input("Enter the RollNo : "))
        rollno.append(y)
        z=float(input("Enter the CGPA :"))
        cgpa.append(z)
inputs()
def output():
    for i in range(len(sname)):
        print("Students Name : ",sname[i]," Roll No : ",rollno[i]," CGPA : ",cgpa[i])
output()
