from django.shortcuts import render
from .forms import ContactForm
from django.views.generic import FormView , CreateView
from django.urls import reverse_lazy


class ContactUsView(CreateView):
    form_class = ContactForm
    template_name = 'contact-us.html'
    success_url = reverse_lazy('home')
