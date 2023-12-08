# from django.db import models
# from django.contrib.auth.models import AbstractUser
#
#
# class User(AbstractUser):
#     username = models.CharField(max_length=20, unique=True)
#     password = models.CharField(max_length=128, null=True)
#     is_active = models.BooleanField(default=True)
#     is_superuser = models.BooleanField(default=False)
#
#
# class Client(AbstractUser):
#     telegram_id = models.PositiveIntegerField()
#     telegram_username = models.CharField(max_length=20, unique=True)
#     phone = models.CharField(max_length=12, blank=True, null=True)
#     full_name = models.CharField(max_length=255)
#     updated_at = models.DateTimeField(auto_now=True)
#     created_at = models.DateTimeField(auto_now_add=True)

