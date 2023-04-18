from django import forms
from test_dates.models import TestDate

class TestDateForm(forms.ModelForm):
    class Meta:
        model = TestDate
        fields = ['location', 'test_type', 'date_and_time', 'max_candidates']

    date_time_formats = ['%m/%d/%Y %H:%M', '%m/%d/%y %H:%M']
    location = forms.CharField(label="Test Location", max_length=100)
    test_type = forms.ChoiceField(choices=TestDate.TEST_TYPES) 
    date_and_time = forms.DateTimeField(label ="Date and Time of Test",input_formats=date_time_formats, 
                help_text="Please use the format: <em>MM/DD/YY HH:mm</em>.")
    max_candidates = forms.IntegerField(label="Maximum number of Candidates", min_value=1, max_value=250)