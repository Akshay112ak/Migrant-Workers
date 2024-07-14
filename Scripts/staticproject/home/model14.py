from django.db import models
from . model5 import SCHOME
from . model3 import Home3
class Home14(models.Model):
    Nameoncard=models.CharField(max_length=255)
    Cardnumber=models.IntegerField(null=True)
    CVV=models.IntegerField(null=True)
    Expiredate=models.CharField(max_length=255)
    Claimscheme=models.ForeignKey(SCHOME,on_delete=models.CASCADE,null=True,blank=True)
    Amount=models.IntegerField(null=True)
    Date=models.DateField(null=True)
    Insuranceagency=models.ForeignKey(Home3,on_delete=models.CASCADE,null=True,blank=True)
    