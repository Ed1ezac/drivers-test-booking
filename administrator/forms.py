from django import forms

class TestDateForm(forms.Form):
    date_time_formats = ['%m/%d/%Y %H:%M', '%m/%d/%y %H:%M']
    location = forms.CharField(label="Test Location", max_length=100)
    date = forms.DateTimeField(label ="Date of Test",input_formats=date_time_formats, 
                help_text="Please use the following format: <em>MM/DD/YY</em>.")
    max_candidates = forms.IntegerField(label="Maximum number of Candidates", min_value=1, max_value=250)