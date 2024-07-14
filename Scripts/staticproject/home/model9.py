from django.db import models
from . model1 import Home1
from . models import Home


class Home9(models.Model):
    JOB_CATEGORY_CHOICES=(('PAINTING','PAINTING'),('CONSTRUCTION','CONSTRUCTION'),('PLUMBER','PLUMBER'),('ELECTRICIAN','ELECTRICIAN'),
                          ('MECHANIC','MECHANIC'),('LIFT OPERATOR','LIFT OPERATOR'),)
    JOB_CATEGORY=models.CharField(max_length=25,choices=JOB_CATEGORY_CHOICES)
    Working_place=models.CharField(max_length=255,null=True)
    WORKER=models.ForeignKey(Home1,on_delete=models.CASCADE,null=True,blank=True)
    
    
    
