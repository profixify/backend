from django.db import models

from core.models import BaseModel


class DefaultCurrencyChoices(models.TextChoices):
    DOLLAR = "DOLLAR", "DOLLAR"
    EURO = "EURO", "EURO"
    TURKISH_LIRA = "TURKISH_LIRA", "TURKISH_LIRA"


class Settings(BaseModel):
    default_currency = models.CharField(
        max_length=20,
        choices=DefaultCurrencyChoices.choices,
    )

    def __str__(self) -> str:
        return self.default_currency
