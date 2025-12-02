from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, Count
from .models import BarangayInfo
from apps.residents.models import Resident
from apps.projects.models import Project
from apps.officials.models import Official

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'core/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['barangay_info'] = BarangayInfo.objects.first()
        
        # Key Metrics
        context['total_population'] = Resident.objects.filter(is_active=True).count()
        context['total_households'] = Resident.objects.values('street_address').distinct().count() # Rough estimate
        context['active_projects_count'] = Project.objects.filter(status=Project.Status.ON_GOING).count()
        context['active_officials_count'] = Official.objects.filter(is_active=True).count()
        
        # Recent Projects
        context['recent_projects'] = Project.objects.exclude(status=Project.Status.ARCHIVED).order_by('-updated_at')[:5]
        
        # Population Breakdown
        context['senior_count'] = Resident.objects.filter(classification=Resident.Classification.SENIOR, is_active=True).count()
        context['youth_count'] = Resident.objects.filter(classification=Resident.Classification.YOUTH, is_active=True).count()
        context['pwd_count'] = Resident.objects.filter(classification=Resident.Classification.PWD, is_active=True).count()
        
        return context

