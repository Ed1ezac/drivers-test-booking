from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import TestDate

class DatesListView(ListView):
    model = TestDate
    template_name = 'dates.html'

class WelcomePage(TemplateView):
    template_name = 'home.html'