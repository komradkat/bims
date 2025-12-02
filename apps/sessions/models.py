from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

class ActivityLog(models.Model):
    class Action(models.TextChoices):
        CREATE = 'CREATE', _('Create')
        UPDATE = 'UPDATE', _('Update')
        DELETE = 'DELETE', _('Delete')
        LOGIN = 'LOGIN', _('Login')
        LOGOUT = 'LOGOUT', _('Logout')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    action = models.CharField(max_length=20, choices=Action.choices)
    model_name = models.CharField(max_length=100, blank=True)
    object_repr = models.CharField(max_length=255, blank=True)
    details = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = _('Activity Log')
        verbose_name_plural = _('Activity Logs')

    def __str__(self):
        return f"{self.user} - {self.action} - {self.timestamp}"

class Session(models.Model):
    title = models.CharField(_('Session Title'), max_length=255)
    date = models.DateField(_('Date'))
    agenda = models.TextField(_('Agenda'))
    minutes = models.TextField(_('Minutes of the Meeting'), blank=True)
    
    attendees = models.ManyToManyField('officials.Official', related_name='sessions_attended', blank=True)
    
    attachments = models.FileField(_('Attachments'), upload_to='session_attachments/', blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']
        verbose_name = _('Session')
        verbose_name_plural = _('Sessions')

    def __str__(self):
        return f"{self.title} ({self.date})"
