from django.urls import path
from .views import UserLogin,UserLogout,InternsView,InternDetail,GetAllInterns

urlpatterns = [
    path('login',UserLogin.as_view()),
    path('logout',UserLogout.as_view()),
    path('interns',InternsView.as_view()),
    path('intern/<int:pk>',InternDetail.as_view()),
    path('allinterns',GetAllInterns.as_view())
]