from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserManagement.as_view(), name='users'),
    path('login', views.AuthenticationManagement.as_view(), name='login'),
]
