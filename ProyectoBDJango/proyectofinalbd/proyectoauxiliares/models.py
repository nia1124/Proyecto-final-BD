from django.db import models

# Create your models here.

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.TextField()

    def __str__(self):
        return self.nombre
