from django.db import models
from django.urls import reverse

# Create your models here.
class TestDate(models.Model):
    #location
    location = models.CharField(max_length=100)
    #date
    date = models.DateTimeField()
    #type of test
    #no_of_candidates
    #max_no_candidates
    max_candidates = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.location +' - '+ self.date.strftime('%d %b %Y - %H:%M %p')
    
    def get_absolute_url(self):
        return reverse('dates')