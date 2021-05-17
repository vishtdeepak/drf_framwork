from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from customuser.models import MyUser
from rest_framework import generics, serializers, status
from .serializers import MyTokenObtainPairSerializer, UserRegistrationSerializer
from rest_framework.response import Response




class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer