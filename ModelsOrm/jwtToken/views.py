from rest_framework.generics import ListCreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from .models import Cookies
from .serializers import CookieSerializer
from rest_framework.permissions import IsAuthenticated


class CookiesView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Cookies.objects.all()
    serializer_class = CookieSerializer

class CookieDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Cookies.objects.all()
    serializer_class = CookieSerializer

class ListAllCookies(ListAPIView):
    queryset = Cookies.objects.all()
    serializer_class = CookieSerializer
