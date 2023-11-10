from django.shortcuts import render

def home(request):
    return render(request,"home.html")
def add(request):
    a=request.GET["a"];
    b=request.GET["b"];
    res=int(a)+int(b)
    return render(request,"result.html",{'Result':res})


# Create your views here.
