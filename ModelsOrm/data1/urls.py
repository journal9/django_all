from django.urls import path
from .views import AuthorView,AuthorExperienceView,BookView,BookManageView

urlpatterns = [
    path('d1',AuthorView.as_view()),
    path('d1/<int:id>',AuthorExperienceView.as_view()),
    path('book',BookView.as_view()),
    path('book/<int:id>',BookManageView.as_view())
]