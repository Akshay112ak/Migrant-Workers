from django.db import models
from . model1 import Home1
from . model2 import Home2
class Home12(models.Model):
    Worker=models.ForeignKey(Home1,on_delete=models.CASCADE,null=True,blank=True)
    police=models.ForeignKey(Home2,on_delete=models.CASCADE,null=True,blank=True)
    CURRENTDATE=models.DateField(null=True)
    file=models.FileField(upload_to='uploads/')

