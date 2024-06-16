from django.urls import path
from.views import UserLogin,LogoutUser,Clients,ClientsDetail,GetAllClients

urlpatterns = [
    path('login',UserLogin.as_view()),
    path('logout',LogoutUser.as_view()),
    path('client',Clients.as_view()),
    path('clients',GetAllClients.as_view()),
    path('clients/<int:pk>',ClientsDetail.as_view()),
]