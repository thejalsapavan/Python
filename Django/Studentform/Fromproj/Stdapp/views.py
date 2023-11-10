from django.shortcuts import render

# Create your views here.
count=0
val=-1
flag=0

def home(request):
    return render(request,'home.html')
def getStudentDetails(request):
    global val
    global flag
    val=int(request.GET['no'])
    return render(request,"StudentDetails.html")
def createStudentObj(request):
    global count
    global val
    global flag
    count=count+1;
    if(count<=val):
        reg=request.GET["reg"]
        name=request.GET["nam"]
        m1=float(request.GET["m1"])
        m2=float(request.GET["m2"])
        avg=(m1+m2)/2
        obj={reg,name,avg}
        flag=1
        return render(request,"StudentDetails.html",{'flag':flag,'robj':reg,'nobj':name,'aobj':avg})
    else:
        flag=2
        return render(request,"StudentDetails.html",{'flag':flag,'Msg':"Morethan"+str(val)+"Objects Created"})
    
        
