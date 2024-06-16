from rest_framework.serializers import ModelSerializer
from .models import Interns, User

class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class InternsSerializer(ModelSerializer):

    class Meta:
        model=Interns
        fields=['name','email_id','graduation_year','passed']