from django.urls import path
from .views import UserView,UserUpdateView,UserSecondView,UserSecondDetailView,UserOne,UserById

urlpatterns = [
    path('user',UserView.as_view()),
    path('user/<int:id>',UserUpdateView.as_view()),
    path('post',UserSecondView.as_view()),
    path('post/<int:pk>',UserSecondDetailView.as_view()),
    path('post2',UserOne.as_view()),
    path('post2/<int:pk>',UserById.as_view()),
]