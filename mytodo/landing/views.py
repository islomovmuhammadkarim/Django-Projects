from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import About
# Create your views here.
def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render({}, request))



def about(request):
    about = About.objects.first()  # yoki Profile.objects.first()
    return render(request, 'about.html', {'about': about})

def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render({}, request))
