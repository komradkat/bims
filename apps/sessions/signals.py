from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in, user_logged_out
from .models import ActivityLog
from apps.residents.models import Resident
from apps.projects.models import Project
from apps.officials.models import Official
from apps.documents.models import DocumentRequest

def create_log(user, action, instance, details=""):
    if user and user.is_authenticated:
        ActivityLog.objects.create(
            user=user,
            action=action,
            model_name=instance._meta.verbose_name,
            object_repr=str(instance),
            details=details
        )

# Generic signal handler isn't straightforward because we need the 'request' to get the user.
# For simplicity in this MVP, we'll use a middleware-like approach or just rely on views.
# However, Django signals don't have access to request.
# A common pattern is using thread locals or just logging auth events and specific critical model events where we can infer context or accept 'System' user.

# For this implementation, we will log Auth events which have the request/user.
# For model events, we'll just log what happened, but 'user' might be None unless we use a library like django-crum.
# To keep it simple and robust without extra libs, we will log Auth events fully, 
# and for model events, we will just log the change (Audit Trail) without the user if not easily available, 
# OR we implement logging in the Views (which is cleaner for explicit user tracking).

# Let's implement Auth signals first.

@receiver(user_logged_in)
def log_login(sender, request, user, **kwargs):
    ActivityLog.objects.create(
        user=user,
        action=ActivityLog.Action.LOGIN,
        details="User logged in"
    )

@receiver(user_logged_out)
def log_logout(sender, request, user, **kwargs):
    if user:
        ActivityLog.objects.create(
            user=user,
            action=ActivityLog.Action.LOGOUT,
            details="User logged out"
        )
