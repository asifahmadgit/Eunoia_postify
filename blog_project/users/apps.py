from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # ✅ add this
    name = 'users'

    def ready(self):
        import users.signals
