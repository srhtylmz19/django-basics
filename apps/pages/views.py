from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home_view(request, *args, **kwargs):
    # return HttpResponse('home page function')
    return render(request, 'home.html', {})


def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})
