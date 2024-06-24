from django.shortcuts import render

# Create your views here.
from formulario.models import Formulario


def index(request):
    return render(request, "formularios/formulario.html")


def alta1(request):
    nom = request.POST['nombre']
    ape1 = request.POST['apellido1']
    ape2 = request.POST['apellido2']
    dom = request.POST['domicilio']
    ciu = request.POST['ciudad']
    sex = request.POST['radiosexo']
    sis = request.POST.getlist('sistema')
    contador = 0
    for i in sis:
        if contador == 0:
            sis1 = sis[0]
        else:
            sis1 = sis1 + "," + i
        contador += 1
    com = request.POST['areatext']
    emple = Formulario()
    condicional = emple.insertdato(nom, ape1, ape2, dom, ciu, sex, sis1, com)
    condicional1 = {
        'condicional1': condicional,
    }
    return render(request, "formularios/templateResultado.html", condicional1)
