from django.urls import path
from .views import (
    create_test_date, 
    DeleteTestDate,
    UpdateTestDate,)


urlpatterns = [
    #path('new/date', CreateDateView.as_view(), name='new_date'),
    path('administrator/new/date', create_test_date, name='new_date'),
    path('administrator/date/<int:pk>/edit', UpdateTestDate.as_view(), name='edit_date'),
    path('administrator/date/<int:pk>/delete', DeleteTestDate.as_view(), name='delete_date')
]