from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.accounts.managers import CustomUserManager


class User(AbstractUser):
    username = (None,)
    email = models.EmailField(_("email address"), blank=True, unique=True)
    name = models.CharField(max_length=20, null=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = "user"
        ordering = ["-id"]
