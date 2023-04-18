from django.urls import path
from .views import (
    create_test_date, 
    DeleteTestDate,
    UpdateTestDate,)


urlpatterns = [
    #path('new/date', CreateDateView.as_view(), name='new_date'),
    path('new/date', create_test_date, name='new_date'),
    #path('date/<int:pk>/detail', UpdateTestDate.as_view(), name='date_info'),
    path('date/<int:pk>/edit', UpdateTestDate.as_view(), name='edit_date'),
    path('date/<int:pk>/delete', DeleteTestDate.as_view(), name='delete_date')
]