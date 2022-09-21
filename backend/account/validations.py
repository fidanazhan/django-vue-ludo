from rest_framework import exceptions
from . models import CustomizeUser
import re
from django.db.models import Q

class CustomValidation:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def validate_username_blank(self):
        if not self.username:
            raise exceptions.ValidationError({'error':'Please input an username'})

    def validate_username(self):
        if len(self.username) <= 3 or len(self.username) > 21:
            raise exceptions.ValidationError({'error':"Please input username length between 6 until 20 characters"})

    def validate_password_blank(self):
        if not self.password:
            raise exceptions.ValidationError({'error':'Please input a password'})

    def call_common(self):
        self.validate_username_blank()
        self.validate_username()
        self.validate_password_blank()

class LoginValidation(CustomValidation):

    def __init__(self, username, password):
        CustomValidation.__init__(self, username, password)
        self.user = CustomizeUser.objects.filter(Q(username__iexact=self.username) | Q(email__iexact=self.username)).first()

    def validate_username_not_exist(self):
        if not self.user:
            raise exceptions.ValidationError({'error':'Input does not found.'})

    def validate_password_incorrect(self):
        if not self.user.check_password(self.password):
            raise exceptions.ValidationError({'error':'Incorrect password'})

    def is_valid(self):
        self.call_common()
        self.validate_username_not_exist()
        self.validate_password_incorrect()

class RegisterValidation(CustomValidation):

    def __init__(self, email, username, password, password_confirm):
        CustomValidation.__init__(self, username, password)
        self.email = email
        self.password_confirm = password_confirm

    def validate_email_blank(self):
        if not self.email:
            raise exceptions.ValidationError({'error':'Please input an email'})

    def validate_email_input(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'  

        if not re.fullmatch(regex, self.email):
            raise exceptions.ValidationError({'error':"Email are unvalid. Please input valid email."})   

    def validate_email_exist(self):
        exist = CustomizeUser.objects.filter(email=self.email).first()
        if exist:
            raise exceptions.ValidationError({'error':"Email already registered. Please enter another email."})
    
    def validate_username_exist(self):
        exist = CustomizeUser.objects.filter(username=self.username).first()
        if exist:
            raise exceptions.ValidationError({'error':"Username already existed. Please enter another username."})

    def validate_password_match(self):

        if not self.password_confirm:
            raise exceptions.ValidationError({'error':'Please input a password'})

        if self.password != self.password_confirm:
            raise exceptions.ValidationError({'error':'Password must match'})

    def is_valid(self):
        self.call_common()
        self.validate_email_blank()
        self.validate_email_input()
        self.validate_email_exist()
        self.validate_username_exist()
        self.validate_password_match()


