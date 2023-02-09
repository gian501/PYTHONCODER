from django.shortcuts import render
from django.http import HttpResponse
from AppC.models import Curso

# Create your views here.
'''
def curso(self):
    curso = Curso(nombre = 'Desarrollo web', comision = '19881') #igual que el nombre de la clase en models
    curso.save()
    documentoTexto = f'--> Curso: {curso.nombre} comision: {curso.comision}'
    return HttpResponse(documentoTexto)
'''

def inicio(request):
    return render(request, 'AppC/inicio.html') # usar el nombre del template
    #return HttpResponse('Vista Inicio')

def cursos(request):
    return render(request, 'AppC/cursos.html')
    #return HttpResponse('Vista cursos')

def profesores(request):
    return render(request, 'AppC/profesores.html')
    #return HttpResponse('Vista profesores')

def entregables(request):
    return render(request, 'AppC/entregables.html')
    #return HttpResponse('Vista entregables')

def estudiantes(request):
    return render(request, 'AppC/estudiantes.html')
    #return HttpResponse('Vista estudiantes')