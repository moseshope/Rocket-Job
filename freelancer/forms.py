from django import forms
from .models import Bid

# Create your forms here.


class Bid_Form(forms.ModelForm):

    class Meta:
        model = Bid
        fields = ['bid_text', 'bid_time', 'bid_budget']
