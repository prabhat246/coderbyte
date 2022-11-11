from django.db import models

# Create your models here.
from itertools import groupby
from django.db import models
from django.db.models import Sum

class User(models.Model):
    user = models.CharField(unique=True,max_length=100)
    @property
    def owes_calc(self):
        data = IOU.objects.filter(lender=self)
        dict={}
        for obj in data:
            if obj.lender.user in dict:
                dict[obj.borrower.user]+=obj.amount
            else:
                dict[obj.borrower.user]=obj.amount
        return dict
    
    @property
    def owed_by_calc(self):
        data = IOU.objects.filter(borrower=self)
        dict={}
        for obj in data:
            if obj.lender.user in dict:
                dict[obj.lender.user]+=obj.amount
            else:
                dict[obj.lender.user]=obj.amount
        return dict

    @property
    def balance_calc(self):
        lended = IOU.objects.filter(lender=self).aggregate(Sum('amount'))['amount__sum']
        borrowed = IOU.objects.filter(borrower=self).aggregate(Sum('amount'))['amount__sum']
        if lended is None:
            lended=0
        if borrowed is None:
            borrowed=0
        return lended-borrowed


    def __str__(self):
        return self.user

    
class IOU(models.Model):
    lender = models.ForeignKey(User,on_delete=models.CASCADE,related_name='lenders_user')
    borrower = models.ForeignKey(User,on_delete=models.CASCADE,related_name='borrower_user')
    amount = models.FloatField()
    expiration = models.DateTimeField()