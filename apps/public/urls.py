from django.urls import path
from .views import LandingPageView, PublicOfficialsView, PublicProjectsView

urlpatterns = [
    path('', LandingPageView.as_view(), name='public_home'),
    path('officials/', PublicOfficialsView.as_view(), name='public_officials_list'),
    path('projects/', PublicProjectsView.as_view(), name='public_projects'),
]
