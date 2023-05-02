from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.views.generic import CreateView, ListView
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

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


class showUsers(LoginRequiredMixin, 
        PermissionRequiredMixin, ListView):
        model = CustomUser
        template_name = 'admin/users.html'
        permission_required = 'test_dates.delete_testdate'

def can_manage_others(user):
    return user.is_authenticated and user.has_perm("test_dates.delete_testdate")

@user_passes_test(can_manage_others, login_url="/login")
def to_admin(request, pk):
    user = CustomUser.objects.get(id=pk)
    #flush all groups
    user.groups.clear()
    grp, created = Group.objects.get_or_create(name="Administrator")
    user.groups.add(grp)

    messages.success(request, 'User has been granted Administrator privileges successfully.')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/dates'))

@user_passes_test(can_manage_others, login_url="/login")
def to_officer(request, pk):
    user = CustomUser.objects.get(id=pk)
    #flush all groups 
    user.groups.clear()
    grp, created = Group.objects.get_or_create(name="Officer")
    user.groups.add(grp)

    messages.success(request, 'User has been granted Officer privileges successfully.')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/dates'))

@user_passes_test(can_manage_others, login_url="/login")
def to_client(request, pk):
    user = CustomUser.objects.get(id=pk)
    #flush all groups 
    user.groups.clear()
    grp, created = Group.objects.get_or_create(name="Client")
    user.groups.add(grp)

    messages.success(request, 'User is now a client, privileges removed successfully.')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/dates'))


class NotificationListView(LoginRequiredMixin, ListView):
    model = Notification
    template_name = 'notifications.html'

    def get_queryset(self):
        notifications = Notification.objects.filter(user=self.request.user).order_by("-timestamp")
        notifications.update(is_read=True)
        return notifications