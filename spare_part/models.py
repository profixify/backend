from django.db import models

from core.models import BaseModel
from settings.models import CURRENCY_SYMBOL, Settings


class Brand(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Model(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="models")

    def __str__(self):
        return self.name


class SparePart(BaseModel):
    name = models.CharField(max_length=100, null=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="spare_parts")
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name="spare_parts")
    price = models.FloatField()
    amount = models.PositiveSmallIntegerField()
    left_amount = models.PositiveSmallIntegerField()
    temp_amount = models.PositiveSmallIntegerField(default=0)

    @property
    def price_with_currency(self):
        settings = Settings.objects.first()
        currency = CURRENCY_SYMBOL.get(settings.default_currency, "")
        return f"{self.price} {currency}"

    def save(self, *args, **kwargs) -> None:
        self.left_amount = self.amount
        return super(SparePart, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
