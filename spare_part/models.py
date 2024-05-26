from typing import Iterable

from django.db import models

from core.models import BaseModel
from settings.models import Settings


class SparePart(BaseModel):
    name = models.CharField(max_length=100, null=False)
    price = models.FloatField()
    amount = models.PositiveSmallIntegerField()
    left_amount = models.PositiveSmallIntegerField()

    @property
    def price_with_currency(self):
        settings = Settings.objects.first()
        currency = Settings.CURRENCY_CHOICES.get(settings.default_currency) or ""
        return f"{self.price} {currency}"

    def save(self, *args, **kwargs) -> None:
        self.left_amount = self.amount
        return super(SparePart, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
