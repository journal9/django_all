from django.shortcuts import render
from .models import Interns
from rest_framework.views import APIView
from rest_framework import generics
# from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import InternsSerializer, UserSerializer
from rest_framework.authtoken.models import Token
# Create your views here.

class UserRegister(APIView):
    def post(self,request):
        user_data = UserSerializer(data = request.data)
        response_data = {}
        if user_data.is_valid():
            nu = user_data.save()
            response_data['username'] = nu.username
            response_data['email'] = nu.email
            tk = Token.objects.get(user=nu).key
            response_data['token'] = tk
        else:
            response_data = user_data.errors
        return Response(response_data)


class InternsView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Interns.objects.all()
    serializer_class = InternsSerializer

class InternDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Interns.objects.all()
    serializer_class = InternsSerializer

class GetAllInterns(generics.ListAPIView):
    queryset = Interns.objects.all()
    serializer_class = InternsSerializer
