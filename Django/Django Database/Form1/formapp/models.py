from django.db import models

# Create your models here.
# models.py
from django.db import models

class Employee(models.Model):
    empid = models.IntegerField()
    empname = models.CharField(max_length=20)
    empsalary = models.IntegerField()
    empaddress = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.id},{self.empid},{self.empname},{self.empsalary},{self.empaddress}"
