from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    name=serializers.CharField(max_length=100,required=True)

    class Meta:
        model = User
        fields = ('name',)