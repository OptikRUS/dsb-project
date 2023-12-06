from tortoise import Model, fields


class Settings(Model):
    token = fields.TextField()

    class Meta:
        table = "bot_settings"


class Pages(Model):
    message = fields.TextField()
    slug = fields.CharField(max_length=20, null=False, unique=True)
    buttons = fields.ManyToManyField("models.Buttons", related_name="pages", through="bot_pages_buttons")

    class Meta:
        table = "bot_pages"


class Buttons(Model):
    text = fields.CharField(max_length=10, null=False)
    slug = fields.CharField(max_length=20, null=False, unique=True)
    message = fields.TextField(null=True)
    pages: fields.ManyToManyRelation[Pages]

    class Meta:
        table = "bot_buttons"


class PagesButtons(Model):
    page = fields.ForeignKeyField("models.Pages")
    button = fields.ForeignKeyField("models.Buttons")

    class Meta:
        table = "bot_pages_buttons"
