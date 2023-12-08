from tortoise import Model, fields


class Slot(Model):
    slot_date = fields.DateField()
    slot_time = fields.TimeField()
    is_open = fields.BooleanField(default=True)

    class Meta:
        table = "tickets_slot"


class Ticket(Model):
    client_id = fields.ForeignKeyField(model_name="models.Client")
    slot_id = fields.ForeignKeyField(model_name="models.Slot")
    service_id = fields.ForeignKeyField(model_name="models.Service")
    updated_at = fields.DatetimeField()
    created_at = fields.DatetimeField()
    is_active = fields.BooleanField(default=False)

    class Meta:
        table = "tickets_ticket"
