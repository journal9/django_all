from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, PostsSerializer, CommentsSerializer
from .models import Users

# Create your views here.

class UserView(APIView):

    def post(self,request):
        input_data = UserSerializer(data = request.data)
        if input_data.is_valid():
            input_data.save()
            return Response(input_data.data,status=status.HTTP_201_CREATED)
        else:
            return Response(input_data.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        all_users = Users.objects.all()
        serialized_users = UserSerializer(all_users,many=True)
        return Response(serialized_users.data)
