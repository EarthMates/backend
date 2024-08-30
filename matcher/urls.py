from django.urls import path
from .views import MatchesView
from . import views
urlpatterns = [
    path('match/', MatchesView.as_view(), name='match_view'),
]