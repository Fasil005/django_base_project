from django.urls import path
from . import views

urlpatterns = [
    path('user', views.UserManagement.as_view(), name='users'),
]
