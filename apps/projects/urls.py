from django.urls import path
from .views import ProjectDashboardView

urlpatterns = [
    path('', ProjectDashboardView.as_view(), name='project_dashboard'),
]
