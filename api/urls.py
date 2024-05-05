from django.urls import path
from . import views

urlpatterns = [
    path('startup/', views.StartupCreate.as_view(), name='startup-create'),
    path('startup/delete/<int:pk>/', views.StartupDelete.as_view(), name='startup-delete')
]