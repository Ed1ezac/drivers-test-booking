#from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView
from django.contrib import messages

from .models import TestDate

class DatesListView(LoginRequiredMixin, ListView):
    model = TestDate
    login_url = 'login'
    template_name = 'dates.html'

class WelcomePage(TemplateView):
    template_name = 'home.html'

class DateBooking():
    #user books test
    def user_books_test(request, pk):
        #get date by id
        date = TestDate.objects.get(id=pk)
        #add user model
        if len(date.candidates.all()) < date.max_candidates:
            date.candidates.add(request.user)
            #return back with feedback message
            messages.success(request, 'You have successfully booked the test.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/dates')) 
        else:
            messages.error(request, 'Sorry, a maxium number of candidates have registered.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/dates'))
        endif
    
    def user_cancels_booking(request, pk):
        date = TestDate.objects.get(id=pk)
        date.candidates.remove(request.user)
        messages.success(request, 'You have cancelled your test booking successfully.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/dates')) 
    