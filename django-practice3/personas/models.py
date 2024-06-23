from django.db import models
from django.urls import reverse

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    edad = models.IntegerField()
    donador = models.BooleanField()
    
    def get_absolute_url(self):
        return reverse('browsing', kwargs={'myID': self.id})
    


