from django.db import models
from django.utils.translation import gettext_lazy as _

class Project(models.Model):
    class Status(models.TextChoices):
        NOT_STARTED = 'NOT_STARTED', _('Not Started')
        ON_GOING = 'ON_GOING', _('On-Going')
        COMPLETED = 'COMPLETED', _('Completed')
        ARCHIVED = 'ARCHIVED', _('Archived')

    title = models.CharField(_('Project Title'), max_length=255)
    description = models.TextField(_('Description'), blank=True)
    location = models.CharField(_('Location'), max_length=255)
    
    budget = models.DecimalField(_('Budget'), max_digits=12, decimal_places=2)
    
    start_date = models.DateField(_('Start Date'))
    target_end_date = models.DateField(_('Target End Date'))
    actual_end_date = models.DateField(_('Actual End Date'), null=True, blank=True)
    
    status = models.CharField(
        _('Status'), 
        max_length=20, 
        choices=Status.choices, 
        default=Status.NOT_STARTED
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')
        ordering = ['-start_date']

    def __str__(self):
        return self.title
