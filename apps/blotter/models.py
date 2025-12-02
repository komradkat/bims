from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.residents.models import Resident

class BlotterCase(models.Model):
    class Status(models.TextChoices):
        ACTIVE = 'ACTIVE', _('Active / On-Going')
        SETTLED = 'SETTLED', _('Amicably Settled')
        FILED_ACTION = 'FILED_ACTION', _('Certificate to File Action Issued')
        DISMISSED = 'DISMISSED', _('Dismissed / Withdrawn')

    class CaseType(models.TextChoices):
        NEIGHBORHOOD = 'NEIGHBORHOOD', _('Neighborhood Conflict')
        LAND_DISPUTE = 'LAND', _('Land Dispute')
        COLLECTION = 'COLLECTION', _('Collection of Debt')
        DAMAGES = 'DAMAGES', _('Property Damage')
        UNJUST_VEXATION = 'VEXATION', _('Unjust Vexation')
        OTHERS = 'OTHERS', _('Others')

    complainant = models.ForeignKey(Resident, on_delete=models.CASCADE, related_name='complaints_filed')
    respondent = models.ForeignKey(Resident, on_delete=models.CASCADE, related_name='complaints_received')
    
    case_type = models.CharField(_('Case Type'), max_length=20, choices=CaseType.choices)
    status = models.CharField(_('Status'), max_length=20, choices=Status.choices, default=Status.ACTIVE)
    
    incident_date = models.DateTimeField(_('Date of Incident'))
    incident_place = models.CharField(_('Place of Incident'), max_length=255)
    
    narrative = models.TextField(_('Narrative of Incident'))
    
    date_filed = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = _('Blotter Case')
        verbose_name_plural = _('Blotter Cases')
        ordering = ['-date_filed']

    def __str__(self):
        return f"Case #{self.id}: {self.complainant} vs {self.respondent}"

class Hearing(models.Model):
    case = models.ForeignKey(BlotterCase, on_delete=models.CASCADE, related_name='hearings')
    date = models.DateTimeField(_('Hearing Date'))
    remarks = models.TextField(_('Remarks / Outcome'), blank=True)
    
    class Meta:
        ordering = ['date']
        verbose_name = _('Hearing')
        verbose_name_plural = _('Hearings')

    def __str__(self):
        return f"Hearing for Case #{self.case.id} on {self.date}"
