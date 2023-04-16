from django.urls import path

from .views import DatesListView

urlpatterns = [
    path('', DatesListView.as_view(), name='dates'),
]