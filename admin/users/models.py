from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=20)
    telegram_id = models.PositiveIntegerField()
    telegram_username = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = "users_client"
