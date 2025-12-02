from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Official

class OfficialListView(LoginRequiredMixin, ListView):
    model = Official
    template_name = 'officials/official_list.html'
    context_object_name = 'officials'
    
    def get_queryset(self):
        return Official.objects.filter(is_active=True).order_by('position')
