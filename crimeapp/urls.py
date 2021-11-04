from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dataset.html', views.dataset, name='dataset'),
    path('detection.html', views.detection, name='detection'),
    path('index.html', views.home, name='home')
]
