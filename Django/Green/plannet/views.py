from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Staff

# Create your views here.
def home(request):
    return render(request,"home.html")
def insert(request):
    return render(request,"insert.html")
def New_staff(request):
    sid=request.GET["sid"]
    nam=request.GET["name"]
    eid=request.GET["emid"]
    ph=request.GET["mob"]
    ag=request.GET["age"]
    dpt=request.GET["dept"]
    s=Staff(stid=sid,namei=nam,mobile=ph,emid=eid,age=ag,dept=dpt)
    s.save()
    return render(request,"home.html")
def sr(request):
    return render(request,"S.html")
def Search(request):
    dt=request.GET["dpt"]
    n=request.GET["n"]
    try:
        x=Staff.objects.get(dept=dt,namei=n)
    except:
        return HttpResponse("<h1>No Staff Found</h1>")
    f={'n':x.namei,'id':x.stid,'e':x.emid,'p':x.mobile,'a':x.age,'d':x.dept}
    return render(request,"display.html",f)
def delt(request):
    dt=request.GET["dpt"]
    n=request.GET["n"]
    try:
        x=Staff.objects.get(dept=dt,namei=n)
    except:
        return HttpResponse("<h1>No Staff Found</h1>")
    x.delete()
    return HttpResponse("<h1>Deleted Successfully<h1>")
def up(request):
    dt=request.GET["id"]
    #n=request.GET["n"]
    try:
        x=Staff.objects.get(stid=dt)
    except:
        return HttpResponse("<h1>No Staff Found</h1>")
    e=request.GET["e"]
    p=request.GET["p"]
    x.emid=e
    x.mobile=p
    return HttpResponse("<h1>Updated Successfully<h1>")
def dispall(request):
    x=Staff.objects.all().values()
    li=[]
    for i in x:
        li.append(i)
    print(li)
    return render (request,"disp.html",{'data':li})

