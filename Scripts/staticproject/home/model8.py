from django.db import models

class Home8(models.Model):
    JOB_CATEGORY_CHOICES=(('PAINTING','PAINTING'),('CONSTRUCTION','CONSTRUCTION'),('PLUMBER','PLUMBER'),('ELECTRICIAN','ELECTRICIAN'),
                          ('MECHANIC','MECHANIC'),('LIFT OPERATOR','LIFT OPERATOR'),)
    JOB_CATEGORY=models.CharField(max_length=25,choices=JOB_CATEGORY_CHOICES)
    SALARY_PER_DAY=models.IntegerField(null=True)
    
    
