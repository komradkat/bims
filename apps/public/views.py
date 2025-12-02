from django.views.generic import TemplateView, ListView
from apps.core.models import BarangayInfo
from apps.officials.models import Official
from apps.projects.models import Project

class PublicBaseView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['barangay_info'] = BarangayInfo.objects.first()
        return context

class LandingPageView(PublicBaseView):
    template_name = 'public/landing.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_projects'] = Project.objects.exclude(status=Project.Status.ARCHIVED).order_by('-updated_at')[:3]
        return context

class PublicOfficialsView(PublicBaseView):
    template_name = 'public/officials.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['officials'] = Official.objects.filter(is_active=True).order_by('position')
        return context

class PublicProjectsView(PublicBaseView):
    template_name = 'public/projects.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.exclude(status=Project.Status.ARCHIVED).order_by('-start_date')
        return context
