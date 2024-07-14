from django.db import models
class Home17(models.Model):
    senderid=models.IntegerField(null=True)
    recevierid=models.IntegerField(null=True)
    message=models.TextField(max_length=255)
    date=models.DateTimeField(null=True)