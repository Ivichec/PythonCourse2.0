from django.shortcuts import render

# Create your views here.
from doctores.models import Formulario


def index(request):
    condicional1 = {
        'condicional': False,
    }
    return render(request, "formulario/formulario1.html", condicional1)


def alta1(request):
    condicional = []
    hosp_nombres = request.POST.getlist('hosp')
    emple = Formulario()

    for nombre in hosp_nombres:
        results = emple.insertdato(nombre)
        if results is not None:
            condicional.append(results)
    context = {
        'condicional1': condicional,
        'condicional': True,
    }
    return render(request, "formulario/formulario1.html", context)
