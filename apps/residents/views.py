from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count, Q
from .models import Resident

class ResidentListView(LoginRequiredMixin, ListView):
    model = Resident
    template_name = 'residents/resident_list.html'
    context_object_name = 'residents'
    paginate_by = 10

    def get_queryset(self):
        queryset = Resident.objects.filter(is_active=True)
        
        # Search
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(last_name__icontains=query) | 
                Q(first_name__icontains=query) |
                Q(street_address__icontains=query)
            )
            
        # Filters
        sex = self.request.GET.get('sex')
        if sex:
            queryset = queryset.filter(sex=sex)
            
        classification = self.request.GET.get('classification')
        if classification:
            queryset = queryset.filter(classification=classification)
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classifications'] = Resident.Classification.choices
        return context

class ResidentsDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'residents/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # KPI Cards
        total_population = Resident.objects.filter(is_active=True).count()
        male_count = Resident.objects.filter(is_active=True, sex='M').count()
        female_count = Resident.objects.filter(is_active=True, sex='F').count()
        
        context.update({
            'total_population': total_population,
            'male_count': male_count,
            'female_count': female_count,
        })
        
        # Chart Data
        classification_data = Resident.objects.filter(is_active=True).values('classification').annotate(count=Count('classification'))
        
        # Prepare data for Chart.js
        labels = []
        data = []
        
        # Map codes to labels
        classification_dict = dict(Resident.Classification.choices)
        
        for item in classification_data:
            label = classification_dict.get(item['classification'], item['classification'])
            labels.append(label)
            data.append(item['count'])
            
        context['chart_labels'] = labels
        context['chart_data'] = data
        
        return context
