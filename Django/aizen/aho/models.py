from django.db import models

# Create your models here.
class hostel(models.Model):
    name=models.CharField(max_length=20)
    Age=models.IntegerField()
    PhoneNumber=models.IntegerField()
    Address=models.CharField(max_length=50)
    nativePlace=models.CharField(max_length=20)
    
    def __str__(self):
        return str(self.id)+"\n"+self.name+str(self.age)+"\n"+str(self.phn)+"\n"+self.ad+"\n"+self.np