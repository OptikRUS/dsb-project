from tortoise import Model, fields


class Client(Model):
    telegram_id = fields.IntField()
    name = fields.CharField(max_length=20)
    telegram_username = fields.CharField(max_length=20, unique=True)
    phone = fields.CharField(max_length=12, blank=True, null=True)
    updated_at = fields.DatetimeField(auto_now=True)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "users_client"
