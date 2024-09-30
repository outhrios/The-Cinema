from rest_framework import serializers
from .models import Usuario, Pelicula

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta: 
        fields = '__all__'
        model = Usuario


class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = '__all__'