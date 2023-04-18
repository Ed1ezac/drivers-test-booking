from django.urls import path
from .views import (
    CreateTestDate, 
    DeleteTestDate,
    UpdateTestDate,
    TestDateDetails)


urlpatterns = [
    path('new/date', CreateTestDate.as_view(), name='new_date'),
    path('date/<int:pk>/edit', UpdateTestDate.as_view(), name='edit_date'),
    path('date/<int:pk>/delete', DeleteTestDate.as_view(), name='delete_date'),
    path('date/<int:pk>/details', TestDateDetails.as_view(), name='date_details')
]