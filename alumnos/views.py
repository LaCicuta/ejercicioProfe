from django.shortcuts import render
from .models import Genero, Alumno

# Create your views here.
class persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        super().__init__()


def index(request):
    hijo=persona("Juan Perez", "7")

    lista=["Lazaña", "Charquican", "Porotos granado"]

    alumnos = Alumno.objects.all()

    context={"hijo":hijo, "nombre":"Claudia Andrea", "comidas":lista, "alumnos":alumnos}

    return render(request, 'alumnos/index.html', context)