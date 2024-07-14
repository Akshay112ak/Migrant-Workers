from django.db import models
from . model1 import Home1
from . model5 import SCHOME
class Home11(models.Model):
    Worker=models.ForeignKey(Home1,on_delete=models.CASCADE,null=True,blank=True)
    Scheme=models.ForeignKey(SCHOME,on_delete=models.CASCADE,null=True,blank=True)
    CURRENTDATE=models.DateField(null=True)