from django.contrib import admin
from .models import BarangayInfo

@admin.register(BarangayInfo)
class BarangayInfoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Identity', {
            'fields': ('name', 'logo', 'city_municipality', 'province', 'region')
        }),
        ('Statements', {
            'fields': ('vision', 'mission', 'service_pledge')
        }),
        ('Contact', {
            'fields': ('contact_number', 'email')
        }),
    )
    
    def has_add_permission(self, request):
        # Only allow adding if no instance exists
        if BarangayInfo.objects.exists():
            return False
        return True
