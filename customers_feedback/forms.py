from django.forms import ModelForm
from .models import Feedback
from django import forms


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['description', 'rate']


