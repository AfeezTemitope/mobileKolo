from django.apps import AppConfig


class EwalletConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ewallet'

    def ready(self):
        import ewallet.signals
