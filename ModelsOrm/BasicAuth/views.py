from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
# from django.contrib.sessions.models import Session
from rest_framework.response import Response
from .models import Clientsz
from .serializers import ClientsSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
# Create your views here.

class UserLogin(APIView):

    @csrf_exempt
    def post(self,request):
        print(request.user)
        if request.user.is_authenticated:
            return Response({'message':'Already Logged in'},status=status.HTTP_100_CONTINUE)
        username = request.data['name']
        password = request.data['password']
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            print(request.user)
            print(request.auth)
            # request.session['username'] = username
            # request.session.save()
        else:
            return Response({'message':'Incorrect username or password'},status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'Logged in successfully'},status=status.HTTP_202_ACCEPTED)

class LogoutUser(APIView):

    @csrf_exempt
    def post(self,request):
        logout(request)
        # Session.objects.filter(session_key=request.session.session_key).delete()
        return Response({'message':'Logged out successfully'},status=status.HTTP_200_OK)
    
class Clients(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Clientsz.objects.all()
    serializer_class = ClientsSerializer

class ClientsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Clientsz.objects.all()
    serializer_class = ClientsSerializer

class GetAllClients(generics.ListAPIView):
    queryset = Clientsz.objects.all()
    serializer_class = ClientsSerializer

# class GetAllClients(APIView):

#     def get(self,request):
#         print(request.user)
#         queryset = Clientsz.objects.all()
#         serializer_data = ClientsSerializer(queryset,many = True)
#         return Response(serializer_data.data,status=status.HTTP_200_OK)