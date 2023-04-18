from django.db import models
from django.urls import reverse

from users.models import CustomUser

#Our models here.
class TestDate(models.Model):
    TEST_TYPES = [
        ('WR', 'Written'),
        ('OB', 'Obstacle'),
        ('RD', 'Road'),
    ]
    #location of test
    location = models.CharField(max_length=100)
    #date and time of test
    date_and_time = models.DateTimeField()
    #type of test
    test_type = models.CharField(max_length=2, choices=TEST_TYPES)
    #max number of candidates
    max_candidates = models.PositiveSmallIntegerField()
    #actual candidates
    candidates = models.ManyToManyField(CustomUser)

    def __str__(self):
        return self.location +' - '+ self.date_and_time.strftime('%d %b %Y - %H:%M %p')
    
    def get_absolute_url(self):
        return reverse('dates')