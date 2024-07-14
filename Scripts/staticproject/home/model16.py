from django.db import models
class Home16(models.Model):
    email=models.EmailField(max_length=255,default='labourcommission123@gmail.com')
    password=models.CharField(max_length=255,default='labourcommission123')