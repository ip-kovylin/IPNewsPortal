from django.apps import AppConfig


class PortalappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'PortalApp'

    def ready(self):
        import PortalApp.signals
