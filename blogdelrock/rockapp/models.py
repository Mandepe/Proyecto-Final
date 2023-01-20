from django.db import models

# Create your models here.

class Artista(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_nacimiento = models.DateField()

class Banda(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    


class Album(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE)

class inicio(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    banda = models.ForeignKey(Banda, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)