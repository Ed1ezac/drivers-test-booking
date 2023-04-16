from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView

from .forms import TestDateForm

from .models import TestDate

def create_test_date(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = TestDateForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/")
    else:
        form = TestDateForm()
    
    return render(request, "create_date.html", {"form": form})


class CreateDateView(CreateView):
    model = TestDate
    template_name = 'create_date.html'
    fields = '__all__'