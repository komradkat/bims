from django.contrib import admin
from .models import ActivityLog, Session

@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'model_name', 'object_repr', 'timestamp')
    list_filter = ('action', 'timestamp')
    search_fields = ('user__username', 'details')
    readonly_fields = ('user', 'action', 'model_name', 'object_repr', 'details', 'timestamp')
    
    def has_add_permission(self, request):
        return False
        
    def has_change_permission(self, request, obj=None):
        return False

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    list_filter = ('date',)
    search_fields = ('title', 'agenda')
    filter_horizontal = ('attendees',)
