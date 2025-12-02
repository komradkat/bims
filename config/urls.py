from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.public.urls')),
    path('portal/', include('apps.core.urls')),
    path('auth/', include('apps.authentication.urls')),
    path('residents/', include('apps.residents.urls')),
    path('officials/', include('apps.officials.urls')),
    path('projects/', include('apps.projects.urls')),
    path('documents/', include('apps.documents.urls')),
    path('sessions/', include('apps.sessions.urls')),
    path('blotter/', include('apps.blotter.urls')),
]
