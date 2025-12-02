from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Session, ActivityLog

class SessionListView(LoginRequiredMixin, ListView):
    model = Session
    template_name = 'sessions/session_list.html'
    context_object_name = 'sessions'

class SessionDetailView(LoginRequiredMixin, DetailView):
    model = Session
    template_name = 'sessions/session_detail.html'
    context_object_name = 'session'

class ActivityLogListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = ActivityLog
    template_name = 'sessions/activity_log.html'
    context_object_name = 'logs'
    paginate_by = 50

    def test_func(self):
        return self.request.user.role == 'ADMIN' or self.request.user.is_superuser
