from django import forms

class NuevaPersona(forms.Form):
    nombre = forms.CharField(label="Nombres")
    apellidos = forms.CharField(label="Apellidos")
    edad = forms.IntegerField(label="Edad")
    donador = forms.BooleanField(label="Donador")

# django 4 y 5
class RawPersonaForm(forms.Form):
    nombre = forms.CharField(
        widget = forms.Textarea(
            attrs={
                'placeholder': 'Solo tu nombre porfabor',
                'id': 'nombreID',
                'Class': 'special',
                'cols': 10
            }
        )
    )
    apellidos = forms.CharField()
    edad = forms.IntegerField()
    donador = forms.BooleanField()



