from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'base.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class CelerAppView(TemplateView):
    template_name = 'app.html'

class CelerWebView(TemplateView):
    template_name = 'web.html'

class CelerSecView(TemplateView):
    template_name = 'sec.html'

class CelerDeeView(TemplateView):
    template_name = 'dee.html'

class ServicesView(TemplateView):
    template_name = 'services.html'

class ContactView(TemplateView):
    template_name = 'contact.html'