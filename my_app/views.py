from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def my_app_index(request):
    return render(request,'my_app_templates/index.html')

def my_app_gallary(request):
    return render(request,'my_app_templates/gallary.html')

def my_app_players(request):
    return render(request,'my_app_templates/players.html')

def my_app_about(request):
    return render(request,'my_app_templates/about.html')

def my_app_contact(request):
    return render(request,'my_app_templates/contact.html')