from django.urls import path
from .views import BlotterCaseListView, BlotterCaseDetailView, BlotterCaseCreateView

urlpatterns = [
    path('', BlotterCaseListView.as_view(), name='blotter_case_list'),
    path('add/', BlotterCaseCreateView.as_view(), name='blotter_case_add'),
    path('<int:pk>/', BlotterCaseDetailView.as_view(), name='blotter_case_detail'),
]
