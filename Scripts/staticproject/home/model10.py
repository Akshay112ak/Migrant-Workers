from django.db import models
from . model1 import Home1
class Home10(models.Model):
    Worker=models.ForeignKey(Home1,on_delete=models.CASCADE,null=True,blank=True)
    CURRENTDATE=models.DateField(null=True)