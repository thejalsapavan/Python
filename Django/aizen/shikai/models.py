from django.db import models

# Create your models here.
class Employee(models.Model):
    eid=models.IntegerField()
    nam=models.CharField(max_length=20)
    sal=models.IntegerField()
    ad=models.CharField(max_length=20)

