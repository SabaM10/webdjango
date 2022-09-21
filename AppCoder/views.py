import email
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from AppCoder.models import Estudiante
from AppCoder.forms import form_estudiantes
# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def home(request):
    return render(request, 'home.html')

def cursos(request):
    return render(request, 'cursos.html')

def profesores(request):
    return render(request, 'profesores.html')

def estudiantes(request):
    if request.method == 'POST':
        estudiante = Estudiante(nombre = request.POST['nombre'], apellido = request.POST['apellido'],email = request.POST['email'])
        estudiante.save()
        return render(request, 'home.html')
    return render(request, 'estudiantes.html')

def entregables(request):
    return render(request, 'entregables.html')

def api_estudiantes(request):
    if request.method == 'POST':
        formulario = form_estudiantes(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            estudiante = Estudiante(nombre = informacion['nombre'], apellido = informacion['apellido'],email = informacion['email'])
            estudiante.save()
            return render(request, 'api_estudiantes.html')
    else:
            formulario = form_estudiantes()
    return render(request, 'api_estudiantes.html', {'formulario': formulario})

def buscar_estudiante(request):
    if request.GET['email']:
        email = request.GET['email']
        estudiantes = Estudiante.objects.filter(email__icontains=email)
        return render(request, 'estudiantes.html', {'estudiantes': estudiantes})
    else:
        respuesta = 'No se encontraron estudiantes'
    return HttpResponse(respuesta)

def create_estudiantes(request):
    if request.method == 'POST':
        estudiante = Estudiante(nombre = request.POST['nombre'], apellido = request.POST['apellido'], email = request.POST['email'])
        estudiante.save()
        estudiantes = Estudiante.objects.all() #trae todos los estudiantes
        return render(request, 'estudiantesCRUD/read_estudiantes.html', {'estudiantes': estudiantes})
    return render(request, 'estudiantesCRUD/create_estudiantes.html')

def read_estudiantes(request=None):
    estudiantes = Estudiante.objects.all() #trae todos los estudiantes
    return render(request, 'estudiantesCRUD/read_estudiantes.html', {'estudiantes': estudiantes})

def update_estudiantes(request, estudiante_id):
    estudiante = Estudiante.objects.get(id = estudiante_id)

    if request.method == 'POST':
        formulario = form_estudiantes(request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            estudiante.nombre = informacion['nombre']
            estudiante.apellido = informacion['apellido']
            estudiante.email = informacion['email']
            estudiante.save()
            read_estudiantes()
            estudiantes = Estudiante.objects.all() #trae todos los estudiantes
            return render(request, 'estudiantesCRUD/read_estudiantes.html', {'estudiantes': estudiantes})
    else:
        formulario = form_estudiantes(initial={'nombre': estudiante.nombre, 'apellido': estudiante.apellido, 'email': estudiante.email})
    return render(request, 'estudiantesCRUD/update_estudiantes.html', {'formulario': formulario})

def delete_estudiantes(request, estudiante_id):
    estudiante = Estudiante.objects.get(id =  estudiante_id)
    estudiante.delete()
    
    estudiantes = Estudiante.objects.all()    
    return render(request, "estudiantesCRUD/read_estudiantes.html", {"estudiantes": estudiantes})
