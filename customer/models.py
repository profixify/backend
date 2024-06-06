from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from core.models import BaseModel


class Customer(BaseModel):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    phone_number = PhoneNumberField()

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return self.full_name
