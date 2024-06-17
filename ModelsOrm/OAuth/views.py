from .models import Interns
from rest_framework.views import APIView
from rest_framework import generics
from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.models import Session
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import InternsSerializer
from rest_framework import status
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
# Create your views here.

# class UserLogin(APIView):
#     def post(self,request):
#         username = request.data['username']
#         password = request.data['password']
#         user = authenticate(request,username=username,password=password)
#         if user:
#             login(request,user)
#             request.session['username'] = username
#             request.session.save()
#             print(request.session)
#             return Response({'message':'Logged in successfully'},status=status.HTTP_202_ACCEPTED)
#         else:
#             return Response({'message':'Incorrect credentials provided.'},status=status.HTTP_400_BAD_REQUEST)

# class UserLogout(APIView):  
#     def post(self,request):
#         print(request.session)
#         logout(request)
#         Session.objects.filter(session_key=request.session.session_key).delete()
#         return Response({'message':'Logged out successfully'},status=status.HTTP_202_ACCEPTED)
    
class InternsView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated,TokenHasReadWriteScope]
    queryset = Interns.objects.all()
    serializer_class = InternsSerializer

class InternDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated,TokenHasReadWriteScope]
    queryset = Interns.objects.all()
    serializer_class = InternsSerializer

class GetAllInterns(generics.ListAPIView):
    queryset = Interns.objects.all()
    serializer_class = InternsSerializer
