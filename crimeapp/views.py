from django.shortcuts import render
from .models import year

# Create your views here.

def home(request):
    return render(request, 'index.html')

def detection(request):
    return render(request, 'detection.html')

def dataset(request):
    years = year.objects.all()
    return render(request, 'dataset.html', {'years': years})