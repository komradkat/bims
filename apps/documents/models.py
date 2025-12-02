from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.residents.models import Resident

class DocumentRequest(models.Model):
    class DocumentType(models.TextChoices):
        CLEARANCE = 'CLEARANCE', _('Barangay Clearance')
        INDIGENCY = 'INDIGENCY', _('Certificate of Indigency')
        RESIDENCY = 'RESIDENCY', _('Certificate of Residency')
        BUSINESS_CLEARANCE = 'BUSINESS', _('Business Clearance')
        BARANGAY_ID = 'ID', _('Barangay ID')

    resident = models.ForeignKey(Resident, on_delete=models.CASCADE, related_name='document_requests')
    document_type = models.CharField(_('Document Type'), max_length=20, choices=DocumentType.choices)
    purpose = models.CharField(_('Purpose'), max_length=255)
    
    or_number = models.CharField(_('OR Number'), max_length=50, blank=True, help_text=_('Official Receipt Number if applicable'))
    amount_paid = models.DecimalField(_('Amount Paid'), max_digits=10, decimal_places=2, default=0)
    
    date_issued = models.DateTimeField(auto_now_add=True)
    issued_by = models.ForeignKey('authentication.User', on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        verbose_name = _('Document Request')
        verbose_name_plural = _('Document Requests')
        ordering = ['-date_issued']

    def __str__(self):
        return f"{self.get_document_type_display()} - {self.resident}"
