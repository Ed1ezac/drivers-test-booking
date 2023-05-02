from django.contrib import admin
from .models import TestDate, TestResult
from .models import TestApplication
# Register your models here.

admin.site.register(TestDate)
admin.site.register(TestResult)
admin.site.register(TestApplication)