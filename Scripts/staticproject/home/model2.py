from django.db import models
from . model1 import Home1

class Home2(models.Model):
    stationid=models.CharField(max_length=255)
    addressline1=models.TextField(max_length=255)
    addressline2=models.TextField(max_length=255)
    pincode=models.IntegerField(null=True)
    state=models.CharField(max_length=255)
    district=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    contactnumber=models.IntegerField(null=True)
    email=models.EmailField(max_length=255,unique=True, error_messages={'unique': 'This email address is already in use.'})
    password=models.CharField(max_length=255)
    user_type=models.CharField(max_length=255,default='police')
    Worker=models.ForeignKey(Home1,on_delete=models.CASCADE,null=True,blank=True)
    


# Create your models here.
