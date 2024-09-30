from django.shortcuts import render
from rest_framework import viewsets
from .serializer import UsuarioSerializer, PeliculaSerializer
from .models import Usuario, Pelicula

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer

def home(request):
    return render(request, 'myapp/index.html')

def clasicos(request):
    return render(request, 'myapp/clasicos.html')

def contacto(request):
    return render(request, 'myapp/contacto.html')

def estrenos(request):
    return render(request, 'myapp/estrenos.html')

def generos(request):
    return render(request, 'myapp/generos.html')

def registro(request):
    return render(request, 'myapp/registro.html')

