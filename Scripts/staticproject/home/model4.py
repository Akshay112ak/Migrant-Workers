from django.db import models

class NOTI(models.Model):
    NOTIFICATION=models.TextField(max_length=255)
    CURRENTDATE=models.DateField(null=True)
    
    


# Create your models here.
