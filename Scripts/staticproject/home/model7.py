from django.db import models
from . model1 import Home1

class Home7(models.Model):
    ATTENDANCES_CHOICES=(('P','PRESENT'),('A','ABSENT'),)
    ATTENDANCE=models.CharField(max_length=25,choices=ATTENDANCES_CHOICES)
    WORKER=models.ForeignKey(Home1,on_delete=models.CASCADE,null=True,blank=True)
    CURRENTDATE=models.DateField(null=True)
    currentmonth=models.IntegerField(null=True)
    