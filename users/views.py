from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import Group
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CustomUserCreationForm
from .models import Notification, CustomUser

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('dates')
    template_name = 'registration/register.html'
    
    def form_valid(self, form):
        self.object = form.save()
        #add self.object to the group
        client_group, created = Group.objects.get_or_create(name="Client")
        self.object.groups.add(client_group)
        self.object.status = 'F' #for Free/available
        #Progress,
        self.object.progress = '1'
        self.object.save()
        return super(SignUpView, self).form_valid(form)  #save user


class NotificationListView(LoginRequiredMixin, ListView):
    model = Notification
    template_name = 'notifications.html'

    def get_queryset(self):
        notifications = Notification.objects.filter(user=self.request.user).order_by("-timestamp")
        notifications.update(is_read=True)
        return notifications