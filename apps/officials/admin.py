from django.contrib import admin
from .models import Official

@admin.register(Official)
class OfficialAdmin(admin.ModelAdmin):
    list_display = ('position', 'last_name', 'first_name', 'committee', 'is_active')
    list_filter = ('position', 'is_active')
    search_fields = ('last_name', 'first_name', 'committee')
