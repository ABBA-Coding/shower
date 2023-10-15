from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "shower.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import shower.users.signals  # noqa: F401
        except ImportError:
            pass
