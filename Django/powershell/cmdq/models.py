from django.db import models
# Create your models here.
class Std(models.Model):
    reg=models.IntegerField()
    name=models.CharField(max_length=20)

    def __str__(self):
        return str(self.reg)+"\n"+self.name+"\n"
