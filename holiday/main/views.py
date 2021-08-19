from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    slider = Slider.objects.all()
    data = {
        'slider': slider
    }
    return render(request, 'main/index.html', data)

def about(request):
    slider = Slider.objects.all()
    manager_list = ManagersList.objects.all()
    tours = Tours.objects.all()
    data = {
        'slider': slider,
        'managers': manager_list,
        'tours': tours
    }
    return render(request, 'main/about.html', data)

def tours(request):
    slider = Slider.objects.all()
    data = {
        'slider': slider,
    }
    return render(request, 'main/tours.html', data)

def contact(request):
    slider = Slider.objects.all()
    data = {
        'slider': slider,
    }
    return render(request, 'main/contact.html', data)