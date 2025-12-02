from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import BarangayInfo

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'core/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['barangay_info'] = BarangayInfo.objects.first()
        return context

