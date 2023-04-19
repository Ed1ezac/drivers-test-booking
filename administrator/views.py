from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import (AccessMixin,
    LoginRequiredMixin, PermissionRequiredMixin)


from .forms import TestDateForm
from test_dates.models import TestDate

class CreateTestDate(LoginRequiredMixin, 
    PermissionRequiredMixin, AccessMixin, CreateView):
    model = TestDate
    login_url = 'login'
    form_class = TestDateForm
    permission_required = 'test_dates.add_testdate'
    template_name = 'test_dates/create_date.html'
    success_url = reverse_lazy('dates')

    def handle_no_permission(self):
        messages.error(self.request, 'Sorry, you are not authorized for that.')
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER', '/dates'))

class TestDateDetails(LoginRequiredMixin, 
    PermissionRequiredMixin,AccessMixin, DetailView):
    model = TestDate
    login_url = 'login'
    permission_required = 'test_dates.view_testdate'
    template_name = 'test_dates/date_details.html'

    def handle_no_permission(self):
        messages.error(self.request, 'Sorry, you are not authorized for that.')
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER', '/dates'))

class UpdateTestDate(LoginRequiredMixin,
    PermissionRequiredMixin,AccessMixin, UpdateView):
    model = TestDate
    login_url = 'login'
    template_name = 'test_dates/update_date.html'
    success_url = reverse_lazy('dates')
    permission_required = 'test_dates.change_testdate'
    fields = ['location', 'date_and_time', 'test_type', 'max_candidates']

    def handle_no_permission(self):
        messages.error(self.request, 'Sorry, you are not authorized for that.')
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER', '/dates'))

class DeleteTestDate(LoginRequiredMixin,
     PermissionRequiredMixin,AccessMixin, DeleteView):
    model = TestDate
    login_url = 'login'
    template_name = 'test_dates/delete_date.html'
    success_url = reverse_lazy('dates')
    #raise_exception = False
    #handle_no_permission = handle_unauthorized
    permission_required = 'test_dates.delete_testdate'
    fields = ['location', 'date_and_time', 'test_type']

    def handle_no_permission(self):
        messages.error(self.request, 'Sorry, you are not authorized for that.')
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER', '/dates'))

def create_groups_and_perms(request):
    #groups
    client, created = Group.objects.get_or_create(name="Client")
    officer, created = Group.objects.get_or_create(name="Officer")
    administrator, created = Group.objects.get_or_create(name="Administrator")

    content_type = ContentType.objects.get_for_model(TestDate)
    test_date_perms = Permission.objects.filter(content_type=content_type)

    print([perm.codename for perm in test_date_perms])

    for perm in test_date_perms:
        if (perm.codename == "add_testdate" or 
            perm.codename == "delete_testdate"):
            administrator.permissions.add(perm)

        elif perm.codename == "view_testdate":
            officer.permissions.add(perm)
            administrator.permissions.add(perm)

        else:
            client.permissions.add(perm)
            officer.permissions.add(perm)
            administrator.permissions.add(perm)

    messages.success(request, 'Groups and permissions added successfully.')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/dates'))

#In template
#{{ user.groups.all.0 }}
#{{ perms.app_name }}