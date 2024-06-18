from rest_framework.serializers import ModelSerializer
from .models import Cookies

class CookieSerializer(ModelSerializer):

    class Meta:
        model= Cookies
        fields= '__all__'