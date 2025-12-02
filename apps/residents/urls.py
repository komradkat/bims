from django.urls import path
from .views import ResidentListView, ResidentsDashboardView

urlpatterns = [
    path('', ResidentsDashboardView.as_view(), name='residents_dashboard'),
    path('list/', ResidentListView.as_view(), name='resident_list'),
]
