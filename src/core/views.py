from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def detalles(request):
    return render(request, 'core/detalles.html')