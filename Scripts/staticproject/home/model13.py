from django.db import models
from . model1 import Home1
from . model5 import SCHOME
from . model11 import Home11
class Home13(models.Model):
    Worker=models.ForeignKey(Home1,on_delete=models.CASCADE,null=True,blank=True)
    Scheme=models.ForeignKey(SCHOME,on_delete=models.CASCADE,null=True,blank=True)
    applyscheme=models.ForeignKey(Home11,on_delete=models.CASCADE,null=True,blank=True)
    CURRENTDATE=models.DateField(null=True)
    file=models.FileField(upload_to='uploads/')
    payment_status=models.IntegerField(null=True)
    