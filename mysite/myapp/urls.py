from django.urls import path, include
from .views import home, clasicos, contacto, estrenos, generos, registro
from rest_framework import routers
from myapp import views

router = routers.DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'peliculas', views.PeliculaViewSet)

urlpatterns = [
    path('', home, name='home'), 
    path('clasicos/', clasicos, name='clasicos'), 
    path('contacto/', contacto, name='contacto'), 
    path('estrenos/', estrenos, name='estrenos'), 
    path('generos/', generos, name='generos'),   
    path('registro/', registro, name='registro'),    
    path('api/', include(router.urls)), 
]