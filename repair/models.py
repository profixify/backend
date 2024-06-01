from typing import Iterable

from django.db import models

from core.models import BaseModel
from customer.models import Customer
from repair.utils import generate_repair_code
from spare_part.models import SparePart


class RepairStatusChoices(models.TextChoices):
    WAITING_REPAIR = "WAITING_REPAIR"
    REPAIRING = "REPAIRING"
    REPAIRED = "REPAIRED"


class Repair(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="repairs")
    code = models.CharField(max_length=10, auto_created=True, default=generate_repair_code, editable=False)
    phone_lock = models.CharField(max_length=20, null=True, blank=True)
    sim_lock = models.CharField(max_length=20, null=True, blank=True)
    spare_part = models.ForeignKey(SparePart, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.code


class RepairStatus(BaseModel):
    status = models.CharField(
        max_length=20,
        choices=RepairStatusChoices.choices,
        default=RepairStatusChoices.WAITING_REPAIR,
    )
    title = models.CharField(max_length=100)
    note = models.TextField(null=True, default="No information")
    repair = models.ForeignKey(Repair, on_delete=models.CASCADE, related_name="statuses")

    def __str__(self) -> str:
        return f"{self.title} ({self.status})"
