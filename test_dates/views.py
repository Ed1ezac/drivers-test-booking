from django.shortcuts import render
from django.views.generic import ListView
from .models import TestDate

class DatesListView(ListView):
    model = TestDate
    template_name = 'dates.html'