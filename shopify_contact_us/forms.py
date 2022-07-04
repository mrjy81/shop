from django.forms import ModelForm
from .models import Contact
from django import forms


class ContactForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'موضوع'}))
    message = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'پیغام شما'}))

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message', 'subject']
