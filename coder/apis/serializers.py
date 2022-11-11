from rest_framework import serializers
from .models import User,IOU
from django.db.models import Sum

class UserSerializer(serializers.ModelSerializer):
    user=serializers.CharField(max_length=100,required=True)
    owes = serializers.ReadOnlyField(source='owes_calc')
    owed_by = serializers.ReadOnlyField(source='owed_by_calc')
    balance = serializers.ReadOnlyField(source='balance_calc')

    # def owes_calc(self, instance):         
    #     data = IOU.objects.filter(lender=self).annotate(sum=Sum('amount'))
    #     return {"asdf":"Asdf"}

    class Meta:
        model = User
        fields = ('user','owes','owed_by','balance')

class IOUSerializer(serializers.ModelSerializer):
    class Meta:
        model = IOU
        fields = ('__all__')

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['lender'] = instance.lender.user
        ret['borrower'] = instance.borrower.user
        return ret

    class Meta:
        model = IOU
        fields = ('__all__')