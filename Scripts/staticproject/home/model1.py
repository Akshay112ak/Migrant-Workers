from django.db import models
from . models import Home
class Home1(models.Model):
    workername=models.CharField(max_length=255)
    address=models.TextField(max_length=255)
    pincode=models.IntegerField(null=True)
    state=models.CharField(max_length=255)
    district=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    aadharnumber=models.IntegerField(null=True)
    contactnumber=models.IntegerField(null=True)
    email=models.EmailField(max_length=255,unique=True, error_messages={'unique': 'This email address is already in use.'})
    password=models.CharField(max_length=255)
    user_type=models.CharField(max_length=255,default='worker')
    pass_status=models.IntegerField(null=True)
    agency=models.ForeignKey(Home,on_delete=models.CASCADE,null=True,blank=True)
   
    


# Create your models here.
