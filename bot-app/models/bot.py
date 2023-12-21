from tortoise import Model, fields


class Settings(Model):
    token = fields.TextField()

    class Meta:
        table = "bot_settings"


class Page(Model):
    message = fields.TextField()
    slug = fields.CharField(max_length=20, null=False, unique=True)
    button = fields.ManyToManyField(
        "models.Button", related_name="page", through="bot_pages_buttons"
    )

    class Meta:
        table = "bot_pages"


class Button(Model):
    text = fields.CharField(max_length=10, null=False)
    slug = fields.CharField(max_length=20, null=False, unique=True)
    message = fields.TextField(null=True)
    page: fields.ManyToManyRelation[Page]

    class Meta:
        table = "bot_buttons"


class PagesButtons(Model):
    page = fields.ForeignKeyField("models.Page")
    button = fields.ForeignKeyField("models.Button")

    class Meta:
        table = "bot_pages_buttons"
