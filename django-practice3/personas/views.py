from django.shortcuts import render
from django.http import HttpResponse
from .models import Persona
from .forms import NuevaPersona

# Create your views here.
def myHomeView(request, *args, **kargs):
    #objeto = Persona.objects.get(id = 1)
    mycontext = {
        'mytext': 'Esto es sobre nosotros :|',
        'mynumber': 123,
        'mylist': [33, 44, 55]
    }
    return render(request, 'home.html', mycontext)

def mySecondView(request, *args, **kargs):
    objeto = Persona.objects.get(id = 1)
    context = {
        'nombre': objeto.nombre,
        'edad': objeto.edad
    }
    return render(request, 'test.html', context)

def myForm(request, *args, **kargs):
    print(request.GET)
    Persona.objects.create(nombre=request.GET[nombre], apellidos=request.GET[apellidos], edad=request.GET[edad], donador=request.GET[donador])
    return render(request, 'formulario.html', {
                      'form': NuevaPersona
                  })
