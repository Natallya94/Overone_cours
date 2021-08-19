from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('tours', tours, name='tours'),
    path('contact', contact, name='contact'),
]