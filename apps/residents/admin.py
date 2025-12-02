from django.contrib import admin
from .models import Resident, Household

class ResidentInline(admin.TabularInline):
    model = Resident
    fields = ('first_name', 'last_name', 'relationship_to_head', 'birthdate')
    extra = 0

@admin.register(Household)
class HouseholdAdmin(admin.ModelAdmin):
    list_display = ('household_number', 'street_address', 'housing_material', 'ownership_status', 'member_count')
    list_filter = ('housing_material', 'ownership_status')
    search_fields = ('household_number', 'street_address')
    inlines = [ResidentInline]
    
    def member_count(self, obj):
        return obj.members.count()
    member_count.short_description = 'Members'

@admin.register(Resident)
class ResidentAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'sex', 'age', 'classification', 'household', 'is_active')
    list_filter = ('sex', 'classification', 'is_active', 'household')
    search_fields = ('last_name', 'first_name', 'street_address')
    list_editable = ('is_active',)
    autocomplete_fields = ['household']
    
    def age(self, obj):
        from datetime import date
        today = date.today()
        return today.year - obj.birthdate.year - ((today.month, today.day) < (obj.birthdate.month, obj.birthdate.day))
