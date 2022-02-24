from django.urls import path
from . import views #import the function from views

urlpatterns = [
    path("",views.index, name="index"), #index is the function name in views.py
    path("bunvin",views.bunvin, name="bunvin"),
    path("<str:name>", views.greet, name="greet") #name is what's after /
]