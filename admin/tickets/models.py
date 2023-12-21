from django.db import models


class Slot(models.Model):
    slot_date = models.DateField()
    slot_time = models.TimeField()
    is_open = models.BooleanField(default=True)

    def __str__(self):
        return str(self.slot_date) + str(self.slot_time)

    class Meta:
        managed = False
        db_table = "tickets_slot"


class Ticket(models.Model):
    client = models.ForeignKey("users.Client", on_delete=models.CASCADE)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    service = models.ForeignKey("services.Service", on_delete=models.CASCADE)
    updated_at = models.DateTimeField()
    created_at = models.DateTimeField()
    is_active = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = "tickets_ticket"
