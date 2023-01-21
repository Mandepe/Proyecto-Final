from django.shortcuts import render
from .models import Artistas, Bandas, Albums, inicio
from django.http import HttpResponse

# Create your views here.


def artistas(request):
    return render (request, "rockapp/artistas.html")

def bandas(request):
    return render (request, "rockapp/bandas.html")

def albums(request):   
    return render (request, "rockapp/albums.html")

def inicio(request):
    return render (request, "rockapp/inicio.html")