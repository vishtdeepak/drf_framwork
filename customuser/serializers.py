from django.db.models import fields
from rest_framework import serializers
from .models import MyUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny



class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('email','password', 'name')
        extra_kwargs = {
            'name': {'required': True}
        }
        
    # def create(self, validated_data):
    #     user = MyUser.objects.create_user(validated_data['email'], validated_data['password'] , validated_data['name'])
    #     user.save()
    #     return user

    def create(self, validated_data):
        user = MyUser.objects.create(
            email = validated_data['email'],
            name = validated_data['name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token =  super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['email'] = user.email
        return token


