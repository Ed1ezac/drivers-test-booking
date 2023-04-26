from django.urls import path
from .views import SignUpView, NotificationListView

urlpatterns = [
    path('register/', SignUpView.as_view(), name='register'),
    path('notifications/', NotificationListView.as_view(), name='notifications'),
]