from django.db import models

# Create your models here.

from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    
class IOU(models.Model):
    lender = models.ForeignKey(User,on_delete=models.CASCADE,related_name='lender')
    borrower = models.ForeignKey(User,on_delete=models.CASCADE,related_name='borrower')
    amount = models.FloatField()
    expiration = models.DateTimeField()