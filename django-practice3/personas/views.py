from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Persona
from .forms import NuevaPersona, RawPersonaForm
from django.views.generic import ListView, DetailView

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
    Persona.objects.create(nombre=request.GET['nombre'], apellidos=request.GET['apellidos'], edad=request.GET['edad'], donador=request.GET['donador'])
    return render(request, 'formulario.html', {
                      'form': NuevaPersona
                  })

# Django 4  y 5
def personasAnotherCreateView(request):
    form = RawPersonaForm()
    if request.method == "POST":
        form = RawPersonaForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Persona.objects.create(**form.cleaned_data)
        else:
            print(form.errors)
    context = {
        'form': form,
    }
    return render(request, 'personasCreate.html', context)

def personasShowObject(request, myID):
    obj = get_object_or_404(Persona, id = myID)
    context = {
        'objeto': obj
    }
    return render(request, 'descripcion.html', context)

def personasListView(request):
    queryset = Persona.objects.all()
    context = {
        'objectList': queryset, 
    }
    return render(request, 'personasLista.html', context)

def personasDeleteView(request, myID):
    obj = get_object_or_404(Persona, id = myID)
    if request.method == 'POST':
        print('lo borro')
        obj.delete()
    context = {
        'objeto': obj
    }
    return render(request, 'personasBorrar.html', context)

class PersonaListView(ListView):
    model = Persona
    queryset = Persona.objects.filter(edad__lte='12')
    
class PersonaDetailView(DetailView):
    model = Persona