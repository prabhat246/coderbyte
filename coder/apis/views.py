# from django.shortcuts import render

# # Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User,IOU
from .serializers import UserSerializer

class UserView(APIView):
    def get(self,request,*args,**kwargs):
        result = User.objects.all()
        serializers = UserSerializer
        return Response({'status':'success','users':result},status=status.HTTP_200_OK)

    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response({'status':'success','data':serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({'status':'error','data':serializer.errors},status=status.HTTP_400_BAD_REQUEST)