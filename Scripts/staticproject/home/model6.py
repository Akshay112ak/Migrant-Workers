from django.db import models

class COMP(models.Model):
    COMPLAINT_SUBJECT=models.CharField(max_length=255)
    COMPLAINT=models.TextField(max_length=255)
    
    


# Create your models here.
