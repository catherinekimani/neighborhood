from django.apps import AppConfig


class NeighborhoodappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'neighborhoodapp'

    def ready(self):
        import neighborhoodapp.signals