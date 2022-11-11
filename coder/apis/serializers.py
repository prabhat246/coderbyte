from rest_framework import serializers
from .models import User,IOU

class UserSerializer(serializers.ModelSerializer):
    user=serializers.CharField(max_length=100,required=True)

    class Meta:
        model = User
        fields = ('__all__')

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