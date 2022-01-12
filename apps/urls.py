from django.urls import path
from . import views

urlpatterns = [
    path('users', views.AdminManagement.as_view(), name='users'),
    path('user/<pk>', views.SingleAdminManagement.as_view(), name='user'),
]
