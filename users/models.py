from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    STATUS = [
        ('A', 'Applied'),
        ('F', 'Free'),        
    ]

    STAGES = [
        ('1', 'Theory'),
        ('2', 'Obstacle'),
        ('3', 'Road'),
        ('4', 'Done'),
    ]

    status = models.CharField(max_length=1, choices=STATUS)
    progress = models.CharField(max_length=1, choices=STAGES)

class Notification(models.Model):
    is_read = models.BooleanField(default=False)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username +' - ' + self.message + (" : Read ") if self.is_read  else " : Unread"