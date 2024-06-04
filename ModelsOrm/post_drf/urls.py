from django.urls import path
from .views import UserView,UserUpdateView,UserSecondView,UserSecondDetailView

urlpatterns = [
    path('user',UserView.as_view()),
    path('user/<int:id>',UserUpdateView.as_view()),
    path('post',UserSecondView.as_view()),
    path('post/<int:id>',UserSecondDetailView.as_view()),
]