from django.db.models import F
from django.db.models.signals import post_save
from django.dispatch import receiver

from repair.models import Repair, RepairStatus, RepairStatusChoices
from spare_part.models import SparePart


@receiver(post_save, sender=Repair)
def create_repair(sender, instance, created, **kwargs):
    if not created:
        print("updated")
        if instance.statuses.last().status == "REPAIRED":
            breakpoint()
            spare_part = SparePart.objects.filter(uuid=instance.spare_part.uuid)
            spare_part.update(temp_amount=F("temp_amount") - 1, left_amount=F("left_amount") - 1)
    else:
        print("created")
        repair_status = RepairStatus.objects.create(
            status=RepairStatusChoices.WAITING_REPAIR, title="Repair created", repair=instance
        )
        spare_part = SparePart.objects.filter(uuid=instance.spare_part.uuid)
        spare_part.update(temp_amount=F("temp_amount") + 1)


@receiver(post_save, sender=RepairStatus)
def update_repair_status(sender, instance, created, **kwargs):
    if created:
        if instance.status == "REPAIRED":
            spare_part = SparePart.objects.filter(uuid=instance.repair.spare_part.uuid)
            spare_part.update(temp_amount=F("temp_amount") - 1, left_amount=F("left_amount") - 1)
