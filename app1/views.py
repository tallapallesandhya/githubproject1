from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sandhya(request):
    return HttpResponse('<h1><marquee>hello!!!!!!!!!!!!!!<marquee></h1>')
