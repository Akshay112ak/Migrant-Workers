from django.db import models

class Home3(models.Model):
    agencyname=models.CharField(max_length=255)
    state=models.CharField(max_length=255)
    district=models.CharField(max_length=255)
    contactnumber=models.IntegerField(null=True)
    regid=models.CharField(max_length=255)
    email=models.EmailField(max_length=255,unique=True, error_messages={'unique': 'This email address is already in use.'})
    password=models.CharField(max_length=255)
    user_type=models.CharField(max_length=255,default='insuranceagency')
    


# Create your models here.
