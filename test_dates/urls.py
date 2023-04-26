from django.urls import path

from .views import DatesListView, MyDatesListView, WelcomePage, DateBooking

urlpatterns = [
    path('', WelcomePage.as_view(), name='home'),
    path('dates', DatesListView.as_view(), name='dates'),
    path('date/my-dates', MyDatesListView.as_view(), name='my_dates'),
    path('date/<int:pk>/register', DateBooking.user_books_test, name='book_test'),
    path('date/<int:pk>/de-register', DateBooking.user_cancels_booking, name='cancel_booking'),
]