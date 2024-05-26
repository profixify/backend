from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from core.models import BaseModel


class Customer(BaseModel):
    name = models.CharField(max_length=100, null=False)
    surname = models.CharField(max_length=100, null=False)
    identity_number = models.CharField(max_length=11, null=False)
    phone_number = PhoneNumberField()

    @property
    def full_name(self):
        return f"{self.name} {self.surname}"

    def __str__(self) -> str:
        return self.full_name
