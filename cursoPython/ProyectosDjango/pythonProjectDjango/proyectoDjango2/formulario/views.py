from django.shortcuts import render

# Create your views here.
from formulario.models import Formulario

def alta1(request):
    nom = request.POST['nombre']
    ape1 = request.POST['apellido1']
    ape2 = request.POST['apellido2']
    dom = request.POST['domicilio']
    ciu = request.POST['ciudad']
    sex = request.POST['radiosexo']
    sis = request.POST.getlist('sistema')
    com = request.POST['areatext']
    emple = Formulario()
    condicional = emple.insertdato(nom, ape1, ape2, dom, ciu, sex, sis,com)
    condicional1 = {
        'condicional1': condicional,
    }
    return render(request, "formularios/formulario1.html", condicional1)


