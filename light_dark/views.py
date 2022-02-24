from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request): #represent the http request
    return render(request, "light_dark/index.html")
    #return render, (request, "light_dark/index.html")
#but when do you response? urls.py -> manually added when route will

def bunvin(request):
    return HttpResponse("Hello, Bun!")

#def greet(request, name):
 #   return HttpResponse(f"Hello, {name.capitalize()}!")

def greet(request, name):
    return render(request, "light_dark/greet.html", {"name": name.capitalize()})