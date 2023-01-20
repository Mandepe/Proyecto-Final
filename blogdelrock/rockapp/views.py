from django.shortcuts import render
from .models import Artista, Banda, Album
from django.http import HttpResponse

# Create your views here.


def artistas(request):
    artistas = Artista.objects.all()
    artistas.save()
    cadena = "Guardado correctamente"
    return HttpResponse(artistas)

def bandas(request):
    bandas = Banda.objects.all()
    bandas.save()
    cadena = "Guardado correctamente"
    return HttpResponse(bandas)

def albums(request):
    albums = Album.objects.all()
    albums.save()
    cadena = "Guardado correctamente"   
    return HttpResponse(albums)
