from django.db import models
class SCHOME(models.Model):
    SCHEME_TYPE=models.CharField(max_length=255)
    SCHEME_NAME=models.CharField(max_length=255)
    SCHEME_AMOUNT=models.IntegerField(null=True)
    MONTHLY_AMOUNT=models.IntegerField(null=True)
    INTEREST_RATE=models.CharField(max_length=255)
    SCHEME_DETAILS=models.TextField(max_length=255)
    
    
