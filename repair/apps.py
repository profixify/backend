import importlib

from django.apps import AppConfig


class RepairConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "repair"

    def ready(self):
        importlib.import_module("repair.signals")
