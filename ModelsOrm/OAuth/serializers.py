from rest_framework.serializers import ModelSerializer
from .models import Interns, Client
from django.contrib.auth.models import User

class ClientSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', "first_name", "last_name")

class InternsSerializer(ModelSerializer):

    class Meta:
        model=Interns
        fields=['name','email_id','graduation_year','passed']