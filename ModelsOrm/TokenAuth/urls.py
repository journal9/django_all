from django.urls import path
from .views import UserRegister,InternsView,InternDetail,GetAllInterns
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register',UserRegister.as_view()),
    path('interns',InternsView.as_view()),
    path('intern/<int:pk>',InternDetail.as_view()),
    path('allinterns',GetAllInterns.as_view()),
    path('login',obtain_auth_token)
]