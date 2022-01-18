from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime


class AdminTable(AbstractUser):
    class Meta:
        db_table = 'admins'

    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=256)
    status = models.IntegerField()
    last_login = models.DateTimeField(null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    username = None
    first_name = None
    last_name = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
