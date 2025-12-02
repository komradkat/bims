from django.urls import path
from .views import OfficialListView

urlpatterns = [
    path('', OfficialListView.as_view(), name='official_list'),
]
