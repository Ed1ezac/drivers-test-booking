from django.urls import path
from .views import (
        SignUpView,
        showUsers,
        to_client,
        to_admin,
        to_officer,
        NotificationListView)

urlpatterns = [
    path('register/', SignUpView.as_view(), name='register'),
    path('notifications/', NotificationListView.as_view(), name='notifications'),
    path('manage/', showUsers.as_view(), name='man_users'),
    path('<int:pk>/make-admin/', to_admin, name='mk_admin'),
    path('<int:pk>/make-officer/', to_officer, name='mk_officer'),
    path('<int:pk>/make-client/', to_client, name='mk_client'),
]