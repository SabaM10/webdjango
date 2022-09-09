from django.http import HttpResponse
from django.template import loader
from AppCoder.models import Curso
def home(self, name):
    return HttpResponse(f'Hello World! {name}')

def homePage(self):
    lista = [1,2,3,4,5,6,7,8,9]
    data = {'nombre': 'Saba', 'apellido': 'Miro', 'lista': lista} 
    planilla = loader.get_template('home.html')
    documento = planilla.render(data)
    return HttpResponse(documento)

def cursos(self):
    curso = Curso(nombre='UX/UI', camada=12345)
    curso.save()
    #planilla = loader.get_template('cursos.html')
    documento = f'Curso:{curso.nombre} camada:{curso.camada}'
    return HttpResponse(documento)