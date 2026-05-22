from django.apps import AppConfig

# Ensures Django loads the signal when the app starts


class PlanningAppConfig(AppConfig):
    """Configuration for the planning_app Django application.

    Ensures signals are registered when the app is ready.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "planning_app"

    def ready(self):
        import planning_app.signals
