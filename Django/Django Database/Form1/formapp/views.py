from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import Employee_form
from .models import Employee

# Create your views here.

def display(request):
    form=Employee.objects.all()
    return render(request,'display.html',context={'form':form})
def insert_view(request):
    form=Employee_form()
    if request.method == "POST":
        form = Employee_form(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/display/')
    return render(request,'insert.html',context={'form':form})
def update_view(request, id):
    employee=Employee.objects.get(id=id)
    form=Employee_form(instance=employee)
    if request.method=="POST":
        form=Employee_form(request.POST,instance=employee)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/display/')
    return render(request,"update.html",context={"employee":form})
def delete_view(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return HttpResponseRedirect('/display/')
def home(request):
    return render(request,"home.html")
