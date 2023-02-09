from django.shortcuts import render
from django.http import HttpResponse
from AppC.models import Curso

# Create your views here.
def curso(self):
    curso = Curso(nombre = 'Desarrollo web', comision = '19881') #igual que el nombre de la clase en models
    curso.save()
    documentoTexto = f'--> Curso: {curso.nombre} comision: {curso.comision}'
    return HttpResponse(documentoTexto)