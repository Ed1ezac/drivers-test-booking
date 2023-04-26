from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CustomUserCreationForm
from .models import Notification

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('dates')
    template_name = 'registration/register.html'
    
    def form_valid(self, form):
        response = super().form_valid(form)  #save user
        # add self.object to the group
        client_group, created = Group.objects.get_or_create(name="Client")
        self.object.groups.add(client_group)
        self.status = 'F' #for FREE
        #Progress, Notification
        self.progress = '1'
        return response

class NotificationListView(LoginRequiredMixin, ListView):
    model = Notification
    template_name = 'notifications.html'

    def get_queryset(self):
        notifications = Notification.objects.filter(user=self.request.user).order_by("-timestamp")
        notifications.update(is_read=True)
        return notifications