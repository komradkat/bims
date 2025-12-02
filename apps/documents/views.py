from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
from weasyprint import HTML
from .models import DocumentRequest
from apps.residents.models import Resident
from apps.core.models import BarangayInfo
from apps.officials.models import Official
from django import forms

class DocumentRequestForm(forms.ModelForm):
    class Meta:
        model = DocumentRequest
        fields = ['resident', 'document_type', 'purpose', 'or_number', 'amount_paid']
        widgets = {
            'resident': forms.Select(attrs={'class': 'form-control'}),
            'document_type': forms.Select(attrs={'class': 'form-control'}),
            'purpose': forms.TextInput(attrs={'class': 'form-control'}),
            'or_number': forms.TextInput(attrs={'class': 'form-control'}),
            'amount_paid': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class DocumentRequestCreateView(LoginRequiredMixin, CreateView):
    model = DocumentRequest
    form_class = DocumentRequestForm
    template_name = 'documents/request_form.html'
    success_url = reverse_lazy('document_request_create')

    def form_valid(self, form):
        form.instance.issued_by = self.request.user
        response = super().form_valid(form)
        # Redirect to PDF generation instead of success_url
        return HttpResponse(status=302, headers={'Location': reverse('document_generate_pdf', kwargs={'pk': self.object.pk})})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_requests'] = DocumentRequest.objects.all()[:5]
        return context

class DocumentPDFView(LoginRequiredMixin, TemplateView):
    def get(self, request, pk, *args, **kwargs):
        doc_request = get_object_or_404(DocumentRequest, pk=pk)
        barangay_info = BarangayInfo.objects.first()
        captain = Official.objects.filter(position=Official.Position.CHAIRMAN, is_active=True).first()
        
        context = {
            'doc': doc_request,
            'resident': doc_request.resident,
            'barangay': barangay_info,
            'captain': captain,
            'date': doc_request.date_issued,
        }
        
        # Select template based on type
        template_map = {
            DocumentRequest.DocumentType.CLEARANCE: 'documents/pdf/clearance.html',
            DocumentRequest.DocumentType.INDIGENCY: 'documents/pdf/indigency.html',
            DocumentRequest.DocumentType.RESIDENCY: 'documents/pdf/residency.html',
            DocumentRequest.DocumentType.BUSINESS_CLEARANCE: 'documents/pdf/business.html',
        }
        
        template_name = template_map.get(doc_request.document_type, 'documents/pdf/generic.html')
        
        html_string = render_to_string(template_name, context)
        html = HTML(string=html_string, base_url=request.build_absolute_uri())
        pdf = html.write_pdf()
        
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename="{doc_request.document_type}_{doc_request.resident.last_name}.pdf"'
        return response
