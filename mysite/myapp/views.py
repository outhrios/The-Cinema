from django.shortcuts import render

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