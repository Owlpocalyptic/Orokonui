from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.datastructures import MultiValueDictKeyError
from django.template import loader
from django.urls import reverse
from django.views import View

# Create your views here.

class IndexView(View):
	
    template_name = 'kakas/index.html'

    def get(self, request, *args, **kwargs):
        title = "Kaka Conservation"
        return render(request, self.template_name, {'title': title})

class AboutView(View):
	
    template_name = 'kakas/about.html'

    def get(self, request, *args, **kwargs):
        title = "About Us"
        return render(request, self.template_name, {'title': title})

class ContactView(View):
	
    template_name = 'kakas/contact.html'

    def get(self, request, *args, **kwargs):
        title = "About Us"
        return render(request, self.template_name, {'title': title})

class DownloadView(View):
	
    template_name = 'kakas/downloads.html'

    def get(self, request, *args, **kwargs):
        title = "About Us"
        return render(request, self.template_name, {'title': title})