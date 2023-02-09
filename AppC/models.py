from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=40) #letras
    comision = models.IntegerField() # numeros

# crear otra clase para cada elemento
class Estudiante(models.Model):
    nombre = models.CharField(max_length=40) #letras
    apellido = models.CharField(max_length=40) #letras
    email = models.EmailField() # tipo mail

class Profesor(models.Model):
    nombre = models.CharField(max_length=40) #letras
    apellido = models.CharField(max_length=40) #letras
    email = models.EmailField() # tipo mail
    profesion = models.CharField(max_length=30)

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fechaEntrega = models.DateField()
    entregado = models.BooleanField()