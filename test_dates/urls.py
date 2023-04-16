from django.urls import path

from .views import DatesListView, WelcomePage

urlpatterns = [
    path('', WelcomePage.as_view(), name='home'),
    path('dates', DatesListView.as_view(), name='dates'),
]