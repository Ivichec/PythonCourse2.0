from django.shortcuts import render
from request.models import Empleado


def index(request):
    return render(request, "data/template2Alta.html")


def empleados(request):
    ofi = request.POST['txtOficio']
    emple = Empleado()
    cursor = emple.devolverdato(ofi)
    contexto = {
        'listado_empleados': cursor
    }
    return render(request, "data/templateResultado.html", contexto)

