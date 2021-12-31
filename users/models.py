from django.db import models
from django.contrib.auth.models import AbstractUser


class UserTable(AbstractUser):
    class Meta:
        db_table = 'users'
