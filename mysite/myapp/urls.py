from django.urls import path
from .views import home, clasicos, contacto, estrenos, generos, registro

urlpatterns = [
    path('', home, name='home'), 
    path('clasicos/', clasicos, name='clasicos'), 
    path('contacto/', contacto, name='contacto'), 
    path('estrenos/', estrenos, name='estrenos'), 
    path('generos/', generos, name='generos'),   
    path('registro/', registro, name='registro'),    
]