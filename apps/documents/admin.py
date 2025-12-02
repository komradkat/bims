from django.contrib import admin
from .models import DocumentRequest

@admin.register(DocumentRequest)
class DocumentRequestAdmin(admin.ModelAdmin):
    list_display = ('resident', 'document_type', 'purpose', 'date_issued', 'issued_by')
    list_filter = ('document_type', 'date_issued')
    search_fields = ('resident__last_name', 'resident__first_name', 'or_number')
    autocomplete_fields = ['resident']
