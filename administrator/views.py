from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import TestDateForm
from test_dates.models import TestDate


def create_test_date(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = TestDateForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect("/")
    else:
        form = TestDateForm()
    
    return render(request, "create_date.html", {"form": form})

class CreateTestDate(LoginRequiredMixin, CreateView):
    model = TestDate
    login_url = 'login'
    template_name = 'update_date.html'
    success_url = reverse_lazy('dates')
    fields = ['location', 'date_and_time', 'max_candidates']


class UpdateTestDate(LoginRequiredMixin, UpdateView):
    model = TestDate
    login_url = 'login'
    template_name = 'update_date.html'
    success_url = reverse_lazy('dates')
    fields = ['location', 'date_and_time', 'max_candidates']

class DeleteTestDate(LoginRequiredMixin, DeleteView):
    model = TestDate
    login_url = 'login'
    template_name = 'delete_date.html'
    success_url = reverse_lazy('dates')
    fields = ['location', 'date_and_time']