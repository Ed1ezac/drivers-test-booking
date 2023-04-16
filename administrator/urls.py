from django.urls import path

from .views import create_test_date#CreateDateView


urlpatterns = [
    #path('new/date', CreateDateView.as_view(), name='new_date'),
    path('new/date', create_test_date, name='new_date'),
]