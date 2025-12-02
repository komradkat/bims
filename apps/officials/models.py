from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class Official(models.Model):
    class Position(models.TextChoices):
        CHAIRMAN = 'CHAIRMAN', _('Barangay Chairman')
        KAGAWAD = 'KAGAWAD', _('Barangay Kagawad')
        SECRETARY = 'SECRETARY', _('Barangay Secretary')
        TREASURER = 'TREASURER', _('Barangay Treasurer')
        SK_CHAIRMAN = 'SK_CHAIRMAN', _('SK Chairman')

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='official_profile'
    )
    
    # If not linked to a user account, we still need their name
    first_name = models.CharField(_('First Name'), max_length=100)
    last_name = models.CharField(_('Last Name'), max_length=100)
    
    position = models.CharField(_('Position'), max_length=50, choices=Position.choices)
    committee = models.CharField(_('Committee'), max_length=100, blank=True, help_text=_('e.g., Committee on Peace and Order'))
    induction_date = models.DateField(_('Induction Date'))
    term_end_date = models.DateField(_('Term End Date'), null=True, blank=True)
    
    photo = models.ImageField(_('Photo'), upload_to='officials_photos/', blank=True, null=True)
    
    is_active = models.BooleanField(_('Active'), default=True)

    class Meta:
        verbose_name = _('Official')
        verbose_name_plural = _('Officials')
        ordering = ['position', 'last_name']

    def __str__(self):
        return f"{self.get_position_display()} - {self.last_name}"
