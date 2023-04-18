from django.db import models
from django.urls import reverse

from users.models import CustomUser

#Our models here.
class TestDate(models.Model):
    location = models.CharField(max_length=100)
    #date and time
    date_and_time = models.DateTimeField()
    #type of test
    #max_no_candidates
    max_candidates = models.PositiveSmallIntegerField()
    candidates = models.ManyToManyField(CustomUser)

    def __str__(self):
        return self.location +' - '+ self.date_and_time.strftime('%d %b %Y - %H:%M %p')
    
    def get_absolute_url(self):
        return reverse('dates')