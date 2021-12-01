from rest_framework import serializers
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from .models import *

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'




















# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

    def create(self, validated_data):
        user = User.objects.create()


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user

class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)
    
    def validate_email(self, email):
        email_exists = User.objects.filter(email__iexact=email).exists()
        if email_exists:
            raise serializers.ValidationError(_("A user is already registered with this e-mail address."))
        return email


    def save(self, request):
        email = self.validated_data.get('email')
        password = self.validated_data.get('password')    
        user = User()    
        user.email = email
        user.set_password(password)
        user.save()
