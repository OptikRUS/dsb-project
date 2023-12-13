from tortoise import Model, fields


class Service(Model):
    name = fields.CharField(max_length=20)
    description = fields.TextField()
    price = fields.IntField()
    place = fields.ForeignKeyField(model_name="models.Place")

    class Meta:
        table = "services_service"


class Place(Model):
    name = fields.CharField(max_length=20)
    description = fields.TextField()

    class Meta:
        table = "services_place"
