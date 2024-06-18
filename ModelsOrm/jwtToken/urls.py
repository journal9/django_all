from django.urls import path
from .views import ListAllCookies, CookiesView, CookieDetail

urlpatterns = [
    path('cookie',CookiesView.as_view()),
    path('cookie/<int:pk>',CookieDetail.as_view()),
    path('cookies',ListAllCookies.as_view()),
]