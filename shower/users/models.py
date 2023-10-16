from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from shower.users.managers import UserManager
from django.db import models


class User(AbstractUser):
    """
    Default custom user model for Shower.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    email = EmailField(_("email address"), unique=True)
    username = None  # type: ignore

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"pk": self.id})


class Business(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = CharField(max_length=255)
    url = CharField(max_length=255)
    industry = CharField(max_length=255)
    business_size = CharField(max_length=100)

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"
