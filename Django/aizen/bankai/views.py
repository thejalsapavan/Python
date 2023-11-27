from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
v=0
flag=0
count=0
def display(request):
    return HttpResponse("Getsuga Tenshou")
def home(request):
    return render(request,"home.html")
def temp(request):
    return render(request,"shin.html")
def details(request):
    global v
    global flag
    v= int(request.GET["no"]) 
    return render (request,"Det.html")
def process(request):
    global flag
    global v
    flag=0
    count=0
    if(count<v):
        n=request.GET["nam"]
        a=request.GET["age"]
        ad=request.GET["ad"]
        p=request.GET["pno"]
        np=request.GET["np"]
        flag=1
        count=count+1
        tp = {'n': n, 'a': a, 'ad': ad, 'np': np, 'p': p, 'flag':flag}
        return render(request,"Det.html",tp)
    else:
        flag=2
        return render(request,"Det.html",{'flag':flag ,'v':v})

        