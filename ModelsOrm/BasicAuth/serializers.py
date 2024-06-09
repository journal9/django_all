from rest_framework import serializers
from .models import Clientsz

class ClientsSerializer(serializers.ModelSerializer):

    class Meta:
        model=Clientsz
        fields = [
            'id',
            'name',
            'location',
            'capital'
        ]