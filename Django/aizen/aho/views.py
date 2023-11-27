from django.shortcuts import render
from .models import hostel
from .forms import hostel_form
from django.http import *
v=0;
# Create your views here.
def display(request):
    form=hostel.objects.all()
    return render(request,'display.html',{'form':form})
def insert(request):
    la=hostel_form()
    if(request.method=="POST"):
        la=hostel_form(request.POST)
        if la.is_valid():
            la.save()
            return HttpResponseRedirect('/display/')
    return render(request,'insert.html',{'form':la})
def update(request):
    global v
    v =int(request.GET["puno"])
    la=hostel.objects.get(PhoneNumber=v)
    fr=hostel_form(instance=la)
    if(request.method=="POST"):
        fr=hostel_form(request.POST,instance=la)
        if fr.is_valid():
            fr.save()
            return HttpResponseRedirect('/display')
    return render(request,"update.html",context={"hostel":fr})
def delete(request):
    la=hostel.objects.all()
    la.delete()
    return HttpResponseRedirect('/display/')
def search(request):
    return render(request,"search.html")

