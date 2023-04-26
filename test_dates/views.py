#from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView
from django.contrib import messages

from .models import TestDate, TestApplication
from users.models import Notification

class DatesListView(LoginRequiredMixin, ListView):
    model = TestDate
    login_url = 'login'
    template_name = 'test_dates/dates_list.html'

    def get_context_data(self,*args, **kwargs):
        context = super(DatesListView, self).get_context_data(*args,**kwargs)
        unread_notifications = Notification.objects.filter(user=self.request.user, is_read=False).count()
        context["unread_notifications"] = unread_notifications
        return context

class MyDatesListView(LoginRequiredMixin, ListView):
    model = TestDate
    login_url = 'login'
    template_name = 'test_dates/my_dates_list.html'

    def get_object(self, queryset=None):
        return TestDate.objects.filter(user=self.request.user)

class WelcomePage(TemplateView):
    template_name = 'home.html'

class DateBooking():
    #user books test
    def user_books_test(request, pk):
        #get date by id
        date = TestDate.objects.get(id=pk)
        #check if maximum candidates not reached
        if len(date.testapplication_set.all()) < date.max_candidates:
            #add application model to date
            application = TestApplication.create(request.user, date, 'P')
            date.testapplication_set.add(application, bulk = False)
            request.user.status = 'A'
            request.user.save() 
            #return back with feedback messages
            Notification.objects.create(user=request.user, message="Your booking is submitted and awaiting approval!")
            #messages.success(request, 'You have successfully booked the test.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/dates')) 
        else:
            messages.error(request, 'Sorry, a maximum number of candidates have registered.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/dates'))
        endif
    
    def user_cancels_booking(request, pk):
        date = TestDate.objects.get(id=pk)
        date.testapplication_set.filter(user = request.user, test = date).delete()
        request.user.status = 'F'
        request.user.save()
        Notification.objects.create(user=request.user, message="You have cancelled your test booking!")
        messages.success(request, 'You have cancelled your test booking.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/dates')) 
    