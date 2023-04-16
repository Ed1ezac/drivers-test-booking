from django.shortcuts import render
from django.http import HttpResponseRedirect
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

def update_test_date(request):
    if request.method == "POST":
        form = TestDateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        #get the model,
        form = TestDateForm()

class UpdateTestDate(UpdateView):
    model = TestDate
    template_name = 'update_date.html'
    fields = ['location', 'date', 'max_candidates']

class DeleteTestDate(DeleteView):
    model = TestDate
    template_name = 'delete_date.html'
    success_url = reverse_lazy('dates')