from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request): #represent the http request
    return HttpResponse("Hello, world")
#but when do you response? urls.py -> manually added
