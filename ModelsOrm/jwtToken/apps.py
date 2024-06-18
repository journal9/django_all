from django.apps import AppConfig
class JwttokenConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'jwtToken'

    def ready(self):
      import jwtToken.signals
