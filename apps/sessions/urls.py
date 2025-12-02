from django.urls import path
from .views import SessionListView, SessionDetailView, ActivityLogListView

urlpatterns = [
    path('', SessionListView.as_view(), name='session_list'),
    path('<int:pk>/', SessionDetailView.as_view(), name='session_detail'),
    path('logs/', ActivityLogListView.as_view(), name='activity_logs'),
]
