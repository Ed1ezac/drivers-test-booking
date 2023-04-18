from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from .forms import TestDateForm
from test_dates.models import TestDate

class CreateTestDate(LoginRequiredMixin, CreateView):
    model = TestDate
    login_url = 'login'
    form_class = TestDateForm
    template_name = 'test_dates/create_date.html'
    success_url = reverse_lazy('dates')

class TestDateDetails(LoginRequiredMixin, DetailView):
    model = TestDate
    login_url = 'login'
    template_name = 'test_dates/date_details.html'

class UpdateTestDate(LoginRequiredMixin, UpdateView):
    model = TestDate
    login_url = 'login'
    template_name = 'test_dates/update_date.html'
    success_url = reverse_lazy('dates')
    fields = ['location', 'date_and_time', 'test_type', 'max_candidates']

class DeleteTestDate(LoginRequiredMixin, DeleteView):
    model = TestDate
    login_url = 'login'
    template_name = 'test_dates/delete_date.html'
    success_url = reverse_lazy('dates')
    fields = ['location', 'date_and_time', 'test_type']