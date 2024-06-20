from django.shortcuts import render
from request1.models import Empleado1


def index(request):
    return render(request, "data/template2Alta.html")


def empleados1(request):
    dept = request.POST['dept_no']
    nombre = request.POST['dnombre']
    loc = request.POST['loc']
    emple = Empleado1()
    condicional = emple.insertdato(dept,nombre,loc)
    condicional1 = {
        'condicional1': condicional
    }
    if(condicional):
        cursor = emple.devolverdato()
        contexto = {
            'listado_empleados': cursor,
            'condicional1': condicional
        }
        return render(request, "data/templateResultado.html", contexto)
    else:
        return render(request, "data/templateResultado.html", condicional1)


