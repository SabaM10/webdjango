from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('', inicio),
    path('cursos/', cursos),
    path('profesores/', profesores),
    path('estudiantes/', estudiantes),
    path('entregables/', entregables),
    path('home/', home),
    path('api_estudiantes/', api_estudiantes),
    path('buscar_estudiante/', buscar_estudiante),
    path('create_estudiantes/', create_estudiantes),
    path('update_estudiantes/<estudiante_id>', update_estudiantes),        
    path('read_estudiantes/', read_estudiantes),
    path('delete_estudiantes/<estudiante_id>', delete_estudiantes),    
]