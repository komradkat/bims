from django.contrib import admin
from .models import BlotterCase, Hearing

class HearingInline(admin.TabularInline):
    model = Hearing
    extra = 1

@admin.register(BlotterCase)
class BlotterCaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'complainant', 'respondent', 'case_type', 'status', 'date_filed')
    list_filter = ('status', 'case_type', 'date_filed')
    search_fields = ('complainant__last_name', 'respondent__last_name', 'narrative')
    autocomplete_fields = ['complainant', 'respondent']
    inlines = [HearingInline]
