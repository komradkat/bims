from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.utils import timezone
from .models import Project

class ProjectDashboardView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'projects/dashboard.html'
    context_object_name = 'projects'
    
    def get_queryset(self):
        return Project.objects.exclude(status=Project.Status.ARCHIVED)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Financial Aggregates
        current_year = timezone.now().year
        total_budget = Project.objects.filter(start_date__year=current_year).aggregate(Sum('budget'))['budget__sum'] or 0
        
        context['total_annual_budget'] = total_budget
        
        # Projects per month (simplified for now, just total count)
        # In a real app, we'd do a TruncMonth query
        
        return context
