from django.db import models


class Settings(models.Model):
    token = models.TextField()

    class Meta:
        managed = False
        db_table = "bot_settings"


class Button(models.Model):
    text = models.CharField(max_length=10, null=False)
    slug = models.CharField(max_length=20, null=False, unique=True)
    message = models.TextField(null=True)

    class Meta:
        managed = False
        db_table = "bot_buttons"


class Page(models.Model):
    message = models.TextField()
    slug = models.CharField(max_length=20, null=False, unique=True)
    button = models.ManyToManyField(Button, related_name="page", through="PagesButtons")

    class Meta:
        managed = False
        db_table = "bot_pages"


class PagesButtons(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    button = models.ForeignKey(Button, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = "bot_pages_buttons"
