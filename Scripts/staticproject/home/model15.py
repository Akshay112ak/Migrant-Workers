from django.db import models
class Home15(models.Model):
    email=models.EmailField(max_length=255,default='admin123@gmail.com')
    password=models.CharField(max_length=255,default='admin123')