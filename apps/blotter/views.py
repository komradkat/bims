from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django import forms
from .models import BlotterCase

class BlotterCaseListView(LoginRequiredMixin, ListView):
    model = BlotterCase
    template_name = 'blotter/case_list.html'
    context_object_name = 'cases'
    paginate_by = 20

class BlotterCaseDetailView(LoginRequiredMixin, DetailView):
    model = BlotterCase
    template_name = 'blotter/case_detail.html'
    context_object_name = 'case'

class BlotterCaseCreateView(LoginRequiredMixin, CreateView):
    model = BlotterCase
    template_name = 'blotter/case_form.html'
    fields = ['complainant', 'respondent', 'case_type', 'incident_date', 'incident_place', 'narrative']
    success_url = reverse_lazy('blotter_case_list')
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['incident_date'].widget = forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'})
        form.fields['complainant'].widget.attrs.update({'class': 'form-control'})
        form.fields['respondent'].widget.attrs.update({'class': 'form-control'})
        form.fields['case_type'].widget.attrs.update({'class': 'form-control'})
        form.fields['incident_place'].widget.attrs.update({'class': 'form-control'})
        form.fields['narrative'].widget.attrs.update({'class': 'form-control', 'rows': 5})
        return form
