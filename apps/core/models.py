from django.db import models
from django.utils.translation import gettext_lazy as _

class BarangayInfo(models.Model):
    name = models.CharField(_('Barangay Name'), max_length=255, default='Barangay BIMS')
    city_municipality = models.CharField(_('City/Municipality'), max_length=255, blank=True)
    province = models.CharField(_('Province'), max_length=255, blank=True)
    region = models.CharField(_('Region'), max_length=255, blank=True)
    
    logo = models.ImageField(_('Logo'), upload_to='barangay_assets/', blank=True, null=True)
    
    vision = models.TextField(_('Vision'), default='To be a model barangay...')
    mission = models.TextField(_('Mission'), default='To provide quality services...')
    service_pledge = models.TextField(_('Service Pledge'), default='We commit to deliver efficient public service...')
    
    contact_number = models.CharField(_('Contact Number'), max_length=50, blank=True)
    email = models.EmailField(_('Email Address'), blank=True)
    
    class Meta:
        verbose_name = _('Barangay Information')
        verbose_name_plural = _('Barangay Information')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        if not self.pk and BarangayInfo.objects.exists():
            # If you want to prevent creation, raise error. 
            # For now, we'll just allow it but in practice we enforce singleton via view/admin logic
            pass
        return super(BarangayInfo, self).save(*args, **kwargs)
