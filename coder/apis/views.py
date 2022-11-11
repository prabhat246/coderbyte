# from django.shortcuts import render

# # Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User,IOU
from .serializers import UserSerializer,IOUSerializer

class UserView(APIView):
    def get(self,request,*args,**kwargs):
        result = User.objects.all()
        serializers = UserSerializer(data=result, many=True)
        serializers.is_valid()
        data_list = []
        for i in serializers.data:
            data_list.append(dict(i))
        return Response({'users':data_list},status=status.HTTP_200_OK)

    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if(serializer.is_valid()):
            try:
                serializer.save()
                return Response({'data':serializer.data},status=status.HTTP_200_OK)
            except:
                return Response({'data':{"user":{"non_field_errors":"User already exists."}}},status=status.HTTP_400_BAD_REQUEST)    
        else:
            return Response({'data':serializer.errors},status=status.HTTP_400_BAD_REQUEST)


class IOUView(APIView):
    def get(self,request,*args,**kwargs):
        result = IOU.objects.all()
        serializers = IOUSerializer(data=result, many=True)
        serializers.is_valid()
        data_list = []
        for i in serializers.data:
            data_list.append(dict(i))
        return Response({'ious':data_list},status=status.HTTP_200_OK)

    def post(self,request):
        lender=User.objects.get(user=request.data['lender'])
        borrower=User.objects.get(user=request.data['borrower'])
        if lender is None:
            return Response({'data': { "lender": { "non_field_errors": ["Invalid lender."]}}},status=status.HTTP_400_BAD_REQUEST)
        if borrower is None:
            return Response({'data': { "borrower": {  "non_field_errors": ["Invalid borrower."]}}},status=status.HTTP_400_BAD_REQUEST)
        if borrower == lender:
            return Response({'data': { "borrower": {  "non_field_errors": ["Lender and borrowser can not be same."]}}},status=status.HTTP_400_BAD_REQUEST)
        data = request.data
        data['lender'] = lender.pk
        data['borrower'] =  borrower.pk
        
        s=IOUSerializer(data=data)
        # s.clean()
        if(s.is_valid()):
            s.save()
            return Response({'data':s.data},status=status.HTTP_200_OK)
        else:
            return Response({'data':s.errors},status=status.HTTP_400_BAD_REQUEST)


class SettleUpView(APIView):
    def get(self,request,*args,**kwargs):
        if request.data:
            
            result = User.objects.filter(user__in=request.data['users']).order_by('user')
                
            serializers = UserSerializer(data=result, many=True)
            if serializers.is_valid():
                print("success")
            data_list = []
            for i in serializers.data:
                data_list.append(dict(i))
            return Response({'users':data_list},status=status.HTTP_200_OK)

        else:
            result = User.objects.all()
            serializers = UserSerializer(data=result, many=True)
            serializers.is_valid()
            data_list = []
            for i in serializers.data:
                data_list.append(dict(i))
            return Response({'users':data_list},status=status.HTTP_200_OK)

