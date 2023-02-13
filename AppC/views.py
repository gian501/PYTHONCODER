from django.shortcuts import render
from django.http import HttpResponse
from AppC.models import Curso
from AppC.forms import CursoFormulario
# Create your views here.


def inicio(request):
    return render(request, "AppC/inicio.html", )
    #return HttpResponse('Vista Inicio')

def cursos(request):
    if request.method == "POST":
 
        miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
 
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], comision=informacion["comision"])
            curso.save()
            return render(request, "AppC/cursos.html", )
    else:
        miFormulario = CursoFormulario()
    return render(request, 'AppC/cursos.html',{"miFormulario": miFormulario})
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

