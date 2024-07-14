from django.db import models
from . model1 import Home1
class Home18(models.Model):
    Worker=models.ForeignKey(Home1,on_delete=models.CASCADE,null=True,blank=True)
    file=models.FileField(upload_to='uploads/')
    