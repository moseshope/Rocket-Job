from django import forms
from .models import This_Job

# Create your forms here.


class Add_Job_Form(forms.ModelForm):

    class Meta:
        model = This_Job
        fields = ['title', 'short_text', 'time', 'skill', 'budget']
