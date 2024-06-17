from django.urls import path
from .views import InternsView,InternDetail,GetAllInterns

urlpatterns = [
    path('interns',InternsView.as_view()),
    path('intern/<int:pk>',InternDetail.as_view()),
    path('allinterns',GetAllInterns.as_view())
]