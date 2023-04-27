from django import template
from users.models import CustomUser
from test_dates.models import TestApplication

register = template.Library()

@register.simple_tag
def user_has_applied_for_test(date, user):
    return date.testapplication_set.filter(user = user).count()