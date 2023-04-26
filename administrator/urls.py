from django.urls import path
from .views import (
    CreateTestDate, 
    DeleteTestDate,
    UpdateTestDate,
    TestDateDetails,
    reject_candidate,
    approve_candidate,
    create_groups_and_perms)


urlpatterns = [
    path('new/date', CreateTestDate.as_view(), name='new_date'),
    path('create/groups', create_groups_and_perms, name='new_groups'),
    path('date/<int:pk>/edit', UpdateTestDate.as_view(), name='edit_date'),
    path('date/<int:pk>/delete', DeleteTestDate.as_view(), name='delete_date'),
    path('date/<int:pk>/details', TestDateDetails.as_view(), name='date_details'),
    #applications
    path('application/<int:pk>/reject', reject_candidate, name='reject_app'),
    path('application/<int:pk>/approve', approve_candidate, name='approve_app'),
]