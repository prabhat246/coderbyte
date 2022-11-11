import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import User
from ..serializers import UserSerializer


# initialize the APIClient app
client = Client()



class GetUserTest(TestCase):
    """ Test module for GET all puppies API """

    def setUp(self):
        User.objects.create(
            name='Adam')
        User.objects.create(
            name='Bob')
        User.objects.create(
            name='Adam')
    
   
        
    def test_get_all_users(self):
        # get API response
        response = client.get(reverse('url_user'))
        # get data from db
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)