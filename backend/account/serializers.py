from rest_framework import serializers
from rest_framework import exceptions

from rest_framework.exceptions import ValidationError
from .models import CustomizeUser

from rest_framework.serializers import (ModelSerializer,CharField)



class UserSerializer(ModelSerializer):
    password = CharField(required=True,write_only=True)
    
    class Meta:
        model = CustomizeUser
        fields = (
            'id',
            'email',
            'username',
            'password'
        )
        extra_kwargs = {
            'password' : {'write_only': True, 'required':True},
        }

    def	save(self):
        user = CustomizeUser(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password_text = self.validated_data['password']
        user.set_password(password_text)
        user.save()
        return user
