from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'budget', 'start_date', 'target_end_date')
    list_filter = ('status', 'start_date')
    search_fields = ('title', 'location')
    date_hierarchy = 'start_date'
