from django.urls import path
from .views import (
    CreateTestDate, 
    DeleteTestDate,
    UpdateTestDate,
    TestDateDetails,
    reject_candidate,
    approve_candidate,
    add_result_pass,
    add_result_fail,
    delete_candidate_application,
    create_groups_and_perms)


urlpatterns = [
    path('new/date', CreateTestDate.as_view(), name='new_date'),
    path('refresh/groups', create_groups_and_perms, name='new_groups'),
    path('date/<int:pk>/edit', UpdateTestDate.as_view(), name='edit_date'),
    path('date/<int:pk>/delete', DeleteTestDate.as_view(), name='delete_date'),
    path('date/<int:pk>/details', TestDateDetails.as_view(), name='date_details'),
    #applications
    path('application/<int:pk>/reject', reject_candidate, name='reject_app'),
    path('application/<int:pk>/approve', approve_candidate, name='approve_app'),
    path('application/<int:pk>/delete', delete_candidate_application, name='delete_app'),
    #results
    path('application/<int:pk>/pass', add_result_pass, name='pass_app'),
    path('application/<int:pk>/fail', add_result_fail, name='fail_app')
]