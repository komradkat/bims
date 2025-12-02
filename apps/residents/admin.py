from django.contrib import admin
from .models import Resident

@admin.register(Resident)
class ResidentAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'sex', 'classification', 'street_address', 'is_active')
    list_filter = ('sex', 'classification', 'is_active', 'street_address')
    search_fields = ('last_name', 'first_name', 'street_address')
    list_per_page = 20
