from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from api_LMS.models import UserRegistration
from api_LMS.serializers import UserRegistrationSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.

def home(self):
    return HttpResponse("<h1>RestFul API</h1>")

class register(generics.CreateAPIView):
    queryset = UserRegistration
    serializer_class = UserRegistrationSerializer

class list_of_user(generics.ListAPIView):
    queryset = UserRegistration.objects.all()
    serializer_class = UserRegistrationSerializer

class UserProfile(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserRegistrationSerializer

    def get_object(self):
        return self.request.user

        