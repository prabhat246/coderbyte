from django.db import models

# Create your models here.

from django.db import models


class User(models.Model):
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user

    
class IOU(models.Model):
    lender = models.ForeignKey(User,on_delete=models.CASCADE,related_name='lenders_user')
    borrower = models.ForeignKey(User,on_delete=models.CASCADE,related_name='borrower_user')
    amount = models.FloatField()
    expiration = models.DateTimeField()