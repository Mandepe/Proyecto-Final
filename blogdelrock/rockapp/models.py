from django.db import models

# Create your models here.

class Artistas(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_nacimiento = models.DateField()

class Bandas(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    


class Albums(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    artista = models.ForeignKey(Artistas, on_delete=models.CASCADE)
    banda = models.ForeignKey(Bandas, on_delete=models.CASCADE)

class inicio(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    artista = models.ForeignKey(Artistas, on_delete=models.CASCADE)
    banda = models.ForeignKey(Bandas, on_delete=models.CASCADE)
    album = models.ForeignKey(Albums, on_delete=models.CASCADE)