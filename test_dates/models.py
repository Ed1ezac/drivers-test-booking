from django.db import models
from django.urls import reverse

from users.models import CustomUser

#Our models here.
class TestDate(models.Model):
    TEST_TYPES = [
        ('1', 'Written'),
        ('2', 'Obstacle'),
        ('3', 'Road'),
    ]
    #location of test
    location = models.CharField(max_length=100)
    #date and time of test
    date_and_time = models.DateTimeField()
    test_type = models.CharField(max_length=2, choices=TEST_TYPES)
    max_candidates = models.PositiveSmallIntegerField()

    def user_has_applied(self, user):
        return self.testapplication_set.filter(user=self.request.user)


    def __str__(self):
        return self.location +' - '+ self.date_and_time.strftime('%d %b %Y - %H:%M %p')
    
    def get_absolute_url(self):
        return reverse('dates')

class TestApplication(models.Model):
    STATUS = [
        ('P', 'Pending'),
        ('A', 'Approved'),
        ('R', 'Rejected'),
    ]

    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    test = models.ForeignKey(TestDate, on_delete = models.CASCADE)
    application_status = models.CharField(max_length = 1, choices = STATUS)

    @classmethod
    def create(cls, user, test, status):
        application = cls(user = user, test = test, application_status = status)
        return application
    
    def __str__(self):
        return self.user.username + ' - ' + self.test.location +' - '+ self.test.date_and_time.strftime('%d %b %Y - %H:%M %p')

class TestResult(models.Model):
    RESULTS = [
        ('P', 'Pass'),
        ('F', 'Fail'),
        ('X', 'No Show'),
    ]

    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    application = models.OneToOneField(TestApplication, on_delete = models.CASCADE, primary_key=True,)
    test_result = models.CharField(max_length=1, choices=RESULTS)

    @classmethod
    def create(cls, user, test, res):
        application = cls(user = user, test = test, test_result = res)
        return application

    def __str__(self):
        return (self.user.username + ' - ' + 
            self.application.test.location +' - '+ 
            self.application.test.date_and_time.strftime('%d %b %Y - %H:%M %p')+ ' : '+ 
            dict(self.RESULTS).get(self.test_result))