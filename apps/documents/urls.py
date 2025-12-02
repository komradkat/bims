from django.urls import path
from .views import DocumentRequestCreateView, DocumentPDFView

urlpatterns = [
    path('', DocumentRequestCreateView.as_view(), name='document_request_create'),
    path('generate/<int:pk>/', DocumentPDFView.as_view(), name='document_generate_pdf'),
]
