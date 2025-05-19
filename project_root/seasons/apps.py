from django.apps import AppConfig

class SeasonsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField' #type = ignore
    name = 'seasons'

    def ready(self):
        import seasons.signals
