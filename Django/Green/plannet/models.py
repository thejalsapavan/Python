from django.db import models

# Create your models here.
class Staff(models.Model):
    stid=models.IntegerField()
    namei=models.CharField(max_length=20)
    age=models.IntegerField()
    mobile=models.IntegerField()
    emid=models.CharField(max_length=20)
    dept=models.CharField(max_length=5)

    def __str__(self):
        return str(self.stid)+"\n"+self.namei+"\n"+str(self.mobile)+"\n"+self.emid+"\n"+self.dept
