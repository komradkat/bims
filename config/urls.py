from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.public.urls')),
    path('portal/', include('apps.core.urls')),
    path('auth/', include('apps.authentication.urls')),
    path('portal/residents/', include('apps.residents.urls')),
    path('portal/officials/', include('apps.officials.urls')),
    path('portal/projects/', include('apps.projects.urls')),
    path('portal/documents/', include('apps.documents.urls')),
    path('portal/sessions/', include('apps.sessions.urls')),
    path('portal/blotter/', include('apps.blotter.urls')),
]
