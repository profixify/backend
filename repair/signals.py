from django.db.models import F
from django.db.models.signals import post_save
from django.dispatch import receiver

from repair.models import Repair
from spare_part.models import SparePart


@receiver(post_save, sender=Repair)
def create_repair(sender, instance, created, **kwargs):
    if created:
        spare_part = SparePart.objects.filter(uuid=instance.spare_part.uuid)
        spare_part.update(left_amount=F("left_amount") - 1)
