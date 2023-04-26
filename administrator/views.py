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
from test_dates.models import TestApplication,TestResult,TestDate
from users.models import Notification 

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

def approve_candidate(request, pk):
    #user->test_applications->appove
    app = TestApplication.objects.get(id=pk)
    app.application_status = 'A'
    app.save()
    #Result
    TestResult.objects.create(user=app.user, application=app, test_result='X')
    #create a notification obj 
    Notification.objects.create(user=app.user, message="Your Test booking has been approved!")
    messages.success(request, app.user.username +' has been approved for the test.')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/dates'))

def delete_candidate_application(request, pk):
    app = TestApplication.objects.get(id=pk)
    app.user.status = 'F'
    #delete the results
    res = TestResult.objects.filter(user=app.user, application = app)
    if res is not None:
        res.delete()
    app.delete()
    messages.error(request, 'Application has been deleted.')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/dates'))


def reject_candidate(request, pk):
    app = TestApplication.objects.get(id=pk)
    app.application_status = 'R'
    app.save()
    #delete the results
    res = TestResult.objects.filter(user=app.user, application = app)
    if res is not None:
        res.delete()
    #return back
    messages.error(request, app.user.username +' has been rejected for the test.')
    Notification.objects.create(user=app.user, message="Your Test booking has been rejected!")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/dates'))

def add_result_pass(request, pk):
    app = TestApplication.objects.get(id=pk)
    app.testresult.test_result = 'P'
    app.testresult.save()
    #increase progress
    if app.user.progress == '1':
        app.user.progress = '2'
    else:
        app.user.progress = '3'
    #status
    app.user.status = 'F'
    app.user.save()

    messages.success(request, app.user.username +' has been graded a PASS for the test.')
    Notification.objects.create(user=app.user, message="Congratulations! You have passed the test!")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/dates'))
    

def add_result_fail(request, pk):
    app = TestApplication.objects.get(id=pk)
    app.testresult.test_result = 'F'
    app.testresult.save()
    #
    app.user.status = 'F'
    app.user.save()
    #
    messages.error(request, app.user.username +' has been graded a FAIL for the test.')
    Notification.objects.create(user=app.user, message="You have failed the test!")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/dates'))

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
#{{ user.groups }}
#{{ perms.app_name }}