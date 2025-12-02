from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', _('System Administrator')
        OFFICIAL = 'OFFICIAL', _('Barangay Official')

    role = models.CharField(
        max_length=50,
        choices=Role.choices,
        default=Role.OFFICIAL,
        verbose_name=_('Role')
    )

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
