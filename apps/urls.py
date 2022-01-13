from django.urls import path
from . import views

urlpatterns = [
    path('admins', views.AdminManagement.as_view(), name='users'),
    path('admin/<pk>', views.SingleAdminManagement.as_view(), name='user'),
    path('login', views.LoginManagement.as_view(), name='login'),
]
