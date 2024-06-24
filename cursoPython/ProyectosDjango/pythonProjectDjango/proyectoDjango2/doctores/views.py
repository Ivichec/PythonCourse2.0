from django.shortcuts import render

# Create your views here.
from doctores.models import Formulario


def index(request):
    condicional1 = {
        'condicional': False,
    }
    return render(request, "formulario/formulario1.html", condicional1)


def alta1(request):
    hosp_nombres = request.POST.getlist('hosp')
    emple = Formulario()
    contador = 0
    for i in hosp_nombres:
        if contador == 0:
            sis1 = "'" + hosp_nombres[0] + "'"
        else:
            sis1 = sis1 + "," + "'" + i + "'"
        contador += 1
    condicional = emple.insertdato(sis1)
    context = {
        'condicional1': condicional,
        'condicional': True,
        'p1': sis1
    }
    return render(request, "formulario/formulario1.html", context)
