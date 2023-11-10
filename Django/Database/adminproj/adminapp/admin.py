from django.contrib import admin
from .models import Employee as Emp

admin.site.register(Emp)
#@admin.register(Emp)
class Employeeadmin(admin.ModelAdmin):
    list_display=('empid','empname','empaddress')
    list_filter=('empsalary')
    ordering=('empname',)
    search_feids=('empname',)
# Register your models here.
