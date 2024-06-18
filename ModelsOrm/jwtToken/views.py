from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cookies
from .serializers import CookieSerializer
from rest_framework.permissions import IsAuthenticated

class CookiesView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self,request):
        cookie_data = request.data
        serialized_data = CookieSerializer(data = cookie_data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data,status = status.HTTP_201_CREATED)
        else:
            return Response(serialized_data.errors,status=status.HTTP_400_BAD_REQUEST)
class CookieDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Cookies.objects.all()
    serializer_class = CookieSerializer

class ListAllCookies(ListAPIView):
    queryset = Cookies.objects.all()
    serializer_class = CookieSerializer
