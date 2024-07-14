from django.db import models

class Home(models.Model):
    agencyname=models.CharField(max_length=255)
    address=models.TextField(max_length=255)
    pincode=models.IntegerField(null=True)
    district=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    agencyid=models.CharField(max_length=255)
    contactnumber=models.IntegerField(null=True)
    email=models.EmailField(max_length=255,unique=True,error_messages={'unique': 'This email address is already in use.'})
    password=models.CharField(max_length=255)
    user_type=models.CharField(max_length=255,default='agency')
    


# Create your models here.
