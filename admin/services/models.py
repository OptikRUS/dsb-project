from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = "services_place"


class Service(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    price = models.PositiveIntegerField()
    place = models.ForeignKey(Place, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = "services_service"
