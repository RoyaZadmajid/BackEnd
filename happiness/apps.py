from django.apps import AppConfig


class HappinessConfig(AppConfig):
    name = 'happiness'

    def ready(self):
        from . import signals
