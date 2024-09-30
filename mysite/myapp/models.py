from django.db import models

# Create your models here.

class Usuario(models.Model):
    fullname = models.CharField(max_length=100)
    nickname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)


class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    director = models.CharField(max_length=100)
    año_lanzamiento = models.PositiveIntegerField()
    genero = models.CharField(max_length=50)
    sinopsis = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

