from django.db import models
from django.utils.translation import gettext_lazy as _

class Household(models.Model):
    class HousingMaterial(models.TextChoices):
        CONCRETE = 'CONCRETE', _('Concrete')
        SEMI_CONCRETE = 'SEMI_CONCRETE', _('Semi-Concrete')
        LIGHT = 'LIGHT', _('Light Materials')
        SALVAGED = 'SALVAGED', _('Salvaged Materials')

    class OwnershipStatus(models.TextChoices):
        OWNED = 'OWNED', _('Owned')
        RENTED = 'RENTED', _('Rented')
        SHARER = 'SHARER', _('Sharer / Living with Relatives')
        INFORMAL = 'INFORMAL', _('Informal Settler')

    household_number = models.CharField(_('Household Number'), max_length=50, unique=True)
    street_address = models.CharField(_('Street Address'), max_length=255)
    housing_material = models.CharField(_('Housing Material'), max_length=20, choices=HousingMaterial.choices, default=HousingMaterial.CONCRETE)
    ownership_status = models.CharField(_('Ownership Status'), max_length=20, choices=OwnershipStatus.choices, default=OwnershipStatus.OWNED)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Household #{self.household_number} - {self.street_address}"

class Resident(models.Model):
    class Sex(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')

    class Classification(models.TextChoices):
        CHILD = 'CHILD', _('Child (0-14)')
        YOUTH = 'YOUTH', _('Youth (15-30)')
        SENIOR = 'SENIOR', _('Senior Citizen (60+)')
        PWD = 'PWD', _('Person with Disability')
        INDIGENT = 'INDIGENT', _('Indigent')
        NOT_CLASSIFIED = 'NONE', _('Not Classified')

    class Relationship(models.TextChoices):
        HEAD = 'HEAD', _('Head of Family')
        SPOUSE = 'SPOUSE', _('Spouse')
        CHILD = 'CHILD', _('Child')
        PARENT = 'PARENT', _('Parent')
        SIBLING = 'SIBLING', _('Sibling')
        OTHER = 'OTHER', _('Other Relative/Non-Relative')

    first_name = models.CharField(_('First Name'), max_length=100)
    middle_name = models.CharField(_('Middle Name'), max_length=100, blank=True)
    last_name = models.CharField(_('Last Name'), max_length=100)
    sex = models.CharField(_('Sex'), max_length=1, choices=Sex.choices)
    birthdate = models.DateField(_('Birthdate'))
    
    # Address fields
    street_address = models.CharField(_('Street Address'), max_length=255)
    
    # Household Link
    household = models.ForeignKey(Household, on_delete=models.SET_NULL, null=True, blank=True, related_name='members')
    relationship_to_head = models.CharField(_('Relationship to Head'), max_length=20, choices=Relationship.choices, blank=True)
    
    contact_number = models.CharField(_('Contact Number'), max_length=20, blank=True)
    classification = models.CharField(
        _('Classification'), 
        max_length=20, 
        choices=Classification.choices, 
        default=Classification.NOT_CLASSIFIED
    )
    
    photo = models.ImageField(_('Photo'), upload_to='residents_photos/', blank=True, null=True)
    is_active = models.BooleanField(_('Active'), default=True)

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = _('Resident')
        verbose_name_plural = _('Residents')

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}".strip()
