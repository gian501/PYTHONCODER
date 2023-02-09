from django.urls import path
from AppC import views
# importando las funciones desde views


urlpatterns = [
    path('', views.inicio, name='Inicio'), # esta conectado con views
    path('cursos/', views.cursos, name='Cursos'),
    path('profesores/', views.profesores, name='Profesores'),
    path('estudiantes/', views.estudiantes, name='Estudiantes'),
    path('entregables/', views.entregables, name='Entregables'), # aqui indico donde se parte
]