from django import forms

class NuevaPersona(forms.Form):
    nombre = forms.CharField(label="Nombres")
    apellidos = forms.CharField(label="Apellidos")
    edad = forms.IntegerField(label="Edad")
    donador = forms.BooleanField(label="Donador")

# django 4 y 5
class RawPersonaForm(forms.Form):
    nombre = forms.CharField(label = "Your Name")
    apellidos = forms.CharField()
    edad = forms.IntegerField(initial = 2)
    donador = forms.BooleanField()
