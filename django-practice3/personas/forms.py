from django import forms

class NuevaPersona(forms.Form):
    nombre = forms.CharField(label="Nombres")
    apellidos = forms.CharField(label="Apellidos")
    edad = forms.IntegerField(label="Edad")
    donador = forms.BooleanField(label="Donador")
