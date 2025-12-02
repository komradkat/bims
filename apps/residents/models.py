from django.db import models
from django.utils.translation import gettext_lazy as _

class Resident(models.Model):
    class Sex(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')

    class Classification(models.TextChoices):
        CHILD = 'CHILD', _('Child (0-14)')
        YOUTH = 'YOUTH', _('Youth (15-30)')
        SENIOR = 'SENIOR', _('Senior Citizen (60+)')
        INDIGENT = 'INDIGENT', _('Indigent')
        PWD = 'PWD', _('Person with Disability')
        NOT_CLASSIFIED = 'NONE', _('Not Classified')

    first_name = models.CharField(_('First Name'), max_length=100)
    last_name = models.CharField(_('Last Name'), max_length=100)
    middle_name = models.CharField(_('Middle Name'), max_length=100, blank=True)
    
    sex = models.CharField(_('Sex'), max_length=1, choices=Sex.choices)
    birthdate = models.DateField(_('Birthdate'))
    
    street_address = models.CharField(_('Street Address'), max_length=255)
    contact_number = models.CharField(_('Contact Number'), max_length=20, blank=True)
    
    classification = models.CharField(
        _('Classification'), 
        max_length=20, 
        choices=Classification.choices,
        default=Classification.NOT_CLASSIFIED
    )
    
    photo = models.ImageField(_('Photo'), upload_to='residents_photos/', blank=True, null=True)
    
    is_active = models.BooleanField(_('Active'), default=True, help_text=_('Designates whether this resident should be treated as active. Unselect this instead of deleting accounts.'))
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Resident')
        verbose_name_plural = _('Residents')
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
