from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.TextField()
    apellido = models.TextField()
    edad = models.IntegerField()
    
    def __str__(self):
        return self.nombre + ' ' + self.apellido