from django.db import models


class Slot(models.Model):
    slot_date = models.DateField()
    slot_time = models.TimeField()
    is_open = models.BooleanField(default=True)

    class Meta:
        managed = False
        db_table = "tickets_slot"


class Ticket(models.Model):
    client_id = models.ForeignKey("users.Client", on_delete=models.CASCADE)
    slot_id = models.ForeignKey(Slot, on_delete=models.CASCADE)
    service_id = models.ForeignKey("services.Service", on_delete=models.CASCADE)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    is_active = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = "tickets_ticket"
